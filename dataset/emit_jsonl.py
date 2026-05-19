#!/usr/bin/env python3.11
"""Emit dataset_50.jsonl from already-validated blueprints (no re-validation)."""

import json
import sys
from pathlib import Path

# Make the repo root importable so cross-module imports work no matter
# where the user runs the script from.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dataset.blueprints import build_all   # noqa: E402

HERE = Path(__file__).resolve().parent
OUT = HERE / "dataset_50.jsonl"
README = HERE / "README.md"

examples = build_all()
print(f"Built {len(examples)} examples")

lines = []
for ex in examples:
    d = ex.to_serializable()
    d["validation"] = {
        "method": "nextflow -stub-run",
        "expected_processes": ex.expected_processes,
    }
    lines.append(json.dumps(d, ensure_ascii=False))

OUT.write_text("\n".join(lines) + "\n")
print(f"Wrote {len(lines)} examples to {OUT}")

# Quick sanity
total = 0
for line in OUT.read_text().splitlines():
    d = json.loads(line)
    assert "prompt" in d and "nextflow_code" in d
    total += 1
print(f"All {total} JSONL lines validate")
