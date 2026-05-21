# LLM multi-turn evaluation — detailed report

Total conversations: **159**  ·  total turns: **330**  ·  per-turn pass: **287/330**  ·  conversations fully passing: **136/159**

## Pass rate by modification kind (per turn)

| kind | turns | pass |
|----|-----:|-----:|
| `add` | 104 | 95 |
| `replace` | 99 | 96 |
| `drop` | 66 | 48 |
| `switch_species` | 61 | 48 |

## Error category breakdown

| Category | Count |
|----|----:|
| `none` | 287 |
| `missing_param` | 16 |
| `partial_dag` | 14 |
| `silent_no_op` | 9 |
| `file_not_found` | 3 |
| `arity_error` | 1 |

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
| 14 | `MOD_M14_E02_switch_species_to_salmonella` | `switch_species` | ✅ | ✅ |  |
| 15 | `MOD_M15_A04_switch_species_to_ecoli` | `switch_species` | ✅ | ✅ |  |
| 16 | `MOD_M16_E07_switch_species_to_salmonella` | `switch_species` | ✅ | ✅ |  |
| 17 | `MOD_M17_D05_switch_species_to_ecoli` | `switch_species` | ✅ | ✅ |  |
| 18 | `MOD_K01_add_mlst_to_chewbbaca_lis_spades` | `add` | ✅ | ✅ |  |
| 19 | `MOD_K02_add_mlst_to_chewbbaca_sal_spades` | `add` | ✅ | ✅ |  |
| 20 | `MOD_K03_add_mlst_to_chewbbaca_eco_spades` | `add` | ✅ | ✅ |  |
| 21 | `MOD_K04_add_abricate_to_chewbbaca_lis_spades` | `add` | ✅ | ✅ |  |
| 22 | `MOD_K05_add_abricate_to_chewbbaca_sal_spades` | `add` | ✅ | ✅ |  |
| 23 | `MOD_K06_add_prokka_to_chewbbaca_lis_spades` | `add` | ✅ | ✅ |  |
| 24 | `MOD_K07_add_prokka_to_chewbbaca_sal_spades` | `add` | ✅ | ✅ |  |
| 25 | `MOD_K08_add_chewbbaca_to_mlst_lis_spades` | `add` | ✅ | ✅ |  |
| 26 | `MOD_K09_add_chewbbaca_to_mlst_eco_spades` | `add` | ✅ | ✅ |  |
| 27 | `MOD_K10_add_abricate_to_mlst_lis_spades` | `add` | ✅ | ✅ |  |
| 28 | `MOD_K11_add_abricate_to_mlst_eco_spades` | `add` | ✅ | ✅ |  |
| 29 | `MOD_K12_add_abricate_to_mlst_sal_spades` | `add` | ✅ | ✅ |  |
| 30 | `MOD_K13_add_prokka_to_mlst_lis_spades` | `add` | ✅ | ✅ |  |
| 31 | `MOD_K14_add_prokka_to_mlst_eco_spades` | `add` | ✅ | ✅ |  |
| 32 | `MOD_K15_add_prokka_to_mlst_sal_spades` | `add` | ✅ | ✅ |  |
| 33 | `MOD_K16_add_prokka_to_mlst_cam_spades` | `add` | ✅ | ✅ |  |
| 34 | `MOD_K17_add_prokka_to_abricate_lis_spades` | `add` | ✅ | ✅ |  |
| 35 | `MOD_K18_add_prokka_to_abricate_eco_spades` | `add` | ✅ | ✅ |  |
| 36 | `MOD_K19_add_mlst_to_abricate_sal_spades` | `add` | ✅ | ✅ |  |
| 37 | `MOD_K20_add_mlst_to_abricate_eco_spades` | `add` | ✅ | ✅ |  |
| 38 | `MOD_K21_add_mlst_to_flaA_cam_spades` | `add` | ✅ | ✅ |  |
| 39 | `MOD_K22_add_staramr_to_flaA_cam_spades` | `add` | ✅ | ✅ |  |
| 40 | `MOD_K23_add_abricate_to_flaA_cam_spades` | `add` | ✅ | ✅ |  |
| 41 | `MOD_K24_add_prokka_to_flaA_cam_spades` | `add` | ✅ | ✅ |  |
| 42 | `MOD_K25_add_mlst_to_staramr_cam_spades` | `add` | ✅ | ✅ |  |
| 43 | `MOD_K26_add_flaA_to_staramr_cam_spades` | `add` | ✅ | ✅ |  |
| 44 | `MOD_K27_add_abricate_to_staramr_cam_spades` | `add` | ✅ | ✅ |  |
| 45 | `MOD_K28_add_prokka_to_staramr_cam_spades` | `add` | ✅ | ✅ |  |
| 46 | `MOD_K29_add_flaA_to_mlst_cam_spades` | `add` | ✅ | ✅ |  |
| 47 | `MOD_K30_add_staramr_to_mlst_cam_spades` | `add` | ✅ | ✅ |  |
| 48 | `MOD_K31_add_abricate_to_mlst_lis_shovill` | `add` | ✅ | ✅ |  |
| 49 | `MOD_K32_add_prokka_to_mlst_sal_shovill` | `add` | ✅ | ✅ |  |
| 50 | `MOD_K33_add_abricate_to_chewbbaca_lis_unicycler` | `add` | ✅ | ✅ |  |
| 51 | `MOD_K34_add_abricate_to_chewbbaca_sal_unicycler` | `add` | ✅ | ✅ |  |
| 52 | `MOD_K35_add_chewbbaca_to_mlst_eco_shovill` | `add` | ✅ | ✅ |  |
| 53 | `MOD_K36_add_chewbbaca_to_mlst_sal_shovill` | `add` | ✅ | ✅ |  |
| 54 | `MOD_K37_add_abricate_to_mlst_lis_spades` | `add` | ✅ | ✅ |  |
| 55 | `MOD_K38_add_prokka_to_mlst_eco_spades` | `add` | ✅ | ✅ |  |
| 56 | `MOD_R01_replace_asm_spades_to_shovill_lis` | `replace` | ✅ | ✅ |  |
| 57 | `MOD_R02_replace_asm_spades_to_shovill_sal` | `replace` | ✅ | ✅ |  |
| 58 | `MOD_R03_replace_asm_spades_to_shovill_eco` | `replace` | ✅ | ✅ |  |
| 59 | `MOD_R04_replace_asm_spades_to_shovill_cam` | `replace` | ✅ | ✅ |  |
| 60 | `MOD_R05_replace_asm_spades_to_unicycler_lis` | `replace` | ✅ | ✅ |  |
| 61 | `MOD_R06_replace_asm_spades_to_unicycler_sal` | `replace` | ✅ | ✅ |  |
| 62 | `MOD_R07_replace_asm_spades_to_unicycler_cam` | `replace` | ✅ | ✅ |  |
| 63 | `MOD_R08_replace_asm_shovill_to_spades_lis` | `replace` | ✅ | ✅ |  |
| 64 | `MOD_R09_replace_asm_shovill_to_spades_eco` | `replace` | ✅ | ✅ |  |
| 65 | `MOD_R10_replace_asm_shovill_to_unicycler_lis` | `replace` | ✅ | ✅ |  |
| 66 | `MOD_R11_replace_asm_unicycler_to_spades_sal` | `replace` | ✅ | ✅ |  |
| 67 | `MOD_R12_replace_asm_unicycler_to_shovill_eco` | `replace` | ✅ | ✅ |  |
| 68 | `MOD_RT01_replace_trim_fastp_to_trimmomatic_lis` | `replace` | ✅ | ✅ |  |
| 69 | `MOD_RT02_replace_trim_fastp_to_trimmomatic_eco` | `replace` | ✅ | ✅ |  |
| 70 | `MOD_RT03_replace_trim_fastp_to_trimmomatic_sal` | `replace` | ✅ | ✅ |  |
| 71 | `MOD_RT04_replace_trim_fastp_to_trimmomatic_cam` | `replace` | ✅ | ✅ |  |
| 72 | `MOD_RT05_replace_trim_trimmomatic_to_fastp_lis` | `replace` | ✅ | ✅ |  |
| 73 | `MOD_RT06_replace_trim_trimmomatic_to_fastp_sal` | `replace` | ✅ | ✅ |  |
| 74 | `MOD_RTY01_replace_typing_mlst_to_chewbbaca_lis` | `replace` | ✅ | ✅ |  |
| 75 | `MOD_RTY02_replace_typing_mlst_to_chewbbaca_sal` | `replace` | ✅ | ✅ |  |
| 76 | `MOD_RTY03_replace_typing_mlst_to_abricate_lis` | `replace` | ✅ | ✅ |  |
| 77 | `MOD_RTY04_replace_typing_mlst_to_abricate_sal` | `replace` | ✅ | ✅ |  |
| 78 | `MOD_RTY05_replace_typing_mlst_to_prokka_lis` | `replace` | ✅ | ✅ |  |
| 79 | `MOD_RTY06_replace_typing_mlst_to_prokka_eco` | `replace` | ✅ | ✅ |  |
| 80 | `MOD_RTY07_replace_typing_chewbbaca_to_prokka_lis` | `replace` | ✅ | ✅ |  |
| 81 | `MOD_RTY08_replace_typing_chewbbaca_to_abricate_sal` | `replace` | ✅ | ✅ |  |
| 82 | `MOD_RTY09_replace_typing_abricate_to_prokka_eco` | `replace` | ✅ | ✅ |  |
| 83 | `MOD_RTY10_replace_typing_prokka_to_abricate_sal` | `replace` | ✅ | ✅ |  |
| 84 | `MOD_RTY11_replace_typing_flaA_to_mlst_cam` | `replace` | ✅ | ✅ |  |
| 85 | `MOD_RTY12_replace_typing_staramr_to_abricate_cam` | `replace` | ✅ | ✅ |  |
| 86 | `MOD_RM01_replace_mono_mlst_to_chewbbaca_sal` | `replace` | ✅ | ✅ |  |
| 87 | `MOD_RM02_replace_mono_mlst_to_chewbbaca_lis` | `replace` | ✅ | ✅ |  |
| 88 | `MOD_RM03_replace_mono_chewbbaca_to_mlst_lis` | `replace` | ✅ | ✅ |  |
| 89 | `MOD_RM04_replace_mono_chewbbaca_to_mlst_sal` | `replace` | ✅ | ✅ |  |
| 90 | `MOD_RM05_replace_mono_chewbbaca_to_abricate_lis` | `replace` | ✅ | ✅ |  |
| 91 | `MOD_RM06_replace_mono_abricate_to_prokka_eco` | `replace` | ✅ | ✅ |  |
| 92 | `MOD_RM07_replace_mono_abricate_to_mlst_sal` | `replace` | ✅ | ✅ |  |
| 93 | `MOD_RM08_replace_mono_flaA_to_staramr_cam` | `replace` | ✅ | ✅ |  |
| 94 | `MOD_RM09_replace_mono_staramr_to_flaA_cam` | `replace` | ✅ | ✅ |  |
| 95 | `MOD_RM10_replace_mono_staramr_to_mlst_cam` | `replace` | ❌ | ❌ | t1: `missing_param` |
| 96 | `MOD_D01_drop_chewbbaca_keep_mlst_lis` | `drop` | ✅ | ✅ |  |
| 97 | `MOD_D02_drop_chewbbaca_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 98 | `MOD_D03_drop_chewbbaca_keep_mlst_eco` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 99 | `MOD_D04_drop_mlst_keep_chewbbaca_lis` | `drop` | ❌ | ❌ | t1: `file_not_found` |
| 100 | `MOD_D05_drop_mlst_keep_chewbbaca_sal` | `drop` | ✅ | ❌ | t2: `partial_dag` |
| 101 | `MOD_D06_drop_abricate_keep_mlst_lis` | `drop` | ✅ | ✅ |  |
| 102 | `MOD_D07_drop_abricate_keep_mlst_eco` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 103 | `MOD_D08_drop_abricate_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 104 | `MOD_D09_drop_prokka_keep_mlst_sal` | `drop` | ✅ | ✅ |  |
| 105 | `MOD_D10_drop_prokka_keep_abricate_lis` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 106 | `MOD_D11_drop_flaA_keep_mlst_cam` | `drop` | ❌ | ✅ | t1: `missing_param` |
| 107 | `MOD_D12_drop_staramr_keep_mlst_cam` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 108 | `MOD_DA01_drop_assembly_lis` | `drop` | ✅ | ✅ |  |
| 109 | `MOD_DA02_drop_assembly_eco` | `drop` | ✅ | ✅ |  |
| 110 | `MOD_DA03_drop_assembly_sal` | `drop` | ✅ | ✅ |  |
| 111 | `MOD_DA04_drop_assembly_cam` | `drop` | ✅ | ✅ |  |
| 112 | `MOD_DM01_drop_mono_chewbbaca_keep_mlst_lis` | `drop` | ✅ | ✅ |  |
| 113 | `MOD_DM02_drop_mono_chewbbaca_keep_mlst_sal` | `drop` | ✅ | ✅ |  |
| 114 | `MOD_DM03_drop_mono_mlst_keep_chewbbaca_lis` | `drop` | ✅ | ✅ |  |
| 115 | `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco` | `drop` | ✅ | ✅ |  |
| 116 | `MOD_DM05_drop_mono_abricate_keep_mlst_sal` | `drop` | ✅ | ✅ |  |
| 117 | `MOD_DM06_drop_mono_prokka_keep_mlst_lis` | `drop` | ✅ | ✅ |  |
| 118 | `MOD_DM07_drop_mono_staramr_keep_mlst_cam` | `drop` | ✅ | ✅ |  |
| 119 | `MOD_DM08_drop_mono_staramr_keep_flaA_cam` | `drop` | ✅ | ✅ |  |
| 120 | `MOD_DM09_drop_mono_flaA_keep_staramr_cam` | `drop` | ✅ | ✅ |  |
| 121 | `MOD_DM10_drop_mono_flaA_keep_mlst_cam` | `drop` | ✅ | ✅ |  |
| 122 | `MOD_DM11_drop_mono_abricate_keep_prokka_eco` | `drop` | ✅ | ✅ |  |
| 123 | `MOD_DM12_drop_mono_prokka_keep_abricate_lis` | `drop` | ✅ | ✅ |  |
| 124 | `MOD_DM13_drop_mono_prokka_keep_mlst_sal` | `drop` | ✅ | ✅ |  |
| 125 | `MOD_DM14_drop_mono_abricate_keep_prokka_sal` | `drop` | ✅ | ✅ |  |
| 126 | `MOD_S01_cgmlst_retarget_lis_to_sal` | `switch_species` | ✅ | ✅ |  |
| 127 | `MOD_S02_cgmlst_retarget_lis_to_eco` | `switch_species` | ✅ | ❌ | t2: `file_not_found` |
| 128 | `MOD_S03_cgmlst_retarget_sal_to_lis` | `switch_species` | ✅ | ✅ |  |
| 129 | `MOD_S04_cgmlst_retarget_sal_to_eco` | `switch_species` | ✅ | ✅ |  |
| 130 | `MOD_S05_cgmlst_retarget_eco_to_lis` | `switch_species` | ✅ | ✅ |  |
| 131 | `MOD_S06_cgmlst_retarget_eco_to_sal` | `switch_species` | ✅ | ✅ |  |
| 132 | `MOD_SM01_mlst_retarget_lis_to_cam` | `switch_species` | ✅ | ✅ |  |
| 133 | `MOD_SM02_mlst_retarget_sal_to_cam` | `switch_species` | ✅ | ✅ |  |
| 134 | `MOD_SM03_mlst_retarget_eco_to_cam` | `switch_species` | ❌ | ✅ | t1: `file_not_found` |
| 135 | `MOD_SM04_mlst_retarget_cam_to_lis` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 136 | `MOD_SM05_mlst_retarget_cam_to_sal` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 137 | `MOD_SM06_mlst_retarget_cam_to_eco` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 138 | `MOD_SMA01_mlst_mono_retarget_lis_to_sal` | `switch_species` | ✅ | ✅ |  |
| 139 | `MOD_SMA02_mlst_mono_retarget_lis_to_eco` | `switch_species` | ✅ | ✅ |  |
| 140 | `MOD_SMA03_mlst_mono_retarget_sal_to_lis` | `switch_species` | ✅ | ✅ |  |
| 141 | `MOD_SMA04_mlst_mono_retarget_sal_to_eco` | `switch_species` | ✅ | ✅ |  |
| 142 | `MOD_SMA05_mlst_mono_retarget_eco_to_lis` | `switch_species` | ✅ | ✅ |  |
| 143 | `MOD_SMA06_mlst_mono_retarget_eco_to_sal` | `switch_species` | ✅ | ✅ |  |
| 144 | `MOD_SMA07_mlst_mono_retarget_lis_to_cam` | `switch_species` | ✅ | ✅ |  |
| 145 | `MOD_SMA08_mlst_mono_retarget_sal_to_cam` | `switch_species` | ✅ | ✅ |  |
| 146 | `MOD_SMA09_mlst_mono_retarget_eco_to_cam` | `switch_species` | ✅ | ✅ |  |
| 147 | `MOD_SMA10_mlst_mono_retarget_cam_to_lis` | `switch_species` | ✅ | ✅ |  |
| 148 | `MOD_3T01_addAdd_lis` | `add` | ✅ | ✅ |  |
| 149 | `MOD_3T02_addAdd_eco` | `add` | ✅ | ✅ |  |
| 150 | `MOD_3T03_addAdd_sal` | `add` | ✅ | ✅ |  |
| 151 | `MOD_3T_AD01_addThenDrop_lis` | `add` | ✅ | ❌ | t2: `arity_error` |
| 152 | `MOD_3T_AD02_addThenDrop_eco` | `add` | ❌ | ❌ | t1: `missing_param` |
| 153 | `MOD_3T_AD03_addThenDrop_sal` | `add` | ❌ | ❌ | t1: `silent_no_op` |
| 154 | `MOD_3T_RA01_replaceThenAdd_lis` | `replace` | ✅ | ✅ |  |
| 155 | `MOD_3T_RA02_replaceThenAdd_eco` | `replace` | ✅ | ✅ |  |
| 156 | `MOD_3T_RA03_replaceThenAdd_sal` | `replace` | ❌ | ✅ | t1: `silent_no_op` |
| 157 | `MOD_3T_SA01_switchThenAdd_lis_to_sal` | `switch_species` | ❌ | ❌ | t1: `partial_dag` |
| 158 | `MOD_3T_SA02_switchThenAdd_eco_to_lis` | `switch_species` | ✅ | ✅ |  |
| 159 | `MOD_3T_SA03_switchThenAdd_sal_to_eco` | `switch_species` | ❌ | ❌ | t1: `silent_no_op` |

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

