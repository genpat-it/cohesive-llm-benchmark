#!/usr/bin/env python3.11
"""
Validate every turn of every multi-turn LLM conversation.

For each line in runs_modifications.jsonl (produced by run_llm_multi_turn.py),
runs each turn's LLM-generated .nf through nextflow -stub-run and produces
a flat per-turn verdict record plus a human-readable Markdown report.

Outputs (under $BENCH_RUNS_DIR):
  verdicts_modifications.jsonl   one record per turn (24+ fields)
  report_modifications.md        human-readable per-conversation summary
  report_modifications.tsv       grep-friendly
  report_modifications.csv       Excel-friendly
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from harness.harness import Example, Harness   # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_llm import analyse_code, categorize, syntax_check, determine_inputs  # noqa: E402

HERE = Path(__file__).resolve().parent
RUNS_DIR = Path(os.environ.get("BENCH_RUNS_DIR", HERE / "_out")).resolve()
RUNS_DIR.mkdir(parents=True, exist_ok=True)
RUNS = RUNS_DIR / "runs_modifications.jsonl"
VERDICTS = RUNS_DIR / "verdicts_modifications.jsonl"
REPORT_MD = RUNS_DIR / "report_modifications.md"


def validate_turn(harness: Harness, conv: dict, turn_rec: dict) -> dict:
    """Validate a single turn's LLM-generated nextflow code.

    Returns a flat record (one per turn) matching the same field naming as
    validate_llm.py so a downstream TSV-emitter can treat them uniformly.
    """
    eid = f"{conv['id']}_t{turn_rec['turn_index']}"
    prompt = turn_rec["user_prompt"]
    params = dict(turn_rec["params"])
    expected = turn_rec["expected_processes"]
    nf_code = turn_rec["llm_response"].get("nextflow_code")
    gt_code = turn_rec["ground_truth_code"]

    # Augment params so getInput/getSingleInput/getAssembly are all happy.
    if "input" in params and ("cmp" not in params or "riscd" not in params):
        first = (params["input"] or [{}])[0]
        params.setdefault("cmp",   first.get("cmp"))
        params.setdefault("riscd", first.get("riscd"))
    elif "cmp" in params and "riscd" in params and "input" not in params:
        params["input"] = [{"cmp": params["cmp"], "riscd": params["riscd"]}]

    gt_analysis = analyse_code(gt_code)
    llm_analysis = analyse_code(nf_code or "")
    gt_steps = set(gt_analysis["called_steps"] or gt_analysis["included_steps"])
    llm_steps = set(llm_analysis["called_steps"] or llm_analysis["included_steps"])

    row: dict = {
        "id":                 eid,
        "conv_id":            conv["id"],
        "turn_index":         turn_rec["turn_index"],
        "category":           conv["category"],
        "modification_kind":  conv.get("modification_kind"),
        "base_id":            conv.get("base_id"),
        "prompt":             prompt,
        "ground_truth_code":  gt_code,
        "params":             params,
        "expected_processes": expected,
        "llm_reply_excerpt":  turn_rec["llm_response"].get("reply", "")[:300],
        "nextflow_code":      nf_code,
        "syntax_valid":       None,
        "semantic_valid":     None,
        "n_processes":        0,
        "error_category":     None,
        "error_detail":       "",
        "elapsed_s":          turn_rec.get("elapsed_s"),
        "turns":              turn_rec["llm_response"].get("turns"),
        "code_chars":         llm_analysis["code_chars"],
        "code_lines":         llm_analysis["code_lines"],
        "included_steps":     llm_analysis["included_steps"],
        "called_steps":       llm_analysis["called_steps"],
        "hallucinated_steps": llm_analysis["hallucinated_steps"],
        "n_workflow_calls":   llm_analysis["n_workflow_calls"],
        "ground_truth_steps": sorted(gt_steps),
        "matches_gt_steps":   gt_steps == llm_steps,
        "extra_steps":        sorted(llm_steps - gt_steps),
        "missing_steps":      sorted(gt_steps - llm_steps),
    }

    if not nf_code:
        row["error_category"] = "no_code"
        row["error_detail"] = turn_rec["llm_response"].get("error", "no nextflow_code returned")
        row["syntax_valid"] = False
        row["semantic_valid"] = False
        return row

    ok_syntax, syntax_log = syntax_check(nf_code, eid, params)
    row["syntax_valid"] = ok_syntax

    ex = Example(eid=f"llm_{eid}", category=conv["category"],
                 prompt=prompt, nextflow_code=nf_code, params=params,
                 inputs=determine_inputs(params),
                 expected_processes=expected,
                 notes="LLM-generated multi-turn validation")
    v = harness.run(ex)

    scratch_log = harness.scratch / f"llm_{eid}" / "nextflow.log"
    log_text = scratch_log.read_text() if scratch_log.exists() else syntax_log

    names = set(re.findall(r":([A-Za-z][A-Za-z0-9_]*)\s+[-|]", log_text))
    names.update(re.findall(r"\[[a-f0-9]{2}/[a-f0-9]+\] [^\n]+:([A-Za-z][A-Za-z0-9_]*)", log_text))
    row["n_processes"] = len(names)
    row["semantic_valid"] = v.passed
    cat, detail = categorize(log_text, len(names), expected)
    row["error_category"] = cat
    row["error_detail"] = detail
    if not ok_syntax and v.passed:
        row["syntax_valid"] = True
    return row


def main() -> None:
    convs = [json.loads(l) for l in RUNS.read_text().splitlines() if l.strip()]
    print(f"Loaded {len(convs)} conversations from {RUNS.name}", flush=True)
    H = Harness()

    rows: list[dict] = []
    n_turn_pass = 0
    n_turn_total = 0
    for i, conv in enumerate(convs, start=1):
        for turn_rec in conv["turns"]:
            n_turn_total += 1
            row = validate_turn(H, conv, turn_rec)
            rows.append(row)
            if row["semantic_valid"]:
                n_turn_pass += 1
            status = "PASS" if row["semantic_valid"] else "FAIL"
            print(f"[{i:3d}/{len(convs)}] {conv['id']:50s}  "
                  f"t{turn_rec['turn_index']}  {status:5s}  "
                  f"procs={row['n_processes']}/{row['expected_processes']}  "
                  f"cat={row['error_category']}",
                  flush=True)

    VERDICTS.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n")
    print(f"\nWrote per-turn verdicts to {VERDICTS}")
    write_report(convs, rows, n_turn_pass, n_turn_total)


def write_report(convs: list[dict], rows: list[dict],
                 n_turn_pass: int, n_turn_total: int) -> None:
    from collections import Counter, defaultdict
    by_conv: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_conv[r["conv_id"]].append(r)

    n_conv_full_pass = sum(
        1 for cid, rs in by_conv.items()
        if rs and all(r["semantic_valid"] for r in rs)
    )

    cats = Counter(r["error_category"] for r in rows)

    lines: list[str] = []
    lines.append("# LLM multi-turn evaluation — detailed report\n")
    lines.append(f"Total conversations: **{len(convs)}**  ·  total turns: **{n_turn_total}**  "
                 f"·  per-turn pass: **{n_turn_pass}/{n_turn_total}**  "
                 f"·  conversations fully passing: **{n_conv_full_pass}/{len(convs)}**\n")

    # by-kind breakdown
    by_kind: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_kind[r["modification_kind"] or "?"].append(r)
    lines.append("## Pass rate by modification kind (per turn)\n")
    lines.append("| kind | turns | pass |")
    lines.append("|----|-----:|-----:|")
    for kind in ("add", "replace", "drop", "switch_species"):
        rs = by_kind.get(kind, [])
        if not rs:
            continue
        p = sum(1 for r in rs if r["semantic_valid"])
        lines.append(f"| `{kind}` | {len(rs)} | {p} |")
    lines.append("")

    lines.append("## Error category breakdown\n")
    lines.append("| Category | Count |")
    lines.append("|----|----:|")
    for cat, n in cats.most_common():
        lines.append(f"| `{cat}` | {n} |")
    lines.append("")

    lines.append("## Per-conversation outcome\n")
    lines.append("| # | conv_id | kind | t1 | t2 | error category (failing turn) |")
    lines.append("|---|---------|------|----|----|------------------------------|")
    for i, conv in enumerate(convs, start=1):
        rs = by_conv[conv["id"]]
        t1 = next((r for r in rs if r["turn_index"] == 1), None)
        t2 = next((r for r in rs if r["turn_index"] == 2), None)
        def em(r):
            return "✅" if (r and r["semantic_valid"]) else ("❌" if r else "·")
        cat = ""
        for r in rs:
            if not r["semantic_valid"]:
                cat = f"t{r['turn_index']}: `{r['error_category']}`"
                break
        lines.append(f"| {i} | `{conv['id']}` | `{conv.get('modification_kind')}` | "
                     f"{em(t1)} | {em(t2)} | {cat} |")
    lines.append("")

    fails = [r for r in rows if not r["semantic_valid"]]
    if fails:
        lines.append("## Failure detail (one section per failing turn)\n")
        for r in fails:
            lines.append(f"### `{r['id']}` — `{r['error_category']}`")
            lines.append(f"**Conversation:** `{r['conv_id']}` ({r['modification_kind']}) — "
                         f"turn {r['turn_index']}")
            lines.append(f"**Prompt:** {r['prompt']}\n")
            llm_steps = r.get("called_steps") or r.get("included_steps") or []
            gt_steps  = r.get("ground_truth_steps", [])
            lines.append(f"**Steps (LLM):** `{', '.join(llm_steps) or '(none)'}`")
            lines.append(f"**Steps (GT):**  `{', '.join(gt_steps) or '(none)'}`\n")
            if r.get("hallucinated_steps"):
                lines.append(f"**Hallucinated steps:** `{', '.join(r['hallucinated_steps'])}`")
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

    REPORT_MD.write_text("\n".join(lines))
    print(f"Wrote report to {REPORT_MD}")


if __name__ == "__main__":
    main()
