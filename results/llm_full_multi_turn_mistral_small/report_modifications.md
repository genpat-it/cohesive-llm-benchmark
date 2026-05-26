# LLM multi-turn evaluation — detailed report

Total conversations: **159**  ·  total turns: **329**  ·  per-turn pass: **222/329**  ·  conversations fully passing: **88/159**

## Pass rate by modification kind (per turn)

| kind | turns | pass |
|----|-----:|-----:|
| `add` | 104 | 75 |
| `replace` | 98 | 82 |
| `drop` | 66 | 30 |
| `switch_species` | 61 | 35 |

## Error category breakdown

| Category | Count |
|----|----:|
| `none` | 201 |
| `missing_param` | 55 |
| `file_not_found` | 34 |
| `no_code` | 13 |
| `arity_error` | 13 |
| `silent_no_op` | 10 |
| `channel_emit` | 2 |
| `partial_dag` | 1 |

## Per-conversation outcome

| # | conv_id | kind | t1 | t2 | error category (failing turn) |
|---|---------|------|----|----|------------------------------|
| 1 | `MOD_M01_E02_add_mlst` | `add` | ✅ | ✅ |  |
| 2 | `MOD_M02_D01_add_chewbbaca` | `add` | ✅ | ❌ | t2: `partial_dag` |
| 3 | `MOD_M03_B01_add_trimming` | `add` | ✅ | ❌ | t2: `no_code` |
| 4 | `MOD_M04_A04_add_mlst_parallel` | `add` | ✅ | ❌ | t2: `silent_no_op` |
| 5 | `MOD_M05_E07_add_prokka` | `add` | ✅ | ✅ |  |
| 6 | `MOD_M06_D01_replace_spades_with_shovill` | `replace` | ✅ | ✅ |  |
| 7 | `MOD_M07_D03_replace_trimmomatic_with_fastp` | `replace` | ✅ | ❌ | t2: `silent_no_op` |
| 8 | `MOD_M08_E01_replace_spades_with_unicycler` | `replace` | ✅ | ✅ |  |
| 9 | `MOD_M09_E07_replace_abricate_with_prokka` | `replace` | ❌ | ❌ | t1: `silent_no_op` |
| 10 | `MOD_M10_A05_replace_cgmlst_with_mlst` | `replace` | ✅ | ✅ |  |
| 11 | `MOD_M11_H01_drop_cgmlst` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 12 | `MOD_M12_D01_drop_assembly` | `drop` | ✅ | ✅ |  |
| 13 | `MOD_M13_I01_drop_kmerfinder` | `drop` | ❌ | ❌ | t1: `file_not_found` |
| 14 | `MOD_M14_E02_switch_species_to_salmonella` | `switch_species` | ✅ | ❌ | t2: `silent_no_op` |
| 15 | `MOD_M15_A04_switch_species_to_ecoli` | `switch_species` | ✅ | ✅ |  |
| 16 | `MOD_M16_E07_switch_species_to_salmonella` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 17 | `MOD_M17_D05_switch_species_to_ecoli` | `switch_species` | ✅ | ❌ | t2: `arity_error` |
| 18 | `MOD_K01_add_mlst_to_chewbbaca_lis_spades` | `add` | ✅ | ✅ |  |
| 19 | `MOD_K02_add_mlst_to_chewbbaca_sal_spades` | `add` | ✅ | ✅ |  |
| 20 | `MOD_K03_add_mlst_to_chewbbaca_eco_spades` | `add` | ✅ | ✅ |  |
| 21 | `MOD_K04_add_abricate_to_chewbbaca_lis_spades` | `add` | ✅ | ✅ |  |
| 22 | `MOD_K05_add_abricate_to_chewbbaca_sal_spades` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 23 | `MOD_K06_add_prokka_to_chewbbaca_lis_spades` | `add` | ✅ | ❌ | t2: `no_code` |
| 24 | `MOD_K07_add_prokka_to_chewbbaca_sal_spades` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 25 | `MOD_K08_add_chewbbaca_to_mlst_lis_spades` | `add` | ✅ | ✅ |  |
| 26 | `MOD_K09_add_chewbbaca_to_mlst_eco_spades` | `add` | ✅ | ✅ |  |
| 27 | `MOD_K10_add_abricate_to_mlst_lis_spades` | `add` | ✅ | ✅ |  |
| 28 | `MOD_K11_add_abricate_to_mlst_eco_spades` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 29 | `MOD_K12_add_abricate_to_mlst_sal_spades` | `add` | ✅ | ❌ | t2: `arity_error` |
| 30 | `MOD_K13_add_prokka_to_mlst_lis_spades` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 31 | `MOD_K14_add_prokka_to_mlst_eco_spades` | `add` | ✅ | ✅ |  |
| 32 | `MOD_K15_add_prokka_to_mlst_sal_spades` | `add` | ❌ | ✅ | t1: `arity_error` |
| 33 | `MOD_K16_add_prokka_to_mlst_cam_spades` | `add` | ✅ | ✅ |  |
| 34 | `MOD_K17_add_prokka_to_abricate_lis_spades` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 35 | `MOD_K18_add_prokka_to_abricate_eco_spades` | `add` | ✅ | ❌ | t2: `no_code` |
| 36 | `MOD_K19_add_mlst_to_abricate_sal_spades` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 37 | `MOD_K20_add_mlst_to_abricate_eco_spades` | `add` | ✅ | ❌ | t2: `no_code` |
| 38 | `MOD_K21_add_mlst_to_flaA_cam_spades` | `add` | ✅ | ✅ |  |
| 39 | `MOD_K22_add_staramr_to_flaA_cam_spades` | `add` | ✅ | ❌ | t2: `no_code` |
| 40 | `MOD_K23_add_abricate_to_flaA_cam_spades` | `add` | ✅ | ✅ |  |
| 41 | `MOD_K24_add_prokka_to_flaA_cam_spades` | `add` | ✅ | ✅ |  |
| 42 | `MOD_K25_add_mlst_to_staramr_cam_spades` | `add` | ✅ | ✅ |  |
| 43 | `MOD_K26_add_flaA_to_staramr_cam_spades` | `add` | ✅ | ✅ |  |
| 44 | `MOD_K27_add_abricate_to_staramr_cam_spades` | `add` | ✅ | ✅ |  |
| 45 | `MOD_K28_add_prokka_to_staramr_cam_spades` | `add` | ✅ | ✅ |  |
| 46 | `MOD_K29_add_flaA_to_mlst_cam_spades` | `add` | ✅ | ✅ |  |
| 47 | `MOD_K30_add_staramr_to_mlst_cam_spades` | `add` | ✅ | ✅ |  |
| 48 | `MOD_K31_add_abricate_to_mlst_lis_shovill` | `add` | ✅ | ✅ |  |
| 49 | `MOD_K32_add_prokka_to_mlst_sal_shovill` | `add` | ❌ | ❌ | t1: `arity_error` |
| 50 | `MOD_K33_add_abricate_to_chewbbaca_lis_unicycler` | `add` | ✅ | ✅ |  |
| 51 | `MOD_K34_add_abricate_to_chewbbaca_sal_unicycler` | `add` | ✅ | ✅ |  |
| 52 | `MOD_K35_add_chewbbaca_to_mlst_eco_shovill` | `add` | ✅ | ✅ |  |
| 53 | `MOD_K36_add_chewbbaca_to_mlst_sal_shovill` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 54 | `MOD_K37_add_abricate_to_mlst_lis_spades` | `add` | ✅ | ✅ |  |
| 55 | `MOD_K38_add_prokka_to_mlst_eco_spades` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 56 | `MOD_R01_replace_asm_spades_to_shovill_lis` | `replace` | ✅ | ✅ |  |
| 57 | `MOD_R02_replace_asm_spades_to_shovill_sal` | `replace` | ✅ | ❌ | t2: `file_not_found` |
| 58 | `MOD_R03_replace_asm_spades_to_shovill_eco` | `replace` | ✅ | ✅ |  |
| 59 | `MOD_R04_replace_asm_spades_to_shovill_cam` | `replace` | ✅ | ✅ |  |
| 60 | `MOD_R05_replace_asm_spades_to_unicycler_lis` | `replace` | ❌ | ❌ | t1: `arity_error` |
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
| 80 | `MOD_RTY07_replace_typing_chewbbaca_to_prokka_lis` | `replace` | ❌ | ❌ | t1: `silent_no_op` |
| 81 | `MOD_RTY08_replace_typing_chewbbaca_to_abricate_sal` | `replace` | ✅ | ✅ |  |
| 82 | `MOD_RTY09_replace_typing_abricate_to_prokka_eco` | `replace` | ❌ | ✅ | t1: `silent_no_op` |
| 83 | `MOD_RTY10_replace_typing_prokka_to_abricate_sal` | `replace` | ✅ | ❌ | t2: `no_code` |
| 84 | `MOD_RTY11_replace_typing_flaA_to_mlst_cam` | `replace` | ✅ | ✅ |  |
| 85 | `MOD_RTY12_replace_typing_staramr_to_abricate_cam` | `replace` | ✅ | ✅ |  |
| 86 | `MOD_RM01_replace_mono_mlst_to_chewbbaca_sal` | `replace` | ✅ | ✅ |  |
| 87 | `MOD_RM02_replace_mono_mlst_to_chewbbaca_lis` | `replace` | ✅ | ✅ |  |
| 88 | `MOD_RM03_replace_mono_chewbbaca_to_mlst_lis` | `replace` | ❌ | ✅ | t1: `missing_param` |
| 89 | `MOD_RM04_replace_mono_chewbbaca_to_mlst_sal` | `replace` | ❌ | ❌ | t1: `missing_param` |
| 90 | `MOD_RM05_replace_mono_chewbbaca_to_abricate_lis` | `replace` | ✅ | ✅ |  |
| 91 | `MOD_RM06_replace_mono_abricate_to_prokka_eco` | `replace` | ✅ | ✅ |  |
| 92 | `MOD_RM07_replace_mono_abricate_to_mlst_sal` | `replace` | ✅ | ✅ |  |
| 93 | `MOD_RM08_replace_mono_flaA_to_staramr_cam` | `replace` | ✅ | ✅ |  |
| 94 | `MOD_RM09_replace_mono_staramr_to_flaA_cam` | `replace` | ✅ | ❌ | t2: `missing_param` |
| 95 | `MOD_RM10_replace_mono_staramr_to_mlst_cam` | `replace` | ✅ | ✅ |  |
| 96 | `MOD_D01_drop_chewbbaca_keep_mlst_lis` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 97 | `MOD_D02_drop_chewbbaca_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 98 | `MOD_D03_drop_chewbbaca_keep_mlst_eco` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 99 | `MOD_D04_drop_mlst_keep_chewbbaca_lis` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 100 | `MOD_D05_drop_mlst_keep_chewbbaca_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 101 | `MOD_D06_drop_abricate_keep_mlst_lis` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 102 | `MOD_D07_drop_abricate_keep_mlst_eco` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 103 | `MOD_D08_drop_abricate_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 104 | `MOD_D09_drop_prokka_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 105 | `MOD_D10_drop_prokka_keep_abricate_lis` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 106 | `MOD_D11_drop_flaA_keep_mlst_cam` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 107 | `MOD_D12_drop_staramr_keep_mlst_cam` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 108 | `MOD_DA01_drop_assembly_lis` | `drop` | ✅ | ✅ |  |
| 109 | `MOD_DA02_drop_assembly_eco` | `drop` | ✅ | ✅ |  |
| 110 | `MOD_DA03_drop_assembly_sal` | `drop` | ❌ | ✅ | t1: `arity_error` |
| 111 | `MOD_DA04_drop_assembly_cam` | `drop` | ✅ | ✅ |  |
| 112 | `MOD_DM01_drop_mono_chewbbaca_keep_mlst_lis` | `drop` | ✅ | ✅ |  |
| 113 | `MOD_DM02_drop_mono_chewbbaca_keep_mlst_sal` | `drop` | ✅ | ✅ |  |
| 114 | `MOD_DM03_drop_mono_mlst_keep_chewbbaca_lis` | `drop` | ✅ | ✅ |  |
| 115 | `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco` | `drop` | ✅ | ❌ | t2: `arity_error` |
| 116 | `MOD_DM05_drop_mono_abricate_keep_mlst_sal` | `drop` | ✅ | ✅ |  |
| 117 | `MOD_DM06_drop_mono_prokka_keep_mlst_lis` | `drop` | ❌ | ✅ | t1: `arity_error` |
| 118 | `MOD_DM07_drop_mono_staramr_keep_mlst_cam` | `drop` | ✅ | ✅ |  |
| 119 | `MOD_DM08_drop_mono_staramr_keep_flaA_cam` | `drop` | ✅ | ✅ |  |
| 120 | `MOD_DM09_drop_mono_flaA_keep_staramr_cam` | `drop` | ❌ | ✅ | t1: `file_not_found` |
| 121 | `MOD_DM10_drop_mono_flaA_keep_mlst_cam` | `drop` | ✅ | ✅ |  |
| 122 | `MOD_DM11_drop_mono_abricate_keep_prokka_eco` | `drop` | ✅ | ✅ |  |
| 123 | `MOD_DM12_drop_mono_prokka_keep_abricate_lis` | `drop` | ✅ | ✅ |  |
| 124 | `MOD_DM13_drop_mono_prokka_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 125 | `MOD_DM14_drop_mono_abricate_keep_prokka_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 126 | `MOD_S01_cgmlst_retarget_lis_to_sal` | `switch_species` | ✅ | ❌ | t2: `no_code` |
| 127 | `MOD_S02_cgmlst_retarget_lis_to_eco` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 128 | `MOD_S03_cgmlst_retarget_sal_to_lis` | `switch_species` | ✅ | ❌ | t2: `no_code` |
| 129 | `MOD_S04_cgmlst_retarget_sal_to_eco` | `switch_species` | ✅ | ✅ |  |
| 130 | `MOD_S05_cgmlst_retarget_eco_to_lis` | `switch_species` | ✅ | ✅ |  |
| 131 | `MOD_S06_cgmlst_retarget_eco_to_sal` | `switch_species` | ✅ | ✅ |  |
| 132 | `MOD_SM01_mlst_retarget_lis_to_cam` | `switch_species` | ✅ | ❌ | t2: `file_not_found` |
| 133 | `MOD_SM02_mlst_retarget_sal_to_cam` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 134 | `MOD_SM03_mlst_retarget_eco_to_cam` | `switch_species` | ❌ | ✅ | t1: `missing_param` |
| 135 | `MOD_SM04_mlst_retarget_cam_to_lis` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 136 | `MOD_SM05_mlst_retarget_cam_to_sal` | `switch_species` | ✅ | ❌ | t2: `no_code` |
| 137 | `MOD_SM06_mlst_retarget_cam_to_eco` | `switch_species` | ✅ | ✅ |  |
| 138 | `MOD_SMA01_mlst_mono_retarget_lis_to_sal` | `switch_species` | ✅ | ✅ |  |
| 139 | `MOD_SMA02_mlst_mono_retarget_lis_to_eco` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 140 | `MOD_SMA03_mlst_mono_retarget_sal_to_lis` | `switch_species` | ✅ | ✅ |  |
| 141 | `MOD_SMA04_mlst_mono_retarget_sal_to_eco` | `switch_species` | ✅ | ✅ |  |
| 142 | `MOD_SMA05_mlst_mono_retarget_eco_to_lis` | `switch_species` | ✅ | ✅ |  |
| 143 | `MOD_SMA06_mlst_mono_retarget_eco_to_sal` | `switch_species` | ✅ | ✅ |  |
| 144 | `MOD_SMA07_mlst_mono_retarget_lis_to_cam` | `switch_species` | ✅ | ✅ |  |
| 145 | `MOD_SMA08_mlst_mono_retarget_sal_to_cam` | `switch_species` | ✅ | ❌ | t2: `no_code` |
| 146 | `MOD_SMA09_mlst_mono_retarget_eco_to_cam` | `switch_species` | ✅ | ❌ | t2: `silent_no_op` |
| 147 | `MOD_SMA10_mlst_mono_retarget_cam_to_lis` | `switch_species` | ✅ | ✅ |  |
| 148 | `MOD_3T01_addAdd_lis` | `add` | ✅ | ✅ |  |
| 149 | `MOD_3T02_addAdd_eco` | `add` | ✅ | ✅ | t3: `silent_no_op` |
| 150 | `MOD_3T03_addAdd_sal` | `add` | ✅ | ✅ |  |
| 151 | `MOD_3T_AD01_addThenDrop_lis` | `add` | ❌ | ❌ | t1: `missing_param` |
| 152 | `MOD_3T_AD02_addThenDrop_eco` | `add` | ❌ | ❌ | t1: `missing_param` |
| 153 | `MOD_3T_AD03_addThenDrop_sal` | `add` | ❌ | ❌ | t1: `missing_param` |
| 154 | `MOD_3T_RA01_replaceThenAdd_lis` | `replace` | ✅ | ✅ |  |
| 155 | `MOD_3T_RA02_replaceThenAdd_eco` | `replace` | ✅ | ❌ | t2: `no_code` |
| 156 | `MOD_3T_RA03_replaceThenAdd_sal` | `replace` | ✅ | ❌ | t2: `file_not_found` |
| 157 | `MOD_3T_SA01_switchThenAdd_lis_to_sal` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 158 | `MOD_3T_SA02_switchThenAdd_eco_to_lis` | `switch_species` | ✅ | ❌ | t2: `arity_error` |
| 159 | `MOD_3T_SA03_switchThenAdd_sal_to_eco` | `switch_species` | ❌ | ❌ | t1: `missing_param` |

