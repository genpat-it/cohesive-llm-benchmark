# Patches for `mgradyn/izs-llm`

Three concrete code-level fixes we applied locally during the May 2026
cohesive-llm-benchmark sessions. They make the service usable on Mistral
free / labs tiers (and don't hurt paid tiers). Diff: see
[`izs_llm_patches.diff`](./izs_llm_patches.diff).

## Summary

| # | File | Fix | Why |
|---|---|---|---|
| 1 | `app/services/llm.py` | `max_tokens` 128000 → 8000 | Mistral reserves max_tokens up-front against TPM. 128k > free-tier TPM ceiling triggers immediate 429 even on first call. 8k is more than enough for any Consultant/Architect output. |
| 2 | `app/services/agents.py` | `consultant_agent` and `architect_agent` chains are wrapped with `.with_retry(stop_after_attempt=6, wait_exponential_jitter=True)` AFTER `with_structured_output(...)` | The architect/repair loop can fire 5-10 internal Mistral calls per `/chat`. On free/labs tiers this saturates TPM. Retry with exponential backoff transparently absorbs transient 429s. Must be applied AFTER `with_structured_output` -- RunnableRetry has no `.with_structured_output` method. |
| 3 | `app/services/agents.py` | `time.sleep(LLM_CALL_SPACING_S)` before each Mistral `.invoke()` (consultant + architect), with `LLM_CALL_SPACING_S` env var (default 8s) | Spaces the burst over time so the rolling TPM window has room to drain. Set to 0 on Tier 1+ where the burst fits inside TPM headroom. |

## How to apply

```bash
cd /path/to/izs-llm
git apply /path/to/cohesive-llm-benchmark/docs/izs_llm_patches.diff
git diff --stat        # sanity check
```

Or do the changes manually -- the diff is small (~100 lines total).

## Recommended deployment config

Set in your deployment environment (e.g. `.env` or systemd unit):

```bash
# Free / labs Mistral tier: space out internal bursts
LLM_CALL_SPACING_S=8

# Paid Tier 1+: no spacing needed (TPM headroom is 10x)
# LLM_CALL_SPACING_S=0
```

## Test

After applying, send a /chat request with an APPROVED-style prompt that
triggers the full consultant + architect + repair path. Without the
patches the call 429s within seconds; with the patches it completes
(slower on free tier, normal on paid).

## Wider proposal

Two additional non-patch suggestions that would help any future
benchmark / monitoring tool:

* `/info` endpoint exposing `model`, `git_commit`, `vector_store_size`,
  `mistral_tier` -- so external tools can record provenance
  authoritatively instead of guessing from env vars.
* Echo upstream Mistral rate-limit headers (`x-ratelimit-*`) in the
  `/chat` JSON response under `rate_limit: {...}` so clients can
  compute exact reset windows instead of guessing.

See [`IZS_LLM_INFO_ENDPOINT_PROPOSAL.md`](./IZS_LLM_INFO_ENDPOINT_PROPOSAL.md)
for details.
