# Triggering a benchmark run from `izs-llm` CI

This repo exposes a workflow,
[`llm-eval.yml`](../.github/workflows/llm-eval.yml),
that can be fired from any other GitHub repository via the
[`repository_dispatch`](https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event)
event with type `izs-llm-updated`. The intended use is:

> Every time you (Grady) push a release-worthy commit to
> [`mgradyn/izs-llm`](https://github.com/mgradyn/izs-llm), the bench
> automatically re-runs the full single-turn + multi-turn evaluation
> against that exact commit, refreshes the badges in this repo, and
> commits the new `results/ci_<timestamp>_<sha>/` folder.

---

## 1. Create a Personal Access Token (one-time)

In your GitHub account → *Settings → Developer settings → Personal access
tokens → Fine-grained tokens* generate a token with:

- **Repository access**: only `genpat-it/cohesive-llm-benchmark`
- **Permissions**: *Actions → Read and write* (everything else can stay denied)
- **Expiration**: as long as you are comfortable with (e.g. 1 year)

Copy the token (`github_pat_…`).

## 2. Add it as a secret in `izs-llm`

In `mgradyn/izs-llm` → *Settings → Secrets and variables → Actions → New
repository secret*:

- **Name**: `BENCH_DISPATCH_TOKEN`
- **Value**: the token from step 1

## 3. Add a workflow to `izs-llm`

In `mgradyn/izs-llm`, create `.github/workflows/trigger-bench.yml`:

```yaml
name: trigger cohesive-llm-benchmark

on:
  push:
    branches: [ main ]
  release:
    types: [ published ]

jobs:
  dispatch:
    runs-on: ubuntu-latest
    steps:
      - name: Send repository_dispatch
        env:
          GH_TOKEN: ${{ secrets.BENCH_DISPATCH_TOKEN }}
        run: |
          gh api -X POST \
            repos/genpat-it/cohesive-llm-benchmark/dispatches \
            -f event_type=izs-llm-updated \
            -f "client_payload[izs_llm_ref]=${GITHUB_SHA}" \
            -f "client_payload[run_label]=upstream_${GITHUB_REF_NAME}_$(echo ${GITHUB_SHA} | cut -c1-7)"
```

That's it. Each push to `main` or each published release of `izs-llm`
will now fire the bench against the *exact commit you just pushed*.

---

## 4. (Optional) Manual trigger

You can also fire the bench yourself from the command line:

```bash
gh api -X POST \
  repos/genpat-it/cohesive-llm-benchmark/dispatches \
  -f event_type=izs-llm-updated \
  -f "client_payload[izs_llm_ref]=main" \
  -f "client_payload[llm_model]=mistral-large-latest"
```

…or by clicking *Run workflow* on the
[`LLM eval`](https://github.com/genpat-it/cohesive-llm-benchmark/actions/workflows/llm-eval.yml)
page in the GitHub UI.

## What the bench needs in its own secrets

The bench needs to talk to the Mistral API on your behalf. In
`genpat-it/cohesive-llm-benchmark` → *Settings → Secrets and
variables → Actions* the maintainer of this repo configures:

- `MISTRAL_API_KEY` — a valid Mistral key.

If the secret is missing, the workflow fails fast with an explicit
error message; it does NOT silently send unauthenticated requests.

## What gets committed back

After a successful run the workflow auto-commits to `main`:

- `results/ci_<timestamp>_<sha>/runs.jsonl`,
  `runs_modifications.jsonl`, `verdicts*.jsonl`, `report*.md/.tsv/.csv`,
  `metadata.json`
- `docs/badges/*.json` — refreshed `shields.io` endpoints
- `docs/data/*.jsonl` — snapshots that the GitHub Pages explorer reads

So you'll see the badges and the live site update automatically within
the few minutes after the workflow finishes.