### `MOD_RM10_replace_mono_staramr_to_mlst_cam_t1` — `missing_param`
**Conversation:** `MOD_RM10_replace_mono_staramr_to_mlst_cam` (replace) — turn 1
**Prompt:** Run staramr on a pre-existing Campylobacter jejuni assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4AN_AMR__staramr`
**Steps (GT):**  `step_4AN_AMR__staramr`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
workflow {
    step_4AN_AMR__staramr(getInput(), param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    kmerfinder_out = step_3TX_species__kmerfinder(getSingleInput())
    step_4AN_AMR__staramr(kmerfinder_out.assigned_species.map { [it[0], it[1]] }, kmerfinder_out.assigned_species.map { it[1] })
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_RM10_replace_mono_staramr_to_mlst_cam_t2` — `missing_param`
**Conversation:** `MOD_RM10_replace_mono_staramr_to_mlst_cam` (replace) — turn 2
**Prompt:** Use mlst on that same assembly instead.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4TY_MLST__mlst`
**Steps (GT):**  `step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    step_4TY_MLST__mlst(getInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getAssembly } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    kmerfinder_out = step_3TX_species__kmerfinder(getAssembly())
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D02_drop_chewbbaca_keep_mlst_sal_t1` — `partial_dag`
**Conversation:** `MOD_D02_drop_chewbbaca_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4TY_cgMLST__chewbbaca(spades_out.assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4TY_MLST__mlst(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 7/10 expected processes appeared in the DAG
```

### `MOD_D02_drop_chewbbaca_keep_mlst_sal_t2` — `partial_dag`
**Conversation:** `MOD_D02_drop_chewbbaca_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4TY_MLST__mlst(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 4/7 expected processes appeared in the DAG
```

### `MOD_D03_drop_chewbbaca_keep_mlst_eco_t1` — `missing_param`
**Conversation:** `MOD_D03_drop_chewbbaca_keep_mlst_eco` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4TY_MLST__mlst(assembled)
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

        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

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

### `MOD_D03_drop_chewbbaca_keep_mlst_eco_t2` — `silent_no_op`
**Conversation:** `MOD_D03_drop_chewbbaca_keep_mlst_eco` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

**Steps (LLM):** `step_2AS_mapping__bowtie, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4AN_AMR__staramr, step_4TY_MLST__mlst`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        step_2AS_mapping__bowtie(trimmed, assembly)

        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

        step_4AN_AMR__abricate(assembly)

        step_4AN_AMR__staramr(assembly, 'campylobacter')

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

### `MOD_D04_drop_mlst_keep_chewbbaca_lis_t1` — `file_not_found`
**Conversation:** `MOD_D04_drop_mlst_keep_chewbbaca_lis` (drop) — turn 1
**Prompt:** Run both mlst and chewbbaca on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca, step_2AS_denovo__spades`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { extractKey } from '../functions/common.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

def genus_species = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        assembly
        
    
    main:
        assembly.cross(genus_species) { extractKey(it) }.multiMap {
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, '')
    
}

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    module_typing_bacteria(spades_out.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch_mt/_shared_inputdir/2026/2026.LIS.224.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_D04_drop_mlst_keep_chewbbaca_lis_t2` — `partial_dag`
**Conversation:** `MOD_D04_drop_mlst_keep_chewbbaca_lis` (drop) — turn 2
**Prompt:** Drop mlst, keep only chewbbaca.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

def genusSpecies = 'Listeria monocytogenes'

def schema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4TY_cgMLST__chewbbaca(spades_out.assembled, genusSpecies, schema)
}
```
**Error excerpt:**
```
Only 6/9 expected processes appeared in the DAG
```

### `MOD_D05_drop_mlst_keep_chewbbaca_sal_t2` — `partial_dag`
**Conversation:** `MOD_D05_drop_mlst_keep_chewbbaca_sal` (drop) — turn 2
**Prompt:** Drop mlst, keep only chewbbaca.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4TY_cgMLST__chewbbaca(spades_out.assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
Only 6/9 expected processes appeared in the DAG
```

### `MOD_D07_drop_abricate_keep_mlst_eco_t1` — `partial_dag`
**Conversation:** `MOD_D07_drop_abricate_keep_mlst_eco` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__abricate(assembled)
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    assembled = step_2AS_denovo__spades(getSingleInput())
    step_4AN_AMR__abricate(assembled.assembled)
    step_4TY_MLST__mlst(assembled.assembled)
}
```
**Error excerpt:**
```
Only 5/8 expected processes appeared in the DAG
```

### `MOD_D07_drop_abricate_keep_mlst_eco_t2` — `partial_dag`
**Conversation:** `MOD_D07_drop_abricate_keep_mlst_eco` (drop) — turn 2
**Prompt:** Drop abricate, keep only mlst.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4TY_MLST__mlst(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 4/7 expected processes appeared in the DAG
```

### `MOD_D08_drop_abricate_keep_mlst_sal_t1` — `partial_dag`
**Conversation:** `MOD_D08_drop_abricate_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__abricate(assembled)
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4AN_AMR__abricate(spades_out.assembled)
    step_4TY_MLST__mlst(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 5/8 expected processes appeared in the DAG
```

### `MOD_D08_drop_abricate_keep_mlst_sal_t2` — `silent_no_op`
**Conversation:** `MOD_D08_drop_abricate_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop abricate, keep only mlst.

**Steps (LLM):** `step_4TY_MLST__mlst, step_2AS_denovo__spades`
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
    spades_out = step_2AS_denovo__spades(getSingleInput())
    module_typing_bacteria(getTrimmedReads(true), spades_out.assembled)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D10_drop_prokka_keep_abricate_lis_t1` — `partial_dag`
**Conversation:** `MOD_D10_drop_prokka_keep_abricate_lis` (drop) — turn 1
**Prompt:** Run both prokka and abricate on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_genes__prokka(assembled)
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4AN_genes__prokka(spades_out.assembled.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    step_4AN_AMR__abricate(spades_out.assembled)
    step_4TY_MLST__mlst(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 6/8 expected processes appeared in the DAG
```

### `MOD_D10_drop_prokka_keep_abricate_lis_t2` — `partial_dag`
**Conversation:** `MOD_D10_drop_prokka_keep_abricate_lis` (drop) — turn 2
**Prompt:** Drop prokka, keep only abricate.

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4AN_AMR__abricate(spades_out.assembled)
    step_4TY_MLST__mlst(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 5/7 expected processes appeared in the DAG
```

### `MOD_D11_drop_flaA_keep_mlst_cam_t1` — `missing_param`
**Conversation:** `MOD_D11_drop_flaA_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both flaA and mlst on Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_flaA__flaA(assembled, param('genus_species'))
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { module_typing_bacteria } from '../modules/module_typing_bacteria'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D12_drop_staramr_keep_mlst_cam_t1` — `partial_dag`
**Conversation:** `MOD_D12_drop_staramr_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both staramr and mlst on Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__staramr(assembled, param('genus_species'))
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_AMR__staramr(assembly, 'campylobacter')
        step_4TY_MLST__mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    module_typing_bacteria(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 5/8 expected processes appeared in the DAG
```

### `MOD_D12_drop_staramr_keep_mlst_cam_t2` — `partial_dag`
**Conversation:** `MOD_D12_drop_staramr_keep_mlst_cam` (drop) — turn 2
**Prompt:** Drop staramr, keep only mlst.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4TY_MLST__mlst(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 4/7 expected processes appeared in the DAG
```

### `MOD_S02_cgmlst_retarget_lis_to_eco_t2` — `file_not_found`
**Conversation:** `MOD_S02_cgmlst_retarget_lis_to_eco` (switch_species) — turn 2
**Prompt:** Apply the same pipeline to Escherichia coli.

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

def genus_species = 'Escherichia coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_cgMLST__chewbbaca(assembled, genus_species, null)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch_mt/_shared_inputdir/2026/2026.ECO.220.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_SM03_mlst_retarget_eco_to_cam_t1` — `file_not_found`
**Conversation:** `MOD_SM03_mlst_retarget_eco_to_cam` (switch_species) — turn 1
**Prompt:** MLST pipeline for Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_AMR__abricate, step_4AN_genes__prokka`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_preprocess_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        trimmed
        
        assembled
        
    
}

workflow wf_typing_and_amr {
    
    take:
        
        assembly
        
    
    main:
        step_4TY_MLST__mlst(assembly)
        step_4AN_AMR__abricate(assembly)
        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    wf_preprocess_and_assemble(getSingleInput())
    wf_typing_and_amr(wf_preprocess_and_assemble.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch_mt/_shared_inputdir/2026/2026.ECO.224.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_SM04_mlst_retarget_cam_to_lis_t1` — `missing_param`
**Conversation:** `MOD_SM04_mlst_retarget_cam_to_lis` (switch_species) — turn 1
**Prompt:** MLST pipeline for Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_MLST__mlst`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    species_out = step_3TX_species__kmerfinder(assembled)
    step_4TY_MLST__mlst(assembled)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_SM04_mlst_retarget_cam_to_lis_t2` — `missing_param`
**Conversation:** `MOD_SM04_mlst_retarget_cam_to_lis` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Listeria monocytogenes.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_MLST__mlst`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = step_2AS_denovo__spades(trimmed)
    species_out = step_3TX_species__kmerfinder(assembled)
    step_4TY_MLST__mlst(assembled)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_SM05_mlst_retarget_cam_to_sal_t1` — `missing_param`
**Conversation:** `MOD_SM05_mlst_retarget_cam_to_sal` (switch_species) — turn 1
**Prompt:** MLST pipeline for Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_MLST__mlst`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    kmerfinder_out = step_3TX_species__kmerfinder(assembled)
    step_4TY_MLST__mlst(assembled)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_SM05_mlst_retarget_cam_to_sal_t2` — `missing_param`
**Conversation:** `MOD_SM05_mlst_retarget_cam_to_sal` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Salmonella enterica.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_MLST__mlst`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    kmerfinder_out = step_3TX_species__kmerfinder(assembled)
    step_4TY_MLST__mlst(assembled)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_SM06_mlst_retarget_cam_to_eco_t1` — `missing_param`
**Conversation:** `MOD_SM06_mlst_retarget_cam_to_eco` (switch_species) — turn 1
**Prompt:** MLST pipeline for Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_3TX_species__kmerfinder, step_4AN_AMR__abricate`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_MLST__mlst(assembled)

    step_3TX_species__kmerfinder(assembled)

    step_4AN_AMR__abricate(assembled)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_SM06_mlst_retarget_cam_to_eco_t2` — `missing_param`
**Conversation:** `MOD_SM06_mlst_retarget_cam_to_eco` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Escherichia coli.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_3TX_species__kmerfinder`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_3TX_species__kmerfinder(assembled)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD01_addThenDrop_lis_t2` — `arity_error`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 2
**Prompt:** Also add ABRicate AMR screening in parallel.

**Steps (LLM):** `step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

        step_4AN_AMR__abricate(assembly)

        step_4TY_MLST__mlst(assembly)

        step_4TY_flaA__flaA(assembly.map { [ it[0], it[1], 'campylobacter' ] })

        step_4TY_cgMLST__chewbbaca(assembly.map { [ it[0], it[1], 'campylobacter' ] }, 'campylobacter', '')
    
}

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())

    module_typing_bacteria(spades_out.assembled)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `module_typing_bacteria:step_4TY_flaA__flaA` declares 2 input channels but 1 were given
```

### `MOD_3T_AD02_addThenDrop_eco_t1` — `missing_param`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 1
**Prompt:** cgMLST profile for Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

### `MOD_3T_AD02_addThenDrop_eco_t2` — `missing_param`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 2
**Prompt:** Also add ABRicate AMR screening in parallel.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { module_typing_bacteria } from '../modules/module_typing_bacteria'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD02_addThenDrop_eco_t3` — `missing_param`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 3
**Prompt:** Actually, drop the ABRicate step.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

### `MOD_3T_AD03_addThenDrop_sal_t1` — `silent_no_op`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 1
**Prompt:** cgMLST profile for Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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
        
        genus_species
        
    
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

### `MOD_3T_AD03_addThenDrop_sal_t2` — `silent_no_op`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 2
**Prompt:** Also add ABRicate AMR screening in parallel.

**Steps (LLM):** `step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4AN_AMR__resfinder, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
// ⚠️ WARNING: Pipeline generation failed strict DSL2 validation.
// The code above is potentially broken or incomplete and was output as a best-effort draft.

nextflow.enable.dsl=2

// --- IMPORTS ---

// --- GLOBALS ---

def referenceCode = 'NC_045512.2'

def referencePath = "${params.assets_dir}/module_covid_emergency/NC_045512.fasta"

def referenceRiscd = '220308-020220308005121273-2AS_import-external'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        step_4AN_AMR__abricate(assembly)

        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

        assembly.cross(assigned_species) { extractKey(it) }.multiMap { 
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4AN_AMR__resfinder(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, '')
    
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

### `MOD_3T_AD03_addThenDrop_sal_t3` — `silent_no_op`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 3
**Prompt:** Actually, drop the ABRicate step.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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
        
        genus_species
        
    
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

### `MOD_3T_RA03_replaceThenAdd_sal_t1` — `silent_no_op`
**Conversation:** `MOD_3T_RA03_replaceThenAdd_sal` (replace) — turn 1
**Prompt:** Trim + assemble Salmonella enterica from paired Illumina FASTQ (fastp + SPAdes).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_filtered_denovo {
    
    take:
        
        reads
        
        reference
        
    
    main:
        reads.cross(reference) { extractKey(it) }.multiMap {
            reads: it[0]
            refs:  it[1][1..3]
        }.set { readsAndReferences }

        trimmed = step_1PP_trimming__fastp(readsAndReferences.reads).trimmed
        assembled = step_2AS_denovo__spades(trimmed)
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_filtered_denovo(getSingleInput(), getReference('fa'))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_3T_SA01_switchThenAdd_lis_to_sal_t1` — `partial_dag`
**Conversation:** `MOD_3T_SA01_switchThenAdd_lis_to_sal` (switch_species) — turn 1
**Prompt:** MLST pipeline for Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4TY_MLST__mlst(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 4/7 expected processes appeared in the DAG
```

### `MOD_3T_SA01_switchThenAdd_lis_to_sal_t2` — `partial_dag`
**Conversation:** `MOD_3T_SA01_switchThenAdd_lis_to_sal` (switch_species) — turn 2
**Prompt:** Apply the same to Salmonella enterica.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4TY_MLST__mlst(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 4/7 expected processes appeared in the DAG
```

### `MOD_3T_SA01_switchThenAdd_lis_to_sal_t3` — `partial_dag`
**Conversation:** `MOD_3T_SA01_switchThenAdd_lis_to_sal` (switch_species) — turn 3
**Prompt:** Also add cgMLST in parallel for this species.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

def genus_species = 'salmonella_enterica'

def schema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4TY_MLST__mlst(spades_out.assembled)
    step_4TY_cgMLST__chewbbaca(spades_out.assembled, genus_species, schema)
}
```
**Error excerpt:**
```
Only 7/10 expected processes appeared in the DAG
```

### `MOD_3T_SA03_switchThenAdd_sal_to_eco_t1` — `silent_no_op`
**Conversation:** `MOD_3T_SA03_switchThenAdd_sal_to_eco` (switch_species) — turn 1
**Prompt:** MLST pipeline for Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

workflow wf_typing_and_amr {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
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
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    wf_typing_and_amr(trimmed, assembly)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_3T_SA03_switchThenAdd_sal_to_eco_t2` — `silent_no_op`
**Conversation:** `MOD_3T_SA03_switchThenAdd_sal_to_eco` (switch_species) — turn 2
**Prompt:** Apply the same to Escherichia coli.

**Steps (LLM):** `step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

workflow wf_typing_and_amr {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
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
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    wf_typing_and_amr(trimmed, assembled)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```
