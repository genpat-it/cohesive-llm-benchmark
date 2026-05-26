# LLM multi-turn evaluation — detailed report

Total conversations: **159**  ·  total turns: **328**  ·  per-turn pass: **281/328**  ·  conversations fully passing: **134/159**

## Pass rate by modification kind (per turn)

| kind | turns | pass |
|----|-----:|-----:|
| `add` | 103 | 90 |
| `replace` | 99 | 97 |
| `drop` | 65 | 42 |
| `switch_species` | 61 | 52 |

## Error category breakdown

| Category | Count |
|----|----:|
| `none` | 281 |
| `missing_param` | 23 |
| `partial_dag` | 10 |
| `silent_no_op` | 6 |
| `file_not_found` | 3 |
| `no_code` | 3 |
| `ngsmanager_naming` | 2 |

## Per-conversation outcome

| # | conv_id | kind | t1 | t2 | error category (failing turn) |
|---|---------|------|----|----|------------------------------|
| 1 | `MOD_M01_E02_add_mlst` | `add` | ✅ | ✅ |  |
| 2 | `MOD_M02_D01_add_chewbbaca` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 3 | `MOD_M03_B01_add_trimming` | `add` | ✅ | ✅ |  |
| 4 | `MOD_M04_A04_add_mlst_parallel` | `add` | ✅ | ✅ |  |
| 5 | `MOD_M05_E07_add_prokka` | `add` | ❌ | ❌ | t1: `missing_param` |
| 6 | `MOD_M06_D01_replace_spades_with_shovill` | `replace` | ✅ | ✅ |  |
| 7 | `MOD_M07_D03_replace_trimmomatic_with_fastp` | `replace` | ✅ | ✅ |  |
| 8 | `MOD_M08_E01_replace_spades_with_unicycler` | `replace` | ✅ | ✅ |  |
| 9 | `MOD_M09_E07_replace_abricate_with_prokka` | `replace` | ✅ | ✅ |  |
| 10 | `MOD_M10_A05_replace_cgmlst_with_mlst` | `replace` | ✅ | ✅ |  |
| 11 | `MOD_M11_H01_drop_cgmlst` | `drop` | ❌ | ❌ | t1: `ngsmanager_naming` |
| 12 | `MOD_M12_D01_drop_assembly` | `drop` | ✅ | ✅ |  |
| 13 | `MOD_M13_I01_drop_kmerfinder` | `drop` | ✅ | ✅ |  |
| 14 | `MOD_M14_E02_switch_species_to_salmonella` | `switch_species` | ✅ | ✅ |  |
| 15 | `MOD_M15_A04_switch_species_to_ecoli` | `switch_species` | ✅ | ✅ |  |
| 16 | `MOD_M16_E07_switch_species_to_salmonella` | `switch_species` | ✅ | ✅ |  |
| 17 | `MOD_M17_D05_switch_species_to_ecoli` | `switch_species` | ❌ | ❌ | t1: `silent_no_op` |
| 18 | `MOD_K01_add_mlst_to_chewbbaca_lis_spades` | `add` | ✅ | ✅ |  |
| 19 | `MOD_K02_add_mlst_to_chewbbaca_sal_spades` | `add` | ✅ | ✅ |  |
| 20 | `MOD_K03_add_mlst_to_chewbbaca_eco_spades` | `add` | ✅ | ✅ |  |
| 21 | `MOD_K04_add_abricate_to_chewbbaca_lis_spades` | `add` | ✅ | ✅ |  |
| 22 | `MOD_K05_add_abricate_to_chewbbaca_sal_spades` | `add` | ✅ | ❌ | t2: `file_not_found` |
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
| 96 | `MOD_D01_drop_chewbbaca_keep_mlst_lis` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 97 | `MOD_D02_drop_chewbbaca_keep_mlst_sal` | `drop` | ✅ | ✅ |  |
| 98 | `MOD_D03_drop_chewbbaca_keep_mlst_eco` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 99 | `MOD_D04_drop_mlst_keep_chewbbaca_lis` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 100 | `MOD_D05_drop_mlst_keep_chewbbaca_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 101 | `MOD_D06_drop_abricate_keep_mlst_lis` | `drop` | ✅ | ✅ |  |
| 102 | `MOD_D07_drop_abricate_keep_mlst_eco` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 103 | `MOD_D08_drop_abricate_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 104 | `MOD_D09_drop_prokka_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 105 | `MOD_D12_drop_staramr_keep_mlst_cam` | `drop` | ❌ | · | t1: `no_code` |
| 106 | `MOD_DA01_drop_assembly_lis` | `drop` | ✅ | ✅ |  |
| 107 | `MOD_DA02_drop_assembly_eco` | `drop` | ✅ | ✅ |  |
| 108 | `MOD_DA03_drop_assembly_sal` | `drop` | ✅ | ✅ |  |
| 109 | `MOD_DA04_drop_assembly_cam` | `drop` | ✅ | ✅ |  |
| 110 | `MOD_DM01_drop_mono_chewbbaca_keep_mlst_lis` | `drop` | ✅ | ✅ |  |
| 111 | `MOD_DM02_drop_mono_chewbbaca_keep_mlst_sal` | `drop` | ✅ | ✅ |  |
| 112 | `MOD_DM03_drop_mono_mlst_keep_chewbbaca_lis` | `drop` | ✅ | ✅ |  |
| 113 | `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco` | `drop` | ✅ | ✅ |  |
| 114 | `MOD_DM05_drop_mono_abricate_keep_mlst_sal` | `drop` | ✅ | ✅ |  |
| 115 | `MOD_DM06_drop_mono_prokka_keep_mlst_lis` | `drop` | ✅ | ✅ |  |
| 116 | `MOD_DM07_drop_mono_staramr_keep_mlst_cam` | `drop` | ❌ | ✅ | t1: `missing_param` |
| 117 | `MOD_DM08_drop_mono_staramr_keep_flaA_cam` | `drop` | ✅ | ✅ |  |
| 118 | `MOD_DM09_drop_mono_flaA_keep_staramr_cam` | `drop` | ✅ | ✅ |  |
| 119 | `MOD_DM10_drop_mono_flaA_keep_mlst_cam` | `drop` | ❌ | ✅ | t1: `missing_param` |
| 120 | `MOD_DM11_drop_mono_abricate_keep_prokka_eco` | `drop` | ✅ | ✅ |  |
| 121 | `MOD_DM12_drop_mono_prokka_keep_abricate_lis` | `drop` | ✅ | ✅ |  |
| 122 | `MOD_DM13_drop_mono_prokka_keep_mlst_sal` | `drop` | ✅ | ✅ |  |
| 123 | `MOD_DM14_drop_mono_abricate_keep_prokka_sal` | `drop` | ✅ | ✅ |  |
| 124 | `MOD_S01_cgmlst_retarget_lis_to_sal` | `switch_species` | ✅ | ✅ |  |
| 125 | `MOD_S02_cgmlst_retarget_lis_to_eco` | `switch_species` | ✅ | ✅ |  |
| 126 | `MOD_S03_cgmlst_retarget_sal_to_lis` | `switch_species` | ✅ | ✅ |  |
| 127 | `MOD_S04_cgmlst_retarget_sal_to_eco` | `switch_species` | ✅ | ✅ |  |
| 128 | `MOD_S05_cgmlst_retarget_eco_to_lis` | `switch_species` | ✅ | ✅ |  |
| 129 | `MOD_S06_cgmlst_retarget_eco_to_sal` | `switch_species` | ✅ | ✅ |  |
| 130 | `MOD_SM01_mlst_retarget_lis_to_cam` | `switch_species` | ✅ | ✅ |  |
| 131 | `MOD_SM02_mlst_retarget_sal_to_cam` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 132 | `MOD_SM03_mlst_retarget_eco_to_cam` | `switch_species` | ✅ | ✅ |  |
| 133 | `MOD_SM04_mlst_retarget_cam_to_lis` | `switch_species` | ✅ | ✅ |  |
| 134 | `MOD_SM05_mlst_retarget_cam_to_sal` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 135 | `MOD_SM06_mlst_retarget_cam_to_eco` | `switch_species` | ✅ | ✅ |  |
| 136 | `MOD_SMA01_mlst_mono_retarget_lis_to_sal` | `switch_species` | ✅ | ✅ |  |
| 137 | `MOD_SMA02_mlst_mono_retarget_lis_to_eco` | `switch_species` | ✅ | ✅ |  |
| 138 | `MOD_SMA03_mlst_mono_retarget_sal_to_lis` | `switch_species` | ✅ | ✅ |  |
| 139 | `MOD_SMA04_mlst_mono_retarget_sal_to_eco` | `switch_species` | ✅ | ✅ |  |
| 140 | `MOD_SMA05_mlst_mono_retarget_eco_to_lis` | `switch_species` | ✅ | ✅ |  |
| 141 | `MOD_SMA06_mlst_mono_retarget_eco_to_sal` | `switch_species` | ✅ | ✅ |  |
| 142 | `MOD_SMA07_mlst_mono_retarget_lis_to_cam` | `switch_species` | ✅ | ✅ |  |
| 143 | `MOD_SMA08_mlst_mono_retarget_sal_to_cam` | `switch_species` | ✅ | ✅ |  |
| 144 | `MOD_SMA09_mlst_mono_retarget_eco_to_cam` | `switch_species` | ✅ | ✅ |  |
| 145 | `MOD_SMA10_mlst_mono_retarget_cam_to_lis` | `switch_species` | ✅ | ✅ |  |
| 146 | `MOD_3T01_addAdd_lis` | `add` | ✅ | ✅ |  |
| 147 | `MOD_3T02_addAdd_eco` | `add` | ✅ | ✅ | t3: `file_not_found` |
| 148 | `MOD_3T03_addAdd_sal` | `add` | ✅ | ✅ |  |
| 149 | `MOD_3T_AD01_addThenDrop_lis` | `add` | ❌ | ❌ | t1: `missing_param` |
| 150 | `MOD_3T_AD02_addThenDrop_eco` | `add` | ❌ | ❌ | t1: `missing_param` |
| 151 | `MOD_3T_AD03_addThenDrop_sal` | `add` | ❌ | ❌ | t1: `missing_param` |
| 152 | `MOD_3T_RA01_replaceThenAdd_lis` | `replace` | ✅ | ✅ |  |
| 153 | `MOD_3T_RA02_replaceThenAdd_eco` | `replace` | ✅ | ✅ |  |
| 154 | `MOD_3T_RA03_replaceThenAdd_sal` | `replace` | ✅ | ✅ |  |
| 155 | `MOD_3T_SA01_switchThenAdd_lis_to_sal` | `switch_species` | ✅ | ✅ |  |
| 156 | `MOD_3T_SA02_switchThenAdd_eco_to_lis` | `switch_species` | ✅ | ✅ |  |
| 157 | `MOD_3T_SA03_switchThenAdd_sal_to_eco` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 158 | `MOD_D10_drop_prokka_keep_abricate_lis` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 159 | `MOD_D11_drop_flaA_keep_mlst_cam` | `drop` | ❌ | ❌ | t1: `missing_param` |

## Failure detail (one section per failing turn)

### `MOD_M02_D01_add_chewbbaca_t2` — `file_not_found`
**Conversation:** `MOD_M02_D01_add_chewbbaca` (add) — turn 2
**Prompt:** Now also compute cgMLST allelic profiles on the resulting assembly.

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

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def genusSpecies = 'listeria_monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, genusSpecies, null)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_devstral_labs/_shared_inputdir/2026/2026.LIS.4.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_M05_E07_add_prokka_t1` — `missing_param`
**Conversation:** `MOD_M05_E07_add_prokka` (add) — turn 1
**Prompt:** Resistance gene detection with ABRicate on Escherichia coli from Illumina paired FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

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