## Failure detail (one section per failing turn)

### `MOD_M02_D01_add_chewbbaca_t2` — `partial_dag`
**Conversation:** `MOD_M02_D01_add_chewbbaca` (add) — turn 2
**Prompt:** Now also compute cgMLST allelic profiles on the resulting assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

def listeriaSchema = 'listeria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    spades_out = step_2AS_denovo__spades(trimmed)

    step_4TY_MLST__mlst(spades_out.assembled)
}
```
**Error excerpt:**
```
Only 7/9 expected processes appeared in the DAG
```

### `MOD_M03_B01_add_trimming_t2` — `no_code`
**Conversation:** `MOD_M03_B01_add_trimming` (add) — turn 2
**Prompt:** Add a fastp trimming step before the assembly.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_M04_A04_add_mlst_parallel_t2` — `silent_no_op`
**Conversation:** `MOD_M04_A04_add_mlst_parallel` (add) — turn 2
**Prompt:** Also run classic MLST on the same assembly.

**Steps (LLM):** `step_4TY_cgMLST__chewbbaca, step_4TY_MLST__mlst`
**Steps (GT):**  `step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    asm = getInput()
    step_4TY_cgMLST__chewbbaca(asm, param('genus_species'), optionalOrDefault('schema', ''))
    step_4TY_MLST__mlst(asm)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getRisCd } from '../functions/common.nf'

// --- GLOBALS ---

def genusSpecies = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_cgmlst_mlst {
    
    take:
        
        assembly
        
        schema
        
    
    main:
        step_4TY_cgMLST__chewbbaca(assembly.map { [getRisCd(), it, genusSpecies] }, genusSpecies, schema)
        step_4TY_MLST__mlst(assembly.map { [getRisCd(), it] })
    
}

// --- ENTRYPOINT ---
workflow {
    ch_assembly = getSingleInput()
    ch_schema = getReference('cgmlst_schema')
    wf_listeria_cgmlst_mlst(ch_assembly, ch_schema)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_M07_D03_replace_trimmomatic_with_fastp_t2` — `silent_no_op`
**Conversation:** `MOD_M07_D03_replace_trimmomatic_with_fastp` (replace) — turn 2
**Prompt:** Replace Trimmomatic with fastp.

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

include { getSingleInput; hasEnoughFastqData; hasFastqData } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

def params = [:]

def params.outdir = "${workflow.launchDir}/results"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_reads_processing {
    
    take:
        
        rawReads
        
    
    main:
        rawReads.branch {
            with_data: hasFastqData(it[1])
            no_reads: true
        }
        .set { rawreads_branched }

        trimmed = step_1PP_trimming__fastp(rawreads_branched.with_data).trimmed

        trimmed.branch {
            with_data: hasEnoughFastqData(it[1])
            insufficient_number_of_reads: true
        }
        .set { trimmed_branched }
    
    emit:
        
        trimmed
        
    
}

workflow wf_assembly {
    
    take:
        
        trimmed
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    // Process raw Illumina paired-end reads
    rawReads = getSingleInput()

    // Trim reads and perform QC
    wf_reads_processing(rawReads)

    // Assemble trimmed reads de novo
    wf_assembly(wf_reads_processing.out.trimmed)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_M09_E07_replace_abricate_with_prokka_t1` — `silent_no_op`
**Conversation:** `MOD_M09_E07_replace_abricate_with_prokka` (replace) — turn 1
**Prompt:** Resistance gene detection with ABRicate on Escherichia coli from Illumina paired FASTQ.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4AN_AMR__abricate`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def step_0SQ_rawreads__fastq = '../steps/0SQ_rawreads__fastq.nf'

def step_1PP_trimming__fastp = '../steps/1PP_trimming__fastp.nf'

def step_2AS_denovo__shovill = '../steps/2AS_denovo__shovill.nf'

def step_4AN_AMR__abricate = '../steps/4AN_AMR__abricate.nf'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    rawreads = step_0SQ_rawreads__fastq()
    trimmed = step_1PP_trimming__fastp(rawreads)
    assembly = step_2AS_denovo__shovill(trimmed)
    step_4AN_AMR__abricate(assembly)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_M09_E07_replace_abricate_with_prokka_t2` — `arity_error`
**Conversation:** `MOD_M09_E07_replace_abricate_with_prokka` (replace) — turn 2
**Prompt:** Switch from ABRicate to Prokka annotation.

**Steps (LLM):** `step_2AS_denovo__shovill, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_1PP_trimming__fastp, step_0SQ_rawreads__fastq`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def prokkaKingdom = 'Bacteria'

def abricateDb = 'vfdb'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_assembly_and_annotation {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            assembly: [ it[0], it[1] ]
        }.set { prep }

        shovill_out = step_2AS_denovo__shovill(prep.trimmed)

        prokka_in = shovill_out.assembly.map { [ it[0], it[1], prokkaKingdom, '-', '-', getEmpty() ] }
        step_4AN_genes__prokka(prokka_in)

        abricate_in = shovill_out.assembly
        step_4AN_AMR__abricate(abricate_in)
    
}

workflow wf_trim_and_qc {
    
    take:
        
        rawreads
        
    
    main:
        trimmed_out = step_1PP_trimming__fastp(rawreads)

        trimmed_out.trimmed.set { trimmed }

        fastqc(trimmed)

        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap {
            rawreads: it[0]
            trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed
        
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = step_0SQ_rawreads__fastq(getSingleInput())

    wf_trim_and_qc(rawreads)

    wf_assembly_and_annotation(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_trim_and_qc` declares 1 input channels but 0 were given
```

### `MOD_M11_H01_drop_cgmlst_t1` — `missing_param`
**Conversation:** `MOD_M11_H01_drop_cgmlst` (drop) — turn 1
**Prompt:** Run both MLST and cgMLST typing on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def genusSpecies = 'Listeria monocytogenes'

def cgMLSTSchema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_preprocess_and_assemble {
    
    take:
        
        rawReads
        
    
    main:
        fastp_out = step_1PP_trimming__fastp(rawReads)

        trimmed = fastp_out.trimmed

        trimmed.multiMap {
            trimmed: it
            reference: [ '-', '-', getEmpty() ]
        }.set { trAndRef }

        shovill_out = step_2AS_denovo__shovill(trimmed)
    
    emit:
        
        assembly = shovill_out.assembly
        
    
}

workflow wf_confirm_species {
    
    take:
        
        reads
        
    
    main:
        kmerfinder_out = step_3TX_species__kmerfinder(reads)
    
    emit:
        
        speciesConfirmed = kmerfinder_out.assigned_species
        
    
}

workflow wf_typing {
    
    take:
        
        assembly
        
        genusSpecies
        
        cgMLSTSchema
        
    
    main:
        step_4TY_MLST__mlst(assembly)
        step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, cgMLSTSchema)
    
}

// --- ENTRYPOINT ---
workflow {
    // Input handling
    rawReads = getSingleInput()

    // Preprocessing and assembly
    wf_preprocess_and_assemble(rawReads)

    // Species confirmation
    wf_confirm_species(wf_preprocess_and_assemble.out.assembly)

    // Validate species
    speciesConfirmed = wf_confirm_species.out.speciesConfirmed
    speciesConfirmed.branch {
        listeria_monocytogenes: it[1] == 'Listeria monocytogenes'
        other: true
    }.set { speciesBranched }

    // Exit if not Listeria monocytogenes
    speciesBranched.other.view { "Species confirmation failed: ${it[1]}" }
    workflow.onComplete {
        if (speciesBranched.other.count() > 0) {
            exit 1, "Species confirmation failed for ${speciesBranched.other.count()} samples. Only Listeria monocytogenes is supported."
        }
    }

    // Typing
    wf_typing(wf_preprocess_and_assemble.out.assembly, genusSpecies, cgMLSTSchema)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_M11_H01_drop_cgmlst_t2` — `missing_param`
**Conversation:** `MOD_M11_H01_drop_cgmlst` (drop) — turn 2
**Prompt:** Drop the cgMLST step, only keep MLST.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_1PP_trimming__fastp, step_1PP_hostdepl__bowtie, step_4TY_MLST__mlst`
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

include { getHostUnkeyed; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey } from '../functions/common.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def listeriaMonocytogenesSpecies = 'Listeria monocytogenes'

def listeriaMonocytogenesRiscd = '230415-020223041500512127-3TX_species-kmerfinder'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_species_confirmation {
    
    take:
        
        depletedOrTrimmed
        
    
    main:
        kmerfinder_out = step_3TX_species__kmerfinder(depletedOrTrimmed)

        // Validate species assignment
        kmerfinder_out.assigned_species.map { [it[0], it[1]] }.branch {
            listeria_monocytogenes: it[1] == listeriaMonocytogenesSpecies
            other_species: true
        }.set { species_branch }

        if (species_branch.other_species) {
            error "Species confirmation failed: detected ${species_branch.other_species[0][1]} instead of ${listeriaMonocytogenesSpecies}"
        }
    
    emit:
        
        species_assigned = kmerfinder_out.assigned_species
        
    
}

workflow wf_assembly {
    
    take:
        
        depletedOrTrimmed
        
    
    main:
        shovill_out = step_2AS_denovo__shovill(depletedOrTrimmed)
    
    emit:
        
        assembly = shovill_out.assembly
        
    
}

// --- ENTRYPOINT ---
workflow {
    // Step 1: Input handling - get paired Illumina FASTQ files
    rawreads = getSingleInput()

    // Step 2: Preprocessing - Trimming
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // Step 3: Optional Host Depletion
    // Prepare input for host depletion: [riscd, reads, host]
    trimmed.cross(getHostUnkeyed()) { extractKey(it) }.map { [ it[0][0], it[0][1], it[1][1] ] }.set { prep }
    depleted = step_1PP_hostdepl__bowtie(prep)

    // Create channel with host-depleted reads OR trimmed reads if host depletion skipped
    // Use branch to handle conditional logic
    trimmed.cross(getHostUnkeyed()) { extractKey(it) }.map { [ it[0][0], it[0][1], it[1][1] ] }.branch {
        with_host: it[1][1] != null
        without_host: true
    }.set { host_branch }

    // If host depletion was performed, use depleted reads; otherwise use trimmed reads
    ready = host_branch.with_host.mix(depleted).map { it[0,1] }

    // Step 4: Species Confirmation
    wf_species_confirmation(ready)

    // Step 5: Assembly
    wf_assembly(ready)

    // Step 6: MLST Typing
    step_4TY_MLST__mlst(wf_assembly.out.assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_M13_I01_drop_kmerfinder_t1` — `file_not_found`
**Conversation:** `MOD_M13_I01_drop_kmerfinder` (drop) — turn 1
**Prompt:** Identify the species with KmerFinder, in parallel trim with fastp and assemble with SPAdes (Illumina paired).

**Steps (LLM):** `step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    raw = getSingleInput()
    step_3TX_species__kmerfinder(raw)
    trimmed   = step_1PP_trimming__fastp(raw).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def step_1PP_trimming__fastp = '../steps/step_1PP_trimming__fastp.nf'

def step_2AS_denovo__spades = '../steps/step_2AS_denovo__spades.nf'

def step_3TX_species__kmerfinder = '../steps/step_3TX_species__kmerfinder.nf'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_assemble {
    
    take:
        
        trimmed
        
    
    main:
        spades_out = step_2AS_denovo__spades(trimmed)
    
    emit:
        
        assembled = spades_out.assembled
        
    
}

workflow wf_identify_species {
    
    take:
        
        rawreads
        
    
    main:
        kmerfinder_out = step_3TX_species__kmerfinder(rawreads)
    
    emit:
        
        assigned_species = kmerfinder_out.assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()

    // Parallel execution: fastp trimming and KmerFinder species identification
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // Assemble trimmed reads with SPAdes
    spades_out = wf_trim_assemble(trimmed)

    // Identify species from raw reads in parallel
    kmerfinder_out = wf_identify_species(rawreads)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.UNK.5.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_M13_I01_drop_kmerfinder_t2` — `file_not_found`
**Conversation:** `MOD_M13_I01_drop_kmerfinder` (drop) — turn 2
**Prompt:** Drop the KmerFinder species ID. Keep only trim + assembly.

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

include { getInput; hasEnoughFastqData; hasFastqData; isIlluminaPaired; isIonTorrent; isNanopore } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

def spadesMethodCode = 'spades'

def spadesStepCode = '2AS_denovo'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawReads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawReads).trimmed
        spades_out = step_2AS_denovo__spades(trimmed)
    
    emit:
        
        assembled = spades_out.assembled
        
    
}

