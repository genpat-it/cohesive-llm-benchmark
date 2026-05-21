# Proposal — `/info` endpoint on `izs-llm`

For Grady (`mgradyn/izs-llm`). Two small additions that would make the
benchmark (and any future deployment) materially more observable.

## Why

Today the only metadata `izs-llm` exposes is `/health` which returns:

```json
{ "status": "online", "vector_store": "loaded" }
```

To learn the model name, the tier, or whether a 429 just hit, we have
to either trust the run's `metadata.json` (which is captured at
benchmark time, not deploy time) or hunt through environment
variables. This costs time, and during the May 21 rate-limit incident
it cost us the ability to distinguish *"the model is failing"* from
*"the upstream API is rate-limited"* until we manually `curl`ed `/chat`
with a probe.

## Proposal 1 — `/info`

Add a GET endpoint that returns the deploy's static configuration:

```json
GET /info
{
  "service":           "izs-llm",
  "version":           "0.3.1",
  "git_commit":        "73ace31",
  "model":             "labs-devstral-small-2512",
  "provider":          "mistral.ai",
  "max_turns":         4,
  "vector_store":      "loaded",
  "vector_store_size": 1234,
  "deployed_at":       "2026-05-19T10:12:00Z"
}
```

This single endpoint lets:

- the bench's `metadata.json` capture both the **client commit** and
  the **server's deployed model** (today it captures only client);
- a downstream user verify they are talking to the model they think
  they are talking to;
- monitoring tools alert on unexpected model swaps.

## Proposal 2 — surface upstream rate-limit headers

Mistral returns these headers on every response (free and paid tier):

- `x-ratelimit-limit-tokens-minute`
- `x-ratelimit-remaining-tokens-minute`
- `x-ratelimit-reset-tokens-minute` (seconds-until-reset)
- analogous `…-requests-minute` triplet

When `/chat` proxies a Mistral response — success **or** 429 — echo
those four (eight if you want both axes) in either:

- the response body, under `rate_limit: { ... }` (preferred — survives
  HTTP layer transformations); or
- response headers on the izs-llm side (cheaper but loses some clients
  through proxies)

With this, a client that gets a 429 can compute an **exact** sleep
duration rather than guessing with exponential backoff. For our
benchmark this would replace the current ~15-minute backoff budget
with the precise reset-window time, often <60 s on TPM resets.

## Proposal 3 (nice-to-have) — `/usage` snapshot

Optional. A periodically-updated `/usage` endpoint showing requests-
this-hour, tokens-this-hour, current Mistral tier, monthly cap usage.
Lets a UI render a quota meter; lets the bench abort gracefully if the
monthly cap is near exhaustion before launching another long run.

Could be implemented as a 60-second cache over Mistral's billing API
(which their dashboards already query).

## Recommended priority

1. `/info` — small (≤20 LOC), high signal, no per-request cost.
2. Rate-limit echo in `/chat` body — small (≤30 LOC), eliminates an
   entire class of run failures.
3. `/usage` — larger (caching, billing API), defer until after the
   first two land.

Happy to open a PR with `/info` + body-level rate-limit echo if you
want a starting point — they're independent and either one is a
working improvement on its own.
