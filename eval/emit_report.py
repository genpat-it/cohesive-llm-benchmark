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
SRC = RUNS_DIR / "verdicts.jsonl"
TSV = RUNS_DIR / "report.tsv"
CSV = RUNS_DIR / "report.csv"

COLUMNS = [
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


rows = [json.loads(l) for l in SRC.read_text().splitlines() if l.strip()]

# also flatten category (auto-derived)
for r in rows:
    r.setdefault("category", r["id"].split("_", 1)[0])

# --- TSV (one line per example, newlines literalised) ---
with TSV.open("w", encoding="utf-8") as f:
    f.write("\t".join(COLUMNS) + "\n")
    for r in rows:
        f.write("\t".join(tsv_safe(r.get(c, "")) for c in COLUMNS) + "\n")
print(f"Wrote {TSV}")

# --- CSV (RFC-4180, multi-line fields preserved) ---
with CSV.open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(COLUMNS)
    for r in rows:
        w.writerow([jsonish(r.get(c, "")) for c in COLUMNS])
print(f"Wrote {CSV}")

print(f"\n{len(rows)} rows × {len(COLUMNS)} columns")
