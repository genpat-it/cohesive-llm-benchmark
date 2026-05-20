# LLM multi-turn evaluation — detailed report

Total conversations: **17**  ·  total turns: **34**  ·  per-turn pass: **29/34**  ·  conversations fully passing: **14/17**

## Pass rate by modification kind (per turn)

| kind | turns | pass |
|----|-----:|-----:|
| `add` | 10 | 8 |
| `replace` | 10 | 10 |
| `drop` | 6 | 4 |
| `switch_species` | 8 | 7 |

## Error category breakdown

| Category | Count |
|----|----:|
| `none` | 29 |
| `missing_param` | 3 |
| `silent_no_op` | 1 |
| `file_not_found` | 1 |

## Per-conversation outcome

| # | conv_id | kind | t1 | t2 | error category (failing turn) |
|---|---------|------|----|----|------------------------------|
| 1 | `MOD_M01_E02_add_mlst` | `add` | ✅ | ✅ |  |
| 2 | `MOD_M02_D01_add_chewbbaca` | `add` | ✅ | ✅ |  |
| 3 | `MOD_M03_B01_add_trimming` | `add` | ❌ | ❌ | t1: `missing_param` |
| 4 | `MOD_M04_A04_add_mlst_parallel` | `add` | ✅ | ✅ |  |
| 5 | `MOD_M05_E07_add_prokka` | `add` | ✅ | ✅ |  |
| 6 | `MOD_M06_D01_replace_spades_with_shovill` | `replace` | ✅ | ✅ |  |
| 7 | `MOD_M07_D03_replace_trimmomatic_with_fastp` | `replace` | ✅ | ✅ |  |
| 8 | `MOD_M08_E01_replace_spades_with_unicycler` | `replace` | ✅ | ✅ |  |
| 9 | `MOD_M09_E07_replace_abricate_with_prokka` | `replace` | ✅ | ✅ |  |
| 10 | `MOD_M10_A05_replace_cgmlst_with_mlst` | `replace` | ✅ | ✅ |  |
| 11 | `MOD_M11_H01_drop_cgmlst` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 12 | `MOD_M12_D01_drop_assembly` | `drop` | ✅ | ✅ |  |
| 13 | `MOD_M13_I01_drop_kmerfinder` | `drop` | ✅ | ✅ |  |
| 14 | `MOD_M14_E02_switch_species_to_salmonella` | `switch_species` | ❌ | ✅ | t1: `file_not_found` |
| 15 | `MOD_M15_A04_switch_species_to_ecoli` | `switch_species` | ✅ | ✅ |  |
| 16 | `MOD_M16_E07_switch_species_to_salmonella` | `switch_species` | ✅ | ✅ |  |
| 17 | `MOD_M17_D05_switch_species_to_ecoli` | `switch_species` | ✅ | ✅ |  |

## Failure detail (one section per failing turn)

### `MOD_M03_B01_add_trimming_t1` — `missing_param`
**Conversation:** `MOD_M03_B01_add_trimming` (add) — turn 1
**Prompt:** De novo genome assembly with SPAdes from Illumina paired-end reads of Listeria monocytogenes.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
**Steps (GT):**  `step_2AS_denovo__spades`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    step_2AS_denovo__spades(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_denovo {
    
    take:
        
        trimmedReads
        
        host
        
    
    main:
        trimmedReads.cross(host) { extractKey(it) }
            .map { [ it[0][0], it[0][1], it[1][1] ] }
            .branch {
                with_host: it[1][1]
                without_host: true
            }
            .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set { denovoInput }

        assembled = step_2AS_denovo__spades(denovoInput)
    
    emit:
        
        assembled
        
        depleted
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_denovo(getSingleInput(), getHost())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: hosts_dir
```

### `MOD_M03_B01_add_trimming_t2` — `missing_param`
**Conversation:** `MOD_M03_B01_add_trimming` (add) — turn 2
**Prompt:** Add a fastp trimming step before the assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getHostUnkeyed; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmedAndHost = trimmed.cross(getHostUnkeyed()) { extractKey(it) }.map { [ it[0][0], it[0][1], it[1][1] ] }
    depleted = step_1PP_hostdepl__bowtie(trimmedAndHost)

    assembled = step_2AS_denovo__spades(depleted).assembled
}
```
**Error excerpt:**
```
ERROR ~ missing required param: hosts_dir
```

### `MOD_M11_H01_drop_cgmlst_t1` — `missing_param`
**Conversation:** `MOD_M11_H01_drop_cgmlst` (drop) — turn 1
**Prompt:** Run both MLST and cgMLST typing on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        if (!params.skip_bestref_mapping) {
          trimmed.cross(assigned_species) { extractKey(it) }.multiMap {
            trimmed: it[0]
            species: it[1][1]
            referencePath: it[1][2]
          }.set { trimAndAndSpecies }
          step_2AS_mapping__bowtie(trimAndAndSpecies.trimmed, trimAndAndSpecies.referencePath)
        }

        step_4AN_AMR__abricate(assembly)

        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

        assembly.cross(assigned_species) { extractKey(it) }.multiMap {
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, '')
    
    emit:
        
        genus_species = assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_M11_H01_drop_cgmlst_t2` — `silent_no_op`
**Conversation:** `MOD_M11_H01_drop_cgmlst` (drop) — turn 2
**Prompt:** Drop the cgMLST step, only keep MLST.

**Steps (LLM):** `step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
// ⚠️ WARNING: Pipeline generation failed strict DSL2 validation.
// The code above is potentially broken or incomplete and was output as a best-effort draft.

nextflow.enable.dsl=2

// --- IMPORTS ---

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        step_4TY_MLST__mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_M14_E02_switch_species_to_salmonella_t1` — `file_not_found`
**Conversation:** `MOD_M14_E02_switch_species_to_salmonella` (switch_species) — turn 1
**Prompt:** cgMLST allelic profile for Listeria monocytogenes from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, params.genus_species, params.schema)
}
```
**Error excerpt:**
```
WARN: file not found: '/tmp/cohesive_llm_bench/_shared_inputdir/2026/2026.LIS.6.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```