workflow module_reads_processing {
    
    take:
        
        rawReads
        
    
    main:
        rawReads.branch {
            with_data: hasFastqData(it[1])
            no_reads: true
        }
        .set { rawreads_branched }

        rawreads_branched.with_data.branch {
            illumina: isIlluminaPaired(it[1])
            ion: isIonTorrent(it[1])
            nanopore: isNanopore(it[1])
            other: true // won't be processed
        }
        .set { trimming_by_seqtype }

        // fastp
        trimmed_by_fastp = step_1PP_trimming__fastp(trimming_by_seqtype.illumina.mix(trimming_by_seqtype.ion)).trimmed

        trimmed_by_fastp.branch {
            with_data: hasEnoughFastqData(it[1])
            insufficient_number_of_reads: true
        }
        .set { trimmed_branched }
    
    emit:
        
        no_reads = rawreads_branched.no_reads
        
        trimmed_with_data = trimmed_branched.with_data
        
        insufficient_number_of_reads = trimmed_branched.insufficient_number_of_reads
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_reads_processing(getInput())
    wf_trim_and_assemble(module_reads_processing.trimmed_with_data)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.UNK.5.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_M14_E02_switch_species_to_salmonella_t2` — `silent_no_op`
**Conversation:** `MOD_M14_E02_switch_species_to_salmonella` (switch_species) — turn 2
**Prompt:** Run the same pipeline for Salmonella enterica instead of Listeria monocytogenes.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

def params = [:]

def params.outdir = "${workflow.launchDir}/results"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Trimming
    trimmed = step_1PP_trimming__fastp(getSingleInput())

    // Step 2: De Novo Assembly
    assembly = step_2AS_denovo__spades(trimmed)

    // Step 3: MLST Typing
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_M16_E07_switch_species_to_salmonella_t1` — `missing_param`
**Conversation:** `MOD_M16_E07_switch_species_to_salmonella` (switch_species) — turn 1
**Prompt:** Resistance gene detection with ABRicate on Escherichia coli from Illumina paired FASTQ.

**Steps (LLM):** `step_2AS_denovo__shovill, step_4AN_AMR__abricate, step_3TX_species__kmerfinder, step_1PP_trimming__fastp`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def abricateDb = 'vfdb'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_resistance {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ '-', 'Escherichia coli', file("${params.assets_dir}/wf_ecoli_resistance/ecoli_ref.fasta") ]
        }.set { trimmedAndRef }

        // Step 3: Assembly (Shovill)
        assembly = step_2AS_denovo__shovill(trimmedAndRef.trimmed)

        // Step 4: Resistance Gene Detection (ABRicate)
        step_4AN_AMR__abricate(assembly.assembly)
    
}

