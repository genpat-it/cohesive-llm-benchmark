#!/usr/bin/env python3.11
"""Emit the multi-turn JSONL corpora.

Writes:
  - dataset_modifications.jsonl       (the curated base 17 conversations)
  - dataset_modifications_full.jsonl  (base 17 + 142 extended = 159 conversations)
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dataset.modifications          import build_modifications           # noqa: E402
from dataset.modifications_extended import build_extended_modifications  # noqa: E402

HERE = Path(__file__).resolve().parent


def emit(path: Path, convs: list) -> None:
    lines = []
    for c in convs:
        d = c.to_serializable()
        d["validation"] = {
            "method": "nextflow -stub-run (per turn)",
            "n_turns": len(c.turns),
        }
        lines.append(json.dumps(d, ensure_ascii=False))
    path.write_text("\n".join(lines) + "\n")
    n_turns = sum(len(c.turns) for c in convs)
    print(f"Wrote {len(lines)} conversations ({n_turns} turns) to {path}")


base = build_modifications()
ext  = build_extended_modifications()
emit(HERE / "dataset_modifications.jsonl",      base)
emit(HERE / "dataset_modifications_full.jsonl", base + ext)
