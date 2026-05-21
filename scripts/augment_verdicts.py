#!/usr/bin/env python3.11
"""Augment verdicts.jsonl with the LLM's full reply and verdict tags.

For each verdict in <results-dir>/verdicts.jsonl:
  * Pull the matching `llm_response.reply` and `llm_response.turn_logs`
    from <results-dir>/runs.jsonl (joining on `id` / `conv_id+turn_index`).
  * Compute `verdict_tags` describing the *shape* of the LLM's deviation
    from the ground truth (literal match vs reasonable extras vs noise).

Tag taxonomy
------------
  literal-match            extras_steps empty AND missing_steps empty.
  extras-best-practice     extras_steps are upstream conveniences (trimming,
                           species-id, normalisation) -- biologically sound
                           but beyond the literal prompt.
  extras-irrelevant        extras_steps are not a common best-practice add-on
                           (typing/AMR steps tacked on for no reason, etc.).
  missing-steps            ground-truth steps are absent in the LLM output.
  hallucinated             LLM uses include/step names that don't exist in
                           the framework.

A verdict can carry MULTIPLE tags (e.g. extras-best-practice + missing-steps).

Outputs
-------
  <results-dir>/verdicts_augmented.jsonl

The new fields are *additive* -- no existing keys are dropped, so downstream
consumers (badges, history, explorer) keep working.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]


# Step-name prefix → category. Anything starting with these is considered an
# "upstream convenience" that a bioinformatician would commonly insert before
# the requested step.
BEST_PRACTICE_PREFIXES = (
    "step_1PP_",                            # ANY pre-processing: trimming,
                                            # host depletion, dedup, ...
    "step_1SP_species_identification__",    # kraken2, kmerfinder
    "step_1RC_read_correction__",           # any read correction
    "step_1QC_quality_control__",           # FastQC etc.
)


def classify_tags(v: dict[str, Any]) -> list[str]:
    tags: list[str] = []
    extras = v.get("extra_steps") or []
    missing = v.get("missing_steps") or []
    halluc = v.get("hallucinated_steps") or []
    matches_gt = v.get("matches_gt_steps")

    if matches_gt and not extras and not missing:
        tags.append("literal-match")

    if extras:
        # All extras starting with a best-practice prefix → upstream-extras-ok.
        # If mixed, prefer the stronger label.
        bp = [s for s in extras if any(s.startswith(p) for p in BEST_PRACTICE_PREFIXES)]
        other = [s for s in extras if s not in bp]
        if bp and not other:
            tags.append("extras-best-practice")
        elif other:
            tags.append("extras-irrelevant")
            if bp:
                tags.append("extras-best-practice")

    if missing:
        tags.append("missing-steps")
    if halluc:
        tags.append("hallucinated")
    return tags


def load_jsonl(p: Path) -> list[dict[str, Any]]:
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        out.append(json.loads(line))
    return out


def augment_dir(results_dir: Path) -> tuple[int, Path]:
    # Single-turn uses verdicts.jsonl / runs.jsonl; multi-turn uses
    # verdicts_modifications.jsonl / runs_modifications.jsonl.
    if (results_dir / "verdicts.jsonl").exists():
        v_in, r_in, out_name = "verdicts.jsonl", "runs.jsonl", "verdicts_augmented.jsonl"
    else:
        v_in, r_in, out_name = ("verdicts_modifications.jsonl",
                                "runs_modifications.jsonl",
                                "verdicts_modifications_augmented.jsonl")
    verdicts = load_jsonl(results_dir / v_in)
    runs = load_jsonl(results_dir / r_in)
    if not verdicts:
        return 0, results_dir / out_name

    # Build lookup from runs.jsonl.  Single-turn: one row per example, keyed
    # on `id`. Multi-turn: one row per CONVERSATION carrying a `turns` list
    # of per-turn dicts (each with `llm_response.reply` + `turn_logs`).
    by_id: dict[str, dict[str, Any]] = {}
    by_conv: dict[tuple[str, int], dict[str, Any]] = {}
    for r in runs:
        if isinstance(r.get("turns"), list) and r.get("id"):
            # Multi-turn conversation row: explode into per-turn lookups.
            for t in r["turns"]:
                idx = t.get("turn_index")
                if idx is None:
                    continue
                by_conv[(r["id"], idx)] = {"llm_response": t.get("llm_response", {})}
        elif "id" in r:
            by_id[r["id"]] = r

    out_path = results_dir / out_name
    n = 0
    with out_path.open("w", encoding="utf-8") as f:
        for v in verdicts:
            tags = classify_tags(v)
            reply = ""
            turn_logs: list[dict[str, Any]] = []
            if "conv_id" in v and "turn_index" in v:
                r = by_conv.get((v["conv_id"], v["turn_index"]))
            else:
                r = by_id.get(v.get("id", ""))
            if r:
                resp = r.get("llm_response", {}) or {}
                reply = resp.get("reply", "") or ""
                turn_logs = resp.get("turn_logs", []) or []

            aug = dict(v)
            aug["verdict_tags"] = tags
            aug["llm_full_reply"] = reply
            aug["llm_turn_logs"] = turn_logs
            f.write(json.dumps(aug, ensure_ascii=False) + "\n")
            n += 1
    return n, out_path


def main() -> int:
    targets = sys.argv[1:] or [
        "results/llm_full_200",
        "results/llm_full_multi_turn",
        "results/example_run_mistral",
        "results/example_run_mistral_multi_turn",
    ]
    grand = 0
    for t in targets:
        d = (REPO / t).resolve()
        if not d.exists():
            print(f"skip (no dir): {t}")
            continue
        n, out = augment_dir(d)
        print(f"  augmented {n} -> {out.relative_to(REPO)}")
        grand += n
    print(f"\nTotal augmented verdicts: {grand}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