workflow wf_species_check {
    
    take:
        
        trimmed
        
    
    main:
        // Step 2: Species Identification (KmerFinder)
        kmerfinder_out = step_3TX_species__kmerfinder(trimmed)
    
    emit:
        
        assigned_species = kmerfinder_out.assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    // Step 1: Preprocessing (Trimming)
    trimmed = step_1PP_trimming__fastp(getSingleInput())

    // Species check sub-workflow
    wf_species_check(trimmed)

    // Resistance detection sub-workflow
    wf_ecoli_resistance(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_M16_E07_switch_species_to_salmonella_t2` — `missing_param`
**Conversation:** `MOD_M16_E07_switch_species_to_salmonella` (switch_species) — turn 2
**Prompt:** Switch to Salmonella enterica.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4AN_AMR__abricate`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def abricateDb = 'vfdb'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.multiMap {
        trimmed: it
        species_check_input: it
    }.set { prep }

    kmerfinder_out = step_3TX_species__kmerfinder(prep.species_check_input)

    assembly = step_2AS_denovo__shovill(trimmed).assembly

    assembly.multiMap {
        assembly: it
        abricate_input: it
    }.set { abricate_in }

    step_4AN_AMR__abricate(abricate_in.abricate_input)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_M17_D05_switch_species_to_ecoli_t2` — `arity_error`
**Conversation:** `MOD_M17_D05_switch_species_to_ecoli` (switch_species) — turn 2
**Prompt:** Apply the same pipeline to an Escherichia coli sample.

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

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { module_qc_quast } from '../modules/module_qc_quast'

include { module_qc_fastqc } from '../modules/module_qc_fastqc'

// --- GLOBALS ---

def trimmedRiscd = '1PP_trimming-fastp'

def assembledRiscd = '2AS_denovo-spades'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        fastp_out = step_1PP_trimming__fastp(rawreads)

        spades_in = fastp_out.trimmed.multiMap {
            reads: it
            riscd: trimmedRiscd
        }

        spades_out = step_2AS_denovo__spades(spades_in)

        module_qc_fastqc(fastp_out.trimmed)
        module_qc_quast(spades_out.assembled)
    
    emit:
        
        assembled = spades_out.assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_and_assemble(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_trim_and_assemble:step_2AS_denovo__spades` declares 1 input channels but 2 were given
```

### `MOD_K05_add_abricate_to_chewbbaca_sal_spades_t1` — `file_not_found`
**Conversation:** `MOD_K05_add_abricate_to_chewbbaca_sal_spades` (add) — turn 1
**Prompt:** chewbbaca on Salmonella enterica from paired Illumina FASTQ (fastp + spades).

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

def genusSpecies = 'Salmonella enterica'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_typing {
    
    take:
        
        trimmed
        
    
    main:
        trimmed_out = step_1PP_trimming__fastp(trimmed)

        assembly_out = step_2AS_denovo__spades(trimmed_out.trimmed)

        assembly.cross(genusSpecies) { extractKey(it) }.multiMap {
            assembly: it[0]
            species: it[1]
        }.set { assemblyAndSpecies }
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, '')
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_typing(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.SAL.201.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K06_add_prokka_to_chewbbaca_lis_spades_t2` — `no_code`
**Conversation:** `MOD_K06_add_prokka_to_chewbbaca_lis_spades` (add) — turn 2
**Prompt:** Now also run prokka in parallel on the same assembly.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_K07_add_prokka_to_chewbbaca_sal_spades_t2` — `file_not_found`
**Conversation:** `MOD_K07_add_prokka_to_chewbbaca_sal_spades` (add) — turn 2
**Prompt:** Now also run prokka in parallel on the same assembly.

**Steps (LLM):** `step_2AS_denovo__spades, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def genusSpecies = 'Salmonella_enterica'

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_typing_annotation {
    
    take:
        
        trimmed
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmed)

        chewbbaca(assembled.assembled, genusSpecies, '')
        prokka(assembled.assembled.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_salmonella_typing_annotation(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.SAL.202.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K11_add_abricate_to_mlst_eco_spades_t2` — `file_not_found`
**Conversation:** `MOD_K11_add_abricate_to_mlst_eco_spades` (add) — turn 2
**Prompt:** Now also run abricate in parallel on the same assembly.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

def mlstMethod = 'mlst'

def abricateMethod = 'abricate'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_mlst_abricate_ecoli {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
        }
        .set { trimmedMap }

        spades_out = step_2AS_denovo__spades(trimmedMap.trimmed)
        step_4TY_MLST__mlst(spades_out.assembled)
        step_4AN_AMR__abricate(spades_out.assembled)
    
}

workflow module_qc_fastqc {
    
    take:
        
        reads
        
    
    main:
        fastqc(reads)
    
}

workflow module_qc_quast {
    
    take:
        
        assembly
        
    
    main:
        quast(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())

    module_qc_fastqc(trimmed)

    wf_mlst_abricate_ecoli(trimmed)

    module_qc_quast(wf_mlst_abricate_ecoli.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.ECO.202.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K12_add_abricate_to_mlst_sal_spades_t2` — `arity_error`
**Conversation:** `MOD_K12_add_abricate_to_mlst_sal_spades` (add) — turn 2
**Prompt:** Now also run abricate in parallel on the same assembly.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getRisCd } from '../functions/common.nf'

// --- GLOBALS ---

def mlstMethod = 'mlst'

def abricateMethod = 'abricate'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_mlst_amr {
    
    take:
        
        trimmed_reads
        
    
    main:
        trimmed_reads.multiMap {
            trimmed: it
            riscd: getRisCd(md, ex, '2AS_denovo', 'spades')
        }.set { prep }

        spades_out = step_2AS_denovo__spades(prep)

        spades_out.assembled.multiMap {
            assembly: it
            riscd: getRisCd(md, ex, '4TY_MLST', mlstMethod)
        }.set { mlst_in }
        step_4TY_MLST__mlst(mlst_in)

        spades_out.assembled.multiMap {
            assembly: it
            riscd: getRisCd(md, ex, '4AN_AMR', abricateMethod)
        }.set { abricate_in }
        step_4AN_AMR__abricate(abricate_in)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed_reads = step_1PP_trimming__fastp(getSingleInput())

    wf_salmonella_mlst_amr(trimmed_reads)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_salmonella_mlst_amr:step_2AS_denovo__spades` declares 1 input channels but 2 were given
```

### `MOD_K13_add_prokka_to_mlst_lis_spades_t1` — `file_not_found`
**Conversation:** `MOD_K13_add_prokka_to_mlst_lis_spades` (add) — turn 1
**Prompt:** mlst on Listeria monocytogenes from paired Illumina FASTQ (fastp + spades).

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_1PP_trimming__fastp`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getRisCd } from '../functions/common.nf'

// --- GLOBALS ---

def mlstExcludedSchemas = 'abc,def'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_mlst_listeria {
    
    take:
        
        trimmed_reads
        
    
    main:
        trimmed_reads.multiMap {
            trimmed: it
            riscd: getRisCd(md, ex, '2AS_denovo', 'spades')
        }.set { prep }

        spades_out = step_2AS_denovo__spades(prep.trimmed)

        spades_out.assembled.multiMap {
            assembly: it
            riscd: getRisCd(md, ex, '4TY_MLST', 'mlst')
        }.set { asm }
        step_4TY_MLST__mlst(asm.assembly)
    
}

workflow wf_trim_fastp {
    
    take:
        
        raw_reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(raw_reads).trimmed
    
    emit:
        
        trimmed_reads = trimmed
        
    
}

// --- ENTRYPOINT ---
workflow {
    raw_reads = getSingleInput()

    wf_trim_fastp(raw_reads)
    wf_mlst_listeria(trimmed_reads)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.LIS.205.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K15_add_prokka_to_mlst_sal_spades_t1` — `arity_error`
**Conversation:** `MOD_K15_add_prokka_to_mlst_sal_spades` (add) — turn 1
**Prompt:** mlst on Salmonella enterica from paired Illumina FASTQ (fastp + spades).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

def mlstSchema = 'salmonella'

def spadesRiscd = '220308-020220308005121273-2AS_denovo-spades'

def fastpRiscd = '220308-020220308005121273-1PP_trimming-fastp'

def mlstRiscd = '220308-020220308005121273-4TY_lineage-mlst'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_mlst {
    
    take:
        
        raw_reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(raw_reads.map { [ it[0], it[1] ] }, fastpRiscd)

        assembly = step_2AS_denovo__spades(trimmed.trimmed.map { [ it[0], it[1] ] }, spadesRiscd)
        step_4TY_MLST__mlst(assembly.assembled.map { [ it[0], it[1], mlstSchema ] }, mlstRiscd)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_mlst(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_salmonella_mlst:step_1PP_trimming__fastp` declares 1 input channels but 2 were given
```

### `MOD_K17_add_prokka_to_abricate_lis_spades_t1` — `file_not_found`
**Conversation:** `MOD_K17_add_prokka_to_abricate_lis_spades` (add) — turn 1
**Prompt:** abricate on Listeria monocytogenes from paired Illumina FASTQ (fastp + spades).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def params = "${params}"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_amr_listeria {
    
    take:
        
        raw_reads
        
    
    main:
        raw_reads.multiMap {
            reads: it
        }.set { reads_map }

        trimmed = step_1PP_trimming__fastp(reads_map.reads)

        trimmed.multiMap {
            trimmed: it
        }.set { trimmed_map }

        assembled = step_2AS_denovo__spades(trimmed_map.trimmed)

        assembled.multiMap {
            assembly: it
        }.set { assembly_map }

        step_4AN_AMR__abricate(assembly_map.assembly)
    
}

workflow step_1PP_trimming__fastp {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = fastp(rawreads).trimmed

        fastqc(trimmed)

        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap {
            rawreads: it[0]
            trimmed: it[1]
        }

        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed
        
    
}

workflow step_2AS_denovo__spades {
    
    take:
        
        trimmed
        
    
    main:
        denovo_out = denovo(trimmed)

        assembly_filter_out = assembly_filter(denovo_out.scaffolds)

        quast(assembly_filter_out.fasta)

        fasta = assembly_filter_out.fasta
    
    emit:
        
        assembled = fasta
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_amr_listeria(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.LIS.206.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K18_add_prokka_to_abricate_eco_spades_t2` — `no_code`
**Conversation:** `MOD_K18_add_prokka_to_abricate_eco_spades` (add) — turn 2
**Prompt:** Now also run prokka in parallel on the same assembly.

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

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_K19_add_mlst_to_abricate_sal_spades_t2` — `file_not_found`
**Conversation:** `MOD_K19_add_mlst_to_abricate_sal_spades` (add) — turn 2
**Prompt:** Now also run mlst in parallel on the same assembly.

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst, step_1PP_trimming__fastp`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

def step_1PP_trimming__fastp = '../steps/step_1PP_trimming__fastp.nf'

def step_2AS_denovo__spades = '../steps/step_2AS_denovo__spades.nf'

def step_4AN_AMR__abricate = '../steps/step_4AN_AMR__abricate.nf'

def step_4TY_MLST__mlst = '../steps/step_4TY_MLST__mlst.nf'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_abricate_mlst_salmonella {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
        }.set { trimmedOnly }

        spades_out = step_2AS_denovo__spades(trimmedOnly.trimmed)

        abricate(step_4AN_AMR__abricate(spades_out.assembled))
        mlst(step_4TY_MLST__mlst(spades_out.assembled))
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())

    wf_abricate_mlst_salmonella(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.SAL.205.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K20_add_mlst_to_abricate_eco_spades_t2` — `no_code`
**Conversation:** `MOD_K20_add_mlst_to_abricate_eco_spades` (add) — turn 2
**Prompt:** Now also run mlst in parallel on the same assembly.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_K22_add_staramr_to_flaA_cam_spades_t2` — `no_code`
**Conversation:** `MOD_K22_add_staramr_to_flaA_cam_spades` (add) — turn 2
**Prompt:** Now also run staramr in parallel on the same assembly.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_flaA__flaA(assembled, param('genus_species'))
    step_4AN_AMR__staramr(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
http 500: {"detail":"unexpected '{' in field name"}
```

### `MOD_K32_add_prokka_to_mlst_sal_shovill_t1` — `arity_error`
**Conversation:** `MOD_K32_add_prokka_to_mlst_sal_shovill` (add) — turn 1
**Prompt:** mlst on Salmonella enterica from paired Illumina FASTQ (fastp + shovill).

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def mlstSchemaDir = "/NGStools/mlst/db/pubmlst"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    rawreads = step_0SQ_rawreads__fastq(getSingleInput())
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed
    assembly = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were given
```

### `MOD_K32_add_prokka_to_mlst_sal_shovill_t2` — `file_not_found`
**Conversation:** `MOD_K32_add_prokka_to_mlst_sal_shovill` (add) — turn 2
**Prompt:** Now also run prokka in parallel on the same assembly.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst, step_4AN_genes__prokka`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4AN_genes__prokka, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_MLST__mlst(assembled)
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def mlstRiscd = '231219-0202231219124455-4TY_MLST-mlst'

def prokkaRiscd = '231219-0202231219124455-4AN_genes-prokka'

def shovillRiscd = '231219-0202231219124455-2AS_denovo-shovill'

def fastpRiscd = '231219-0202231219124455-1PP_trimming-fastp'

def fastqRiscd = '231219-0202231219124455-0SQ_rawreads-fastq'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Accept paired Illumina FASTQ reads as input
    rawreads = step_0SQ_rawreads__fastq([fastqRiscd, getSingleInput()])

    // Step 2: Trim reads using fastp
    trimmed = step_1PP_trimming__fastp([fastpRiscd, rawreads]).trimmed

    // Step 3: Assemble trimmed reads using shovill
    assembly = step_2AS_denovo__shovill([shovillRiscd, trimmed]).assembly

    // Step 4: Parallel MLST typing and Prokka annotation on the same assembly
    step_4TY_MLST__mlst([mlstRiscd, assembly])
    step_4AN_genes__prokka([prokkaRiscd, assembly.map { [it[0], it[1], 'Bacteria', '-', '-', getEmpty()] }])
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.SAL.206.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K36_add_chewbbaca_to_mlst_sal_shovill_t2` — `file_not_found`
**Conversation:** `MOD_K36_add_chewbbaca_to_mlst_sal_shovill` (add) — turn 2
**Prompt:** Now also run chewbbaca in parallel on the same assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def genusSpecies = 'Salmonella enterica'

def cgMLSTSchema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        contigs_from_pe = step_2AS_denovo__shovill(trimmed).assembly
        contigs_from_se = step_2AS_denovo__shovill(trimmed).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)

        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }

        assembly = contigs
    
    emit:
        
        assembly
        
    
}

workflow wf_typing {
    
    take:
        
        assembly
        
    
    main:
        step_4TY_MLST__mlst(assembly)
        step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, cgMLSTSchema)

        mlst_results = mlst_out
        cgmlst_results = chewbbaca_out.alleles_with_new
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()

    wf_trim_and_assemble_out = wf_trim_and_assemble(rawreads)
    wf_typing(wf_trim_and_assemble_out.assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.SAL.208.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K38_add_prokka_to_mlst_eco_spades_t2` — `file_not_found`
**Conversation:** `MOD_K38_add_prokka_to_mlst_eco_spades` (add) — turn 2
**Prompt:** Now also run prokka in parallel on the same assembly.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_genes__prokka, step_1PP_trimming__trimmomatic`
**Steps (GT):**  `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'

// --- GLOBALS ---

def kingdomEcoli = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_mlst_and_annotation {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            assembly: [ it[0], it[1], it[2] ]
        }.set { trimmedAndAssembly }

        spades_out = step_2AS_denovo__spades(trimmedAndAssembly.trimmed)

        spades_out.assembled.multiMap {
            assembly: it
            kingdom: kingdomEcoli
            riscd_ref: '-'
            refid: '-'
            refpath: getEmpty()
        }.set { prokkaInput }

        step_4TY_MLST__mlst(spades_out.assembled)
        step_4AN_genes__prokka(prokkaInput.assembly, prokkaInput.kingdom, prokkaInput.riscd_ref, prokkaInput.refid, prokkaInput.refpath)
    
}

workflow wf_ecoli_trimming {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__trimmomatic(rawreads)
    
    emit:
        
        trimmed
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_ecoli_trimming(getSingleInput())
    wf_ecoli_mlst_and_annotation(wf_ecoli_trimming.trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.ECO.207.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_R02_replace_asm_spades_to_shovill_sal_t2` — `file_not_found`
**Conversation:** `MOD_R02_replace_asm_spades_to_shovill_sal` (replace) — turn 2
**Prompt:** Replace spades with shovill.

**Steps (LLM):** `step_1PP_trimming__fastp, step_1PP_hostdepl__bowtie, step_2AS_denovo__shovill`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def step_1PP_trimming__fastp = 'step_1PP_trimming__fastp'

def step_1PP_hostdepl__bowtie = 'step_1PP_hostdepl__bowtie'

def step_2AS_denovo__shovill = 'step_2AS_denovo__shovill'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_denovo {
    
    take:
        
        rawReads
        
        host
        
    
    main:
        trimmed_out = step_1PP_trimming__fastp(rawReads)

        trimmedAndHost = trimmed_out.trimmed.cross(host) { extractKey(it) }
            .map { [ it[0][0], it[0][1], it[1][1] ] }
            .branch {
                with_host: it[2]
                without_host: true
            }
            .set { branchedTrimmed }

        depleted_out = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        readyForAssembly = branchedTrimmed.without_host
            .mix(depleted_out)
            .map { it[0,1] }

        shovill_out = step_2AS_denovo__shovill(readyForAssembly)
    
    emit:
        
        assembly = shovill_out.assembly
        
    
}

workflow module_denovo {
    
    take:
        
        rawReads
        
        host
        
    
    main:
        wf_salmonella_denovo(rawReads, host)
    
}

// --- ENTRYPOINT ---
workflow {
    module_denovo(getSingleInput(), getHost())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.SAL.209.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_R05_replace_asm_spades_to_unicycler_lis_t1` — `arity_error`
**Conversation:** `MOD_R05_replace_asm_spades_to_unicycler_lis` (replace) — turn 1
**Prompt:** Trim + assemble Listeria monocytogenes from paired Illumina FASTQ using fastp + spades.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { module_qc_quast } from '../modules/module_qc_quast'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { module_qc_fastqc } from '../modules/module_qc_fastqc'

// --- GLOBALS ---

def stepCodeRawReads = '0SQ_rawreads'

def methodCodeRawReads = 'fastq'

def stepCodeTrimming = '1PP_trimming'

def methodCodeTrimming = 'fastp'

def stepCodeAssembly = '2AS_denovo'

def methodCodeAssembly = 'spades'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Input FASTQ Files
    rawreads = step_0SQ_rawreads__fastq(getSingleInput())

    // Step 2: Trimming with fastp
    trimmed = step_1PP_trimming__fastp(rawreads)

    // Step 3: De Novo Assembly with SPAdes
    assembled = step_2AS_denovo__spades(trimmed)

    // Optional: QC modules (void tools)
    module_qc_fastqc(trimmed)
    module_qc_quast(assembled.map { it[1] }) // Extract FASTA path from tuple
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were given
```

### `MOD_R05_replace_asm_spades_to_unicycler_lis_t2` — `arity_error`
**Conversation:** `MOD_R05_replace_asm_spades_to_unicycler_lis` (replace) — turn 2
**Prompt:** Replace spades with unicycler.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__unicycler`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__unicycler`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__unicycler(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { module_qc_quast } from '../modules/module_qc_quast'

include { module_qc_fastqc } from '../modules/module_qc_fastqc'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

// --- GLOBALS ---

def unicyclerContainer = 'docker.io/biocontainers/unicycler:v0.4.7dfsg-2-deb_cv1'

def fastpContainer = 'ghcr.io/genpat-it/fastp:0.23.1--e4ac3df4c5'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Input FASTQ Files (step_0SQ_rawreads__fastq)
    rawreads = step_0SQ_rawreads__fastq(getSingleInput())

    // Step 2: Trimming with fastp (step_1PP_trimming__fastp)
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // Step 3: De Novo Assembly with Unicycler (step_2AS_denovo__unicycler)
    assembled = step_2AS_denovo__unicycler(trimmed).assembled

    // Optional: QC modules (void tools)
    module_qc_fastqc(trimmed)
    module_qc_quast(assembled)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were given
```

### `MOD_RTY07_replace_typing_chewbbaca_to_prokka_lis_t1` — `silent_no_op`
**Conversation:** `MOD_RTY07_replace_typing_chewbbaca_to_prokka_lis` (replace) — turn 1
**Prompt:** chewbbaca on Listeria monocytogenes from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).

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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

def genusSpecies = 'Listeria monocytogenes'

def chewbbacaSchema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Input channel setup
    Channel.fromPath(params.input_fastq)
        .map { file -> [file.baseName, file] }
        .groupTuple()
        .map { name, files -> [name, files[0], files[1]] }
        .set { reads }

    // Step 2: Trimming with fastp
    trimmed = step_1PP_trimming__fastp(reads)

    // Step 3: De novo assembly with SPAdes
    assembled = step_2AS_denovo__spades(trimmed)

    // Step 4: cgMLST typing with chewbbaca
    step_4TY_cgMLST__chewbbaca(assembled.assembled, genusSpecies, chewbbacaSchema)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_RTY07_replace_typing_chewbbaca_to_prokka_lis_t2` — `no_code`
**Conversation:** `MOD_RTY07_replace_typing_chewbbaca_to_prokka_lis` (replace) — turn 2
**Prompt:** Switch the downstream step from chewbbaca to prokka.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
http 500: {"detail":"unexpected '{' in field name"}
```

### `MOD_RTY09_replace_typing_abricate_to_prokka_eco_t1` — `silent_no_op`
**Conversation:** `MOD_RTY09_replace_typing_abricate_to_prokka_eco` (replace) — turn 1
**Prompt:** abricate on Escherichia coli from paired Illumina FASTQ (fastp + SPAdes + abricate).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def params = "${workflow.parameters}"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_abricate_e_coli {
    
    take:
        
        reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(reads).trimmed
        assembled = step_2AS_denovo__spades(trimmed).assembled
        step_4AN_AMR__abricate(assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_abricate_e_coli(getSingleInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_RTY10_replace_typing_prokka_to_abricate_sal_t2` — `no_code`
**Conversation:** `MOD_RTY10_replace_typing_prokka_to_abricate_sal` (replace) — turn 2
**Prompt:** Switch the downstream step from prokka to abricate.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_RM03_replace_mono_chewbbaca_to_mlst_lis_t1` — `missing_param`
**Conversation:** `MOD_RM03_replace_mono_chewbbaca_to_mlst_lis` (replace) — turn 1
**Prompt:** Run chewbbaca on a pre-existing Listeria monocytogenes assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def genus = 'Listeria'

def species = 'monocytogenes'

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

        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', genus, species, getEmpty() ] })

        assembly.cross(assigned_species) { extractKey(it) }.multiMap { 
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, params.cgmlst_schema ?: '')
    
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

### `MOD_RM04_replace_mono_chewbbaca_to_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_RM04_replace_mono_chewbbaca_to_mlst_sal` (replace) — turn 1
**Prompt:** Run chewbbaca on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def speciesCode = 'Salmonella_enterica'

def speciesRiscd = '220308-020220308005121273-3TX_species-kmerfinder'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        assembly.cross(assigned_species) { extractKey(it) }.multiMap { 
            assembly: it[0]
            species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4AN_AMR__abricate(assembly)

        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, '')
    
    emit:
        
        genus_species = assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    assembly = getAssembly()
    module_typing_bacteria(assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_RM04_replace_mono_chewbbaca_to_mlst_sal_t2` — `missing_param`
**Conversation:** `MOD_RM04_replace_mono_chewbbaca_to_mlst_sal` (replace) — turn 2
**Prompt:** Use mlst on that same assembly instead.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly } from '../functions/parameters.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def skip_bestref_mapping = 'true'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        if (!params.skip_bestref_mapping.toBoolean()) {
            trimmed.cross(assigned_species) { extractKey(it) }.multiMap { 
                trimmed: it[0]
                species: it[1][1]
                referencePath: it[1][2]
            }.set { trimAndSpecies }
            step_2AS_mapping__bowtie(trimAndSpecies.trimmed, trimAndSpecies.referencePath)
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
    
    emit:
        
        genus_species = assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria([], getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_RM09_replace_mono_staramr_to_flaA_cam_t2` — `missing_param`
**Conversation:** `MOD_RM09_replace_mono_staramr_to_flaA_cam` (replace) — turn 2
**Prompt:** Use flaA on that same assembly instead.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
workflow {
    step_4TY_flaA__flaA(getInput(), param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def campylobacterSpecies = 'Campylobacter jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_typing {
    
    take:
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        assembly.cross(assigned_species) { extractKey(it) }.multiMap { 
            assembly: it[0]
            species: it[1][1]
            referencePath: it[1][2]
        }.set { assemblyAndSpecies }

        step_4AN_AMR__abricate(assemblyAndSpecies.assembly)

        step_4AN_genes__prokka(assemblyAndSpecies.assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, campylobacterSpecies)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, campylobacterSpecies)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, campylobacterSpecies, '')
    
}

// --- ENTRYPOINT ---
workflow {
    wf_campylobacter_typing(getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D01_drop_chewbbaca_keep_mlst_lis_t1` — `missing_param`
**Conversation:** `MOD_D01_drop_chewbbaca_keep_mlst_lis` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def listeriaMonocytogenesSchema = 'l_mono_chewie_1748_220623'

def listeriaMonocytogenesSpecies = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_monocytogenes_typing {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembly = step_2AS_denovo__shovill(trimmed).assembly

        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        assemblyAndSpecies = assembly.cross(assigned_species) { extractKey(it) }.multiMap {
            assembly: it[0]
            species: it[1][1]
        }

        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)

        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, listeriaMonocytogenesSchema)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_listeria_monocytogenes_typing(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D01_drop_chewbbaca_keep_mlst_lis_t2` — `missing_param`
**Conversation:** `MOD_D01_drop_chewbbaca_keep_mlst_lis` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_MLST__mlst`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def listeriaMlstSchema = 'listeria_monocytogenes'

def listeriaSpeciesCode = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_mlst {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembly = step_2AS_denovo__shovill(trimmed).assembly

        assigned_species = step_3TX_species__kmerfinder(trimmed).check.map { [ it[0], getCalculatedSpecies(it[1]), getBacterialReferencePath(it[1]) ] }

        assemblyAndSpecies = assembly.cross(assigned_species) { extractKey(it) }.multiMap {
            assembly: it[0]
            species: it[1][1]
        }

        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_listeria_mlst(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D02_drop_chewbbaca_keep_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_D02_drop_chewbbaca_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca, step_4TY_MLST__mlst`
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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def chewbbacaSchema = 's_enterica_chewie_3255_210531'

def genusSpecies = 'salmonella_enterica'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    reads = step_0SQ_rawreads__fastq(getSingleInput())
    trimmed = step_1PP_trimming__fastp(reads).trimmed
    species_report = step_3TX_species__kmerfinder(trimmed).assigned_species
    assembly = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, chewbbacaSchema)
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D02_drop_chewbbaca_keep_mlst_sal_t2` — `missing_param`
**Conversation:** `MOD_D02_drop_chewbbaca_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def params = "${workflow.projectDir}/nextflow_schema.json"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Input raw paired Illumina FASTQ files
    rawreads = step_0SQ_rawreads__fastq(getSingleInput())

    // Step 2: Trim adapters and low-quality bases using fastp
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // Step 3: Species identification using KmerFinder to confirm Salmonella enterica
    kmerfinder_out = step_3TX_species__kmerfinder(trimmed)

    // Step 4: De novo assembly using Shovill
    assembly = step_2AS_denovo__shovill(trimmed).assembly

    // Step 5: Typing using mlst
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D03_drop_chewbbaca_keep_mlst_eco_t1` — `missing_param`
**Conversation:** `MOD_D03_drop_chewbbaca_keep_mlst_eco` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca, step_4TY_MLST__mlst`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { module_qc_quast } from '../modules/module_qc_quast'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { module_qc_fastqc } from '../modules/module_qc_fastqc'

// --- GLOBALS ---

def genusSpecies = 'escherichia_coli'

def chewbbacaSchema = 'e_coli_chewie_2360_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_typing {
    
    take:
        
        rawReads
        
    
    main:
        module_qc_fastqc(rawReads)

        trimmed = step_1PP_trimming__fastp(rawReads).trimmed

        module_qc_fastqc(trimmed)

        species_out = step_3TX_species__kmerfinder(trimmed)

        // Branch: only proceed if species is Escherichia coli
        species_out.assigned_species.branch {
            escherichia_coli: it[1] == 'escherichia_coli'
            other: true
        }.set { speciesBranched }

        // Exit if not E. coli
        speciesBranched.other.view { "Species confirmation failed: not Escherichia coli. Exiting."; System.exit(1) }

        assembly = step_2AS_denovo__shovill(trimmed).assembly

        module_qc_quast(assembly)
        step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, chewbbacaSchema)

        step_4TY_MLST__mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_ecoli_typing(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D03_drop_chewbbaca_keep_mlst_eco_t2` — `missing_param`
**Conversation:** `MOD_D03_drop_chewbbaca_keep_mlst_eco` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { module_qc_quast } from '../modules/module_qc_quast'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { module_qc_fastqc } from '../modules/module_qc_fastqc'

// --- GLOBALS ---

def ecoliSpecies = 'Escherichia coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_typing {
    
    take:
        
        rawreads
        
    
    main:
        module_qc_fastqc(rawreads)

        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        module_qc_fastqc(trimmed)

        species_out = step_3TX_species__kmerfinder(trimmed)
        assigned_species = species_out.assigned_species.map { it[1] }

        // Species confirmation: exit if not E. coli
        assigned_species.branch {
            ecoli: it == ecoliSpecies
            not_ecoli: true
        }.set { species_branch }

        if (species_branch.not_ecoli) {
            error "Species confirmation failed: detected species is not Escherichia coli. Detected: ${species_branch.not_ecoli.first()}"
        }

        assembly = step_2AS_denovo__shovill(trimmed).assembly

        module_qc_quast(assembly)

        step_4TY_MLST__mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_ecoli_typing(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D04_drop_mlst_keep_chewbbaca_lis_t1` — `missing_param`
**Conversation:** `MOD_D04_drop_mlst_keep_chewbbaca_lis` (drop) — turn 1
**Prompt:** Run both mlst and chewbbaca on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def genusSpecies = 'Listeria monocytogenes'

def chewbbacaSchema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())

    species_out = step_3TX_species__kmerfinder(trimmed)

    assembly = step_2AS_denovo__shovill(trimmed)

    step_4TY_MLST__mlst(assembly)

    step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, chewbbacaSchema)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D04_drop_mlst_keep_chewbbaca_lis_t2` — `missing_param`
**Conversation:** `MOD_D04_drop_mlst_keep_chewbbaca_lis` (drop) — turn 2
**Prompt:** Drop mlst, keep only chewbbaca.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def chewBBACASchema = 'l_mono_chewie_1748_220623'

def chewBBACAGenusSpecies = 'listeria_monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    kmerfinder_out = step_3TX_species__kmerfinder(trimmed)

    assembly = step_2AS_denovo__shovill(trimmed).assembly

    step_4TY_cgMLST__chewbbaca(assembly, chewBBACAGenusSpecies, chewBBACASchema)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D05_drop_mlst_keep_chewbbaca_sal_t1` — `missing_param`
**Conversation:** `MOD_D05_drop_mlst_keep_chewbbaca_sal` (drop) — turn 1
**Prompt:** Run both mlst and chewbbaca on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def genusSpecies = 'Salmonella enterica'

def cgMLSTSchema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed
    assembly = step_2AS_denovo__shovill(trimmed).assembly
    kmerfinder_out = step_3TX_species__kmerfinder(assembly).assigned_species
    step_4TY_MLST__mlst(assembly)
    step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, cgMLSTSchema)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D05_drop_mlst_keep_chewbbaca_sal_t2` — `missing_param`
**Conversation:** `MOD_D05_drop_mlst_keep_chewbbaca_sal` (drop) — turn 2
**Prompt:** Drop mlst, keep only chewbbaca.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def genusSpecies = 'Salmonella enterica'

def cgMLSTSchema = 'salmonella_enterica'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__shovill(trimmed).assembly
    species_out = step_3TX_species__kmerfinder(assembly).assigned_species
    step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, cgMLSTSchema)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D06_drop_abricate_keep_mlst_lis_t1` — `missing_param`
**Conversation:** `MOD_D06_drop_abricate_keep_mlst_lis` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4AN_AMR__abricate, step_4TY_MLST__mlst`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { module_qc_quast } from '../modules/module_qc_quast'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { module_qc_fastqc } from '../modules/module_qc_fastqc'

// --- GLOBALS ---

def ListeriaMonocytogenesSpeciesCode = 'Listeria monocytogenes'

def ListeriaMonocytogenesRisCd = '230315-020223031500512127-3TX_species-kmerfinder'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_qc_trimming {
    
    take:
        
        rawreads
        
    
    main:
        module_qc_fastqc(rawreads)
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        module_qc_fastqc(trimmed)
    
    emit:
        
        trimmed
        
    
}

workflow wf_species_confirmation {
    
    take:
        
        trimmed
        
    
    main:
        kmerfinder_out = step_3TX_species__kmerfinder(trimmed)
        species_confirmed = kmerfinder_out.assigned_species
        species_confirmed.branch {
            listeria_monocytogenes: it[1] == ListeriaMonocytogenesSpeciesCode
            other: true
        }.set { branched }
        // VOID tool call for KmerFinder report (no emit needed)
        step_3TX_species__kmerfinder(branched.other)
    
    emit:
        
        species_confirmed
        
    
}

workflow wf_assembly_and_annotation {
    
    take:
        
        trimmed
        
    
    main:
        assembly = step_2AS_denovo__shovill(trimmed)
        module_qc_quast(assembly)
        step_4AN_AMR__abricate(assembly)
    
    emit:
        
        assembly
        
    
}

workflow wf_mlst_typing {
    
    take:
        
        assembly
        
    
    main:
        step_4TY_MLST__mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    // Quality Control and Trimming
    wf_qc_trimming(getSingleInput()) | wf_qc_trimming.out.trimmed

    // Species Confirmation (KmerFinder)
    wf_species_confirmation(wf_qc_trimming.out.trimmed) | wf_species_confirmation.out.species_confirmed

    // De Novo Assembly and Annotation
    wf_assembly_and_annotation(wf_species_confirmation.out.species_confirmed.listeria_monocytogenes)

    // MLST Typing
    wf_mlst_typing(wf_assembly_and_annotation.out.assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D06_drop_abricate_keep_mlst_lis_t2` — `missing_param`
**Conversation:** `MOD_D06_drop_abricate_keep_mlst_lis` (drop) — turn 2
**Prompt:** Drop abricate, keep only mlst.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def kmerfinderSpeciesRiscd = '220308-020220308005121273-3TX_import-external'

def shovillRiscd = '220308-020220308005121273-2AS_import-external'

def mlstRiscd = '220308-020220308005121273-4TY_import-external'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()

    // 1. Quality Control (FastQC)
    step_0SQ_rawreads__fastq(rawreads)

    // 2. Trimming (fastp)
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // 3. Species Identification (KmerFinder)
    kmerfinder_out = step_3TX_species__kmerfinder(trimmed)

    // 4. De Novo Assembly (Shovill)
    assembly = step_2AS_denovo__shovill(trimmed).assembly

    // 5. MLST Typing (MLST)
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D07_drop_abricate_keep_mlst_eco_t1` — `missing_param`
**Conversation:** `MOD_D07_drop_abricate_keep_mlst_eco` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4AN_AMR__abricate, step_4TY_MLST__mlst`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def ecoliSpecies = 'Escherichia coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_typing_amr {
    
    take:
        
        raw_reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(raw_reads)

        // Species confirmation
        kmerfinder_out = step_3TX_species__kmerfinder(trimmed)

        // Assembly
        assembly = step_2AS_denovo__shovill(trimmed)

        // AMR detection
        step_4AN_AMR__abricate(assembly)

        // MLST typing
        step_4TY_MLST__mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    // Get paired Illumina FASTQ input
    raw_reads = getSingleInput()

    // Run the E. coli typing and AMR pipeline
    wf_ecoli_typing_amr(raw_reads)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D07_drop_abricate_keep_mlst_eco_t2` — `missing_param`
**Conversation:** `MOD_D07_drop_abricate_keep_mlst_eco` (drop) — turn 2
**Prompt:** Drop abricate, keep only mlst.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def ecoliSpecies = 'Escherichia coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_mlst {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        species_out = step_3TX_species__kmerfinder(trimmed)

        assembly = step_2AS_denovo__shovill(trimmed)

        step_4TY_MLST__mlst(assembly.assembly)
    
}

workflow module_qc_fastqc {
    
    take:
        
        reads
        
    
    main:
        fastqc(reads)
    
}

workflow module_qc_quast {
    
    take:
        
        assembly
        
    
    main:
        quast(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    // Input: paired Illumina FASTQ files
    rawreads = getSingleInput()

    // Run QC on raw reads
    module_qc_fastqc(rawreads)

    // Run the main E. coli MLST workflow
    wf_ecoli_mlst(rawreads)

    // Run QC on the assembled genome
    assembly_ch = wf_ecoli_mlst.out.assembly
    module_qc_quast(assembly_ch)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D08_drop_abricate_keep_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_D08_drop_abricate_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_1PP_hostdepl__bowtie, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4AN_AMR__abricate, step_4TY_MLST__mlst, step_0SQ_rawreads__fastq`
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

include { extractKey } from '../functions/common.nf'

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def abricateDbCode = 'viruses_TREF'

def abricateDbPath = "${params.assets_dir}/module_vdraft/viruses_TREF"

def kmerfinderSpeciesDir = "${params.assets_dir}/step_3TX_species__kmerfinder"

def shovillMethod = 'shovill'

def fastpMethod = 'fastp'

def bowtieMethod = 'bowtie'

def kmerfinderMethod = 'kmerfinder'

def abricateMethod = 'abricate'

def mlstMethod = 'mlst'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_enterica {
    
    take:
        
        raw_reads
        
        host_reference
        
    
    main:
        // Quality Control (FastQC)
        module_qc_fastqc(raw_reads)

        // Trimming (fastp)
        trimmed_reads = step_1PP_trimming__fastp(raw_reads).trimmed

        // Host Depletion (Bowtie2) - conditional
        trimmed_reads.cross(host_reference) { extractKey(it) }
            .map { [ it[0][0], it[0][1], it[1][1] ] }
            .set { prep }
        depleted_reads = step_1PP_hostdepl__bowtie(prep)
        ready_reads = depleted_reads.mix(trimmed_reads.map { it[0,1] })

        // Species Identification (KmerFinder)
        kmerfinder_out = step_3TX_species__kmerfinder(ready_reads)

        // De Novo Assembly (Shovill)
        assembly = step_2AS_denovo__shovill(ready_reads).assembly

        // AMR Gene Detection (Abricate)
        step_4AN_AMR__abricate(assembly)

        // MLST Typing (MLST)
        step_4TY_MLST__mlst(assembly)
    
}

workflow module_qc_fastqc {
    
    take:
        
        reads
        
    
    main:
        step_0SQ_rawreads__fastq(reads)
    
}

// --- ENTRYPOINT ---
workflow {
    // Instantiate input channels
    raw_reads = getSingleInput()
    host_reference = getHost()

    // Execute the Salmonella enterica workflow
    wf_salmonella_enterica(raw_reads, host_reference)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D08_drop_abricate_keep_mlst_sal_t2` — `missing_param`
**Conversation:** `MOD_D08_drop_abricate_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop abricate, keep only mlst.

**Steps (LLM):** `step_1PP_trimming__fastp, step_1PP_hostdepl__bowtie, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_MLST__mlst, step_0SQ_rawreads__fastq`
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

include { extractKey } from '../functions/common.nf'

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def kmerfinderSpeciesRiscd = '230315-020230315005121273-3TX_import-external'

def shovillRiscd = '230315-020230315005121273-2AS_import-external'

def fastpRiscd = '230315-020230315005121273-1PP_import-external'

def fastqcRiscd = '230315-020230315005121273-0SQ_import-external'

def bowtieHostDepletionRiscd = '230315-020230315005121273-1PP_import-external'

def mlstRiscd = '230315-020230315005121273-4TY_import-external'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_mlst {
    
    take:
        
        raw_reads
        
        host_reference
        
    
    main:
        module_qc_fastqc(raw_reads)

        trimmed = step_1PP_trimming__fastp(raw_reads).trimmed
        module_qc_fastqc(trimmed)

        readsCheckInput = raw_reads.cross(trimmed) { extractKey(it) }.multiMap {
            rawreads: it[0]
            trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)

        trimmedAndHost = trimmed.cross(host_reference) { extractKey(it) }.map { [ it[0][0], it[0][1], it[1][1] ] }
        depleted = step_1PP_hostdepl__bowtie(trimmedAndHost)

        trimmedOrDepleted = trimmed.mix(depleted)

        speciesOut = step_3TX_species__kmerfinder(trimmedOrDepleted)

        assembly = step_2AS_denovo__shovill(trimmedOrDepleted).assembly

        step_4TY_MLST__mlst(assembly)
    
}

workflow module_qc_fastqc {
    
    take:
        
        reads
        
    
    main:
        fastqc(reads)
    
}

// --- ENTRYPOINT ---
workflow {
    raw_reads = step_0SQ_rawreads__fastq(getSingleInput())

    wf_salmonella_mlst(raw_reads, getHost())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D09_drop_prokka_keep_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_D09_drop_prokka_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both prokka and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4AN_genes__prokka, step_4TY_MLST__mlst`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def kingdom = 'Bacteria'

def species = 'Salmonella enterica'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    rawreads = step_0SQ_rawreads__fastq(getSingleInput())
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    trimmed_kmerfinder = trimmed.multiMap {
        trimmed: it
        reference: [ '-', species, getEmpty() ]
    }

    kmerfinder_out = step_3TX_species__kmerfinder(trimmed_kmerfinder.trimmed)

    assembly = step_2AS_denovo__shovill(trimmed)

    prokka_in = assembly.assembly.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] }
    step_4AN_genes__prokka(prokka_in)

    step_4TY_MLST__mlst(assembly.assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D09_drop_prokka_keep_mlst_sal_t2` — `missing_param`
**Conversation:** `MOD_D09_drop_prokka_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop prokka, keep only mlst.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def speciesCode = 'Salmonella_enterica'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Quality Control on raw reads
    step_0SQ_rawreads__fastq(getSingleInput())

    // Trimming
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    // Species Identification (KmerFinder)
    step_3TX_species__kmerfinder(trimmed)

    // De Novo Assembly
    assembly = step_2AS_denovo__shovill(trimmed).assembly

    // MLST Typing
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D10_drop_prokka_keep_abricate_lis_t1` — `missing_param`
**Conversation:** `MOD_D10_drop_prokka_keep_abricate_lis` (drop) — turn 1
**Prompt:** Run both prokka and abricate on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4AN_genes__prokka, step_4AN_AMR__abricate`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def kingdomListeria = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_4AN_genes__prokka__reference = getEmpty()
    // 1. Input Handling
    rawreads = step_0SQ_rawreads__fastq(getSingleInput())

    // 2. Preprocessing: Trimming
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // 3. Species Identification
    species_out = step_3TX_species__kmerfinder(trimmed)

    // 4. Assembly
    assembly = step_2AS_denovo__shovill(trimmed).assembly

    // 5. Gene Annotation
    prokka_input = assembly.map { [ it[0], it[1], kingdomListeria, '-', '-', step_4AN_genes__prokka__reference ] }
    step_4AN_genes__prokka(prokka_input)

    // 6. AMR Profiling
    step_4AN_AMR__abricate(assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D10_drop_prokka_keep_abricate_lis_t2` — `silent_no_op`
**Conversation:** `MOD_D10_drop_prokka_keep_abricate_lis` (drop) — turn 2
**Prompt:** Drop prokka, keep only abricate.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4AN_AMR__abricate`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def params = [:]

def params.outdir = "${params.outdir}"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Preprocessing (Trimming)
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    // Step 2: Species Identification (Kmerfinder)
    kmerfinder_out = step_3TX_species__kmerfinder(trimmed)
    assigned_species = kmerfinder_out.assigned_species

    // Step 3: Assembly (Shovill)
    assembly = step_2AS_denovo__shovill(trimmed).assembly

    // Step 4: AMR Profiling (Abricate)
    step_4AN_AMR__abricate(assembly)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D11_drop_flaA_keep_mlst_cam_t1` — `missing_param`
**Conversation:** `MOD_D11_drop_flaA_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both flaA and mlst on Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_flaA__flaA, step_4TY_MLST__mlst, step_0SQ_rawreads__fastq`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def genusSpecies = 'Campylobacter jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_typing {
    
    take:
        
        rawReads
        
    
    main:
        rawReads.multiMap {
            reads: it
            genus_species: genusSpecies
        }.set { prep }

        trimmed = step_1PP_trimming__fastp(prep.reads).trimmed

        species_out = step_3TX_species__kmerfinder(trimmed)

        assembly = step_2AS_denovo__shovill(trimmed).assembly
        step_4TY_flaA__flaA(assembly, prep.genus_species)
        step_4TY_MLST__mlst(assembly)
    
}

workflow module_qc_fastqc {
    
    take:
        
        reads
        
    
    main:
        fastqc(reads)
    
}

workflow module_qc_quast {
    
    take:
        
        assembly
        
    
    main:
        quast(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    rawReads = step_0SQ_rawreads__fastq(getSingleInput())

    wf_campylobacter_typing(rawReads)

    module_qc_fastqc(rawReads)

    module_qc_quast(step_2AS_denovo__shovill(rawReads).assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D11_drop_flaA_keep_mlst_cam_t2` — `missing_param`
**Conversation:** `MOD_D11_drop_flaA_keep_mlst_cam` (drop) — turn 2
**Prompt:** Drop flaA, keep only mlst.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def campySpeciesCode = 'Campylobacter jejuni'

def campySpeciesRiscd = '230315-020223031500512127-3TX_import-external'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campy_species_check {
    
    take:
        
        species_assigned
        
    
    main:
        species_assigned.branch {
            campy_jejuni: it[1] == campySpeciesCode
            other: true
        }.set { branched }

        if (params.skip_species_check) {
            branched.campy_jejuni.mix(branched.other).set { ready }
        } else {
            ready = branched.campy_jejuni
        }
    
}

workflow wf_campy_assembly_qc {
    
    take:
        
        assembly
        
    
    main:
        quast(assembly)
        if (!params.skip_checkm) {
            checkm(assembly)
        }
    
}

// --- ENTRYPOINT ---
workflow {
    // Step 1: Raw reads input
    rawreads = step_0SQ_rawreads__fastq(getSingleInput())

    // Step 2: Trimming
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // Step 3: Species identification
    species_out = step_3TX_species__kmerfinder(trimmed)
    assigned_species = species_out.assigned_species

    // Step 4: Species confirmation sub-workflow
    wf_campy_species_check(assigned_species)

    // Step 5: De novo assembly
    assembly = step_2AS_denovo__shovill(trimmed).assembly

    // Step 6: Assembly QC sub-workflow
    wf_campy_assembly_qc(assembly)

    // Step 7: MLST typing
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D12_drop_staramr_keep_mlst_cam_t1` — `missing_param`
**Conversation:** `MOD_D12_drop_staramr_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both staramr and mlst on Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4AN_AMR__staramr, step_4TY_MLST__mlst`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def campylobacterSpecies = 'Campylobacter jejuni'

def genusSpeciesParam = 'campylobacter_jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_jejuni_analysis {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        kmerfinder_out = step_3TX_species__kmerfinder(trimmed)
        assigned_species = kmerfinder_out.assigned_species

        // Validate species is Campylobacter jejuni
        assigned_species.map { it[1] }.branch {
            campylobacter_jejuni: it == campylobacterSpecies
            other: true
        }.set { species_branch }

        // Exit if not Campylobacter jejuni
        species_branch.other.map { exit 1, "Species identified as ${it}, expected ${campylobacterSpecies}. Pipeline only supports ${campylobacterSpecies}." }

        // Proceed only if Campylobacter jejuni
        assembly = step_2AS_denovo__shovill(trimmed).assembly

        // AMR profiling
        step_4AN_AMR__staramr(assembly, genusSpeciesParam)

        // MLST typing
        step_4TY_MLST__mlst(assembly)
    
}

workflow module_qc_fastqc {
    
    take:
        
        reads
        
    
    main:
        fastqc(reads)
    
}

workflow module_qc_quast {
    
    take:
        
        assembly
        
    
    main:
        quast(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    // Instantiate input channel
    rawreads = getSingleInput()

    // Run Campylobacter jejuni analysis pipeline
    wf_campylobacter_jejuni_analysis(rawreads)

    // Run QC modules on raw reads
    module_qc_fastqc(rawreads)

    // QC module on assembly (optional, if needed)
    // assembly = step_2AS_denovo__shovill(rawreads).assembly
    // module_qc_quast(assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D12_drop_staramr_keep_mlst_cam_t2` — `no_code`
**Conversation:** `MOD_D12_drop_staramr_keep_mlst_cam` (drop) — turn 2
**Prompt:** Drop staramr, keep only mlst.

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
http 500: {"detail":"Invalid variable name 'params.outdir' in f-string template. Variable names cannot contain attribute access (.) or indexing ([])."}
```

### `MOD_DA03_drop_assembly_sal_t1` — `arity_error`
**Conversation:** `MOD_DA03_drop_assembly_sal` (drop) — turn 1
**Prompt:** Trim + assemble Salmonella enterica from paired Illumina FASTQ (fastp + SPAdes).

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def spadesRiscd = '220308-020220308005121273-2AS_denovo-spades'

def fastpRiscd = '220308-020220308005121273-1PP_trimming-fastp'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    raw_reads = step_0SQ_rawreads__fastq(getSingleInput())

    trimmed_reads = step_1PP_trimming__fastp(raw_reads)

    spades_out = step_2AS_denovo__spades(trimmed_reads)

    step_2AS_denovo__spades(spades_out.assembled)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were given
```

### `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco_t2` — `arity_error`
**Conversation:** `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco` (drop) — turn 2
**Prompt:** Drop mlst, keep only chewbbaca.

**Steps (LLM):** `step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getAssembly } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def escherichiaColiSpecies = 'Escherichia coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        assembly
        
    
    main:
        step_4TY_cgMLST__chewbbaca(assembly.map{ [ it[0], it[1], escherichiaColiSpecies, '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `module_typing_bacteria:step_4TY_cgMLST__chewbbaca` declares 3 input channels but 1 were given
```

### `MOD_DM06_drop_mono_prokka_keep_mlst_lis_t1` — `arity_error`
**Conversation:** `MOD_DM06_drop_mono_prokka_keep_mlst_lis` (drop) — turn 1
**Prompt:** Run both prokka and mlst on a pre-existing Listeria monocytogenes assembly.

**Steps (LLM):** `step_4AN_genes__prokka, step_4TY_MLST__mlst`
**Steps (GT):**  `step_4AN_genes__prokka, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    asm = getInput()
    step_4AN_genes__prokka(asm)
    step_4TY_MLST__mlst(asm)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kingdomListeria = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    assembly = getSingleInput()

    // Prokka annotation
    prokka_in = assembly.multiMap {
        assembly: it
        kingdom: kingdomListeria
        reference: ['-', '-', getEmpty()]
    }
    step_4AN_genes__prokka(prokka_in.assembly, prokka_in.kingdom, prokka_in.reference)

    // MLST typing
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_4AN_genes__prokka` declares 1 input channels but 3 were given
```

### `MOD_DM09_drop_mono_flaA_keep_staramr_cam_t1` — `file_not_found`
**Conversation:** `MOD_DM09_drop_mono_flaA_keep_staramr_cam` (drop) — turn 1
**Prompt:** Run both flaA and staramr on a pre-existing Campylobacter jejuni assembly.

**Steps (LLM):** `step_4TY_flaA__flaA, step_4AN_AMR__staramr`
**Steps (GT):**  `step_4AN_AMR__staramr, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
workflow {
    asm = getInput()
    step_4TY_flaA__flaA(asm, param('genus_species'))
    step_4AN_AMR__staramr(asm, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def flaASchema = 'flaA'

def genusSpecies = 'Campylobacter jejuni'

def allowedGenus = ['campylobacter']

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_flaA_typing {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        step_4TY_flaA__flaA(assembly, genus_species)
        flaA_results = mlst_flaa_out.collectFile { it[0] == '*.csv' || it[0] == '*.tsv' ? it : null }.flatten()
    
}

workflow wf_staramr_amr {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        step_4AN_AMR__staramr(assembly, genus_species)
        staramr_results = staramr_out.collectFile { it[0] == 'result/*.tsv' || it[0] == 'result/*.xlsx' ? it : null }.flatten()
    
}

// --- ENTRYPOINT ---
workflow {
    assembly = getSingleInput()

    // Prepare genus_species channel as [sample_id, "Campylobacter jejuni"]
    genus_species = assembly.map { [ it[0], genusSpecies ] }

    // Run flaA and staramr in parallel
    wf_flaA_typing(assembly, genus_species)
    wf_staramr_amr(assembly, genus_species)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.CAM.224.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM13_drop_mono_prokka_keep_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_DM13_drop_mono_prokka_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both prokka and mlst on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_4AN_genes__prokka, step_4TY_MLST__mlst, step_3TX_species__kmerfinder`
**Steps (GT):**  `step_4AN_genes__prokka, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    asm = getInput()
    step_4AN_genes__prokka(asm)
    step_4TY_MLST__mlst(asm)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_annotation {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap {
            assembly: it
            kingdom: kingdom
        }.set { prokkaInput }
        step_4AN_genes__prokka(prokkaInput)
        step_4TY_MLST__mlst(assembly)
    
}

workflow wf_salmonella_species_check {
    
    take:
        
        assembly
        
    
    main:
        kmerfinder_out = step_3TX_species__kmerfinder(assembly)
    
    emit:
        
        assigned_species = kmerfinder_out.assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    // Optional species confirmation step (can be omitted if not required)
    wf_salmonella_species_check(getSingleInput())

    // Core annotation and MLST steps
    wf_salmonella_annotation(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_DM13_drop_mono_prokka_keep_mlst_sal_t2` — `missing_param`
**Conversation:** `MOD_DM13_drop_mono_prokka_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop prokka, keep only mlst.

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

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def stepCodeKmerfinder = '3TX_species__kmerfinder'

def stepCodeMLST = '4TY_MLST__mlst'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_mlst {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap {
            assembly: it
            riscd: [it[0]]
        }.set { prep }

        // Optional species confirmation
        kmerfinder_out = step_3TX_species__kmerfinder(prep.assembly)

        // MLST typing
        step_4TY_MLST__mlst(prep.assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    // Get the assembly input (FASTA)
    assembly = getSingleInput()

    // Run the Salmonella MLST workflow
    wf_salmonella_mlst(assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_DM14_drop_mono_abricate_keep_prokka_sal_t1` — `missing_param`
**Conversation:** `MOD_DM14_drop_mono_abricate_keep_prokka_sal` (drop) — turn 1
**Prompt:** Run both abricate and prokka on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4AN_AMR__abricate`
**Steps (GT):**  `step_4AN_AMR__abricate, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    asm = getInput()
    step_4AN_AMR__abricate(asm)
    step_4AN_genes__prokka(asm)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_assembly_analysis {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap {
            assembly: it
            kingdom: kingdom
        }.set { prokkaInput }

        kmerfinder_out = step_3TX_species__kmerfinder(assembly)
        step_4AN_AMR__abricate(assembly)
        prokka(assembly.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_assembly_analysis(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_DM14_drop_mono_abricate_keep_prokka_sal_t2` — `missing_param`
**Conversation:** `MOD_DM14_drop_mono_abricate_keep_prokka_sal` (drop) — turn 2
**Prompt:** Drop abricate, keep only prokka.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4AN_genes__prokka`
**Steps (GT):**  `step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    step_4AN_genes__prokka(getInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_species_confirmation {
    
    take:
        
        assembly
        
    
    main:
        kmerfinder_out = step_3TX_species__kmerfinder(assembly)
    
    emit:
        
        assigned_species = kmerfinder_out.assigned_species
        
    
}

workflow wf_genome_annotation {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    // Instantiate assembly channel from single input FASTA
    assembly = getSingleInput()

    // Species confirmation sub-workflow
    wf_species_confirmation(assembly)

    // Genome annotation sub-workflow
    wf_genome_annotation(assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_S01_cgmlst_retarget_lis_to_sal_t2` — `no_code`
**Conversation:** `MOD_S01_cgmlst_retarget_lis_to_sal` (switch_species) — turn 2
**Prompt:** Apply the same pipeline to Salmonella enterica.

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

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_S02_cgmlst_retarget_lis_to_eco_t1` — `missing_param`
**Conversation:** `MOD_S02_cgmlst_retarget_lis_to_eco` (switch_species) — turn 1
**Prompt:** cgMLST pipeline for Listeria monocytogenes from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def LISTERIA_MONOCYTOGENES_SPECIES = 'Listeria monocytogenes'

def LISTERIA_MONOCYTOGENES_SCHEMA = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_listeria {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembly = step_2AS_denovo__spades(trimmed).assembled

        kmerfinder_out = step_3TX_species__kmerfinder(assembly).assigned_species

        assembly.cross(kmerfinder_out) { extractKey(it) }.multiMap {
            assembly: it[0]
            species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, LISTERIA_MONOCYTOGENES_SPECIES, LISTERIA_MONOCYTOGENES_SCHEMA)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_cgmlst_listeria(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_S02_cgmlst_retarget_lis_to_eco_t2` — `missing_param`
**Conversation:** `MOD_S02_cgmlst_retarget_lis_to_eco` (switch_species) — turn 2
**Prompt:** Apply the same pipeline to Escherichia coli.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def escherichiaColiSchema = 'e_coli_chewie_2360_210531'

def escherichiaColiGenusSpecies = 'escherichia_coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_cgmlst {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembly = step_2AS_denovo__spades(trimmed).assembled

        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        assemblyAndSpecies = assembly.cross(assigned_species) { extractKey(it) }.multiMap {
            assembly: it[0]
            species: it[1][1]
        }

        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, escherichiaColiSchema)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_ecoli_cgmlst(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_S03_cgmlst_retarget_sal_to_lis_t2` — `no_code`
**Conversation:** `MOD_S03_cgmlst_retarget_sal_to_lis` (switch_species) — turn 2
**Prompt:** Apply the same pipeline to Listeria monocytogenes.

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

```
**Error excerpt:**
```
http 500: {"detail":"Invalid variable name ' it -> [it.baseName, it] ' in f-string template. Variable names cannot contain attribute access (.) or indexing ([])."}
```

### `MOD_SM01_mlst_retarget_lis_to_cam_t2` — `file_not_found`
**Conversation:** `MOD_SM01_mlst_retarget_lis_to_cam` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Campylobacter jejuni.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_flaA__flaA`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def genusSpecies = 'Campylobacter jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_jejuni_typing {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembly = step_2AS_denovo__spades(trimmed).assembled
        step_4TY_MLST__mlst(assembly)
        step_4TY_flaA__flaA(assembly, genusSpecies)
    
}

workflow step_1PP_trimming__fastp {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = fastp(rawreads).trimmed
        fastqc(trimmed)
        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap { 
          rawreads: it[0]
          trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed
        
    
}

workflow step_2AS_denovo__spades {
    
    take:
        
        trimmed
        
    
    main:
        denovo_out = denovo(trimmed)
        assembly_filter_out = assembly_filter(denovo_out.scaffolds)
        quast(assembly_filter_out.fasta)
        assembled = assembly_filter_out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_campylobacter_jejuni_typing(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.CAM.226.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_SM02_mlst_retarget_sal_to_cam_t1` — `missing_param`
**Conversation:** `MOD_SM02_mlst_retarget_sal_to_cam` (switch_species) — turn 1
**Prompt:** MLST pipeline for Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def speciesCode = 'Salmonella_enterica'

def speciesRiscd = '230515-020223051500512127-3TX_import-external'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_mlst {
    
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
            }.set { trimAndSpecies }
            step_2AS_mapping__bowtie(trimAndSpecies.trimmed, trimAndSpecies.referencePath)
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
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    wf_salmonella_mlst(trimmed, assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_SM02_mlst_retarget_sal_to_cam_t2` — `missing_param`
**Conversation:** `MOD_SM02_mlst_retarget_sal_to_cam` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Campylobacter jejuni.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_MLST__mlst, step_4TY_flaA__flaA`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def MLST_SCHEMA_CAMPYLOBACTER = 'campylobacter'

def FLAA_SCHEMA_NAME = 'flaA'

def GENUS_ALLOWED_FLAA = ['campylobacter']

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_mlst {
    
    take:
        
        raw_reads
        
    
    main:
        raw_reads.multiMap { reads: it }
            .set { ch_reads }

        // Step 1: Trimming
        trimmed = step_1PP_trimming__fastp(ch_reads.reads).trimmed

        // Step 2: De novo Assembly
        assembly = step_2AS_denovo__spades(trimmed).assembled

        // Step 3: Species Confirmation
        species_out = step_3TX_species__kmerfinder(assembly)
        assigned_species = species_out.assigned_species.map { [ it[0], it[1] ] }

        // Step 4: MLST Typing
        step_4TY_MLST__mlst(assembly)
        mlst_profile = mlst_out.map { [ it[0], it[1] ] }

        // Step 5 (Optional): flaA Typing
        step_4TY_flaA__flaA(assembly, assigned_species.map { it[1] })
        flaa_profile = flaa_out.map { [ it[0], it[1] ] }
    
    emit:
        
        assembly
        
        assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    // Instantiate input channel
    raw_reads = getSingleInput()

    // Run the custom MLST pipeline for Campylobacter jejuni
    wf_campylobacter_mlst(raw_reads)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_SM03_mlst_retarget_eco_to_cam_t1` — `missing_param`
**Conversation:** `MOD_SM03_mlst_retarget_eco_to_cam` (switch_species) — turn 1
**Prompt:** MLST pipeline for Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp, step_2AS_denovo__shovill`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def escherichiaColiSpecies = 'Escherichia coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_typing {
    
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
            }.set { trimAndSpecies }
            step_2AS_mapping__bowtie(trimAndSpecies.trimmed, trimAndSpecies.referencePath)
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
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__shovill(trimmed)
    wf_ecoli_typing(trimmed, assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_SM04_mlst_retarget_cam_to_lis_t1` — `missing_param`
**Conversation:** `MOD_SM04_mlst_retarget_cam_to_lis` (switch_species) — turn 1
**Prompt:** MLST pipeline for Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp, step_2AS_denovo__shovill`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def speciesRiscd = '240315-020240315005121273-3TX_species__kmerfinder'

def speciesCode = 'Campylobacter jejuni'

def mlstSchema = 'campylobacter'

def flaaSchema = 'campylobacter'

def chewbbacaSchema = 'campylobacter'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_typing {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        trimmed.cross(assigned_species) { extractKey(it) }.multiMap { 
          trimmed: it[0]
          species: it[1][1]
          referencePath: it[1][2]
        }.set { trimAndSpecies }

        step_2AS_mapping__bowtie(trimAndSpecies.trimmed, trimAndSpecies.referencePath)

        step_4AN_AMR__abricate(assembly)

        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

        assembly.cross(assigned_species) { extractKey(it) }.multiMap { 
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, chewbbacaSchema)
    
    emit:
        
        genus_species = assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())

    assembly = step_2AS_denovo__shovill(trimmed)

    wf_campylobacter_typing(trimmed, assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_SM04_mlst_retarget_cam_to_lis_t2` — `file_not_found`
**Conversation:** `MOD_SM04_mlst_retarget_cam_to_lis` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Listeria monocytogenes.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4AN_AMR__staramr, step_4TY_MLST__mlst`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

def listeriaKingdom = 'Bacteria'

def listeriaSpecies = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_typing {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembly = trimmed.map { [ it[0], it[1] ] }

        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        // Validate species is Listeria monocytogenes
        validated_species = assigned_species.map { speciesTuple ->
            def (riscd, species, refPath) = speciesTuple
            if (species == listeriaSpecies) {
                return [riscd, species, refPath]
            } else {
                log.warn "Species ${species} is not Listeria monocytogenes. Skipping MLST and downstream steps."
                return null
            }
        }.filter { it != null }

        // Proceed only if species is validated
        prokka_input = assembly.map { [ it[0], it[1], listeriaKingdom, '-', '-', getEmpty() ] }

        step_4AN_genes__prokka(prokka_input)

        step_4AN_AMR__abricate(assembly)

        step_4AN_AMR__staramr(assembly, listeriaSpecies)

        step_4TY_MLST__mlst(assembly)
    
}

workflow step_1PP_trimming__fastp {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = fastp(rawreads).trimmed

        fastqc(trimmed)

        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap { 
            rawreads: it[0]
            trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed
        
    
}

workflow step_3TX_species__kmerfinder {
    
    take:
        
        data
        
    
    main:
        kmerfinder(data);
        assigned_species = kmerfinder.out.check.map { [ it[0], getCalculatedSpecies(it[1]), getBacterialReferencePath(it[1]) ] }
    
    emit:
        
        assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_listeria_typing(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.LIS.237.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_SM05_mlst_retarget_cam_to_sal_t2` — `no_code`
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

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_SMA02_mlst_mono_retarget_lis_to_eco_t1` — `missing_param`
**Conversation:** `MOD_SMA02_mlst_mono_retarget_lis_to_eco` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Listeria monocytogenes assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4TY_MLST__mlst, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4AN_AMR__staramr, step_4TY_cgMLST__chewbbaca, step_4TY_flaA__flaA`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def listeriaSpecies = 'Listeria monocytogenes'

def cgMLSTSchema = "${params.assets_dir}/module_typing_bacteria/listeria_monocytogenes_cgmlst_schema"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_typing {
    
    take:
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        assembly.cross(assigned_species) { extractKey(it) }.multiMap { 
            assembly: it[0]
            species: it[1][1]
        }.set { assemblyAndSpecies }
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
        step_4AN_AMR__abricate(assembly)
        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, cgMLSTSchema)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
    
    emit:
        
        genus_species = assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_listeria_typing(getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_SMA02_mlst_mono_retarget_lis_to_eco_t2` — `missing_param`
**Conversation:** `MOD_SMA02_mlst_mono_retarget_lis_to_eco` (switch_species) — turn 2
**Prompt:** Same thing but for Escherichia coli.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca, step_2AS_mapping__bowtie`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def escherichiaColiRiscd = '220308-020220308005121273-4AN_import-external'

def escherichiaColiCode = 'Escherichia coli'

def escherichiaColiSchema = 'ecoli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_typing {
    
    take:
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        assembly.cross(assigned_species) { extractKey(it) }.multiMap { 
            assembly: it[0]
            species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4AN_AMR__abricate(assembly)
        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, escherichiaColiSchema)
    
}

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
            }.set { trimAndSpecies }
            step_2AS_mapping__bowtie(trimAndSpecies.trimmed, trimAndSpecies.referencePath)
        }

        wf_ecoli_typing(assembly)
    
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

### `MOD_SMA08_mlst_mono_retarget_sal_to_cam_t2` — `no_code`
**Conversation:** `MOD_SMA08_mlst_mono_retarget_sal_to_cam` (switch_species) — turn 2
**Prompt:** Same thing but for Campylobacter jejuni.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_SMA09_mlst_mono_retarget_eco_to_cam_t2` — `silent_no_op`
**Conversation:** `MOD_SMA09_mlst_mono_retarget_eco_to_cam` (switch_species) — turn 2
**Prompt:** Same thing but for Campylobacter jejuni.

**Steps (LLM):** `step_4TY_MLST__mlst`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def mlstExcludedSchemas = 'Campylobacter jejuni' 'Campylobacter coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    assembly = getSingleInput()
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_3T02_addAdd_eco_t3` — `silent_no_op`
**Conversation:** `MOD_3T02_addAdd_eco` (add) — turn 3
**Prompt:** Also add cgMLST in parallel.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def escherichiaColiSchema = 'e_coli_chewie_2360_210531'

def escherichiaColiSpecies = 'escherichia_coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    raw_reads = step_0SQ_rawreads__fastq(getSingleInput())
    trimmed = step_1PP_trimming__fastp(raw_reads).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4TY_cgMLST__chewbbaca(assembled.multiMap { [it[0], it[1], escherichiaColiSchema] }.combine([escherichiaColiSpecies]), escherichiaColiSpecies, escherichiaColiSchema)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_3T_AD01_addThenDrop_lis_t1` — `missing_param`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 1
**Prompt:** cgMLST profile for Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_1PP_hostdepl__bowtie, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def hostRiscd = '220308-020220308005121273-1PP_import-external'

def hostCode = 'Homo_sapiens'

def hostPath = "${params.assets_dir}/module_cgmlst_listeria/Homo_sapiens.fasta"

def kmerfinderRiscd = '220308-020220308005121273-3TX_import-external'

def kmerfinderCode = 'listeria_monocytogenes'

def kmerfinderPath = "${params.assets_dir}/module_cgmlst_listeria/kmerfinder_db"

def chewbbacaRiscd = '220308-020220308005121273-4TY_import-external'

def chewbbacaSchema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_prepare_inputs {
    
    take:
        
        reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(reads)
    
    emit:
        
        trimmed
        
    
}

workflow wf_host_depletion {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.cross(host).map { [ it[0][0], it[0][1], it[1][1] ] }.set { prep }
        depleted = step_1PP_hostdepl__bowtie(prep)
    
    emit:
        
        depleted
        
    
}

workflow wf_assembly {
    
    take:
        
        depleted
        
    
    main:
        assembly = step_2AS_denovo__shovill(depleted)
    
    emit:
        
        assembly
        
    
}

workflow wf_species_confirmation {
    
    take:
        
        assembly
        
    
    main:
        kmerfinder_out = step_3TX_species__kmerfinder(assembly)
        // Validate species is Listeria monocytogenes before proceeding
        assigned_species = kmerfinder_out.assigned_species.filter { it[1] == 'Listeria monocytogenes' }
    
    emit:
        
        assigned_species = kmerfinder_out.assigned_species
        
    
}

workflow wf_cgmlst_profiling {
    
    take:
        
        assembly
        
        assigned_species
        
    
    main:
        step_4TY_cgMLST__chewbbaca(assembly, assigned_species[0][1], chewbbacaSchema)
    
}

// --- ENTRYPOINT ---
workflow {
    // Define static references
    static_host = [ hostRiscd, hostCode, file(hostPath) ]
    static_kmerfinder = [ kmerfinderRiscd, kmerfinderCode, file(kmerfinderPath) ]

    // Prepare input channels
    reads = getSingleInput()
    host = static_host

    // Execute pipeline modules
    wf_prepare_inputs(reads)
    wf_host_depletion(wf_prepare_inputs.out.trimmed)
    wf_assembly(wf_host_depletion.out.depleted)
    wf_species_confirmation(wf_assembly.out.assembly)
    wf_cgmlst_profiling(wf_assembly.out.assembly, wf_species_confirmation.out.assigned_species)

    // Publish final cgMLST profile
    chewbbaca_out = step_4TY_cgMLST__chewbbaca(wf_assembly.out.assembly, wf_species_confirmation.out.assigned_species[0][1], chewbbacaSchema)
    chewbbaca_out.alleles_with_new.publish(file("${params.outdir}/cgMLST_profiles"), pattern: '*_results_alleles.tsv')
    chewbbaca_out.stats.publish(file("${params.outdir}/cgMLST_profiles"), pattern: '*_results_statistics.tsv')
    chewbbaca_check_out = chewbbaca_check(chewbbaca_out.stats)
    chewbbaca_check_out.check.publish(file("${params.outdir}/cgMLST_profiles"), pattern: '*_import_chewbbaca_check.csv')
    hashing(chewbbaca_out.alleles, file("${params.assets_dir}/module_cgmlst_listeria/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip")).publish(file("${params.outdir}/cgMLST_profiles"), pattern: '*_chewbbaca_results_crc32.tsv')
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD01_addThenDrop_lis_t2` — `missing_param`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 2
**Prompt:** Also add ABRicate AMR screening in parallel.

**Steps (LLM):** `step_1PP_trimming__fastp, step_1PP_hostdepl__bowtie, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate`
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

include { getHostUnkeyed; getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey } from '../functions/common.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { module_qc_quast } from '../modules/module_qc_quast'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def kmerfinderDbPath = "${params.assets_dir}/step_3TX_species__kmerfinder__db"

def chewbbacaSchemaPath = "${params.assets_dir}/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip"

def abricateDbPath = "${params.assets_dir}/databases/vfdb"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_monocytogenes_cgmlst_amr {
    
    take:
        
        raw_reads
        
        host_reference
        
        kmerfinder_db
        
        chewbbaca_schema
        
        abricate_db
        
    
    main:
        trimmed = step_1PP_trimming__fastp(raw_reads).trimmed

        trimmedAndHost = trimmed.combine(host_reference) { extractKey(it) }.map { [ it[0][0], it[0][1], it[1] ] }
        depleted = step_1PP_hostdepl__bowtie(trimmedAndHost)

        assembly = step_2AS_denovo__shovill(depleted)
        module_qc_quast(assembly)

        kmerfinder_out = step_3TX_species__kmerfinder(assembly)

        listeria_assembly = kmerfinder_out.assigned_species.filter { it[1] == 'Listeria monocytogenes' }.map { it[0,1] }

        listeria_assembly_crossed = listeria_assembly.cross(kmerfinder_db) { extractKey(it) }.map { [ it[0][0], it[0][1], it[1][1] ] }

        listeria_assembly_crossed_crossed = listeria_assembly_crossed.cross(chewbbaca_schema) { extractKey(it) }.map { [ it[0][0], it[0][1], it[0][2], it[1][1] ] }

        step_4TY_cgMLST__chewbbaca(listeria_assembly_crossed_crossed.reads, listeria_assembly_crossed_crossed.genus_species, listeria_assembly_crossed_crossed.schema)

        listeria_assembly_crossed_abricate = listeria_assembly.cross(abricate_db) { extractKey(it) }.map { [ it[0][0], it[0][1], it[1][1] ] }
        step_4AN_AMR__abricate(listeria_assembly_crossed_abricate)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_listeria_monocytogenes_cgmlst_amr(getSingleInput(), getHostUnkeyed(), kmerfinderDbPath, chewbbacaSchemaPath, abricateDbPath)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD01_addThenDrop_lis_t3` — `missing_param`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 3
**Prompt:** Actually, drop the ABRicate step.

**Steps (LLM):** `step_1PP_trimming__fastp, step_1PP_hostdepl__bowtie, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { module_qc_quast } from '../modules/module_qc_quast'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def hostRiscd = '220308-020220308005121273-1PP_import-external'

def hostCode = 'Homo_sapiens'

def hostPath = "${params.assets_dir}/module_cgMLST_Listeria_monocytogenes/Homo_sapiens.GRCh38.dna.primary_assembly.fa"

def kmerfinderDbRiscd = '220308-020220308005121273-3TX_import-external'

def kmerfinderDbCode = 'Listeria_monocytogenes'

def kmerfinderDbPath = "${params.assets_dir}/module_cgMLST_Listeria_monocytogenes/kmerfinder_db"

def chewbbacaSchemaRiscd = '220308-020220308005121273-4TY_import-external'

def chewbbacaSchemaCode = 'l_mono_chewie_1748_220623'

def chewbbacaSchemaPath = "${params.assets_dir}/module_cgMLST_Listeria_monocytogenes/l_mono_chewie_1748_220623.zip"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_prepare_inputs {
    
    take:
        
        raw_reads
        
    
    main:
        // Trim reads using fastp
        trimmed = step_1PP_trimming__fastp(raw_reads).trimmed

        // Prepare host reference tuple
        trimmed.multiMap {
            trimmed: it
            reference: [ hostRiscd, hostCode, file(hostPath) ]
        }.set { trAndRef }

        // Deplete host contamination
        trimmedAndHost = trAndRef.trimmed.cross(trAndRef.reference) { extractKey(it) }.map { [ it[0][0], it[0][1], it[1][1] ] }
        depleted = step_1PP_hostdepl__bowtie(trimmedAndHost)
    
    emit:
        
        depleted
        
    
}

workflow wf_assembly {
    
    take:
        
        depleted
        
    
    main:
        // Assemble using Shovill
        assembly = step_2AS_denovo__shovill(depleted).assembly
    
    emit:
        
        assembly
        
    
}

workflow wf_assembly_qc {
    
    take:
        
        assembly
        
    
    main:
        // Run QUAST for assembly QC
        module_qc_quast(assembly)
    
}

workflow wf_species_confirmation {
    
    take:
        
        assembly
        
    
    main:
        // Confirm species using KmerFinder
        kmerfinder_out = step_3TX_species__kmerfinder(assembly)
    
    emit:
        
        assigned_species = kmerfinder_out.assigned_species
        
    
}

workflow wf_cgmlst_profiling {
    
    take:
        
        assembly
        
        assigned_species
        
    
    main:
        // Prepare inputs for chewBBACA
        assembly.multiMap {
            assembly: it
            genus_species: assigned_species.map { it[1] }
            schema: chewbbacaSchemaCode
        }.set { chewbbaca_inputs }

        // Generate cgMLST profile
        step_4TY_cgMLST__chewbbaca(chewbbaca_inputs.assembly, chewbbaca_inputs.genus_species, chewbbaca_inputs.schema)
    
}

// --- ENTRYPOINT ---
workflow {
    // Prepare inputs: trimming and host depletion
    depleted = wf_prepare_inputs(getSingleInput()).depleted

    // Assemble depleted reads
    assembly = wf_assembly(depleted).assembly

    // Assembly QC
    wf_assembly_qc(assembly)

    // Species confirmation
    assigned_species = wf_species_confirmation(assembly).assigned_species

    // cgMLST profiling
    wf_cgmlst_profiling(assembly, assigned_species)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD02_addThenDrop_eco_t1` — `missing_param`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 1
**Prompt:** cgMLST profile for Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def genusSpecies = 'escherichia coli'

def schema = 'e_coli_chewie_2360_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_cgmlst {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        kmerfinder_out = step_3TX_species__kmerfinder(trimmed)

        assembly = step_2AS_denovo__shovill(trimmed)

        step_4TY_cgMLST__chewbbaca(assembly.assembly, genusSpecies, schema)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_ecoli_cgmlst(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD02_addThenDrop_eco_t2` — `missing_param`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 2
**Prompt:** Also add ABRicate AMR screening in parallel.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def genusSpecies = 'escherichia coli'

def cgMLSTSchema = 'e_coli_chewie_2360_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_cgmlst_amr {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        kmerfinder_out = step_3TX_species__kmerfinder(trimmed)

        assembly = step_2AS_denovo__shovill(trimmed).assembly

        // Cross assembly with genus species and schema for chewBBACA
        assembly.multiMap {
            assembly: it
            genus_species: genusSpecies
            schema: cgMLSTSchema
        }.set { assemblyAndParams }

        step_4TY_cgMLST__chewbbaca(assemblyAndParams.assembly, assemblyAndParams.genus_species, assemblyAndParams.schema)

        step_4AN_AMR__abricate(assembly)
    
}

workflow wf_validate_ecoli {
    
    take:
        
        kmerfinder_check
        
    
    main:
        kmerfinder_check.branch {
            e_coli: it[1].toLowerCase().contains('escherichia coli')
            not_e_coli: true
        }.set { species_branch }

        if (species_branch.not_e_coli) {
            error "Species confirmation failed: detected species is not Escherichia coli. Detected: ${species_branch.not_e_coli[1]}"
        }
    
}

// --- ENTRYPOINT ---
workflow {
    // Validate species before proceeding
    kmerfinder_check = step_3TX_species__kmerfinder(getSingleInput()).assigned_species
    wf_validate_ecoli(kmerfinder_check)

    // Proceed with full pipeline only if species is confirmed
    wf_ecoli_cgmlst_amr(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD02_addThenDrop_eco_t3` — `file_not_found`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 3
**Prompt:** Actually, drop the ABRicate step.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def chewieSchema = 'e_coli_chewie_2360_210531'

def genusSpecies = 'escherichia coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_cgmlst {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        species_out = step_3TX_species__kmerfinder(trimmed)
        assigned_species = species_out.assigned_species

        assembly = step_2AS_denovo__shovill(trimmed)

        chewbbaca(assembly.assembly, genusSpecies, chewieSchema)
    
}

workflow step_3TX_species__kmerfinder {
    
    take:
        
        trimmed
        
    
    main:
        kmerfinder_out = kmerfinder(trimmed)
    
    emit:
        
        assigned_species = kmerfinder_out.assigned_species
        
    
}

workflow step_2AS_denovo__shovill {
    
    take:
        
        trimmed
        
    
    main:
        shovill_out = shovill(trimmed)
    
    emit:
        
        assembly = shovill_out.assembly
        
    
}

workflow step_1PP_trimming__fastp {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = fastp(rawreads).trimmed
    
    emit:
        
        trimmed
        
    
}

// --- ENTRYPOINT ---
workflow {
    // Validate input reads
    rawreads = getSingleInput()

    // Run E. coli cgMLST workflow
    wf_ecoli_cgmlst(rawreads)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.ECO.232.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_AD03_addThenDrop_sal_t1` — `missing_param`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 1
**Prompt:** cgMLST profile for Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def genusSpecies = 'Salmonella enterica'

def cgMLSTSchema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Trimming Reads
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    // Step 2: Species Identification (Confirmation)
    species_out = step_3TX_species__kmerfinder(trimmed)

    // Step 3: De Novo Assembly
    assembly = step_2AS_denovo__shovill(trimmed).assembly

    // Step 4: cgMLST Profiling
    step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, cgMLSTSchema)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD03_addThenDrop_sal_t2` — `missing_param`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 2
**Prompt:** Also add ABRicate AMR screening in parallel.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def genusSpecies = 'Salmonella enterica'

def cgMLSTSchema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_cgmlst_amr {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        kmerfinder_out = step_3TX_species__kmerfinder(trimmed)

        assembly = step_2AS_denovo__shovill(trimmed)
        step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, cgMLSTSchema)
        step_4AN_AMR__abricate(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_cgmlst_amr(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD03_addThenDrop_sal_t3` — `missing_param`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 3
**Prompt:** Actually, drop the ABRicate step.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def genusSpecies = 'Salmonella_enterica'

def cgMLSTSchema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Trimming Reads
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    // Step 2: Species Identification (Confirmation)
    species_out = step_3TX_species__kmerfinder(trimmed)

    // Step 3: De Novo Assembly
    assembly = step_2AS_denovo__shovill(trimmed).assembly

    // Step 4: cgMLST Profiling
    step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, cgMLSTSchema)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_RA02_replaceThenAdd_eco_t2` — `no_code`
**Conversation:** `MOD_3T_RA02_replaceThenAdd_eco` (replace) — turn 2
**Prompt:** Use Shovill instead of SPAdes.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_3T_RA03_replaceThenAdd_sal_t2` — `file_not_found`
**Conversation:** `MOD_3T_RA03_replaceThenAdd_sal` (replace) — turn 2
**Prompt:** Use Shovill instead of SPAdes.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def trimmedRiscd = '220308-020220308005121273-1PP_trimming-fastp'

def assemblyRiscd = '220308-020220308005121273-2AS_denovo-shovill'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed_out = step_1PP_trimming__fastp(rawreads)

        shovill_out = step_2AS_denovo__shovill(trimmed_out.trimmed)
    
    emit:
        
        assembly = shovill_out.assembly
        
    
}

workflow step_1PP_trimming__fastp {
    
    take:
        
        rawreads
        
    
    main:
        fastp_out = fastp(rawreads)

        fastqc(trimmed)
        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap {
            rawreads: it[0]
            trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed = fastp_out.trimmed
        
    
}

workflow step_2AS_denovo__shovill {
    
    take:
        
        rawreads
        
    
    main:
        shovill_out = shovill(rawreads)

        shovill_se_out = shovill_se(rawreads)
        contigs_from_pe = shovill_out.assembly
        contigs_from_se = shovill_se_out.assembly
        contigs = contigs_from_pe.mix(contigs_from_se)

        quast(contigs)
        if (!params.skip_checkm) {
            checkm(contigs)
        }
    
    emit:
        
        assembly = shovill_out.assembly
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_and_assemble(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn_mistral_small/_shared_inputdir/2026/2026.SAL.243.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_SA01_switchThenAdd_lis_to_sal_t1` — `missing_param`
**Conversation:** `MOD_3T_SA01_switchThenAdd_lis_to_sal` (switch_species) — turn 1
**Prompt:** MLST pipeline for Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def listeriaKingdom = 'Bacteria'

def listeriaSpeciesCode = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_mlst {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            kingdom: listeriaKingdom
            species_code: listeriaSpeciesCode
        }.set { trimmedAndSpecies }

        kmerfinder_out = step_3TX_species__kmerfinder(trimmedAndSpecies.trimmed)

        spades_out = step_2AS_denovo__spades(trimmedAndSpecies.trimmed)

        step_4TY_MLST__mlst(spades_out.assembled)
    
    emit:
        
        assembly = spades_out.assembled
        
        assigned_species = kmerfinder_out.assigned_species
        
    
}

workflow wf_listeria_optional_annotation {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], listeriaKingdom, '-', '-', getEmpty() ] })
    
}

workflow wf_listeria_optional_amr {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_AMR__abricate(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    wf_listeria_mlst(trimmed)

    if (params.annotate) {
        wf_listeria_optional_annotation(wf_listeria_mlst.assembly)
    }

    if (params.detect_amr) {
        wf_listeria_optional_amr(wf_listeria_mlst.assembly)
    }
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_SA01_switchThenAdd_lis_to_sal_t2` — `missing_param`
**Conversation:** `MOD_3T_SA01_switchThenAdd_lis_to_sal` (switch_species) — turn 2
**Prompt:** Apply the same to Salmonella enterica.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_genes__prokka, step_4AN_AMR__abricate`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kingdomSalmonella = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    kmerfinder_out = step_3TX_species__kmerfinder(trimmed)

    spades_out = step_2AS_denovo__spades(trimmed)

    step_4TY_MLST__mlst(spades_out.assembled)

    step_4AN_genes__prokka(spades_out.assembled.map { [ it[0], it[1], kingdomSalmonella, '-', '-', getEmpty() ] })

    step_4AN_AMR__abricate(spades_out.assembled)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_SA01_switchThenAdd_lis_to_sal_t3` — `silent_no_op`
**Conversation:** `MOD_3T_SA01_switchThenAdd_lis_to_sal` (switch_species) — turn 3
**Prompt:** Also add cgMLST in parallel for this species.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca, step_4AN_genes__prokka, step_4AN_AMR__abricate`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def genusSpecies = 'Salmonella enterica'

def cgMLSTSchema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_mlst_cgmlst {
    
    take:
        
        rawReads
        
    
    main:
        rawReads | step_1PP_trimming__fastp | trimOut -> {
            trimmed = trimOut.trimmed
            
            // Species confirmation
            kmerfinder_out = step_3TX_species__kmerfinder(trimmed)
            
            // De novo assembly
            spades_out = step_2AS_denovo__spades(trimmed)
            assembled = spades_out.assembled
            
            // MLST typing
            step_4TY_MLST__mlst(assembled)
            
            // cgMLST typing (parallel)
            genusSpeciesTuple = [genusSpecies]
            schemaTuple = [cgMLSTSchema]
            
            // Cross assembly with genusSpecies and schema
            assembled.cross(genusSpeciesTuple).multiMap { 
                assembly: it[0]
                genus_species: it[1]
            }.cross(schemaTuple).multiMap {
                assembly: it[0].assembly
                genus_species: it[0].genus_species
                schema: it[1]
            }.set { cgmlstInput }
            
            step_4TY_cgMLST__chewbbaca(cgmlstInput.assembly, cgmlstInput.genus_species, cgmlstInput.schema)
            
            // Optional annotation
            prokkaInput = assembled.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] }
            step_4AN_genes__prokka(prokkaInput)
            
            // Optional AMR detection
            step_4AN_AMR__abricate(assembled)
        }
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_mlst_cgmlst(getSingleInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_3T_SA02_switchThenAdd_eco_to_lis_t2` — `arity_error`
**Conversation:** `MOD_3T_SA02_switchThenAdd_eco_to_lis` (switch_species) — turn 2
**Prompt:** Apply the same to Listeria monocytogenes.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def mlstSpecies = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_assembly_mlst {
    
    take:
        
        raw_reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(raw_reads).trimmed
        assembly = step_2AS_denovo__shovill(trimmed).assembly
        step_4TY_MLST__mlst(assembly, mlstSpecies)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_assembly_mlst(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_trim_assembly_mlst:step_4TY_MLST__mlst` declares 1 input channels but 2 were given
```

### `MOD_3T_SA03_switchThenAdd_sal_to_eco_t1` — `missing_param`
**Conversation:** `MOD_3T_SA03_switchThenAdd_sal_to_eco` (switch_species) — turn 1
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def prokkaKingdom = 'Bacteria'

def prokkaRiscd = '-'

def prokkaRefid = '-'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_typing {
    
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
          }.set { trimAndSpecies }
          step_2AS_mapping__bowtie(trimAndSpecies.trimmed, trimAndSpecies.referencePath)
        }

        step_4AN_AMR__abricate(assembly)

        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], prokkaKingdom, prokkaRiscd, prokkaRefid, prokkaRefpath ] })

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
    prokkaRefpath = getEmpty()
    wf_salmonella_typing(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_SA03_switchThenAdd_sal_to_eco_t2` — `missing_param`
**Conversation:** `MOD_3T_SA03_switchThenAdd_sal_to_eco` (switch_species) — turn 2
**Prompt:** Apply the same to Escherichia coli.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp, step_2AS_denovo__shovill`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def escherichiaColiRiscd = '220308-020220308005121273-4AN_import-external'

def escherichiaColiCode = 'Escherichia coli'

def escherichiaColiPath = "${params.assets_dir}/module_typing_bacteria/Escherichia_coli.fasta"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_typing {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        trimmed.cross(assigned_species) { extractKey(it) }.multiMap { 
          trimmed: it[0]
          species: it[1][1]
          referencePath: it[1][2]
        }.set { trimAndSpecies }

        step_2AS_mapping__bowtie(trimAndSpecies.trimmed, trimAndSpecies.referencePath)

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
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__shovill(trimmed)

    wf_ecoli_typing(trimmed, assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_SA03_switchThenAdd_sal_to_eco_t3` — `missing_param`
**Conversation:** `MOD_3T_SA03_switchThenAdd_sal_to_eco` (switch_species) — turn 3
**Prompt:** Also add cgMLST in parallel for this species.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4AN_AMR__abricate, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def escherichiaColiSpecies = 'Escherichia coli'

def escherichiaColiSchema = "${params.assets_dir}/module_typing_bacteria/escherichia_coli_schema"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_typing {
    
    take:
        
        raw_reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(raw_reads).trimmed
        assembly = step_2AS_denovo__shovill(trimmed).assembly

        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        assemblyAndSpecies = assembly.cross(assigned_species) { extractKey(it) }.multiMap {
            assembly: it[0]
            species: it[1][1]
        }

        step_4AN_AMR__abricate(assemblyAndSpecies.assembly)
        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, escherichiaColiSchema)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_ecoli_typing(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```
