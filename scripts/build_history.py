#!/usr/bin/env python3.11
"""Aggregate every results/<run>/ into a single history.jsonl.

One line per directory under results/ that contains a metadata.json. Each
line captures the version pin (LLM commit/branch, framework commit, bench
commit) plus the headline metrics derived from the verdicts file(s).

Used by both the static site (docs/data/history.jsonl) and the README to
build the historical timeline of past runs.
"""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RESULTS = REPO / "results"
OUT_REPO = RESULTS / "history.jsonl"
OUT_DOCS = REPO / "docs" / "data" / "history.jsonl"


def _stats(jsonl: Path) -> dict:
    if not jsonl.exists():
        return {}
    rows = [json.loads(l) for l in jsonl.read_text().splitlines() if l.strip()]
    if not rows:
        return {}
    passed = sum(1 for r in rows if r.get("semantic_valid"))
    total = len(rows)
    return {
        "total": total,
        "passed": passed,
        "pct": round(100 * passed / total) if total else 0,
    }


def _multi_conv_stats(jsonl: Path) -> dict:
    if not jsonl.exists():
        return {}
    rows = [json.loads(l) for l in jsonl.read_text().splitlines() if l.strip()]
    by = {}
    for r in rows:
        cid = r.get("conv_id")
        if cid:
            by.setdefault(cid, []).append(r)
    if not by:
        return {}
    full = sum(1 for rs in by.values() if all(r.get("semantic_valid") for r in rs))
    return {"convs_total": len(by), "convs_full_pass": full,
            "convs_pct": round(100 * full / len(by))}


def main() -> None:
    entries: list[dict] = []
    if not RESULTS.exists():
        print(f"{RESULTS} not present")
        return

    for run_dir in sorted(RESULTS.iterdir()):
        if not run_dir.is_dir():
            continue
        meta_p = run_dir / "metadata.json"
        if not meta_p.exists():
            continue
        meta = json.loads(meta_p.read_text())
        e = {
            "run_id": run_dir.name,
            "run_started_at": meta.get("run_started_at"),
            "llm": meta.get("llm", {}),
            "framework": meta.get("framework", {}),
            "bench": meta.get("bench", {}),
            "dataset": meta.get("dataset"),
            "notes": meta.get("notes", ""),
        }
        # collect headline metrics
        single = _stats(run_dir / "verdicts.jsonl")
        if single:
            e["single_turn"] = single
        multi = _stats(run_dir / "verdicts_modifications.jsonl")
        if multi:
            e["multi_turn"] = multi | _multi_conv_stats(run_dir / "verdicts_modifications.jsonl")
        entries.append(e)

    # newest first
    entries.sort(key=lambda x: x.get("run_started_at", ""), reverse=True)

    body = "\n".join(json.dumps(e, ensure_ascii=False) for e in entries) + "\n"
    OUT_REPO.write_text(body)
    OUT_DOCS.parent.mkdir(parents=True, exist_ok=True)
    OUT_DOCS.write_text(body)

    print(f"Built history.jsonl with {len(entries)} runs")
    for e in entries:
        single = e.get("single_turn", {})
        multi  = e.get("multi_turn", {})
        print(f"  {e['run_started_at']}  {e['run_id']:50s}  "
              f"llm={e['llm'].get('short_commit', '?'):8s}  "
              f"single={single.get('passed','?')}/{single.get('total','?')}  "
              f"multi={multi.get('passed','?')}/{multi.get('total','?')}")


if __name__ == "__main__":
    main()
