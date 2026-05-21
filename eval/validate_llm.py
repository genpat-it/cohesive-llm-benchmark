#!/usr/bin/env python3.11
"""
Validate the LLM-generated .nf files (from llm_eval_runs.jsonl) using the
harness. Produces a detailed per-prompt report covering:

  - prompt
  - llm_response (nextflow code + reply summary)
  - ground_truth_code
  - syntax_valid    (nextflow -preview parses)
  - semantic_valid  (nextflow -stub-run schedules >= expected processes)
  - error_category  (arity_error, missing_param, channel_emit, silent_no_op,
                     unknown_step, no_code, none, other)
  - error_detail    (last meaningful lines of the nextflow log)
  - n_processes     (distinct process placeholders observed)
  - expected_processes

Outputs:
  - llm_eval_verdicts.jsonl  (one structured record per prompt)
  - llm_eval_report.md       (human-readable summary)
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

# Add repo root to path so we can import the harness module from a sibling dir.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from harness.harness import Example, Harness, FW, NEXTFLOW   # noqa: E402

HERE = Path(__file__).resolve().parent
# Default I/O paths: read runs.jsonl from --runs-dir, write report next to it.
RUNS_DIR = Path(os.environ.get("BENCH_RUNS_DIR", HERE / "_out")).resolve()
RUNS_DIR.mkdir(parents=True, exist_ok=True)
RUNS = RUNS_DIR / "runs.jsonl"
VERDICTS = RUNS_DIR / "verdicts.jsonl"
REPORT = RUNS_DIR / "report.md"


# ---------------------------------------------------------------------------
# error categorisation
# ---------------------------------------------------------------------------
ERROR_PATTERNS: list[tuple[str, str, str]] = [
    # (category,  human label,  regex)
    ("arity_error",      "Wrong arity on a workflow call",
     r"declares \d+ input channels? but \d+ were given"),
    ("missing_param",    "Missing required param() at workflow build",
     r"missing required param:"),
    ("missing_input",    "Missing required input params (cmp/riscd)",
     r"missing required params \(cmp,riscd\)"),
    ("unknown_step",     "Reference to a non-existent step/module",
     r"Module ['\"][^'\"]+['\"] does not exist|Unable to find Module|"
     r"No such file or directory:.*steps/"),
    ("channel_emit",     "Wrong emit name on a workflow call",
     r"No such property: (assembled|trimmed|assembly|reads|data|reference) for class"),
    ("compile_error",    "Groovy/DSL2 compile error",
     r"^.*WARN.*Groovy|MultipleCompilationErrorsException|"
     r"Compile error|Unexpected token"),
    ("species_filter",   "when: clause filtered all processes",
     r"isSpeciesSupported.*returned false"),
    ("ngsmanager_naming","Bad sample-file naming convention",
     r"unexpected file name:"),
    ("file_not_found",   "Input file not at expected path",
     r"No files match pattern|file not found:"),
]


def categorize(log: str, scheduled: int, expected: int) -> tuple[str, str]:
    """Return (category, detail). Detail is a short excerpt."""
    for cat, _label, pattern in ERROR_PATTERNS:
        m = re.search(pattern, log, re.M)
        if m:
            # collect a small window around the match
            line_start = log.rfind("\n", 0, m.start()) + 1
            line_end = log.find("\n", m.end())
            if line_end == -1:
                line_end = len(log)
            return cat, log[line_start:line_end].strip()[:300]

    if scheduled == 0:
        return "silent_no_op", "No process placeholders appeared. when: clause filtered everything?"

    if scheduled < expected:
        return "partial_dag", f"Only {scheduled}/{expected} expected processes appeared in the DAG"

    return "none", ""


# ---------------------------------------------------------------------------
# syntax-only check via -preview
# ---------------------------------------------------------------------------
_SYNTAX_TMP = Path(tempfile.gettempdir()) / "cohesive_llm_bench_syntax"
_SYNTAX_TMP.mkdir(parents=True, exist_ok=True)


def syntax_check(nf_code: str, eid: str, params: dict) -> tuple[bool, str]:
    """Drop the .nf into the framework pipelines/ and run `nextflow ... -preview`.
    Return (passed, log)."""
    pipe = FW / "pipelines" / f"_llmval_{eid}.nf"
    pipe.write_text(nf_code)
    # write a minimal params file using a portable temp dir
    params_file = _SYNTAX_TMP / f"{eid}_params.json"
    params_file.write_text(json.dumps({**params,
                                       "inputdir": str(_SYNTAX_TMP / "inputdir"),
                                       "outdir":   str(_SYNTAX_TMP / "out"),
                                       "assets_dir": str(FW / "assets")}))
    try:
        r = subprocess.run(
            [NEXTFLOW, "run", str(pipe), "-preview",
             "-params-file", str(params_file)],
            cwd=str(FW), capture_output=True, text=True, timeout=30,
        )
        log = r.stdout + "\n" + r.stderr
        # -preview is happy if "DSL2 - revision:" appears, regardless of params
        ok = "DSL2 - revision:" in log
        # A workflow-build error (arity/emit) makes preview fail.
        if re.search(r"declares \d+ input channels", log):
            ok = False
        return ok, log
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT in -preview"
    finally:
        pipe.unlink(missing_ok=True)
        params_file.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
def determine_inputs(params: dict) -> list[str]:
    inputs: list[str] = []
    cmp = params.get("cmp")
    if cmp is None:
        return inputs
    riscds = []
    if params.get("riscd"):
        riscds.append(params["riscd"])
    for entry in params.get("input", []) or []:
        if entry.get("riscd"):
            riscds.append(entry["riscd"])
    for r in riscds:
        # riscd format: <DT>-<DS>-<acc>-<met>
        parts = r.split("-")
        # acc is parts[2..-1] joined except the last ('met')
        if len(parts) >= 4:
            acc = "-".join(parts[2:-1])
        else:
            acc = "0SQ_rawreads"
        if acc == "0SQ_rawreads":
            kind = "fastq_paired"
            if params.get("seq_type") in ("nanopore", "ion"):
                kind = "fastq_single"
            inputs.append(f"{kind}:{cmp}")
        elif acc.startswith("2AS_"):
            inputs.append(f"assembly:{cmp}")
        else:
            inputs.append(f"fastq_paired:{cmp}")
    if not inputs:
        inputs.append(f"fastq_paired:{cmp}")
    return inputs


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Static analysis of an .nf string
# ---------------------------------------------------------------------------
INCLUDE_RE  = re.compile(r"include\s*\{\s*([^}]+?)\s*\}\s*from\s*'([^']+)'")
CALL_RE     = re.compile(r"(step_[A-Za-z0-9_]+)\s*\(")
STEPS_DIR   = FW / "steps"
KNOWN_STEPS = {p.stem for p in STEPS_DIR.glob("*.nf")} if STEPS_DIR.is_dir() else set()


def analyse_code(nf_code: str) -> dict:
    """Static analysis of the LLM-generated nextflow code."""
    if not nf_code:
        return {"included_steps": [], "called_steps": [], "hallucinated_steps": [],
                "code_chars": 0, "code_lines": 0, "n_workflow_calls": 0}
    included: set[str] = set()
    for sym_list, path in INCLUDE_RE.findall(nf_code):
        for sym in [s.strip() for s in sym_list.split(";")]:
            if sym.startswith("step_"):
                included.add(sym.split()[0])
    called = list(dict.fromkeys(CALL_RE.findall(nf_code)))
    hallucinated = [s for s in (set(called) | included) if s not in KNOWN_STEPS]
    return {
        "included_steps":    sorted(included),
        "called_steps":      called,
        "hallucinated_steps": sorted(hallucinated),
        "code_chars":        len(nf_code),
        "code_lines":        nf_code.count("\n") + 1,
        "n_workflow_calls":  len(called),
    }


def main() -> None:
    records = [json.loads(l) for l in RUNS.read_text().splitlines() if l.strip()]
    print(f"Loaded {len(records)} LLM runs from {RUNS.name}", flush=True)

    H = Harness()
    rows: list[dict] = []
    for i, rec in enumerate(records, start=1):
        eid = rec["id"]
        prompt = rec["prompt"]
        params = rec["params"]
        expected = rec["expected_processes"]
        nf_code = rec["llm_response"].get("nextflow_code")
        gt_code = rec["ground_truth_code"]

        gt_analysis  = analyse_code(gt_code)
        llm_analysis = analyse_code(nf_code or "")
        # diff steps used
        gt_steps  = set(gt_analysis["called_steps"] or gt_analysis["included_steps"])
        llm_steps = set(llm_analysis["called_steps"] or llm_analysis["included_steps"])

        row = {
            "id":                eid,
            "prompt":            prompt,
            "ground_truth_code": gt_code,
            "params":            params,
            "expected_processes": expected,
            "llm_reply_excerpt": rec["llm_response"].get("reply", "")[:300],
            "nextflow_code":     nf_code,
            "syntax_valid":      None,
            "semantic_valid":    None,
            "n_processes":       0,
            "error_category":    None,
            "error_detail":      "",
            "elapsed_s":         rec.get("elapsed_s"),
            "turns":             rec["llm_response"].get("turns"),
            # static analysis of LLM code
            "code_chars":         llm_analysis["code_chars"],
            "code_lines":         llm_analysis["code_lines"],
            "included_steps":     llm_analysis["included_steps"],
            "called_steps":       llm_analysis["called_steps"],
            "hallucinated_steps": llm_analysis["hallucinated_steps"],
            "n_workflow_calls":   llm_analysis["n_workflow_calls"],
            # comparison with ground truth
            "ground_truth_steps": sorted(gt_steps),
            "matches_gt_steps":   gt_steps == llm_steps,
            "extra_steps":        sorted(llm_steps - gt_steps),
            "missing_steps":      sorted(gt_steps - llm_steps),
        }

        if not nf_code:
            llm_err = rec["llm_response"].get("error") or ""
            llm_err_lc = llm_err.lower()
            # Distinguish upstream-API rate-limit from a genuine LLM failure to
            # produce code.  The former is a Mistral/quota issue (not a model
            # quality problem) and shouldn't be counted in error-category stats
            # as if the model failed.
            if "rate_limit" in llm_err_lc or "429" in llm_err_lc or "ratelimit" in llm_err_lc:
                row["error_category"] = "rate_limited"
                row["error_detail"] = llm_err or "upstream LLM API hit a 429 rate limit"
            else:
                row["error_category"] = "no_code"
                row["error_detail"] = llm_err or "no nextflow_code returned"
            row["syntax_valid"] = False
            row["semantic_valid"] = False
            tag = "RATELIM" if row["error_category"] == "rate_limited" else "NOCODE"
            print(f"[{i:3d}/{len(records)}] {eid:35s}  {tag}", flush=True)
            rows.append(row)
            continue

        # Augment params so both getInput()/array-form AND
        # getSingleInput()/getAssembly()/direct-form are satisfied.
        # The LLM may pick a getter different from the ground truth -- we accept
        # any valid choice as long as the params let it resolve.
        if "input" in params and ("cmp" not in params or "riscd" not in params):
            first = (params["input"] or [{}])[0]
            params = {**params,
                      "cmp":   first.get("cmp", params.get("cmp")),
                      "riscd": first.get("riscd", params.get("riscd"))}
        elif "cmp" in params and "riscd" in params and "input" not in params:
            params = {**params,
                      "input": [{"cmp": params["cmp"], "riscd": params["riscd"]}]}

        # Level 1: syntax-only via -preview
        ok_syntax, syntax_log = syntax_check(nf_code, eid, params)
        row["syntax_valid"] = ok_syntax

        # Level 2: stub-run via the harness  (does proper input materialisation)
        ex = Example(eid=f"llm_{eid}", category=rec.get("category", "?"),
                     prompt=prompt, nextflow_code=nf_code, params=params,
                     inputs=determine_inputs(params),
                     expected_processes=expected,
                     notes="LLM-generated under validation")
        v = H.run(ex)

        # The log path is harness's scratch/<eid>/nextflow.log; use the same
        # default the Harness uses so we read whatever it just wrote.
        scratch_log = H.scratch / f"llm_{eid}" / "nextflow.log"
        log_text = scratch_log.read_text() if scratch_log.exists() else syntax_log

        # Count distinct process names actually scheduled
        names = set(re.findall(r":([A-Za-z][A-Za-z0-9_]*)\s+[-|]", log_text))
        names.update(re.findall(r"\[[a-f0-9]{2}/[a-f0-9]+\] [^\n]+:([A-Za-z][A-Za-z0-9_]*)", log_text))
        row["n_processes"] = len(names)
        row["semantic_valid"] = v.passed

        cat, detail = categorize(log_text, len(names), expected)
        row["error_category"] = cat
        row["error_detail"] = detail

        # If syntax failed but somehow semantic passed, prefer the harness verdict
        if not ok_syntax and v.passed:
            row["syntax_valid"] = True

        status = "PASS" if v.passed else "FAIL"
        print(f"[{i:3d}/{len(records)}] {eid:35s}  {status}  "
              f"syntax={'Y' if row['syntax_valid'] else 'N'}  "
              f"procs={row['n_processes']}/{expected}  "
              f"cat={cat}",
              flush=True)
        rows.append(row)

    # write outputs
    VERDICTS.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n")
    print(f"\nWrote per-example verdicts to {VERDICTS}")

    write_report(rows)


def write_report(rows: list[dict]) -> None:
    total = len(rows)
    n_code      = sum(1 for r in rows if r.get("nextflow_code"))
    n_syntax    = sum(1 for r in rows if r.get("syntax_valid"))
    n_semantic  = sum(1 for r in rows if r.get("semantic_valid"))

    # category breakdown
    from collections import Counter
    cats = Counter(r.get("error_category") for r in rows)

    lines: list[str] = []
    lines.append("# LLM evaluation — detailed report\n")
    n_hallucinated = sum(1 for r in rows if r.get("hallucinated_steps"))
    n_exact_match  = sum(1 for r in rows if r.get("matches_gt_steps") and r.get("nextflow_code"))
    n_extra        = sum(1 for r in rows if r.get("extra_steps"))
    n_missing      = sum(1 for r in rows if r.get("missing_steps"))

    lines.append(f"Total prompts: **{total}**  ·  generated code: **{n_code}**  "
                 f"·  syntactically valid: **{n_syntax}**  "
                 f"·  semantically valid: **{n_semantic}**\n")
    lines.append(f"Step-set vs. ground truth:  exact match **{n_exact_match}**  "
                 f"·  extra steps **{n_extra}**  ·  missing steps **{n_missing}**  "
                 f"·  hallucinated (non-existent) steps **{n_hallucinated}**\n")

    lines.append("## Error category breakdown\n")
    lines.append("| Category | Count | Meaning |")
    lines.append("|----|----|----|")
    cat_meanings = {
        "none":             "no error — pipeline passes",
        "no_code":          "LLM did not return any .nf code",
        "arity_error":      "workflow called with wrong number of arguments",
        "missing_param":    "step requires a param() that was not supplied",
        "missing_input":    "missing required cmp/riscd input params",
        "channel_emit":     "wrong emit name when chaining steps",
        "compile_error":    "Groovy/DSL2 compile error",
        "unknown_step":     "include refers to a non-existent step",
        "species_filter":   "when: clause filtered all processes (unsupported species)",
        "ngsmanager_naming":"input file name does not match parseMetadataFromFileName regex",
        "file_not_found":   "expected input file is not in the framework layout",
        "silent_no_op":     "DAG empty — pipeline runs but produces no output",
        "partial_dag":      "only some of the expected processes appeared in the DAG",
    }
    for cat, n in cats.most_common():
        lines.append(f"| `{cat}` | {n} | {cat_meanings.get(cat, '—')} |")
    lines.append("")

    lines.append("## Per-prompt outcome\n")
    lines.append("| # | id | code? | syntax | semantic | procs | error category | "
                 "first 80 chars of detail |")
    lines.append("|---|----|-------|--------|----------|-------|----------------|"
                 "------|")
    for i, r in enumerate(rows, start=1):
        code_emoji = "✅" if r.get("nextflow_code") else "⚪"
        syn_emoji  = "✅" if r.get("syntax_valid") else "❌"
        sem_emoji  = "✅" if r.get("semantic_valid") else "❌"
        procs = f"{r['n_processes']}/{r['expected_processes']}"
        cat = r.get("error_category", "?")
        det = (r.get("error_detail") or "").replace("|", "\\|").replace("\n", " ")[:80]
        lines.append(f"| {i} | `{r['id']}` | {code_emoji} | {syn_emoji} | {sem_emoji} | "
                     f"{procs} | `{cat}` | {det} |")
    lines.append("")

    # step-set comparison table
    lines.append("## Step-set comparison vs ground truth\n")
    lines.append("| # | id | LLM steps | GT steps | extra | missing | hallucinated |")
    lines.append("|---|----|-----------|----------|-------|---------|--------------|")
    for i, r in enumerate(rows, start=1):
        if not r.get("nextflow_code"):
            continue
        llm_s = ",".join(s.split("__", 1)[-1] for s in (r.get("called_steps") or r.get("included_steps") or []))
        gt_s  = ",".join(s.split("__", 1)[-1] for s in r.get("ground_truth_steps", []))
        extra = ",".join(s.split("__", 1)[-1] for s in r.get("extra_steps", []))
        miss  = ",".join(s.split("__", 1)[-1] for s in r.get("missing_steps", []))
        hal   = ",".join(r.get("hallucinated_steps", []))
        lines.append(f"| {i} | `{r['id']}` | {llm_s} | {gt_s} | {extra or '·'} | "
                     f"{miss or '·'} | {hal or '·'} |")
    lines.append("")

    fails = [r for r in rows if not r.get("semantic_valid")]
    if fails:
        lines.append("## Failure detail (one section per failing prompt)\n")
        for r in fails:
            lines.append(f"### `{r['id']}` — `{r.get('error_category')}`")
            lines.append("")
            lines.append(f"**Prompt:** {r['prompt']}\n")
            llm_steps = r.get("called_steps") or r.get("included_steps") or []
            gt_steps  = r.get("ground_truth_steps", [])
            lines.append(f"**Steps (LLM):** `{', '.join(llm_steps) or '(none)'}`")
            lines.append(f"**Steps (GT):**  `{', '.join(gt_steps) or '(none)'}`")
            if r.get("hallucinated_steps"):
                lines.append(f"**Hallucinated steps:** `{', '.join(r['hallucinated_steps'])}`")
            lines.append("")
            lines.append("**Ground truth (passes validation):**")
            lines.append("```groovy")
            lines.append((r.get("ground_truth_code") or "").rstrip())
            lines.append("```")
            lines.append("**LLM-generated (failed):**")
            lines.append("```groovy")
            lines.append((r.get("nextflow_code") or "").rstrip())
            lines.append("```")
            lines.append("**Error excerpt:**")
            lines.append("```")
            lines.append((r.get("error_detail") or "(no excerpt)"))
            lines.append("```\n")

    REPORT.write_text("\n".join(lines))
    print(f"Wrote report to {REPORT}")


if __name__ == "__main__":
    main()
