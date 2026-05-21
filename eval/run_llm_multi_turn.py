#!/usr/bin/env python3.11
"""
Run the multi-turn modification dataset through the LLM.

For each conversation in dataset_modifications.jsonl, we reuse the same
session_id across all turns so the agent treats subsequent messages as
edits to the previously-proposed pipeline. Each turn is captured
separately so the downstream validator can judge them independently.

Writes:
  <BENCH_RUNS_DIR>/runs_modifications.jsonl
"""

from __future__ import annotations

import json
import os
import sys
import time
import uuid
from pathlib import Path
from typing import Any

import requests

# Reuse the single-turn ask_llm() loop for the actual chat handshake.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_llm import ask_llm   # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DATASET = Path(os.environ.get(
    "BENCH_DATASET_MOD",
    REPO / "dataset" / "dataset_modifications.jsonl",
))
RUNS_DIR = Path(os.environ.get("BENCH_RUNS_DIR", HERE / "_out")).resolve()
RUNS_DIR.mkdir(parents=True, exist_ok=True)
OUT_JSONL = RUNS_DIR / "runs_modifications.jsonl"

API_URL = os.environ.get("LLM_API_URL", "http://127.0.0.1:8765").rstrip("/")


def main() -> None:
    convs = [json.loads(l) for l in DATASET.read_text().splitlines() if l.strip()]

    only = None
    first = None
    for a in sys.argv[1:]:
        if a.startswith("--only="):
            only = set(a.split("=", 1)[1].split(","))
        elif a.startswith("--first="):
            first = int(a.split("=", 1)[1])
    if only:
        convs = [c for c in convs if c["id"] in only]
    if first is not None:
        convs = convs[:first]

    try:
        h = requests.get(f"{API_URL}/health", timeout=5)
        assert h.status_code == 200, h.text
    except Exception as e:
        print(f"API not reachable at {API_URL}: {e}")
        sys.exit(2)

    print(f"Running {len(convs)} conversations against {API_URL}", flush=True)
    OUT_JSONL.unlink(missing_ok=True)

    sys.path.insert(0, str(REPO))
    from scripts.run_metadata import write_metadata  # noqa: E402
    write_metadata(RUNS_DIR,
                   llm_repo_path=os.environ.get("LLM_REPO_PATH"),
                   llm_api_url=API_URL,
                   dataset_used="dataset_modifications.jsonl")

    n_full_pass = 0   # conversations where every turn returned code
    t_start = time.time()
    # Pacing: see run_llm.py for rationale. Applied between turns AND between
    # conversations.
    prompt_sleep = float(os.environ.get("BENCH_PROMPT_SLEEP_S", "0"))
    if prompt_sleep > 0:
        print(f"  [pacing: sleeping {prompt_sleep:.1f}s between turns/convs]", flush=True)
    with OUT_JSONL.open("a", encoding="utf-8") as out:
        for i, conv in enumerate(convs, start=1):
            cid = conv["id"]
            session_id = f"mod-{cid}-{uuid.uuid4().hex[:6]}"
            print(f"[{i:3d}/{len(convs)}] {cid:50s}  asking turn-1...",
                  flush=True)

            turn_responses: list[dict[str, Any]] = []
            all_have_code = True
            t_conv = time.time()
            for j, turn in enumerate(conv["turns"], start=1):
                t0 = time.time()
                res = ask_llm(turn["prompt"], session_id)
                dt = time.time() - t0
                has_code = bool(res.get("nextflow_code"))
                if not has_code:
                    all_have_code = False
                turn_responses.append({
                    "turn_index":     j,
                    "user_prompt":    turn["prompt"],
                    "ground_truth_code": turn["nextflow_code"],
                    "params":         turn["params"],
                    "expected_processes": turn["expected_processes"],
                    "llm_response":   res,
                    "elapsed_s":      round(dt, 1),
                })
                print(f"      turn-{j}: {'CODE' if has_code else 'NOCODE':6s}  "
                      f"({dt:.1f}s)", flush=True)
                if not has_code:
                    break   # no point pretending to refine an empty answer
                # pacing between turns of the same conversation
                if prompt_sleep > 0 and j < len(conv["turns"]):
                    time.sleep(prompt_sleep)
            dt_conv = time.time() - t_conv
            if all_have_code and len(turn_responses) == len(conv["turns"]):
                n_full_pass += 1

            record = {
                "id":                 cid,
                "category":           conv["category"],
                "base_id":            conv.get("base_id"),
                "modification_kind":  conv.get("modification_kind"),
                "session_id":         session_id,
                "n_turns_expected":   len(conv["turns"]),
                "turns":              turn_responses,
                "elapsed_s":          round(dt_conv, 1),
                "notes":              conv.get("notes", ""),
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()
            # pacing between conversations
            if prompt_sleep > 0 and i < len(convs):
                time.sleep(prompt_sleep)

    total = time.time() - t_start
    print(f"\nDone. {n_full_pass}/{len(convs)} conversations had code on every turn "
          f"(total {total/60:.1f} min).")
    print(f"Records: {OUT_JSONL}")


if __name__ == "__main__":
    main()
