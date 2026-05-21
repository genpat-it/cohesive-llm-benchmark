#!/usr/bin/env python3.11
"""Build a single ``benchmark.json`` manifest describing the whole benchmark.

External consumers (papers, dashboards, scripts) often just want one
well-typed JSON to consume the bench from. This script aggregates:

  * dataset corpora (sizes, JSONL paths)
  * every recorded run (metadata.json + summary stats from verdicts*)
  * latest tag distribution (literal-match, extras-best-practice, ...)
  * methodology / docs URLs

Output:
  ``docs/data/benchmark.json``
"""
from __future__ import annotations

import datetime as _dt
import json
from collections import Counter
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
DOCS_DATA = REPO / "docs" / "data"
RESULTS = REPO / "results"

SCHEMA_VERSION = "1.0"
BASE_URL = "https://genpat-it.github.io/cohesive-llm-benchmark"
GH_RAW = "https://raw.githubusercontent.com/genpat-it/cohesive-llm-benchmark/main"


def jsonl_count(p: Path) -> int:
    if not p.exists():
        return 0
    return sum(1 for line in p.read_text(encoding="utf-8").splitlines() if line.strip())


def load_jsonl(p: Path) -> list[dict[str, Any]]:
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def load_json(p: Path) -> dict[str, Any] | None:
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def summarize_single_turn(verdicts: list[dict[str, Any]]) -> dict[str, Any]:
    n = len(verdicts)
    if not n:
        return {"total": 0}
    passed = sum(1 for v in verdicts if v.get("semantic_valid"))
    syntax = sum(1 for v in verdicts if v.get("syntax_valid"))
    no_code = sum(1 for v in verdicts if not v.get("nextflow_code"))
    tags = Counter()
    cats = Counter()
    errs = Counter()
    for v in verdicts:
        for t in (v.get("verdict_tags") or []):
            tags[t] += 1
        cats[v.get("category", "?")] += 1
        if not v.get("semantic_valid"):
            errs[v.get("error_category") or "uncategorized"] += 1
    return {
        "total": n,
        "passed": passed,
        "passed_pct": round(100 * passed / n, 1),
        "syntax_ok": syntax,
        "no_code_returned": no_code,
        "by_category": dict(cats.most_common()),
        "by_error_category": dict(errs.most_common()),
        "by_tag": dict(tags.most_common()),
    }


def summarize_multi_turn(verdicts: list[dict[str, Any]]) -> dict[str, Any]:
    s = summarize_single_turn(verdicts)
    if not verdicts:
        return s
    by_conv: dict[str, list[bool]] = {}
    for v in verdicts:
        by_conv.setdefault(v.get("conv_id", v.get("id", "?")), []).append(
            bool(v.get("semantic_valid")))
    convs_total = len(by_conv)
    convs_full = sum(1 for r in by_conv.values() if r and all(r))
    s["conversations_total"] = convs_total
    s["conversations_fully_passed"] = convs_full
    s["conversations_fully_passed_pct"] = (
        round(100 * convs_full / convs_total, 1) if convs_total else 0.0)
    return s


def build_run_entry(run_dir: Path) -> dict[str, Any] | None:
    """One ``runs[*]`` entry merging metadata.json + verdicts summary."""
    meta = load_json(run_dir / "metadata.json")
    is_multi = (run_dir / "verdicts_modifications.jsonl").exists()
    aug = run_dir / ("verdicts_modifications_augmented.jsonl"
                     if is_multi else "verdicts_augmented.jsonl")
    raw = run_dir / ("verdicts_modifications.jsonl"
                     if is_multi else "verdicts.jsonl")
    v_path = aug if aug.exists() else raw
    verdicts = load_jsonl(v_path)
    if not verdicts and not meta:
        return None
    summary = (summarize_multi_turn(verdicts) if is_multi
               else summarize_single_turn(verdicts))
    rel_v = v_path.relative_to(REPO).as_posix() if v_path.exists() else None
    rel_meta = ((run_dir / "metadata.json").relative_to(REPO).as_posix()
                if (run_dir / "metadata.json").exists() else None)
    return {
        "run_id": run_dir.name,
        "kind": "multi-turn" if is_multi else "single-turn",
        "metadata": meta,
        "summary": summary,
        "files": {
            "verdicts_jsonl": f"{GH_RAW}/{rel_v}" if rel_v else None,
            "metadata_json": f"{GH_RAW}/{rel_meta}" if rel_meta else None,
        },
    }


