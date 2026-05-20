# Dataset schema

## `dataset/dataset_50.jsonl` — ground-truth corpus

One JSON object per line. Every example has passed `nextflow -stub-run`
validation end-to-end against the framework at the commit pinned in
`tools/inventory_snapshot.json`.

| Field | Type | Description |
|---|---|---|
| `id`            | string | Unique example id, e.g. `E02_cgmlst_lis_fastp_spades`. Prefix encodes the category (`A`/`B`/…/`J`). |
| `category`      | string | High-level pipeline shape, e.g. `mono-typing`, `3step`, `4step`, `2step-nanopore`. |
| `prompt`        | string | Natural-language request, in English or Italian. Varies in verbosity. |
| `nextflow_code` | string | The reference `.nf` content. Validates with `nextflow -stub-run`. |
| `params`        | object | Minimum `params.json` the .nf needs. Always contains `cmp` + either `riscd` or `input:[{cmp,riscd}]`. May also carry `genus_species`, `seq_type`, step-specific db params. |
| `notes`         | string | Free-form note, e.g. "MLST classico; il take: del workflow ha solo 'assembly'". |
| `validation`    | object | `{method: "nextflow -stub-run", expected_processes: <int>}` — how many distinct process placeholders should appear in the DAG. |

### Example

```json
{
  "id": "A04_cgmlst_listeria",
  "category": "mono-typing",
  "prompt": "cgMLST allelic profile for Listeria monocytogenes from a pre-existing assembly.",
  "nextflow_code": "nextflow.enable.dsl=2\n\ninclude { getInput; optionalOrDefault; param } from '../functions/parameters.nf'\ninclude { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'\nworkflow {\n    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))\n}\n",
  "params": {
    "cmp": "2026.LIS.2.1.1",
    "input": [{"cmp": "2026.LIS.2.1.1", "riscd": "260224-99999-2AS_import-external"}],
    "genus_species": "listeria_monocytogenes"
  },
  "notes": "",
  "validation": {"method": "nextflow -stub-run", "expected_processes": 3}
}
```

---

## `dataset/dataset_modifications.jsonl` — multi-turn modification corpus

Each line is a *conversation*: a sequence of (`prompt`, `nextflow_code`)
turns simulating a user who iteratively refines a pipeline.

| Field | Type | Description |
|---|---|---|
| `id`                  | string | Conversation id, e.g. `MOD_M01_E02_add_mlst`. |
| `category`            | string | Always `"modification"` for now. |
| `base_id`             | string | The id of the single-turn example this conversation is derived from. |
| `modification_kind`   | string | One of `add`, `replace`, `drop`, `switch_species`. |
| `turns`               | list   | Ordered list of turn objects (see below). |
| `notes`               | string | Human-readable note describing the transformation. |
| `validation`          | object | `{method: "nextflow -stub-run (per turn)", n_turns: <int>}`. |

Each entry in `turns` has:

| Field | Type | Description |
|---|---|---|
| `prompt`              | string | User message for this turn. |
| `nextflow_code`       | string | The reference `.nf` after this turn. |
| `params`              | object | Params needed to validate this turn's `.nf`. |
| `expected_processes`  | int    | Process count required to pass stub-run validation for this turn. |

### Example

```json
{
  "id": "MOD_M06_D01_replace_spades_with_shovill",
  "category": "modification",
  "base_id": "D01_fastp_spades_lis",
  "modification_kind": "replace",
  "turns": [
    {
      "prompt": "From Illumina paired-end FASTQ of Listeria monocytogenes: trim with fastp and assemble with SPAdes.",
      "nextflow_code": "nextflow.enable.dsl=2\n...",
      "params": {"cmp": "2026.LIS.4.1.1", "riscd": "260224-99999-0SQ_rawreads-import", "seq_type": "illumina_paired"},
      "expected_processes": 6
    },
    {
      "prompt": "Use Shovill instead of SPAdes for the assembly.",
      "nextflow_code": "nextflow.enable.dsl=2\n...",
      "params": {"cmp": "2026.LIS.4.1.1", "riscd": "260224-99999-0SQ_rawreads-import", "seq_type": "illumina_paired"},
      "expected_processes": 6
    }
  ],
  "notes": "swap one de-novo assembler for another (emit name changes)",
  "validation": {"method": "nextflow -stub-run (per turn)", "n_turns": 2}
}
```

