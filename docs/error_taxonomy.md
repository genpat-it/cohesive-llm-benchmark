# Error taxonomy

Every LLM-generated `.nf` that fails validation is tagged with one of the
following categories. Use this guide to decide whether a failure is on
the model or on the test fixture.

| Category | Meaning | Detection | Typical fault |
|---|---|---|---|
| `none`              | No error — pipeline schedules ≥ expected processes | `n_processes >= expected_processes` | — |
| `no_code`           | The LLM never returned any `nextflow_code` | `nextflow_code` is null | LLM (the agent gave up or errored) |
| `arity_error`       | A workflow was called with the wrong number of arguments | log contains `declares N input channels but M were given` | LLM (e.g. passing one tuple-channel where the workflow expects three separate args) |
| `missing_param`     | A `param('step_*__db')` returned empty/null | log contains `missing required param:` | Fixture (the user did not supply that db path) OR LLM (it added an upstream step that needs it) |
| `missing_input`     | `cmp` / `riscd` not provided | log contains `missing required params (cmp,riscd)` | Fixture |
| `channel_emit`      | A step's `.emit` name was wrong when chaining | log contains `No such property: assembled / trimmed / …` | LLM (e.g. `.assembled` instead of shovill's actual `.assembly`) |
| `compile_error`     | Generic Groovy / DSL2 compile failure | regex on `MultipleCompilationErrorsException` etc. | LLM |
| `unknown_step`      | `include {…} from '../steps/<id>'` points at a non-existent file | regex on `Module … does not exist` / `No such file or directory:.*steps/` | LLM (hallucinated step) |
| `species_filter`    | A step's `when:` clause rejected the chosen species | regex on `isSpeciesSupported … returned false` | LLM (it picked an unsupported species for that step) |
| `ngsmanager_naming` | An input file name does not match `parseMetadataFromFileName` regex | log contains `unexpected file name:` | Fixture (your dummy file name is malformed) |
| `file_not_found`    | The expected input file is not where `getResult()` looks for it | `No files match pattern` / `file not found:` | Fixture |
| `silent_no_op`      | The pipeline runs but schedules zero process tasks | DAG has 0 placeholders even after stub-run | Mixed — see below |
| `partial_dag`       | Some but not all expected processes appear | scheduled < expected | Mixed |

## Triaging `silent_no_op`

A `silent_no_op` happens when **every** declared process is filtered by a
`when:` clause — e.g. chewbbaca's `when: getSchema(genus_species, schema)`
returning null because the species has no bundled schema.

The verdict is:

- **LLM bug** if the LLM picked an unsupported species despite the prompt
  specifying a supported one (e.g. prompt says "Listeria", LLM emits a
  step that excludes Listeria).
- **Fixture / prompt bug** if the prompt is ambiguous and the LLM made a
  reasonable choice we just didn't fund (e.g. prompt says "bacterial
  isolate", LLM picks chewbbaca, fixture's `cmp` implies an unsupported
  species).

In doubt, inspect the corresponding section of `report.md`: the
ground-truth `.nf` and the LLM's `.nf` are shown side-by-side.

## Triaging `missing_param`

A `missing_param` failure for `step_3TX_species__kmerfinder__db` (or
similar) is **almost always a fixture issue** in the strict sense: the
LLM chose a valid step, the harness simply didn't pass that step's
database path.

But it is also a useful signal about model behaviour: the LLM may be
**over-engineering** simple prompts. A prompt that says "run MLST on this
assembly" does not strictly require a species-ID step upstream — adding
one is a stylistic choice the LLM took unprompted.

If you want a stricter "LLM-only" pass rate, count `missing_param` only
when the LLM's step set differs from the ground truth (the
`extra_steps` column in the report).

## What about a 0-byte gzipped fastq?

Some steps (notably the `1PP_trimming__fastp:sample_reads_check` process)
will crash mid-pipeline when given empty reads. That is expected and
ignored by the bench: we count **scheduled** processes (placeholder rows
in Nextflow's live display), not **completed** ones.
