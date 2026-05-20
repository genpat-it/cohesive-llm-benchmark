#!/usr/bin/env python3.11
"""
Validate every turn of every modification conversation via nextflow -stub-run.

Each turn is wrapped in a dataset_harness.Example and run individually.
A conversation is "valid" iff every one of its turns passes.

Usage:
    python dataset/validate_modifications.py
    python dataset/validate_modifications.py --only=MOD_M01_E02_add_mlst
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from harness.harness import Harness, run_examples, summary   # noqa: E402
from dataset.modifications import build_modifications, Turn   # noqa: E402

if __name__ == "__main__":
    convs = build_modifications()
    if "--extended" in sys.argv:
        from dataset.modifications_extended import build_extended_modifications  # noqa: E402
        convs = convs + build_extended_modifications()

    only = None
    first = None
    for a in sys.argv[1:]:
        if a.startswith("--only="):
            only = set(a.split("=", 1)[1].split(","))
        elif a.startswith("--first="):
            first = int(a.split("=", 1)[1])
    if only:
        convs = [c for c in convs if c.eid in only]
    if first is not None:
        convs = convs[:first]

    # Flatten conversations into one Example per turn for the harness.
    examples = []
    for c in convs:
        for i, t in enumerate(c.turns, start=1):
            examples.append(t.as_example(
                eid=f"{c.eid}_t{i}",
                category=f"modification.{c.modification_kind}",
                notes=c.notes,
            ))

    print(f"Validating {len(convs)} conversations = {len(examples)} turns",
          flush=True)
    verdicts = run_examples(examples)
    summary(verdicts)

    # Aggregate per-conversation
    print("\nPer-conversation result:")
    flat = {v.eid: v.passed for v in verdicts}
    n_pass = 0
    for c in convs:
        all_ok = all(flat.get(f"{c.eid}_t{i}", False)
                     for i in range(1, len(c.turns) + 1))
        n_pass += int(all_ok)
        mark = "PASS" if all_ok else "FAIL"
        print(f"  {mark}  {c.eid:50s}  kind={c.modification_kind}")
    print(f"\n  CONVERSATIONS: {n_pass}/{len(convs)} passed")
