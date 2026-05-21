#!/usr/bin/env python3.11
"""Emit the single-turn JSONL corpora from already-validated blueprints.

Writes:
  - dataset_50.jsonl   (the curated base 50)
  - dataset_200.jsonl  (base 50 + 150 extended)
  - dataset_205.jsonl  (200 + 5 multi-sample workflow blueprints, category X*)
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dataset.blueprints           import build_all              # noqa: E402
from dataset.blueprints_extended  import build_extended         # noqa: E402
from dataset.blueprints_multi     import build_multi_workflows  # noqa: E402

HERE = Path(__file__).resolve().parent


def emit(path: Path, examples: list) -> None:
    lines = []
    for ex in examples:
        d = ex.to_serializable()
        d["validation"] = {
            "method": "nextflow -stub-run",
            "expected_processes": ex.expected_processes,
        }
        lines.append(json.dumps(d, ensure_ascii=False))
    path.write_text("\n".join(lines) + "\n")
    print(f"Wrote {len(lines)} examples to {path}")


base = build_all()
ext  = build_extended()
multi = build_multi_workflows()
emit(HERE / "dataset_50.jsonl",  base)
emit(HERE / "dataset_200.jsonl", base + ext)
emit(HERE / "dataset_205.jsonl", base + ext + multi)