### `MOD_M05_E07_add_prokka_t2` — `missing_param`
**Conversation:** `MOD_M05_E07_add_prokka` (add) — turn 2
**Prompt:** Also annotate the assembly with Prokka.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__abricate(assembled)
    step_4AN_genes__prokka(assembled)
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

### `MOD_M11_H01_drop_cgmlst_t1` — `ngsmanager_naming`
**Conversation:** `MOD_M11_H01_drop_cgmlst` (drop) — turn 1
**Prompt:** Run both MLST and cgMLST typing on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca, step_2AS_denovo__spades`
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

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getSingleInput } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

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

        step_4TY_cgMLST__chewbbaca(assembly, '', '')
    
}

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    module_typing_bacteria(spades_out.assembled)
}
```
**Error excerpt:**
```
ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.C.1.1_R1.fastq.gz
```

### `MOD_M11_H01_drop_cgmlst_t2` — `ngsmanager_naming`
**Conversation:** `MOD_M11_H01_drop_cgmlst` (drop) — turn 2
**Prompt:** Drop the cgMLST step, only keep MLST.

**Steps (LLM):** `step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4TY_MLST__mlst, step_2AS_denovo__spades`
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

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getSingleInput } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
    
}

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    module_typing_bacteria(spades_out.assembled)
}
```
**Error excerpt:**
```
ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.C.1.1_R1.fastq.gz
```

### `MOD_M17_D05_switch_species_to_ecoli_t1` — `silent_no_op`
**Conversation:** `MOD_M17_D05_switch_species_to_ecoli` (switch_species) — turn 1
**Prompt:** Trim and de novo assembly (fastp + SPAdes) for a paired-end Illumina Campylobacter sample.

**Steps (LLM):** `step_1PP_filtering__bowtie, step_2AS_denovo__spades`
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

include { extractKey } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_filtering__bowtie } from '../steps/step_1PP_filtering__bowtie'

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

        filtered = step_1PP_filtering__bowtie(readsAndReferences.reads, readsAndReferences.refs)
        assembled = step_2AS_denovo__spades(filtered)
    
    emit:
        
        assembled
        
        filtered
        
    
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

### `MOD_M17_D05_switch_species_to_ecoli_t2` — `silent_no_op`
**Conversation:** `MOD_M17_D05_switch_species_to_ecoli` (switch_species) — turn 2
**Prompt:** Apply the same pipeline to an Escherichia coli sample.

**Steps (LLM):** `step_1PP_filtering__bowtie, step_2AS_denovo__spades`
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

include { extractKey } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_filtering__bowtie } from '../steps/step_1PP_filtering__bowtie'

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

        filtered = step_1PP_filtering__bowtie(readsAndReferences.reads, readsAndReferences.refs)
        assembled = step_2AS_denovo__spades(filtered)
    
    emit:
        
        assembled
        
        filtered
        
    
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

### `MOD_K05_add_abricate_to_chewbbaca_sal_spades_t2` — `file_not_found`
**Conversation:** `MOD_K05_add_abricate_to_chewbbaca_sal_spades` (add) — turn 2
**Prompt:** Now also run abricate in parallel on the same assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, 'Salmonella enterica', null)
    step_4AN_AMR__abricate(assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_devstral_labs/_shared_inputdir/2026/2026.SAL.201.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
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

include { getAssembly } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    kmerfinder_out = step_3TX_species__kmerfinder(getAssembly())
    step_4AN_AMR__staramr(kmerfinder_out.assigned_species.map { [ it[0], it[1] ] }, kmerfinder_out.assigned_species.map { it[2] })
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getAssembly } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    kmerfinder_out = step_3TX_species__kmerfinder(getAssembly())
    step_4TY_MLST__mlst(kmerfinder_out.assigned_species)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D01_drop_chewbbaca_keep_mlst_lis_t1` — `missing_param`