def build_manifest() -> dict[str, Any]:
    datasets = {
        "single_turn_curated": {
            "path": "dataset/dataset_50.jsonl",
            "url": f"{GH_RAW}/dataset/dataset_50.jsonl",
            "size": jsonl_count(REPO / "dataset" / "dataset_50.jsonl"),
            "description": "Curated single-turn subset (stable historical baseline).",
        },
        "single_turn_full": {
            "path": "dataset/dataset_200.jsonl",
            "url": f"{GH_RAW}/dataset/dataset_200.jsonl",
            "size": jsonl_count(REPO / "dataset" / "dataset_200.jsonl"),
            "description": "200 single-turn prompts (curated 50 + 150 combinatorial extension).",
        },
        "single_turn_full_with_multi": {
            "path": "dataset/dataset_205.jsonl",
            "url": f"{GH_RAW}/dataset/dataset_205.jsonl",
            "size": jsonl_count(REPO / "dataset" / "dataset_205.jsonl"),
            "description": ("200 + 5 multi-sample workflow blueprints "
                            "(category X*: panaroo, vcf2mst, grapetree, "
                            "reportree-alleles, reportree-vcf)."),
        },
        "multi_turn_curated": {
            "path": "dataset/dataset_modifications.jsonl",
            "url": f"{GH_RAW}/dataset/dataset_modifications.jsonl",
            "size": jsonl_count(REPO / "dataset" / "dataset_modifications.jsonl"),
            "description": "17 curated multi-turn conversations (34 turns).",
        },
        "multi_turn_full": {
            "path": "dataset/dataset_modifications_full.jsonl",
            "url": f"{GH_RAW}/dataset/dataset_modifications_full.jsonl",
            "size": jsonl_count(REPO / "dataset" / "dataset_modifications_full.jsonl"),
            "description": "159 multi-turn conversations (330 turns).",
        },
    }

    runs = []
    if RESULTS.exists():
        for d in sorted(RESULTS.iterdir()):
            if not d.is_dir():
                continue
            entry = build_run_entry(d)
            if entry:
                runs.append(entry)

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "name": "cohesive-llm-benchmark",
        "description": ("End-to-end Nextflow-aware benchmark for "
                        "natural-language to bioinformatics pipeline "
                        "generators. Validates that each generated .nf "
                        "parses (DSL2) and schedules the expected number "
                        "of step processes under nextflow -stub-run."),
        "generated_at": _dt.datetime.now(_dt.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"),
        "homepage": BASE_URL,
        "repository": "https://github.com/genpat-it/cohesive-llm-benchmark",
        "framework": "https://github.com/genpat-it/cohesive-ngsmanager",
        "llm_under_test": "https://github.com/mgradyn/izs-llm",
        "docs": {
            "methodology": f"{BASE_URL}/../blob/main/METHODOLOGY.md",
            "error_taxonomy": f"{BASE_URL}/../blob/main/docs/error_taxonomy.md",
            "dataset_schema": f"{BASE_URL}/../blob/main/docs/dataset_schema.md",
            "explorer": f"{BASE_URL}/explorer.html",
        },
        "datasets": datasets,
        "verdict_tags": {
            "literal-match":
                "LLM steps match the ground truth exactly.",
            "extras-best-practice":
                ("LLM added upstream best-practice steps (trimming, species-id, "
                 "host-depletion, ...) -- biologically sound but beyond the "
                 "literal prompt."),
            "extras-irrelevant":
                "LLM added steps that are not a common best-practice add-on.",
            "missing-steps":
                "LLM left out required ground-truth steps.",
            "hallucinated":
                "LLM used step/include names that don't exist in the framework.",
        },
        "runs": runs,
    }
    return manifest


def main() -> int:
    DOCS_DATA.mkdir(parents=True, exist_ok=True)
    manifest = build_manifest()
    out = DOCS_DATA / "benchmark.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"Wrote {out.relative_to(REPO)}")
    print(f"  schema: {manifest['schema_version']}")
    print(f"  datasets: {len(manifest['datasets'])}")
    print(f"  runs: {len(manifest['runs'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
