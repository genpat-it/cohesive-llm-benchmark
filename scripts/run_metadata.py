#!/usr/bin/env python3.11
"""Capture a metadata.json next to a results/<run>/ folder so any later
viewer (explorer, paper, ...) can pin exactly what was tested.

Used by eval/run_llm.py and eval/run_llm_multi_turn.py.

Example invocation:

    from scripts.run_metadata import write_metadata
    write_metadata(out_dir, llm_repo_path=os.environ.get("LLM_REPO_PATH"),
                   llm_api_url=API_URL)
"""

from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
from pathlib import Path


def _git_info(path: str | None) -> dict:
    """Return {commit, short_commit, branch, remote, dirty} for the git repo
    at `path`. None / non-existent / non-git returns empty dict."""
    if not path:
        return {}
    p = Path(path)
    if not (p / ".git").exists() and not (p.parent / ".git").exists():
        return {}
    def g(args: list[str]) -> str:
        try:
            return subprocess.check_output(["git", "-C", str(p), *args],
                                            text=True, stderr=subprocess.DEVNULL).strip()
        except Exception:
            return ""
    sha = g(["rev-parse", "HEAD"])
    if not sha:
        return {}
    return {
        "commit":       sha,
        "short_commit": sha[:7],
        "branch":       g(["rev-parse", "--abbrev-ref", "HEAD"]) or None,
        "remote":       g(["config", "--get", "remote.origin.url"]) or None,
        "dirty":        bool(g(["status", "--porcelain"])),
    }


def write_metadata(out_dir: Path,
                   llm_repo_path: str | None,
                   llm_api_url: str | None,
                   llm_name: str | None = None,
                   llm_model: str | None = None,
                   dataset_used: str | None = None,
                   extra: dict | None = None) -> Path:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    bench_repo = Path(__file__).resolve().parent.parent
    framework_dir = os.environ.get("NGSMANAGER_DIR")
    # repo_path leaks the local username and internal directory layout into a
    # public artifact. Suppress by default; set BENCH_EMIT_REPO_PATH=1 to keep
    # the field when running locally for debugging.
    emit_paths = os.environ.get("BENCH_EMIT_REPO_PATH") == "1"
    bench_info = _git_info(str(bench_repo))
    framework_info = _git_info(framework_dir)
    llm_path = llm_repo_path or os.environ.get("LLM_REPO_PATH")
    llm_info = _git_info(llm_path)
    if emit_paths:
        bench_info["repo_path"] = str(bench_repo)
        framework_info["repo_path"] = framework_dir
        llm_info["repo_path"] = llm_path
    md = {
        "run_started_at": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "bench": bench_info,
        "framework": framework_info,
        "llm": {
            "name":     llm_name or os.environ.get("LLM_NAME", "?"),
            # NOTE: this is the model NAME the LLM service is configured to
            # use, NOT necessarily what runs internally. izs-llm hard-codes
            # its model in app/core/config.py and does not expose it over
            # the wire today, so the bench cannot read it autoritatively
            # at runtime -- when LLM_MODEL is unset we record
            # "unknown_no_info_endpoint" to flag the unverified case
            # (see docs/IZS_LLM_INFO_ENDPOINT_PROPOSAL.md for the fix).
            "model":    llm_model or os.environ.get("LLM_MODEL", "unknown_no_info_endpoint"),
            "api_url":  llm_api_url,
            **llm_info,
        },
        "dataset": dataset_used,
    }
    if extra:
        md["extra"] = extra
    p = out_dir / "metadata.json"
    p.write_text(json.dumps(md, indent=2))
    print(f"[metadata] wrote {p}")
    return p


if __name__ == "__main__":
    import sys
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "./")
    write_metadata(out,
                   llm_repo_path=os.environ.get("LLM_REPO_PATH"),
                   llm_api_url=os.environ.get("LLM_API_URL"))