**Conversation:** `MOD_D01_drop_chewbbaca_keep_mlst_lis` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `(none)`
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

### `MOD_D01_drop_chewbbaca_keep_mlst_lis_t2` — `silent_no_op`
**Conversation:** `MOD_D01_drop_chewbbaca_keep_mlst_lis` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D03_drop_chewbbaca_keep_mlst_eco_t1` — `partial_dag`
**Conversation:** `MOD_D03_drop_chewbbaca_keep_mlst_eco` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Escherichia coli from paired Illumina FASTQ.

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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

def genus_species = 'escherichia_coli'

def schema = 'e_coli_chewie_2360_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4TY_cgMLST__chewbbaca(spades_out.assembled, genus_species, schema)
    step_4TY_MLST__mlst(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 7/10 expected processes appeared in the DAG
```

### `MOD_D03_drop_chewbbaca_keep_mlst_eco_t2` — `partial_dag`
**Conversation:** `MOD_D03_drop_chewbbaca_keep_mlst_eco` (drop) — turn 2
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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

### `MOD_D04_drop_mlst_keep_chewbbaca_lis_t1` — `partial_dag`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        assembly
        
    
    main:
        step_4TY_MLST__mlst(assembly)
        step_4TY_cgMLST__chewbbaca(assembly, '', '')
    
}

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    module_typing_bacteria(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 7/10 expected processes appeared in the DAG
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

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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

### `MOD_D05_drop_mlst_keep_chewbbaca_sal_t1` — `missing_param`
**Conversation:** `MOD_D05_drop_mlst_keep_chewbbaca_sal` (drop) — turn 1
**Prompt:** Run both mlst and chewbbaca on Salmonella enterica from paired Illumina FASTQ.

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

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

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

### `MOD_D05_drop_mlst_keep_chewbbaca_sal_t2` — `silent_no_op`
**Conversation:** `MOD_D05_drop_mlst_keep_chewbbaca_sal` (drop) — turn 2
**Prompt:** Drop mlst, keep only chewbbaca.

**Steps (LLM):** `step_4TY_cgMLST__chewbbaca`
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

include { getAssembly } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

def genus_species = 'salmonella_enterica'

def schema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getAssembly(), genus_species, schema)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D07_drop_abricate_keep_mlst_eco_t1` — `partial_dag`
**Conversation:** `MOD_D07_drop_abricate_keep_mlst_eco` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4TY_MLST__mlst, step_2AS_denovo__spades`
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

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getSingleInput } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_AMR__abricate(assembly)

        assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] }.set { prokkaIn }
        step_4AN_genes__prokka(prokkaIn)

        assembly.map { [ it[0], it[1] ] }.set { assemblyAndSpecies }
        step_4TY_MLST__mlst(assemblyAndSpecies)
    
}

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    module_typing_bacteria(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 6/8 expected processes appeared in the DAG
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_assemble_and_analyze {
    
    take:
        
        rawreads
        
    
    main:
        assembled = step_2AS_denovo__spades(rawreads).assembled
        step_4AN_AMR__abricate(assembled)
        step_4TY_MLST__mlst(assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_assemble_and_analyze(getSingleInput())
}
```
**Error excerpt:**
```
Only 5/8 expected processes appeared in the DAG
```

### `MOD_D08_drop_abricate_keep_mlst_sal_t2` — `partial_dag`
**Conversation:** `MOD_D08_drop_abricate_keep_mlst_sal` (drop) — turn 2
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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

### `MOD_D09_drop_prokka_keep_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_D09_drop_prokka_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both prokka and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_genes__prokka(assembled)
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

### `MOD_D09_drop_prokka_keep_mlst_sal_t2` — `silent_no_op`
**Conversation:** `MOD_D09_drop_prokka_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop prokka, keep only mlst.

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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        assembly
        
    
    main:
        step_4TY_MLST__mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getAssembly())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D12_drop_staramr_keep_mlst_cam_t1` — `no_code`
**Conversation:** `MOD_D12_drop_staramr_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both staramr and mlst on Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_DM07_drop_mono_staramr_keep_mlst_cam_t1` — `missing_param`
**Conversation:** `MOD_DM07_drop_mono_staramr_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both staramr and mlst on a pre-existing Campylobacter jejuni assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_4AN_AMR__staramr, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    asm = getInput()
    step_4AN_AMR__staramr(asm, param('genus_species'))
    step_4TY_MLST__mlst(asm)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

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

### `MOD_DM10_drop_mono_flaA_keep_mlst_cam_t1` — `missing_param`
**Conversation:** `MOD_DM10_drop_mono_flaA_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both flaA and mlst on a pre-existing Campylobacter jejuni assembly.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_4TY_MLST__mlst, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    asm = getInput()
    step_4TY_flaA__flaA(asm, param('genus_species'))
    step_4TY_MLST__mlst(asm)
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

### `MOD_SM02_mlst_retarget_sal_to_cam_t1` — `missing_param`
**Conversation:** `MOD_SM02_mlst_retarget_sal_to_cam` (switch_species) — turn 1
**Prompt:** MLST pipeline for Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

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

### `MOD_SM02_mlst_retarget_sal_to_cam_t2` — `no_code`
**Conversation:** `MOD_SM02_mlst_retarget_sal_to_cam` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Campylobacter jejuni.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_SM05_mlst_retarget_cam_to_sal_t1` — `missing_param`
**Conversation:** `MOD_SM05_mlst_retarget_cam_to_sal` (switch_species) — turn 1
**Prompt:** MLST pipeline for Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `(none)`
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

### `MOD_SM05_mlst_retarget_cam_to_sal_t2` — `missing_param`
**Conversation:** `MOD_SM05_mlst_retarget_cam_to_sal` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Salmonella enterica.

**Steps (LLM):** `(none)`
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

### `MOD_3T02_addAdd_eco_t3` — `file_not_found`
**Conversation:** `MOD_3T02_addAdd_eco` (add) — turn 3
**Prompt:** Also add cgMLST in parallel.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

def genusSpecies = 'escherichia_coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4TY_cgMLST__chewbbaca(assembled, genusSpecies, null)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_devstral_labs/_shared_inputdir/2026/2026.ECO.231.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_AD01_addThenDrop_lis_t1` — `missing_param`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 1
**Prompt:** cgMLST profile for Listeria monocytogenes from paired Illumina FASTQ.

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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

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

### `MOD_3T_AD01_addThenDrop_lis_t2` — `no_code`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 2
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_3T_AD02_addThenDrop_eco_t1` — `missing_param`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 1
**Prompt:** cgMLST profile for Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca`
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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

def genus_species = 'escherichia_coli'

def schema = 'e_coli_chewie_2360_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    species_out = step_3TX_species__kmerfinder(assembled)

    step_4TY_cgMLST__chewbbaca(assembled, genus_species, schema)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD02_addThenDrop_eco_t2` — `missing_param`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 2
**Prompt:** Also add ABRicate AMR screening in parallel.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate`
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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    species_out = step_3TX_species__kmerfinder(assembled)
    step_4TY_cgMLST__chewbbaca(assembled, species_out.assigned_species.map { it[1] }, 'e_coli_chewie_2360_210531')
    step_4AN_AMR__abricate(assembled)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD02_addThenDrop_eco_t3` — `missing_param`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 3
**Prompt:** Actually, drop the ABRicate step.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca`
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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    species_out = step_3TX_species__kmerfinder(assembled)
    step_4TY_cgMLST__chewbbaca(assembled, 'escherichia_coli', null)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD03_addThenDrop_sal_t1` — `missing_param`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 1
**Prompt:** cgMLST profile for Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `(none)`
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

### `MOD_3T_AD03_addThenDrop_sal_t2` — `missing_param`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 2
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

### `MOD_3T_AD03_addThenDrop_sal_t3` — `missing_param`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 3
**Prompt:** Actually, drop the ABRicate step.

**Steps (LLM):** `(none)`
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

### `MOD_3T_SA03_switchThenAdd_sal_to_eco_t1` — `missing_param`
**Conversation:** `MOD_3T_SA03_switchThenAdd_sal_to_eco` (switch_species) — turn 1
**Prompt:** MLST pipeline for Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `(none)`
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

### `MOD_3T_SA03_switchThenAdd_sal_to_eco_t2` — `missing_param`
**Conversation:** `MOD_3T_SA03_switchThenAdd_sal_to_eco` (switch_species) — turn 2
**Prompt:** Apply the same to Escherichia coli.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

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

### `MOD_3T_SA03_switchThenAdd_sal_to_eco_t3` — `missing_param`
**Conversation:** `MOD_3T_SA03_switchThenAdd_sal_to_eco` (switch_species) — turn 3
**Prompt:** Also add cgMLST in parallel for this species.

**Steps (LLM):** `(none)`
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

### `MOD_D10_drop_prokka_keep_abricate_lis_t1` — `partial_dag`
**Conversation:** `MOD_D10_drop_prokka_keep_abricate_lis` (drop) — turn 1
**Prompt:** Run both prokka and abricate on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_genes__prokka, step_4AN_AMR__abricate`
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

include { getEmpty } from '../functions/common.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4AN_genes__prokka(spades_out.assembled.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    step_4AN_AMR__abricate(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 5/8 expected processes appeared in the DAG
```

### `MOD_D10_drop_prokka_keep_abricate_lis_t2` — `partial_dag`
**Conversation:** `MOD_D10_drop_prokka_keep_abricate_lis` (drop) — turn 2
**Prompt:** Drop prokka, keep only abricate.

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_AMR__abricate`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    spades_out = step_2AS_denovo__spades(getSingleInput())
    step_4AN_AMR__abricate(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 4/7 expected processes appeared in the DAG
```

### `MOD_D11_drop_flaA_keep_mlst_cam_t1` — `missing_param`
**Conversation:** `MOD_D11_drop_flaA_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both flaA and mlst on Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

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

### `MOD_D11_drop_flaA_keep_mlst_cam_t2` — `silent_no_op`
**Conversation:** `MOD_D11_drop_flaA_keep_mlst_cam` (drop) — turn 2
**Prompt:** Drop flaA, keep only mlst.

**Steps (LLM):** `step_2AS_mapping__bowtie, step_4TY_MLST__mlst`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        step_2AS_mapping__bowtie(trimmed, assembly)
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
