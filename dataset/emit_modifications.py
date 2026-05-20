#!/usr/bin/env python3.11
"""Emit dataset_modifications.jsonl from the modifications.py blueprints.

One JSON object per conversation. The schema differs from
dataset_50.jsonl: each line carries a list of `turns`, each turn being
(prompt, nextflow_code, params, expected_processes).
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dataset.modifications import build_modifications   # noqa: E402

HERE = Path(__file__).resolve().parent
OUT = HERE / "dataset_modifications.jsonl"

convs = build_modifications()
print(f"Built {len(convs)} modification conversations")

lines = []
for c in convs:
    d = c.to_serializable()
    d["validation"] = {
        "method": "nextflow -stub-run (per turn)",
        "n_turns": len(c.turns),
    }
    lines.append(json.dumps(d, ensure_ascii=False))

OUT.write_text("\n".join(lines) + "\n")
print(f"Wrote {len(lines)} conversations to {OUT}")

# sanity
total_turns = 0
for line in OUT.read_text().splitlines():
    d = json.loads(line)
    assert "turns" in d and len(d["turns"]) >= 2
    total_turns += len(d["turns"])
print(f"Total turns: {total_turns}")
