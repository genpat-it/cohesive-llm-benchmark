#!/usr/bin/env python3.11
"""
Send each of the 50 dataset prompts to the running izs-llm /chat API,
capture the generated nextflow_code, then validate each with the harness.

Produces:
  - llm_eval_runs.jsonl: one record per prompt with the LLM's response
  - llm_eval_report.md:  human summary of pass/fail counts and diffs
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

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DATASET = Path(os.environ.get("BENCH_DATASET", REPO / "dataset" / "dataset_50.jsonl"))
RUNS_DIR = Path(os.environ.get("BENCH_RUNS_DIR", HERE / "_out")).resolve()
RUNS_DIR.mkdir(parents=True, exist_ok=True)
OUT_JSONL = RUNS_DIR / "runs.jsonl"

API_URL = os.environ.get("LLM_API_URL", "http://127.0.0.1:8765").rstrip("/")
MAX_TURNS = 4
TIMEOUT_PER_CALL = 180


RATE_LIMIT_BACKOFFS = (30, 60, 120, 240, 480)  # seconds; ~15 min total budget


def _is_rate_limited(data: dict[str, Any]) -> bool:
    """Detect Mistral's 429 leaking through izs-llm's 'Consultant Agent Failed' wrapper."""
    err = (data.get("error") or "").lower()
    return (data.get("status") == "failed"
            and ("rate_limit" in err or "429" in err or "ratelimit" in err))


def ask_llm(prompt: str, session_id: str) -> dict[str, Any]:
    """Loop a conversation: send prompt, auto-approve once, return final state."""
    current = prompt
    last: dict[str, Any] = {}
    turn_logs: list[dict[str, Any]] = []

    for turn in range(MAX_TURNS):
        t0 = time.time()
        # If the backend is rate-limited by Mistral upstream, the /chat endpoint
        # itself returns 200 with status=failed; sleep & retry transparently so
        # one rate-limit blip doesn't corrupt 100+ prompts in a row.
        for backoff in RATE_LIMIT_BACKOFFS:
            try:
                r = requests.post(
                    f"{API_URL}/chat",
                    json={"session_id": session_id,
                          "message": current,
                          "generate_diagrams": False},
                    timeout=TIMEOUT_PER_CALL,
                )
            except Exception as e:
                return {"error": f"http exception: {e}", "turns": turn + 1,
                        "turn_logs": turn_logs}
            if r.status_code != 200:
                return {"error": f"http {r.status_code}: {r.text[:200]}",
                        "turns": turn + 1, "turn_logs": turn_logs}
            tentative = r.json()
            if not _is_rate_limited(tentative):
                break
            print(f"      [rate-limited; sleeping {backoff}s...]", flush=True)
            time.sleep(backoff)
        else:
            # Exhausted all backoffs; return as-is and let the run continue
            print(f"      [rate-limit persisted after {sum(RATE_LIMIT_BACKOFFS)}s; giving up on this prompt]", flush=True)
        elapsed = time.time() - t0
        data = tentative
        # Preserve the LLM's free-text reply for each turn (truncated at 4k so
        # huge code dumps don't blow up the JSONL). Without this the chat
        # history is lost and we can't audit whether the LLM, e.g., asked a
        # clarifying question we auto-approved away.
        turn_logs.append({"turn": turn + 1, "status": data.get("status"),
                          "elapsed_s": round(elapsed, 1),
                          "has_code": bool(data.get("nextflow_code")),
                          "user_message": current[:4000],
                          "llm_reply": (data.get("reply") or "")[:4000]})
        last = data
        status = data.get("status", "")

        if data.get("nextflow_code"):
            return {"status": status, "nextflow_code": data["nextflow_code"],
                    "reply": data.get("reply", ""), "turns": turn + 1,
                    "turn_logs": turn_logs}

        if status == "APPROVED":
            # status APPROVED but no code yet -- nudge once more
            current = "Generate the pipeline code now."
            continue

        # status CHATTING (or unknown): approve and retry
        current = "Yes, approve it. Proceed with exactly what you suggested."

    return {"status": last.get("status", "?"),
            "nextflow_code": last.get("nextflow_code"),
            "reply": last.get("reply", "")[:500],
            "turns": MAX_TURNS, "turn_logs": turn_logs,
            "error": "no nextflow_code after max turns" if not last.get("nextflow_code") else None}


def main() -> None:
    examples = [json.loads(l) for l in DATASET.read_text().splitlines() if l.strip()]
    only = None
    for a in sys.argv[1:]:
        if a.startswith("--only="):
            only = set(a.split("=", 1)[1].split(","))
        elif a.startswith("--first="):
            examples = examples[: int(a.split("=", 1)[1])]
    if only:
        examples = [e for e in examples if e["id"] in only]

    # Health check
    try:
        h = requests.get(f"{API_URL}/health", timeout=5)
        assert h.status_code == 200, h.text
    except Exception as e:
        print(f"API not reachable at {API_URL}: {e}")
        sys.exit(2)

    print(f"Running {len(examples)} prompts against {API_URL}")
    OUT_JSONL.unlink(missing_ok=True)

    # Record version pin (bench / framework / LLM commit) for reproducibility
    sys.path.insert(0, str(REPO))
    from scripts.run_metadata import write_metadata  # noqa: E402
    write_metadata(RUNS_DIR,
                   llm_repo_path=os.environ.get("LLM_REPO_PATH"),
                   llm_api_url=API_URL,
                   dataset_used="dataset_50.jsonl")

    n_pass_call = 0
    t_start = time.time()
    # Optional inter-prompt sleep to stay under the Mistral TPM ceiling on
    # free/labs tiers. Each /chat call consumes ~5-10k tokens; sleeping 6 s
    # between prompts caps the burst at ~10 calls/min (well under the
    # ~50-100k TPM allowance for labs-class models). Set to 0 on Tier 1+.
    prompt_sleep = float(os.environ.get("BENCH_PROMPT_SLEEP_S", "0"))
    if prompt_sleep > 0:
        print(f"  [pacing: sleeping {prompt_sleep:.1f}s between prompts]")
    with OUT_JSONL.open("a", encoding="utf-8") as out:
        for i, ex in enumerate(examples, start=1):
            eid = ex["id"]
            prompt = ex["prompt"]
            session_id = f"eval-{eid}-{uuid.uuid4().hex[:6]}"
            t0 = time.time()
            print(f"[{i:3d}/{len(examples)}] {eid:35s}  asking...", flush=True)
            res = ask_llm(prompt, session_id)
            dt = time.time() - t0
            has_code = bool(res.get("nextflow_code"))
            n_pass_call += int(has_code)
            print(f"[{i:3d}/{len(examples)}] {eid:35s}  "
                  f"{'CODE' if has_code else 'NOCODE':6s}  "
                  f"turns={res.get('turns')} ({dt:.1f}s)",
                  flush=True)
            record = {
                "id": eid,
                "prompt": prompt,
                "ground_truth_code": ex["nextflow_code"],
                "params": ex["params"],
                "expected_processes": ex["validation"]["expected_processes"],
                "llm_response": res,
                "elapsed_s": round(dt, 1),
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()
            if prompt_sleep > 0 and i < len(examples):
                time.sleep(prompt_sleep)

    total = time.time() - t_start
    print(f"\nDone. {n_pass_call}/{len(examples)} prompts returned code "
          f"(total {total/60:.1f} min).")
    print(f"Records: {OUT_JSONL}")


if __name__ == "__main__":
    main()
