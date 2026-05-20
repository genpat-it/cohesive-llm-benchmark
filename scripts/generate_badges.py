#!/usr/bin/env python3.11
"""Generate shields.io endpoint JSONs from the JSONL artifacts.

Reads:
  dataset/dataset_50.jsonl
  dataset/dataset_modifications.jsonl
  results/example_run_mistral/verdicts.jsonl                  (optional)
  results/example_run_mistral_multi_turn/verdicts_modifications.jsonl  (optional)

Writes one badge JSON per metric under docs/badges/, suitable for
shields.io's "endpoint" badge API:
    https://img.shields.io/endpoint?url=<raw-github-url-to-the-json>

Each badge JSON has the schema documented at
https://shields.io/badges/endpoint-badge
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT  = REPO / "docs" / "badges"
OUT.mkdir(parents=True, exist_ok=True)


def write_badge(name: str, label: str, message: str, color: str) -> None:
    f = OUT / f"{name}.json"
    f.write_text(json.dumps({
        "schemaVersion": 1, "label": label, "message": message, "color": color
    }))
    print(f"  {name:40s}  {label} {message}")


def color_for_pct(pct: float) -> str:
    if pct >= 95: return "brightgreen"
    if pct >= 85: return "green"
    if pct >= 70: return "yellowgreen"
    if pct >= 50: return "yellow"
    if pct >= 30: return "orange"
    return "red"


def main() -> None:
    print("Writing badges…")

    # --- dataset size ------------------------------------------------------
    # We surface the "full" corpora as the headline numbers if they exist,
    # otherwise the curated 50/17 base set.
    single_path = (REPO / "dataset" / "dataset_200.jsonl") if (REPO / "dataset" / "dataset_200.jsonl").exists() else (REPO / "dataset" / "dataset_50.jsonl")
    multi_path  = (REPO / "dataset" / "dataset_modifications_full.jsonl") if (REPO / "dataset" / "dataset_modifications_full.jsonl").exists() else (REPO / "dataset" / "dataset_modifications.jsonl")

    n_single  = sum(1 for _ in single_path.open())
    n_convs   = sum(1 for _ in multi_path.open())
    n_turns   = 0
    for line in multi_path.open():
        d = json.loads(line)
        n_turns += len(d.get("turns", []))

    write_badge("dataset_single",     "single-turn", f"{n_single}",            "informational")
    write_badge("dataset_multi",      "multi-turn",  f"{n_convs} convos · {n_turns} turns", "informational")

    # --- LLM eval scores ----------------------------------------------------
    # Prefer the full-corpus run (llm_full_200) over the curated 50 subset.
    sf = REPO / "results" / "llm_full_200" / "verdicts.jsonl"
    if not sf.exists():
        sf = REPO / "results" / "example_run_mistral" / "verdicts.jsonl"

    mf = REPO / "results" / "llm_full_200" / "verdicts_modifications.jsonl"
    if not mf.exists():
        mf = REPO / "results" / "example_run_mistral_multi_turn" / "verdicts_modifications.jsonl"

    if sf.exists():
        rows = [json.loads(l) for l in sf.read_text().splitlines() if l.strip()]
        passed = sum(1 for r in rows if r.get("semantic_valid"))
        pct = round(100 * passed / len(rows)) if rows else 0
        write_badge("llm_single_turn",
                    "izs-llm · single-turn",
                    f"{passed}/{len(rows)} ({pct}%)",
                    color_for_pct(pct))

    if mf.exists():
        rows = [json.loads(l) for l in mf.read_text().splitlines() if l.strip()]
        passed = sum(1 for r in rows if r.get("semantic_valid"))
        pct = round(100 * passed / len(rows)) if rows else 0
        # also full-conversation pass rate
        by = {}
        for r in rows:
            by.setdefault(r["conv_id"], []).append(r)
        full = sum(1 for rs in by.values() if all(r["semantic_valid"] for r in rs))
        write_badge("llm_multi_turn",
                    "izs-llm · multi-turn (turns)",
                    f"{passed}/{len(rows)} ({pct}%)",
                    color_for_pct(pct))
        cpct = round(100 * full / len(by)) if by else 0
        write_badge("llm_multi_turn_convos",
                    "izs-llm · multi-turn (convos)",
                    f"{full}/{len(by)} ({cpct}%)",
                    color_for_pct(cpct))

    print(f"Wrote badges to {OUT}")


if __name__ == "__main__":
    main()
