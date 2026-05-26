#!/usr/bin/env python3.11
"""Pre-compute docs/data/dashboard.json: per-model KPI breakdowns the static
dashboard SPA renders without re-parsing the raw verdicts on every page load.

For every model present under results/, we collect:

  single_turn  → headline + by_category + by_species + by_error + by_tag
  multi_turn   → headline (turns + convs) + by_kind + by_species + by_error
               + by_tag + by_turn_index

The output is one JSON document so the browser fetches a single file.
"""

from __future__ import annotations

import datetime as dt
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RESULTS = REPO / "results"
OUT = REPO / "docs" / "data" / "dashboard.json"

# Run-dir prefixes the dashboard understands as belonging to a model evaluation.
SINGLE_TURN_PREFIX = "llm_full_200"
MULTI_TURN_PREFIX  = "llm_full_multi_turn"

# Per-id species inference (single-turn ids and multi-turn conv_ids both end
# with a species hint).
SPECIES_HINTS = [
    ("listeria",      r"(_lis(_|$)|listeria)"),
    ("ecoli",         r"(_eco(_|$)|ecoli)"),
    ("salmonella",    r"(_sal(_|$)|salmonella)"),
    ("campylobacter", r"(_cam(_|$)|campylobacter)"),
]


def species_of(eid: str) -> str:
    low = eid.lower()
    for sp, pat in SPECIES_HINTS:
        if re.search(pat, low):
            return sp
    return "other"


def category_of_single(eid: str) -> str:
    """Single-turn ids look like 'A01_mlst_listeria', 'NA08_prokka_eco_assembly'.
    The leading letter cluster (A-Z+) is the category."""
    m = re.match(r"^([A-Z]+)", eid)
    return m.group(1) if m else "?"


def load_jsonl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]


def add(counter: dict, key: str, ok: bool):
    s = counter.setdefault(key, {"total": 0, "passed": 0})
    s["total"] += 1
    if ok:
        s["passed"] += 1


def pct(passed: int, total: int) -> int:
    return round(100 * passed / total) if total else 0


def stats_single(verdicts: list[dict]) -> dict:
    by_error = Counter()
    by_category = {}
    by_species = {}
    by_tag = Counter()
    passed = 0
    for v in verdicts:
        ok = bool(v.get("semantic_valid"))
        passed += int(ok)
        by_error[v.get("error_category") or "unknown"] += 1
        add(by_category, category_of_single(v["id"]), ok)
        add(by_species, species_of(v["id"]), ok)
        # by_species also counts silent_no_op specifically (used by the heatmap)
        if v.get("error_category") == "silent_no_op":
            by_species[species_of(v["id"])].setdefault("silent_no_op", 0)
            by_species[species_of(v["id"])]["silent_no_op"] += 1
        for t in v.get("verdict_tags") or []:
            by_tag[t] += 1
    total = len(verdicts)
    return {
        "headline": {"total": total, "passed": passed, "pct": pct(passed, total)},
        "by_error":   dict(by_error.most_common()),
        "by_category": by_category,
        "by_species":  by_species,
        "by_tag":      dict(by_tag.most_common()),
    }


def stats_multi(verdicts: list[dict]) -> dict:
    by_error = Counter()
    by_kind = {}
    by_species = {}
    by_tag = Counter()
    by_turn = {}
    convs: dict[str, list[bool]] = defaultdict(list)
    passed = 0
    for v in verdicts:
        ok = bool(v.get("semantic_valid"))
        passed += int(ok)
        by_error[v.get("error_category") or "unknown"] += 1
        kind = v.get("modification_kind") or "?"
        add(by_kind, kind, ok)
        sp = species_of(v.get("conv_id") or v.get("id") or "")
        add(by_species, sp, ok)
        if v.get("error_category") == "silent_no_op":
            by_species[sp].setdefault("silent_no_op", 0)
            by_species[sp]["silent_no_op"] += 1
        for t in v.get("verdict_tags") or []:
            by_tag[t] += 1
        ti = v.get("turn_index")
        if ti is not None:
            add(by_turn, f"t{ti}", ok)
        cid = v.get("conv_id")
        if cid:
            convs[cid].append(ok)
    total = len(verdicts)
    full_pass = sum(1 for runs in convs.values() if runs and all(runs))
    return {
        "headline": {
            "turns": {"total": total, "passed": passed, "pct": pct(passed, total)},
            "convs": {"total": len(convs), "full_pass": full_pass,
                      "pct": pct(full_pass, len(convs))},
        },
        "by_error":   dict(by_error.most_common()),
        "by_kind":    by_kind,
        "by_species": by_species,
        "by_tag":     dict(by_tag.most_common()),
        "by_turn":    by_turn,
    }


def collect_models() -> list[dict]:
    """Discover every (model, single?, multi?) tuple under results/.

    Run dirs follow `llm_full_200[_<suffix>]` and `llm_full_multi_turn[_<suffix>]`
    so the suffix groups single+multi for the same model. The "no suffix" pair
    is the default model (codestral-latest in this repo).
    """
    by_suffix: dict[str, dict] = {}

    for d in sorted(RESULTS.iterdir()):
        if not d.is_dir():
            continue
        name = d.name
        if name.startswith(SINGLE_TURN_PREFIX + "_") or name == SINGLE_TURN_PREFIX:
            suffix = name[len(SINGLE_TURN_PREFIX):].lstrip("_") or "default"
            by_suffix.setdefault(suffix, {})["single_run_id"] = name
        elif name.startswith(MULTI_TURN_PREFIX + "_") or name == MULTI_TURN_PREFIX:
            suffix = name[len(MULTI_TURN_PREFIX):].lstrip("_") or "default"
            by_suffix.setdefault(suffix, {})["multi_run_id"] = name
        # ignore everything else (example_run_*, llm_multi_workflows, ci_*)

    models = []
    for suffix, runs in by_suffix.items():
        # Read the model name from whichever metadata.json is available
        st_dir = RESULTS / runs["single_run_id"] if "single_run_id" in runs else None
        mt_dir = RESULTS / runs["multi_run_id"]  if "multi_run_id"  in runs else None
        model_name = None
        for src in (st_dir, mt_dir):
            if src and (src / "metadata.json").exists():
                meta = json.loads((src / "metadata.json").read_text())
                model_name = meta.get("llm", {}).get("model")
                if model_name and model_name != "?":
                    break
        entry = {
            "key": suffix,
            "model_name": model_name or suffix,
            "single_run_id": runs.get("single_run_id"),
            "multi_run_id":  runs.get("multi_run_id"),
        }
        if st_dir:
            entry["single_turn"] = stats_single(load_jsonl(st_dir / "verdicts.jsonl"))
        if mt_dir:
            entry["multi_turn"] = stats_multi(load_jsonl(mt_dir / "verdicts_modifications.jsonl"))
        models.append(entry)

    # Order: default (codestral) first, then alphabetical by display name
    models.sort(key=lambda m: (m["key"] != "default", m["model_name"]))
    return models


def main() -> None:
    models = collect_models()
    doc = {
        "schema_version": 1,
        "generated_at": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "models": models,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, indent=2))
    print(f"Wrote {OUT.relative_to(REPO)} · {len(models)} models")
    for m in models:
        st = m.get("single_turn", {}).get("headline", {})
        mt = m.get("multi_turn", {}).get("headline", {}).get("turns", {})
        print(f"  {m['model_name']:30s} ST={st.get('passed','?')}/{st.get('total','?')}  MT={mt.get('passed','?')}/{mt.get('total','?')}")


if __name__ == "__main__":
    main()
