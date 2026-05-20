#!/usr/bin/env python3.11
"""Convert llm_eval_verdicts.jsonl to a human-reviewable TSV (and a CSV variant).

The TSV keeps multi-line fields by escaping \\n -> literal '\\n' so each
example is one row (good for grep / quick scrolling). The CSV uses RFC-4180
quoting so multi-line fields stay multi-line (good for Excel / LibreOffice).
"""

from __future__ import annotations
import csv
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS_DIR = Path(os.environ.get("BENCH_RUNS_DIR", HERE / "_out")).resolve()

# Emit a TSV/CSV pair for whichever sources are present:
#   single-turn → verdicts.jsonl                → report.{tsv,csv}
#   multi-turn  → verdicts_modifications.jsonl  → report_modifications.{tsv,csv}
SOURCES = [
    (RUNS_DIR / "verdicts.jsonl",
     RUNS_DIR / "report.tsv", RUNS_DIR / "report.csv",
     ("id",)),
    (RUNS_DIR / "verdicts_modifications.jsonl",
     RUNS_DIR / "report_modifications.tsv",
     RUNS_DIR / "report_modifications.csv",
     ("conv_id", "turn_index", "modification_kind", "base_id")),
]

BASE_COLUMNS = [
    "id",
    "category",
    "prompt",
    "syntax_valid",
    "semantic_valid",
    "error_category",
    "error_detail",
    "n_processes",
    "expected_processes",
    "matches_gt_steps",
    "extra_steps",
    "missing_steps",
    "hallucinated_steps",
    "included_steps",
    "called_steps",
    "ground_truth_steps",
    "code_chars",
    "code_lines",
    "n_workflow_calls",
    "turns",
    "elapsed_s",
    "llm_reply_excerpt",
    "nextflow_code",
    "ground_truth_code",
]


def jsonish(v):
    if isinstance(v, (list, tuple)):
        return ", ".join(str(x) for x in v) if v else ""
    if isinstance(v, bool):
        return "Y" if v else "N"
    if v is None:
        return ""
    return str(v)


def tsv_safe(v) -> str:
    s = jsonish(v)
    return s.replace("\t", "    ").replace("\r\n", "\\n").replace("\n", "\\n")


def emit(src: Path, tsv: Path, csv_path: Path, extra: tuple[str, ...]) -> None:
    if not src.exists():
        print(f"(skip) {src.name} not present")
        return
    columns = list(extra) + BASE_COLUMNS
    rows = [json.loads(l) for l in src.read_text().splitlines() if l.strip()]
    for r in rows:
        r.setdefault("category", r["id"].split("_", 1)[0])
    with tsv.open("w", encoding="utf-8") as f:
        f.write("\t".join(columns) + "\n")
        for r in rows:
            f.write("\t".join(tsv_safe(r.get(c, "")) for c in columns) + "\n")
    print(f"Wrote {tsv}")
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(columns)
        for r in rows:
            w.writerow([jsonish(r.get(c, "")) for c in columns])
    print(f"Wrote {csv_path}")
    print(f"  {len(rows)} rows × {len(columns)} columns\n")


for src, tsv, csv_path, extra in SOURCES:
    emit(src, tsv, csv_path, extra)