---

## `results/<run>/runs.jsonl` — raw LLM output per prompt

| Field | Type | Description |
|---|---|---|
| `id`                  | string | Same id as the source example |
| `prompt`              | string | Same prompt sent to the LLM |
| `ground_truth_code`   | string | The reference .nf from the dataset |
| `params`              | object | The params used during validation |
| `expected_processes`  | int    | From the dataset |
| `llm_response`        | object | `{status, nextflow_code, reply, turns, turn_logs, error}` — see below |
| `elapsed_s`           | float  | Wall-clock seconds for the round-trip |

`llm_response.turn_logs` is a list of `{turn, status, elapsed_s, has_code}`
entries — one per conversational turn the chat handshake needed.

---

## `results/<run>/verdicts.jsonl` — validated per-prompt verdict

One JSON object per line, 24 fields:

| Field | Type | Description |
|---|---|---|
| `id`                  | string | Source example id |
| `prompt`              | string | Original prompt |
| `ground_truth_code`   | string | The reference .nf |
| `params`              | object | Params used |
| `expected_processes`  | int    | Process count required to pass |
| `llm_reply_excerpt`   | string | First 300 chars of the LLM's natural-language reply |
| `nextflow_code`       | string | The LLM-generated .nf, verbatim |
| `syntax_valid`        | bool   | `true` iff `nextflow -preview` parsed it |
| `semantic_valid`      | bool   | `true` iff `nextflow -stub-run` scheduled ≥ `expected_processes` |
| `n_processes`         | int    | Distinct process placeholders observed |
| `error_category`      | string | See `error_taxonomy.md` |
| `error_detail`        | string | Last meaningful log excerpt (up to 300 chars) |
| `elapsed_s`           | float  | Wall-clock seconds for the LLM round-trip |
| `turns`               | int    | Conversational turns used by the chat handshake |
| `code_chars`          | int    | Length of the LLM .nf in characters |
| `code_lines`          | int    | Length in lines |
| `included_steps`      | list   | Step ids appearing in `include {...} from '../steps/...'` |
| `called_steps`        | list   | Step ids appearing in `step_X(...)` calls |
| `hallucinated_steps`  | list   | Step ids referenced but **not** found in the framework's `steps/` directory |
| `n_workflow_calls`    | int    | Number of step workflow invocations in the entry workflow |
| `ground_truth_steps`  | list   | Step ids called by the ground-truth .nf |
| `matches_gt_steps`    | bool   | `true` iff the LLM uses **exactly** the same step set |
| `extra_steps`         | list   | Steps in the LLM .nf that are not in the GT |
| `missing_steps`       | list   | Steps in the GT that the LLM omitted |

---

## `report.tsv` / `report.csv`

Same 24 columns as `verdicts.jsonl`, plus a derived `category` column
prefixed from the id. Newlines inside `nextflow_code` are escaped as
literal `\n` in the TSV and preserved inside RFC-4180 quoted fields in
the CSV.

---

## Naming conventions enforced

These come from the framework, not from this bench:

- **`cmp`** must follow `YYYY.<TAG>.<n>.<n>.<n>` (4-digit year, dotted
  TAG, three numeric segments). Example: `2026.LIS.1.1.1`. The first 4
  chars are the *anno* used to construct paths.
- **`riscd`** must follow `<DT_digits>-<DS_digits>-<acc>-<met>[_<ref>]`.
  Example: `260224-99999-0SQ_rawreads-import`.
- **input file names** must match
  `^(DS\d+)\D(DT\d+)_(\d{4})(\.[^.]+\.\d+\.\d+\.\d+)(_[^_]+)?.*$`.
  Example: `DS99999-DT260224_2026.LIS.1.1.1_R1.fastq.gz`.

If you add new prompts, follow these conventions verbatim — the framework
will reject anything else.
