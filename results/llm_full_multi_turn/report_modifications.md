# LLM multi-turn evaluation — detailed report

Total conversations: **159**  ·  total turns: **330**  ·  per-turn pass: **217/330**  ·  conversations fully passing: **91/159**

## Pass rate by modification kind (per turn)

| kind | turns | pass |
|----|-----:|-----:|
| `add` | 104 | 82 |
| `replace` | 99 | 77 |
| `drop` | 66 | 32 |
| `switch_species` | 61 | 26 |

## Error category breakdown

| Category | Count |
|----|----:|
| `none` | 213 |
| `missing_param` | 40 |
| `silent_no_op` | 26 |
| `partial_dag` | 25 |
| `file_not_found` | 16 |
| `arity_error` | 5 |
| `no_code` | 3 |
| `ngsmanager_naming` | 2 |

## Per-conversation outcome

| # | conv_id | kind | t1 | t2 | error category (failing turn) |
|---|---------|------|----|----|------------------------------|
| 1 | `MOD_M01_E02_add_mlst` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 2 | `MOD_M02_D01_add_chewbbaca` | `add` | ✅ | ✅ |  |
| 3 | `MOD_M03_B01_add_trimming` | `add` | ✅ | ✅ |  |
| 4 | `MOD_M04_A04_add_mlst_parallel` | `add` | ❌ | ❌ | t1: `missing_param` |
| 5 | `MOD_M05_E07_add_prokka` | `add` | ✅ | ❌ | t2: `partial_dag` |
| 6 | `MOD_M06_D01_replace_spades_with_shovill` | `replace` | ✅ | ✅ |  |
| 7 | `MOD_M07_D03_replace_trimmomatic_with_fastp` | `replace` | ❌ | ❌ | t1: `silent_no_op` |
| 8 | `MOD_M08_E01_replace_spades_with_unicycler` | `replace` | ✅ | ✅ |  |
| 9 | `MOD_M09_E07_replace_abricate_with_prokka` | `replace` | ❌ | ❌ | t1: `silent_no_op` |
| 10 | `MOD_M10_A05_replace_cgmlst_with_mlst` | `replace` | ✅ | ✅ |  |
| 11 | `MOD_M11_H01_drop_cgmlst` | `drop` | ✅ | ✅ |  |
| 12 | `MOD_M12_D01_drop_assembly` | `drop` | ✅ | ✅ |  |
| 13 | `MOD_M13_I01_drop_kmerfinder` | `drop` | ✅ | ✅ |  |
| 14 | `MOD_M14_E02_switch_species_to_salmonella` | `switch_species` | ❌ | ✅ | t1: `file_not_found` |
| 15 | `MOD_M15_A04_switch_species_to_ecoli` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 16 | `MOD_M16_E07_switch_species_to_salmonella` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 17 | `MOD_M17_D05_switch_species_to_ecoli` | `switch_species` | ❌ | ❌ | t1: `partial_dag` |
| 18 | `MOD_K01_add_mlst_to_chewbbaca_lis_spades` | `add` | ✅ | ✅ |  |
| 19 | `MOD_K02_add_mlst_to_chewbbaca_sal_spades` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 20 | `MOD_K03_add_mlst_to_chewbbaca_eco_spades` | `add` | ✅ | ✅ |  |
| 21 | `MOD_K04_add_abricate_to_chewbbaca_lis_spades` | `add` | ❌ | ✅ | t1: `missing_param` |
| 22 | `MOD_K05_add_abricate_to_chewbbaca_sal_spades` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 23 | `MOD_K06_add_prokka_to_chewbbaca_lis_spades` | `add` | ✅ | ✅ |  |
| 24 | `MOD_K07_add_prokka_to_chewbbaca_sal_spades` | `add` | ✅ | ✅ |  |
| 25 | `MOD_K08_add_chewbbaca_to_mlst_lis_spades` | `add` | ✅ | ✅ |  |
| 26 | `MOD_K09_add_chewbbaca_to_mlst_eco_spades` | `add` | ✅ | ❌ | t2: `silent_no_op` |
| 27 | `MOD_K10_add_abricate_to_mlst_lis_spades` | `add` | ✅ | ✅ |  |
| 28 | `MOD_K11_add_abricate_to_mlst_eco_spades` | `add` | ✅ | ✅ |  |
| 29 | `MOD_K12_add_abricate_to_mlst_sal_spades` | `add` | ✅ | ❌ | t2: `partial_dag` |
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
| 45 | `MOD_K28_add_prokka_to_staramr_cam_spades` | `add` | ✅ | ❌ | t2: `arity_error` |
| 46 | `MOD_K29_add_flaA_to_mlst_cam_spades` | `add` | ✅ | ✅ |  |
| 47 | `MOD_K30_add_staramr_to_mlst_cam_spades` | `add` | ✅ | ✅ |  |
| 48 | `MOD_K31_add_abricate_to_mlst_lis_shovill` | `add` | ✅ | ✅ |  |
| 49 | `MOD_K32_add_prokka_to_mlst_sal_shovill` | `add` | ✅ | ✅ |  |
| 50 | `MOD_K33_add_abricate_to_chewbbaca_lis_unicycler` | `add` | ✅ | ✅ |  |
| 51 | `MOD_K34_add_abricate_to_chewbbaca_sal_unicycler` | `add` | ✅ | ✅ |  |
| 52 | `MOD_K35_add_chewbbaca_to_mlst_eco_shovill` | `add` | ✅ | ✅ |  |
| 53 | `MOD_K36_add_chewbbaca_to_mlst_sal_shovill` | `add` | ✅ | ✅ |  |
| 54 | `MOD_K37_add_abricate_to_mlst_lis_spades` | `add` | ✅ | ✅ |  |
| 55 | `MOD_K38_add_prokka_to_mlst_eco_spades` | `add` | ✅ | ❌ | t2: `partial_dag` |
| 56 | `MOD_R01_replace_asm_spades_to_shovill_lis` | `replace` | ✅ | ✅ |  |
| 57 | `MOD_R02_replace_asm_spades_to_shovill_sal` | `replace` | ❌ | ❌ | t1: `partial_dag` |
| 58 | `MOD_R03_replace_asm_spades_to_shovill_eco` | `replace` | ✅ | ✅ |  |
| 59 | `MOD_R04_replace_asm_spades_to_shovill_cam` | `replace` | ❌ | ❌ | t1: `partial_dag` |
| 60 | `MOD_R05_replace_asm_spades_to_unicycler_lis` | `replace` | ❌ | ✅ | t1: `silent_no_op` |
| 61 | `MOD_R06_replace_asm_spades_to_unicycler_sal` | `replace` | ❌ | ✅ | t1: `partial_dag` |
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
| 73 | `MOD_RT06_replace_trim_trimmomatic_to_fastp_sal` | `replace` | ❌ | ✅ | t1: `silent_no_op` |
| 74 | `MOD_RTY01_replace_typing_mlst_to_chewbbaca_lis` | `replace` | ✅ | ❌ | t2: `file_not_found` |
| 75 | `MOD_RTY02_replace_typing_mlst_to_chewbbaca_sal` | `replace` | ✅ | ❌ | t2: `file_not_found` |
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
| 91 | `MOD_RM06_replace_mono_abricate_to_prokka_eco` | `replace` | ❌ | ❌ | t1: `missing_param` |
| 92 | `MOD_RM07_replace_mono_abricate_to_mlst_sal` | `replace` | ✅ | ✅ |  |
| 93 | `MOD_RM08_replace_mono_flaA_to_staramr_cam` | `replace` | ✅ | ✅ |  |
| 94 | `MOD_RM09_replace_mono_staramr_to_flaA_cam` | `replace` | ✅ | ✅ |  |
| 95 | `MOD_RM10_replace_mono_staramr_to_mlst_cam` | `replace` | ✅ | ✅ |  |
| 96 | `MOD_D01_drop_chewbbaca_keep_mlst_lis` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 97 | `MOD_D02_drop_chewbbaca_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `silent_no_op` |
| 98 | `MOD_D03_drop_chewbbaca_keep_mlst_eco` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 99 | `MOD_D04_drop_mlst_keep_chewbbaca_lis` | `drop` | ✅ | ❌ | t2: `missing_param` |
| 100 | `MOD_D05_drop_mlst_keep_chewbbaca_sal` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 101 | `MOD_D06_drop_abricate_keep_mlst_lis` | `drop` | ❌ | ❌ | t1: `silent_no_op` |
| 102 | `MOD_D07_drop_abricate_keep_mlst_eco` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 103 | `MOD_D08_drop_abricate_keep_mlst_sal` | `drop` | ❌ | ✅ | t1: `missing_param` |
| 104 | `MOD_D09_drop_prokka_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `silent_no_op` |
| 105 | `MOD_D10_drop_prokka_keep_abricate_lis` | `drop` | ❌ | ❌ | t1: `silent_no_op` |
| 106 | `MOD_D11_drop_flaA_keep_mlst_cam` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 107 | `MOD_D12_drop_staramr_keep_mlst_cam` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 108 | `MOD_DA01_drop_assembly_lis` | `drop` | ✅ | ✅ |  |
| 109 | `MOD_DA02_drop_assembly_eco` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 110 | `MOD_DA03_drop_assembly_sal` | `drop` | ✅ | ✅ |  |
| 111 | `MOD_DA04_drop_assembly_cam` | `drop` | ✅ | ✅ |  |
| 112 | `MOD_DM01_drop_mono_chewbbaca_keep_mlst_lis` | `drop` | ✅ | ✅ |  |
| 113 | `MOD_DM02_drop_mono_chewbbaca_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 114 | `MOD_DM03_drop_mono_mlst_keep_chewbbaca_lis` | `drop` | ✅ | ✅ |  |
| 115 | `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco` | `drop` | ❌ | ✅ | t1: `missing_param` |
| 116 | `MOD_DM05_drop_mono_abricate_keep_mlst_sal` | `drop` | ✅ | ✅ |  |
| 117 | `MOD_DM06_drop_mono_prokka_keep_mlst_lis` | `drop` | ✅ | ✅ |  |
| 118 | `MOD_DM07_drop_mono_staramr_keep_mlst_cam` | `drop` | ✅ | ✅ |  |
| 119 | `MOD_DM08_drop_mono_staramr_keep_flaA_cam` | `drop` | ✅ | ✅ |  |
| 120 | `MOD_DM09_drop_mono_flaA_keep_staramr_cam` | `drop` | ✅ | ✅ |  |
| 121 | `MOD_DM10_drop_mono_flaA_keep_mlst_cam` | `drop` | ✅ | ✅ |  |
| 122 | `MOD_DM11_drop_mono_abricate_keep_prokka_eco` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 123 | `MOD_DM12_drop_mono_prokka_keep_abricate_lis` | `drop` | ❌ | ✅ | t1: `arity_error` |
| 124 | `MOD_DM13_drop_mono_prokka_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 125 | `MOD_DM14_drop_mono_abricate_keep_prokka_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 126 | `MOD_S01_cgmlst_retarget_lis_to_sal` | `switch_species` | ✅ | ❌ | t2: `arity_error` |
| 127 | `MOD_S02_cgmlst_retarget_lis_to_eco` | `switch_species` | ❌ | ❌ | t1: `file_not_found` |
| 128 | `MOD_S03_cgmlst_retarget_sal_to_lis` | `switch_species` | ✅ | ✅ |  |
| 129 | `MOD_S04_cgmlst_retarget_sal_to_eco` | `switch_species` | ✅ | ❌ | t2: `arity_error` |
| 130 | `MOD_S05_cgmlst_retarget_eco_to_lis` | `switch_species` | ❌ | ✅ | t1: `file_not_found` |
| 131 | `MOD_S06_cgmlst_retarget_eco_to_sal` | `switch_species` | ✅ | ✅ |  |
| 132 | `MOD_SM01_mlst_retarget_lis_to_cam` | `switch_species` | ❌ | ❌ | t1: `silent_no_op` |
| 133 | `MOD_SM02_mlst_retarget_sal_to_cam` | `switch_species` | ❌ | ✅ | t1: `silent_no_op` |
| 134 | `MOD_SM03_mlst_retarget_eco_to_cam` | `switch_species` | ❌ | ❌ | t1: `silent_no_op` |
| 135 | `MOD_SM04_mlst_retarget_cam_to_lis` | `switch_species` | ❌ | ❌ | t1: `partial_dag` |
| 136 | `MOD_SM05_mlst_retarget_cam_to_sal` | `switch_species` | ❌ | ❌ | t1: `silent_no_op` |
| 137 | `MOD_SM06_mlst_retarget_cam_to_eco` | `switch_species` | ❌ | ❌ | t1: `silent_no_op` |
| 138 | `MOD_SMA01_mlst_mono_retarget_lis_to_sal` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 139 | `MOD_SMA02_mlst_mono_retarget_lis_to_eco` | `switch_species` | ✅ | ✅ |  |
| 140 | `MOD_SMA03_mlst_mono_retarget_sal_to_lis` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 141 | `MOD_SMA04_mlst_mono_retarget_sal_to_eco` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 142 | `MOD_SMA05_mlst_mono_retarget_eco_to_lis` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 143 | `MOD_SMA06_mlst_mono_retarget_eco_to_sal` | `switch_species` | ✅ | ❌ | t2: `missing_param` |
| 144 | `MOD_SMA07_mlst_mono_retarget_lis_to_cam` | `switch_species` | ✅ | ✅ |  |
| 145 | `MOD_SMA08_mlst_mono_retarget_sal_to_cam` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 146 | `MOD_SMA09_mlst_mono_retarget_eco_to_cam` | `switch_species` | ✅ | ✅ |  |
| 147 | `MOD_SMA10_mlst_mono_retarget_cam_to_lis` | `switch_species` | ✅ | ✅ |  |
| 148 | `MOD_3T01_addAdd_lis` | `add` | ✅ | ✅ | t3: `file_not_found` |
| 149 | `MOD_3T02_addAdd_eco` | `add` | ✅ | ✅ | t3: `file_not_found` |
| 150 | `MOD_3T03_addAdd_sal` | `add` | ✅ | ✅ |  |
| 151 | `MOD_3T_AD01_addThenDrop_lis` | `add` | ❌ | ❌ | t1: `missing_param` |
| 152 | `MOD_3T_AD02_addThenDrop_eco` | `add` | ❌ | ❌ | t1: `missing_param` |
| 153 | `MOD_3T_AD03_addThenDrop_sal` | `add` | ❌ | ❌ | t1: `missing_param` |
| 154 | `MOD_3T_RA01_replaceThenAdd_lis` | `replace` | ❌ | ❌ | t1: `partial_dag` |
| 155 | `MOD_3T_RA02_replaceThenAdd_eco` | `replace` | ❌ | ❌ | t1: `partial_dag` |
| 156 | `MOD_3T_RA03_replaceThenAdd_sal` | `replace` | ❌ | ✅ | t1: `partial_dag` |
| 157 | `MOD_3T_SA01_switchThenAdd_lis_to_sal` | `switch_species` | ✅ | ✅ |  |
| 158 | `MOD_3T_SA02_switchThenAdd_eco_to_lis` | `switch_species` | ✅ | ✅ |  |
| 159 | `MOD_3T_SA03_switchThenAdd_sal_to_eco` | `switch_species` | ✅ | ❌ | t2: `missing_param` |

## Failure detail (one section per failing turn)

### `MOD_M01_E02_add_mlst_t1` — `file_not_found`
**Conversation:** `MOD_M01_E02_add_mlst` (add) — turn 1
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.LIS.6.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_M04_A04_add_mlst_parallel_t1` — `missing_param`
**Conversation:** `MOD_M04_A04_add_mlst_parallel` (add) — turn 1
**Prompt:** cgMLST allelic profile for Listeria monocytogenes from a pre-existing assembly.

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

include { getAssembly; getSpecies } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        assembly
        
        species
        
        schema
        
    
    main:
        assembly.cross(species) { extractKey(it) }.cross(schema) { extractKey(it) }.multiMap {
            assembly: it[0][0]
            species: it[0][1]
            schema: it[1]
        }.set { cgmlst_input }

        step_4TY_cgMLST__chewbbaca(cgmlst_input.assembly, cgmlst_input.species, cgmlst_input.schema)
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getAssembly(), getSpecies(), getSchema())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: species
```

### `MOD_M04_A04_add_mlst_parallel_t2` — `file_not_found`
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

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
        genus_species
        
        schema
        
    
    main:
        chewbbaca_result = chewbbaca(assembly, genus_species, schema)
        hashing(chewbbaca_result.alleles)
        chewbbaca_check(chewbbaca_result.stats).check
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
    step_4TY_MLST__mlst(getInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.LIS.2.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_M05_E07_add_prokka_t2` — `partial_dag`
**Conversation:** `MOD_M05_E07_add_prokka` (add) — turn 2
**Prompt:** Also annotate the assembly with Prokka.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
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
Only 5/8 expected processes appeared in the DAG
```

### `MOD_M07_D03_replace_trimmomatic_with_fastp_t1` — `silent_no_op`
**Conversation:** `MOD_M07_D03_replace_trimmomatic_with_fastp` (replace) — turn 1
**Prompt:** Pipeline: trim with Trimmomatic, assemble with SPAdes. Illumina paired-end.

**Steps (LLM):** `step_1PP_filtering__bowtie, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    trimmed   = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_filtering__bowtie } from '../steps/step_1PP_filtering__bowtie'

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

### `MOD_M07_D03_replace_trimmomatic_with_fastp_t2` — `silent_no_op`
**Conversation:** `MOD_M07_D03_replace_trimmomatic_with_fastp` (replace) — turn 2
**Prompt:** Replace Trimmomatic with fastp.

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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_filtering__bowtie } from '../steps/step_1PP_filtering__bowtie'

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

### `MOD_M09_E07_replace_abricate_with_prokka_t1` — `silent_no_op`
**Conversation:** `MOD_M09_E07_replace_abricate_with_prokka` (replace) — turn 1
**Prompt:** Resistance gene detection with ABRicate on Escherichia coli from Illumina paired FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4AN_AMR__abricate`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.cross(getReference('fa')) { extractKey(it) }.multiMap {
        reads: it[0]
        refs: it[1][1..3]
    }.set { sync }

    consensus = step_2AS_mapping__bowtie(sync.reads, sync.refs).consensus

    step_4AN_AMR__abricate(consensus)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_M09_E07_replace_abricate_with_prokka_t2` — `silent_no_op`
**Conversation:** `MOD_M09_E07_replace_abricate_with_prokka` (replace) — turn 2
**Prompt:** Switch from ABRicate to Prokka annotation.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4AN_genes__prokka`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.cross(getReference('fa')) { extractKey(it) }.multiMap {
        reads: it[0]
        refs: it[1][1..3]
    }.set { input }

    consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus

    step_4AN_genes__prokka(consensus.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.LIS.6.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_M15_A04_switch_species_to_ecoli_t1` — `missing_param`
**Conversation:** `MOD_M15_A04_switch_species_to_ecoli` (switch_species) — turn 1
**Prompt:** cgMLST allelic profile for Listeria monocytogenes from a pre-existing assembly.

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

include { getAssembly; getSpecies } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getAssembly(), getSpecies(), getSchema())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: species
```

### `MOD_M15_A04_switch_species_to_ecoli_t2` — `missing_param`
**Conversation:** `MOD_M15_A04_switch_species_to_ecoli` (switch_species) — turn 2
**Prompt:** Same thing but for Escherichia coli.

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_M16_E07_switch_species_to_salmonella_t1` — `missing_param`
**Conversation:** `MOD_M16_E07_switch_species_to_salmonella` (switch_species) — turn 1
**Prompt:** Resistance gene detection with ABRicate on Escherichia coli from Illumina paired FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_3TX_species__kmerfinder`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads)

        assembly = step_2AS_denovo__spades(trimmed.trimmed)

        step_4AN_AMR__abricate(assembly.assembled)

        step_3TX_species__kmerfinder(assembly.assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_M16_E07_switch_species_to_salmonella_t2` — `no_code`
**Conversation:** `MOD_M16_E07_switch_species_to_salmonella` (switch_species) — turn 2
**Prompt:** Switch to Salmonella enterica.

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

### `MOD_M17_D05_switch_species_to_ecoli_t1` — `partial_dag`
**Conversation:** `MOD_M17_D05_switch_species_to_ecoli` (switch_species) — turn 1
**Prompt:** Trim and de novo assembly (fastp + SPAdes) for a paired-end Illumina Campylobacter sample.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
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
Only 5/6 expected processes appeared in the DAG
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_filtering__bowtie } from '../steps/step_1PP_filtering__bowtie'

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
            reads: it[0] // riscd, reads
            refs:  it[1][1..3] // riscd, code, path
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

### `MOD_K02_add_mlst_to_chewbbaca_sal_spades_t1` — `file_not_found`
**Conversation:** `MOD_K02_add_mlst_to_chewbbaca_sal_spades` (add) — turn 1
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.SAL.200.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K04_add_abricate_to_chewbbaca_lis_spades_t1` — `missing_param`
**Conversation:** `MOD_K04_add_abricate_to_chewbbaca_lis_spades` (add) — turn 1
**Prompt:** chewbbaca on Listeria monocytogenes from paired Illumina FASTQ (fastp + spades).

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

include { getSingleInput; getVCFs; optionalOrDefault; param } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembly = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_cgMLST__chewbbaca(assembly, 'bacteria', 'bacteria')

    multi_clustering__reportree(getVCFs(), param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
}
```
**Error excerpt:**
```
ERROR ~ missing required param: multi_clustering__reportree__summary_columns
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.SAL.201.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K09_add_chewbbaca_to_mlst_eco_spades_t2` — `silent_no_op`
**Conversation:** `MOD_K09_add_chewbbaca_to_mlst_eco_spades` (add) — turn 2
**Prompt:** Now also run chewbbaca in parallel on the same assembly.

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembled = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        trimmed
        
        assembled
        
    
}

workflow wf_typing {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        step_4TY_MLST__mlst(assembly)

        step_4TY_cgMLST__chewbbaca(assembly, genus_species, '')
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed, assembled = wf_trim_assemble(getSingleInput())

    wf_typing(assembled, params.genus_species)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_K12_add_abricate_to_mlst_sal_spades_t2` — `partial_dag`
**Conversation:** `MOD_K12_add_abricate_to_mlst_sal_spades` (add) — turn 2
**Prompt:** Now also run abricate in parallel on the same assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_MLST__mlst(assembled)
}
```
**Error excerpt:**
```
Only 7/8 expected processes appeared in the DAG
```

### `MOD_K28_add_prokka_to_staramr_cam_spades_t2` — `arity_error`
**Conversation:** `MOD_K28_add_prokka_to_staramr_cam_spades` (add) — turn 2
**Prompt:** Now also run prokka in parallel on the same assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__staramr(assembled, param('genus_species'))
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        raw_reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(raw_reads)

        assembly = step_2AS_denovo__spades(trimmed.trimmed)

        step_4AN_AMR__staramr(assembly.assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `module_surveillance:step_4AN_AMR__staramr` declares 2 input channels but 1 were given
```

### `MOD_K38_add_prokka_to_mlst_eco_spades_t2` — `partial_dag`
**Conversation:** `MOD_K38_add_prokka_to_mlst_eco_spades` (add) — turn 2
**Prompt:** Now also run prokka in parallel on the same assembly.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_1PP_trimming__trimmomatic`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        trimmed
        
    
    main:
        trimmedReads = trimmed

        spades_out = step_2AS_denovo__spades(trimmedReads)

        step_4TY_MLST__mlst(spades_out.assembled)
    
    emit:
        
        assembly = spades_out.assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__trimmomatic(getSingleInput())

    module_surveillance(trimmed)
}
```
**Error excerpt:**
```
Only 7/8 expected processes appeared in the DAG
```

### `MOD_R02_replace_asm_spades_to_shovill_sal_t1` — `partial_dag`
**Conversation:** `MOD_R02_replace_asm_spades_to_shovill_sal` (replace) — turn 1
**Prompt:** Trim + assemble Salmonella enterica from paired Illumina FASTQ using fastp + spades.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
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
Only 5/6 expected processes appeared in the DAG
```

### `MOD_R02_replace_asm_spades_to_shovill_sal_t2` — `partial_dag`
**Conversation:** `MOD_R02_replace_asm_spades_to_shovill_sal` (replace) — turn 2
**Prompt:** Replace spades with shovill.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__shovill`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
        .set{ denovoInput }

        assembled = step_2AS_denovo__shovill(denovoInput)
    
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
Only 5/6 expected processes appeared in the DAG
```

### `MOD_R04_replace_asm_spades_to_shovill_cam_t1` — `partial_dag`
**Conversation:** `MOD_R04_replace_asm_spades_to_shovill_cam` (replace) — turn 1
**Prompt:** Trim + assemble Campylobacter jejuni from paired Illumina FASTQ using fastp + spades.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
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
Only 5/6 expected processes appeared in the DAG
```

### `MOD_R04_replace_asm_spades_to_shovill_cam_t2` — `partial_dag`
**Conversation:** `MOD_R04_replace_asm_spades_to_shovill_cam` (replace) — turn 2
**Prompt:** Replace spades with shovill.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__shovill`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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

        shovill_out = step_2AS_denovo__shovill(denovoInput)
    
    emit:
        
        assembled = shovill_out.assembly
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_denovo(getSingleInput(), getHost())
}
```
**Error excerpt:**
```
Only 5/6 expected processes appeared in the DAG
```

### `MOD_R05_replace_asm_spades_to_unicycler_lis_t1` — `silent_no_op`
**Conversation:** `MOD_R05_replace_asm_spades_to_unicycler_lis` (replace) — turn 1
**Prompt:** Trim + assemble Listeria monocytogenes from paired Illumina FASTQ using fastp + spades.

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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_filtering__bowtie } from '../steps/step_1PP_filtering__bowtie'

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

### `MOD_R06_replace_asm_spades_to_unicycler_sal_t1` — `partial_dag`
**Conversation:** `MOD_R06_replace_asm_spades_to_unicycler_sal` (replace) — turn 1
**Prompt:** Trim + assemble Salmonella enterica from paired Illumina FASTQ using fastp + spades.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
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
Only 5/6 expected processes appeared in the DAG
```

### `MOD_RT06_replace_trim_trimmomatic_to_fastp_sal_t1` — `silent_no_op`
**Conversation:** `MOD_RT06_replace_trim_trimmomatic_to_fastp_sal` (replace) — turn 1
**Prompt:** Trim + assemble Salmonella enterica from paired Illumina FASTQ using trimmomatic + SPAdes.

**Steps (LLM):** `step_1PP_filtering__bowtie, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    trimmed   = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_filtering__bowtie } from '../steps/step_1PP_filtering__bowtie'

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

### `MOD_RTY01_replace_typing_mlst_to_chewbbaca_lis_t2` — `file_not_found`
**Conversation:** `MOD_RTY01_replace_typing_mlst_to_chewbbaca_lis` (replace) — turn 2
**Prompt:** Switch the downstream step from mlst to chewbbaca.

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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_assemble_cgmlst {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembled = step_2AS_denovo__spades(trimmed).assembled

        step_4TY_cgMLST__chewbbaca(assembled, params.genus_species, params.schema)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_assemble_cgmlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.LIS.216.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_RTY02_replace_typing_mlst_to_chewbbaca_sal_t2` — `file_not_found`
**Conversation:** `MOD_RTY02_replace_typing_mlst_to_chewbbaca_sal` (replace) — turn 2
**Prompt:** Switch the downstream step from mlst to chewbbaca.

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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.SAL.214.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_RM06_replace_mono_abricate_to_prokka_eco_t1` — `missing_param`
**Conversation:** `MOD_RM06_replace_mono_abricate_to_prokka_eco` (replace) — turn 1
**Prompt:** Run abricate on a pre-existing Escherichia coli assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_4AN_AMR__abricate`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    step_4AN_AMR__abricate(getInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_RM06_replace_mono_abricate_to_prokka_eco_t2` — `missing_param`
**Conversation:** `MOD_RM06_replace_mono_abricate_to_prokka_eco` (replace) — turn 2
**Prompt:** Use prokka on that same assembly instead.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_D01_drop_chewbbaca_keep_mlst_lis_t1` — `partial_dag`
**Conversation:** `MOD_D01_drop_chewbbaca_keep_mlst_lis` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_cgMLST__chewbbaca, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.cross(getReference('fa')) { extractKey(it) }.multiMap {
        reads: it[0]
        refs:  it[1][1..3]
    }.set { input }

    consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus

    step_4TY_cgMLST__chewbbaca(consensus, 'listeria_monocytogenes', null)

    step_4TY_MLST__mlst(consensus)
}
```
**Error excerpt:**
```
Only 3/10 expected processes appeared in the DAG
```

### `MOD_D01_drop_chewbbaca_keep_mlst_lis_t2` — `silent_no_op`
**Conversation:** `MOD_D01_drop_chewbbaca_keep_mlst_lis` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.cross(getReference('fa')) { extractKey(it) }.multiMap {
        reads: it[0]
        refs: it[1][1..3]
    }.set { sync }

    consensus = step_2AS_mapping__bowtie(sync.reads, sync.refs).consensus

    step_4TY_MLST__mlst(consensus)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D02_drop_chewbbaca_keep_mlst_sal_t1` — `silent_no_op`
**Conversation:** `MOD_D02_drop_chewbbaca_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate, step_4AN_AMR__staramr, step_4AN_genes__prokka`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput; param } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_map {
    
    take:
        
        rawreads
        
        reference
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        trimmed.cross(reference) { extractKey(it) }
            .multiMap {
                reads: it[0]
                refs: it[1][1..3]
            }.set { input }

        consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus
    
    emit:
        
        consensus
        
    
}

workflow wf_mlst_and_cgmlst {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        step_4TY_MLST__mlst(assembly)
        step_4TY_cgMLST__chewbbaca(assembly, genus_species, '')
    
}

workflow wf_amr {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        step_4AN_AMR__abricate(assembly)
        step_4AN_AMR__staramr(assembly, genus_species)
    
}

workflow wf_prokka {
    
    take:
        
        assembly
        
    
    main:
        assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] }.set { prokkaIn }
        step_4AN_genes__prokka(prokkaIn)
    
}

// --- ENTRYPOINT ---
workflow {
    consensus = wf_trim_and_map(getSingleInput(), getReference('fa'))
    wf_mlst_and_cgmlst(consensus, param('genus_species'))
    wf_amr(consensus, param('genus_species'))
    wf_prokka(consensus)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D02_drop_chewbbaca_keep_mlst_sal_t2` — `file_not_found`
**Conversation:** `MOD_D02_drop_chewbbaca_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst, step_4AN_AMR__abricate, step_4AN_AMR__staramr, step_4AN_genes__prokka`
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

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_map {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        trimmed.cross(reference) { extractKey(it) }.multiMap {
            reads: it[0]
            refs:  it[1][1..3]
        }.set { input }

        consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus
    
    emit:
        
        consensus
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_and_map(getSingleInput()).set { mapping_out }

    step_4TY_MLST__mlst(mapping_out.consensus)
    step_4AN_AMR__abricate(mapping_out.consensus)
    step_4AN_AMR__staramr(mapping_out.consensus, 'bacteria')
    step_4AN_genes__prokka(mapping_out.consensus.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.SAL.221.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_D03_drop_chewbbaca_keep_mlst_eco_t1` — `partial_dag`
**Conversation:** `MOD_D03_drop_chewbbaca_keep_mlst_eco` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_cgMLST__chewbbaca, step_4TY_MLST__mlst`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getReference; getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.cross(getReference('fa')) { extractKey(it) }
        .multiMap {
            reads: it[0]
            refs:  it[1][1..3]
        }.set { input }

    consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus

    step_4TY_cgMLST__chewbbaca(consensus, param('genus_species'), optionalOrDefault('schema', ''))
    step_4TY_MLST__mlst(consensus)
}
```
**Error excerpt:**
```
Only 3/10 expected processes appeared in the DAG
```

### `MOD_D03_drop_chewbbaca_keep_mlst_eco_t2` — `silent_no_op`
**Conversation:** `MOD_D03_drop_chewbbaca_keep_mlst_eco` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getAssembly; getReference; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    step_2AS_mapping__bowtie(trimmed, getReference('fa'))

    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D04_drop_mlst_keep_chewbbaca_lis_t2` — `missing_param`
**Conversation:** `MOD_D04_drop_mlst_keep_chewbbaca_lis` (drop) — turn 2
**Prompt:** Drop mlst, keep only chewbbaca.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp, step_3TX_species__kmerfinder`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_assembly_and_cgmlst {
    
    take:
        
        trimmed
        
    
    main:
        spades_out = step_2AS_denovo__spades(trimmed)

        assemblyAndSpecies = spades_out.assembled.cross(assigned_species) { extractKey(it) }.multiMap {
          assembly: it[0]
          species: it[1][1]
        }

        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, '')
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assigned_species = step_3TX_species__kmerfinder(trimmed).assigned_species

    wf_assembly_and_cgmlst(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D05_drop_mlst_keep_chewbbaca_sal_t1` — `partial_dag`
**Conversation:** `MOD_D05_drop_mlst_keep_chewbbaca_sal` (drop) — turn 1
**Prompt:** Run both mlst and chewbbaca on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    mapped = step_2AS_mapping__bowtie(trimmed, getReference('fa')).consensus

    step_4TY_MLST__mlst(mapped)

    step_4TY_cgMLST__chewbbaca(mapped, params.genus_species, params.schema)
}
```
**Error excerpt:**
```
Only 3/10 expected processes appeared in the DAG
```

### `MOD_D05_drop_mlst_keep_chewbbaca_sal_t2` — `partial_dag`
**Conversation:** `MOD_D05_drop_mlst_keep_chewbbaca_sal` (drop) — turn 2
**Prompt:** Drop mlst, keep only chewbbaca.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_cgMLST__chewbbaca`
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

include { getReference; getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.cross(getReference('fa')) { extractKey(it) }.multiMap {
        reads: it[0]
        refs:  it[1][1..3]
    }.set { input }

    consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus

    step_4TY_cgMLST__chewbbaca(consensus, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
Only 3/9 expected processes appeared in the DAG
```

### `MOD_D06_drop_abricate_keep_mlst_lis_t1` — `silent_no_op`
**Conversation:** `MOD_D06_drop_abricate_keep_mlst_lis` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4TY_MLST__mlst`
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

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.cross(getReference('fa')) { extractKey(it) }
        .multiMap {
            reads: it[0]
            refs:  it[1][1..3]
        }.set { input }

    consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus

    step_4AN_genes__prokka(consensus.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

    step_4AN_AMR__abricate(consensus)

    step_4TY_MLST__mlst(consensus)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D06_drop_abricate_keep_mlst_lis_t2` — `silent_no_op`
**Conversation:** `MOD_D06_drop_abricate_keep_mlst_lis` (drop) — turn 2
**Prompt:** Drop abricate, keep only mlst.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4AN_genes__prokka, step_4TY_MLST__mlst`
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

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.cross(getReference('fa')) { extractKey(it) }.multiMap {
        reads: it[0]
        refs: it[1][1..3]
    }.set { input }

    consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus

    step_4AN_genes__prokka(consensus.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

    step_4TY_MLST__mlst(consensus)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D07_drop_abricate_keep_mlst_eco_t1` — `partial_dag`
**Conversation:** `MOD_D07_drop_abricate_keep_mlst_eco` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    bowtie_out = step_2AS_mapping__bowtie(trimmed, getReference('fa'))

    step_4AN_AMR__abricate(bowtie_out.consensus)

    step_4TY_MLST__mlst(bowtie_out.assembly)
}
```
**Error excerpt:**
```
Only 3/8 expected processes appeared in the DAG
```

### `MOD_D07_drop_abricate_keep_mlst_eco_t2` — `partial_dag`
**Conversation:** `MOD_D07_drop_abricate_keep_mlst_eco` (drop) — turn 2
**Prompt:** Drop abricate, keep only mlst.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.cross(getReference('fa')) { extractKey(it) }.multiMap {
        reads: it[0]
        refs:  it[1][1..3]
    }.set { input }

    consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus

    step_4TY_MLST__mlst(consensus)
}
```
**Error excerpt:**
```
Only 3/7 expected processes appeared in the DAG
```

### `MOD_D08_drop_abricate_keep_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_D08_drop_abricate_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4TY_MLST__mlst`
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

include { getEmpty } from '../functions/common.nf'

include { getSingleInput; getVCFs; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        input
        
    
    main:
        multi_clustering__reportree(input, param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembly = step_2AS_denovo__spades(trimmed).assembled

    step_4AN_genes__prokka(assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

    step_4AN_AMR__abricate(assembly)

    step_4TY_MLST__mlst(assembly)

    module_surveillance(getVCFs())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: multi_clustering__reportree__summary_columns
```

### `MOD_D09_drop_prokka_keep_mlst_sal_t1` — `silent_no_op`
**Conversation:** `MOD_D09_drop_prokka_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both prokka and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_mapping__bowtie, step_4AN_genes__prokka, step_4TY_MLST__mlst`
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

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getEmpty } from '../functions/common.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    reads = getSingleInput()
    reference = getReference('fa')

    mapped = step_2AS_mapping__bowtie(reads, reference)
    step_4AN_genes__prokka(mapped.consensus.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    step_4TY_MLST__mlst(mapped.consensus.map { it[1] })
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D09_drop_prokka_keep_mlst_sal_t2` — `no_code`
**Conversation:** `MOD_D09_drop_prokka_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop prokka, keep only mlst.

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

### `MOD_D10_drop_prokka_keep_abricate_lis_t1` — `silent_no_op`
**Conversation:** `MOD_D10_drop_prokka_keep_abricate_lis` (drop) — turn 1
**Prompt:** Run both prokka and abricate on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4AN_genes__prokka, step_4AN_AMR__abricate`
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

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_map {
    
    take:
        
        rawreads
        
        reference
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        trimmed.cross(reference) { extractKey(it) }.multiMap {
            reads: it[0]
            refs:  it[1][1..3]
        }.set { input }

        consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus
    
    emit:
        
        consensus
        
    
}

workflow wf_annotate_and_amr {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
        step_4AN_AMR__abricate(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    consensus = wf_trim_and_map(getSingleInput(), getReference('fa'))
    wf_annotate_and_amr(consensus)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_D10_drop_prokka_keep_abricate_lis_t2` — `partial_dag`
**Conversation:** `MOD_D10_drop_prokka_keep_abricate_lis` (drop) — turn 2
**Prompt:** Drop prokka, keep only abricate.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4AN_AMR__abricate`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    mapped = step_2AS_mapping__bowtie(trimmed, getReference('fa')).consensus

    step_4AN_AMR__abricate(mapped)
}
```
**Error excerpt:**
```
Only 3/7 expected processes appeared in the DAG
```

### `MOD_D11_drop_flaA_keep_mlst_cam_t1` — `partial_dag`
**Conversation:** `MOD_D11_drop_flaA_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both flaA and mlst on Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
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
Only 5/8 expected processes appeared in the DAG
```

### `MOD_D11_drop_flaA_keep_mlst_cam_t2` — `partial_dag`
**Conversation:** `MOD_D11_drop_flaA_keep_mlst_cam` (drop) — turn 2
**Prompt:** Drop flaA, keep only mlst.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
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
Only 5/7 expected processes appeared in the DAG
```

### `MOD_D12_drop_staramr_keep_mlst_cam_t1` — `missing_param`
**Conversation:** `MOD_D12_drop_staramr_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both staramr and mlst on Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_3TX_species__kmerfinder, step_4AN_AMR__staramr, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    mapped = step_2AS_mapping__bowtie(trimmed, getReference('fa')).consensus

    species = step_3TX_species__kmerfinder(mapped).assigned_species

    step_4AN_AMR__staramr(mapped, species[1])

    step_4TY_MLST__mlst(mapped)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D12_drop_staramr_keep_mlst_cam_t2` — `missing_param`
**Conversation:** `MOD_D12_drop_staramr_keep_mlst_cam` (drop) — turn 2
**Prompt:** Drop staramr, keep only mlst.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_3TX_species__kmerfinder, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    consensus = step_2AS_mapping__bowtie(trimmed, getReference('fa')).consensus

    assigned_species = step_3TX_species__kmerfinder(consensus).assigned_species

    step_4TY_MLST__mlst(assigned_species)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_DA02_drop_assembly_eco_t1` — `partial_dag`
**Conversation:** `MOD_DA02_drop_assembly_eco` (drop) — turn 1
**Prompt:** Trim + assemble Escherichia coli from paired Illumina FASTQ (fastp + SPAdes).

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
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
Only 5/6 expected processes appeared in the DAG
```

### `MOD_DA02_drop_assembly_eco_t2` — `missing_param`
**Conversation:** `MOD_DA02_drop_assembly_eco` (drop) — turn 2
**Prompt:** Drop the assembly step and just trim the reads.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
workflow {
    step_1PP_trimming__fastp(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { module_reads_processing } from '../modules/module_reads_processing'

include { getInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    module_reads_processing(getInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_class__kraken__db_kraken
```

### `MOD_DM02_drop_mono_chewbbaca_keep_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_DM02_drop_mono_chewbbaca_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_DM02_drop_mono_chewbbaca_keep_mlst_sal_t2` — `silent_no_op`
**Conversation:** `MOD_DM02_drop_mono_chewbbaca_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

**Steps (LLM):** `step_2AS_mapping__bowtie, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA`
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

include { getAssembly; getReference; getTrimmedReads; param } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_2AS_mapping__bowtie(getTrimmedReads(true), getReference('fa'))
    step_4AN_genes__prokka(getAssembly().map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    step_4AN_AMR__abricate(getAssembly())
    step_4AN_AMR__staramr(getAssembly(), param('genus_species'))
    step_4TY_MLST__mlst(getAssembly())
    step_4TY_flaA__flaA(getAssembly(), param('genus_species'))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco_t1` — `missing_param`
**Conversation:** `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco` (drop) — turn 1
**Prompt:** Run both mlst and chewbbaca on a pre-existing Escherichia coli assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    asm = getInput()
    step_4TY_MLST__mlst(asm)
    step_4TY_cgMLST__chewbbaca(asm, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_DM11_drop_mono_abricate_keep_prokka_eco_t1` — `missing_param`
**Conversation:** `MOD_DM11_drop_mono_abricate_keep_prokka_eco` (drop) — turn 1
**Prompt:** Run both abricate and prokka on a pre-existing Escherichia coli assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_DM11_drop_mono_abricate_keep_prokka_eco_t2` — `missing_param`
**Conversation:** `MOD_DM11_drop_mono_abricate_keep_prokka_eco` (drop) — turn 2
**Prompt:** Drop abricate, keep only prokka.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_DM12_drop_mono_prokka_keep_abricate_lis_t1` — `arity_error`
**Conversation:** `MOD_DM12_drop_mono_prokka_keep_abricate_lis` (drop) — turn 1
**Prompt:** Run both prokka and abricate on a pre-existing Listeria monocytogenes assembly.

**Steps (LLM):** `step_4AN_genes__prokka, step_4AN_AMR__abricate`
**Steps (GT):**  `step_4AN_AMR__abricate, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    asm = getInput()
    step_4AN_genes__prokka(asm)
    step_4AN_AMR__abricate(asm)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    assembly = getSingleInput()

    prokka_out = step_4AN_genes__prokka(assembly.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] })

    step_4AN_AMR__abricate(prokka_out)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_4AN_AMR__abricate` declares 1 input channels but 0 were given
```

### `MOD_DM13_drop_mono_prokka_keep_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_DM13_drop_mono_prokka_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both prokka and mlst on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_DM13_drop_mono_prokka_keep_mlst_sal_t2` — `missing_param`
**Conversation:** `MOD_DM13_drop_mono_prokka_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop prokka, keep only mlst.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4TY_MLST__mlst`
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

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { extractKey } from '../functions/common.nf'

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

        assembly.cross(assigned_species) { extractKey(it) }.multiMap {
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
    
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

### `MOD_DM14_drop_mono_abricate_keep_prokka_sal_t1` — `missing_param`
**Conversation:** `MOD_DM14_drop_mono_abricate_keep_prokka_sal` (drop) — turn 1
**Prompt:** Run both abricate and prokka on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_DM14_drop_mono_abricate_keep_prokka_sal_t2` — `silent_no_op`
**Conversation:** `MOD_DM14_drop_mono_abricate_keep_prokka_sal` (drop) — turn 2
**Prompt:** Drop abricate, keep only prokka.

**Steps (LLM):** `step_2AS_mapping__bowtie, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { getReference; getSingleInput; param } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    getSingleInput().cross(getReference('fa')) { extractKey(it) }.multiMap {
        reads: it[0]
        refs: it[1][1..3]
    }.set { input }
    step_2AS_mapping__bowtie(input.reads, input.refs)
    step_4AN_genes__prokka(input.reads.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    input.reads.cross(param('genus_species')) { extractKey(it) }.multiMap {
        assembly: it[0]
        species: it[1]
    }.set { assemblyAndSpecies }
    step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
    step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
    step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
    step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, '')
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_S01_cgmlst_retarget_lis_to_sal_t2` — `arity_error`
**Conversation:** `MOD_S01_cgmlst_retarget_lis_to_sal` (switch_species) — turn 2
**Prompt:** Apply the same pipeline to Salmonella enterica.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        trimmed
        
    
    main:
        spades_out = step_2AS_denovo__spades(trimmed)
        step_4TY_cgMLST__chewbbaca(spades_out.assembled)
    
    emit:
        
        assembly = spades_out.assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    module_surveillance(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `module_surveillance:step_4TY_cgMLST__chewbbaca` declares 3 input channels but 1 were given
```

### `MOD_S02_cgmlst_retarget_lis_to_eco_t1` — `file_not_found`
**Conversation:** `MOD_S02_cgmlst_retarget_lis_to_eco` (switch_species) — turn 1
**Prompt:** cgMLST pipeline for Listeria monocytogenes from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).

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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

def genusSpecies = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        assembled
        
    
}

workflow wf_cgmlst {
    
    take:
        
        assembled
        
    
    main:
        step_4TY_cgMLST__chewbbaca(assembled, genusSpecies, null)
    
}

// --- ENTRYPOINT ---
workflow {
    assembled = wf_trim_assemble(getSingleInput())
    wf_cgmlst(assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.LIS.233.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_cgMLST__chewbbaca(assembled, 'escherichia_coli', null)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.ECO.220.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_S04_cgmlst_retarget_sal_to_eco_t2` — `arity_error`
**Conversation:** `MOD_S04_cgmlst_retarget_sal_to_eco` (switch_species) — turn 2
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        trimmed
        
    
    main:
        trimmedReads = step_1PP_trimming__fastp(trimmed).trimmed

        assembled = step_2AS_denovo__spades(trimmedReads).assembled

        step_4TY_cgMLST__chewbbaca(assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `module_surveillance:step_4TY_cgMLST__chewbbaca` declares 3 input channels but 1 were given
```

### `MOD_S05_cgmlst_retarget_eco_to_lis_t1` — `file_not_found`
**Conversation:** `MOD_S05_cgmlst_retarget_eco_to_lis` (switch_species) — turn 1
**Prompt:** cgMLST pipeline for Escherichia coli from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).

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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.ECO.222.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_SM01_mlst_retarget_lis_to_cam_t1` — `silent_no_op`
**Conversation:** `MOD_SM01_mlst_retarget_lis_to_cam` (switch_species) — turn 1
**Prompt:** MLST pipeline for Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_map {
    
    take:
        
        rawreads
        
        reference
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        trimmed.cross(reference) { extractKey(it) }.multiMap {
            reads: it[0]
            refs:  it[1][1..3]
        }.set { sync }

        consensus = step_2AS_mapping__bowtie(sync.reads, sync.refs).consensus
    
    emit:
        
        consensus
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_and_map(getSingleInput(), getReference('fa'))
    step_4TY_MLST__mlst(wf_trim_and_map.out.consensus)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_SM01_mlst_retarget_lis_to_cam_t2` — `no_code`
**Conversation:** `MOD_SM01_mlst_retarget_lis_to_cam` (switch_species) — turn 2
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
no nextflow_code after max turns
```

### `MOD_SM02_mlst_retarget_sal_to_cam_t1` — `silent_no_op`
**Conversation:** `MOD_SM02_mlst_retarget_sal_to_cam` (switch_species) — turn 1
**Prompt:** MLST pipeline for Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst, step_4AN_AMR__abricate, step_4AN_AMR__staramr, step_4TY_cgMLST__chewbbaca, step_4TY_flaA__flaA`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getReference; getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    mapped = step_2AS_mapping__bowtie(trimmed, getReference('fa')).consensus

    step_4TY_MLST__mlst(mapped)

    step_4AN_AMR__abricate(mapped)

    step_4AN_AMR__staramr(mapped, param('genus_species'))

    step_4TY_cgMLST__chewbbaca(mapped, param('genus_species'), optionalOrDefault('schema', ''))

    step_4TY_flaA__flaA(mapped, param('genus_species'))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_SM03_mlst_retarget_eco_to_cam_t1` — `silent_no_op`
**Conversation:** `MOD_SM03_mlst_retarget_eco_to_cam` (switch_species) — turn 1
**Prompt:** MLST pipeline for Escherichia coli from paired Illumina FASTQ.

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

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    getSingleInput().cross(getReference('fa')) { extractKey(it) }
      .multiMap {
          reads: it[0]
          refs:  it[1][1..3]
      }.set { input }
    step_2AS_mapping__bowtie(input.reads, input.refs)
    step_4TY_MLST__mlst(step_2AS_mapping__bowtie.out.consensus)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_SM03_mlst_retarget_eco_to_cam_t2` — `silent_no_op`
**Conversation:** `MOD_SM03_mlst_retarget_eco_to_cam` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Campylobacter jejuni.

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

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        reads
        
        reference
        
    
    main:
        reads.cross(reference) { extractKey(it) }.multiMap {
            reads: it[0]
            refs:  it[1][1..3]
        }.set { sync }
        step_2AS_mapping__bowtie(sync.reads, sync.refs)
        step_4TY_MLST__mlst(sync.reads)
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getSingleInput(), getReference('fa'))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_SM04_mlst_retarget_cam_to_lis_t1` — `partial_dag`
**Conversation:** `MOD_SM04_mlst_retarget_cam_to_lis` (switch_species) — turn 1
**Prompt:** MLST pipeline for Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4AN_AMR__staramr, step_4TY_cgMLST__chewbbaca, step_4TY_flaA__flaA`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getKingdom; getReference; getReferenceOptional; getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    reference = getReference('fa')

    trimmed.cross(reference) { extractKey(it) }.multiMap {
        reads: it[0]
        refs:  it[1][1..3]
    }.set { input }

    consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus

    step_4TY_MLST__mlst(consensus)

    consensus.cross(getKingdom()) { extractKey(it) }.cross(getReferenceOptional('gb')) { extractKey(it) }.map { it.flatten() }.map {
        [ it[0], it[1], it[3], it[5], it[6], it[7] ]
    }.set { prokka_input }

    step_4AN_genes__prokka(prokka_input)

    step_4AN_AMR__abricate(consensus)

    step_4AN_AMR__staramr(consensus, param('genus_species'))

    consensus.cross(param('genus_species')) { extractKey(it) }.cross(optionalOrDefault('schema', '')) { extractKey(it) }.map { it.flatten() }.set { chewbbaca_input }

    step_4TY_cgMLST__chewbbaca(chewbbaca_input)

    step_4TY_flaA__flaA(consensus, param('genus_species'))
}
```
**Error excerpt:**
```
Only 3/7 expected processes appeared in the DAG
```

### `MOD_SM04_mlst_retarget_cam_to_lis_t2` — `silent_no_op`
**Conversation:** `MOD_SM04_mlst_retarget_cam_to_lis` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Listeria monocytogenes.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4AN_AMR__staramr, step_4TY_cgMLST__chewbbaca, step_4TY_flaA__flaA`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getReference; getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    reference = getReference('fa')

    trimmed.cross(reference) { extractKey(it) }.multiMap {
        reads: it[0]
        refs:  it[1][1..3]
    }.set { input }

    consensus = step_2AS_mapping__bowtie(input.reads, input.refs).consensus

    step_4TY_MLST__mlst(consensus)

    consensus.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] }.set { prokkaIn }
    step_4AN_genes__prokka(prokkaIn)

    step_4AN_AMR__abricate(consensus)

    step_4AN_AMR__staramr(consensus, param('genus_species'))

    step_4TY_cgMLST__chewbbaca(consensus, param('genus_species'), optionalOrDefault('schema', ''))

    step_4TY_flaA__flaA(consensus, param('genus_species'))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_SM05_mlst_retarget_cam_to_sal_t1` — `silent_no_op`
**Conversation:** `MOD_SM05_mlst_retarget_cam_to_sal` (switch_species) — turn 1
**Prompt:** MLST pipeline for Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.multiMap {
        trimmed: it
        reference: getReference('fa')
    }.set { trAndRef }

    mapped = step_2AS_mapping__bowtie(trAndRef.trimmed, trAndRef.reference)

    step_4TY_MLST__mlst(mapped.consensus
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_SM05_mlst_retarget_cam_to_sal_t2` — `file_not_found`
**Conversation:** `MOD_SM05_mlst_retarget_cam_to_sal` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Salmonella enterica.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(reads).trimmed

        mapped = step_2AS_mapping__bowtie(trimmed, reference)

        step_4TY_MLST__mlst(mapped.consensus)
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.SAL.235.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_SM06_mlst_retarget_cam_to_eco_t1` — `silent_no_op`
**Conversation:** `MOD_SM06_mlst_retarget_cam_to_eco` (switch_species) — turn 1
**Prompt:** MLST pipeline for Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_4TY_MLST__mlst, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4AN_AMR__staramr, step_4TY_cgMLST__chewbbaca, step_4TY_flaA__flaA`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getEmpty } from '../functions/common.nf'

include { getReference; getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    reference = getReference('fa')

    consensus = step_2AS_mapping__bowtie(trimmed, reference).consensus

    step_4TY_MLST__mlst(consensus)

    step_4AN_genes__prokka(consensus.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

    step_4AN_AMR__abricate(consensus)

    step_4AN_AMR__staramr(consensus, param('genus_species'))

    step_4TY_cgMLST__chewbbaca(consensus, param('genus_species'), optionalOrDefault('schema', ''))

    step_4TY_flaA__flaA(consensus, param('genus_species'))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_SM06_mlst_retarget_cam_to_eco_t2` — `missing_param`
**Conversation:** `MOD_SM06_mlst_retarget_cam_to_eco` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Escherichia coli.

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_SMA01_mlst_mono_retarget_lis_to_sal_t1` — `missing_param`
**Conversation:** `MOD_SMA01_mlst_mono_retarget_lis_to_sal` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Listeria monocytogenes assembly.

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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getEmpty } from '../functions/common.nf'

include { getAssembly; optionalOrDefault; param } from '../functions/parameters.nf'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        input
        
    
    main:
        multi_clustering__reportree(input, param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: multi_clustering__reportree__summary_columns
```

### `MOD_SMA01_mlst_mono_retarget_lis_to_sal_t2` — `missing_param`
**Conversation:** `MOD_SMA01_mlst_mono_retarget_lis_to_sal` (switch_species) — turn 2
**Prompt:** Same thing but for Salmonella enterica.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getEmpty } from '../functions/common.nf'

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    assembly = getSingleInput()

    // Step 1: Kmerfinder to identify the species of the assembly
    kmerfinder_out = step_3TX_species__kmerfinder(assembly)

    // Step 2: Abricate to identify AMR genes in the assembly
    step_4AN_AMR__abricate(assembly)

    // Step 3: Prokka to annotate the assembly
    step_4AN_genes__prokka(assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

    // Step 4: StarAMR to identify AMR genes in the assembly
    step_4AN_AMR__staramr(assembly, param('genus_species'))

    // Step 5: MLST to perform MLST on the assembly
    step_4TY_MLST__mlst(assembly)

    // Step 6: flaA to identify the flaA gene in the assembly
    step_4TY_flaA__flaA(assembly, param('genus_species'))

    // Step 7: ChewBBACA to perform cgMLST on the assembly
    step_4TY_cgMLST__chewbbaca(assembly, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_SMA03_mlst_mono_retarget_sal_to_lis_t1` — `missing_param`
**Conversation:** `MOD_SMA03_mlst_mono_retarget_sal_to_lis` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Salmonella enterica assembly.

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

include { getEmpty } from '../functions/common.nf'

include { getAssembly; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    main:
        multi_clustering__reportree(inputFn(), param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance()
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: multi_clustering__reportree__summary_columns
```

### `MOD_SMA03_mlst_mono_retarget_sal_to_lis_t2` — `missing_param`
**Conversation:** `MOD_SMA03_mlst_mono_retarget_sal_to_lis` (switch_species) — turn 2
**Prompt:** Same thing but for Listeria monocytogenes.

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

include { getEmpty } from '../functions/common.nf'

include { getAssembly; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    main:
        multi_clustering__reportree(inputFn(), param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance()
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: multi_clustering__reportree__summary_columns
```

### `MOD_SMA04_mlst_mono_retarget_sal_to_eco_t1` — `missing_param`
**Conversation:** `MOD_SMA04_mlst_mono_retarget_sal_to_eco` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_SMA04_mlst_mono_retarget_sal_to_eco_t2` — `missing_param`
**Conversation:** `MOD_SMA04_mlst_mono_retarget_sal_to_eco` (switch_species) — turn 2
**Prompt:** Same thing but for Escherichia coli.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_SMA05_mlst_mono_retarget_eco_to_lis_t1` — `missing_param`
**Conversation:** `MOD_SMA05_mlst_mono_retarget_eco_to_lis` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Escherichia coli assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_SMA05_mlst_mono_retarget_eco_to_lis_t2` — `missing_param`
**Conversation:** `MOD_SMA05_mlst_mono_retarget_eco_to_lis` (switch_species) — turn 2
**Prompt:** Same thing but for Listeria monocytogenes.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_SMA06_mlst_mono_retarget_eco_to_sal_t2` — `missing_param`
**Conversation:** `MOD_SMA06_mlst_mono_retarget_eco_to_sal` (switch_species) — turn 2
**Prompt:** Same thing but for Salmonella enterica.

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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getEmpty } from '../functions/common.nf'

include { getAssembly; optionalOrDefault; param } from '../functions/parameters.nf'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        assembly
        
    
    main:
        multi_clustering__reportree(inputFn(assembly), param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: multi_clustering__reportree__summary_columns
```

### `MOD_SMA08_mlst_mono_retarget_sal_to_cam_t1` — `missing_param`
**Conversation:** `MOD_SMA08_mlst_mono_retarget_sal_to_cam` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_SMA08_mlst_mono_retarget_sal_to_cam_t2` — `missing_param`
**Conversation:** `MOD_SMA08_mlst_mono_retarget_sal_to_cam` (switch_species) — turn 2
**Prompt:** Same thing but for Campylobacter jejuni.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `MOD_3T01_addAdd_lis_t3` — `file_not_found`
**Conversation:** `MOD_3T01_addAdd_lis` (add) — turn 3
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_MLST__mlst(assembled)

    step_4TY_cgMLST__chewbbaca(assembled, params.genus_species, params.schema)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.LIS.244.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_MLST__mlst(assembled)

    step_4TY_cgMLST__chewbbaca(assembled, params.genus_species, params.schema)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.ECO.231.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_AD01_addThenDrop_lis_t1` — `missing_param`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 1
**Prompt:** cgMLST profile for Listeria monocytogenes from paired Illumina FASTQ.

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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    assigned_species = step_3TX_species__kmerfinder(assembled).assigned_species

    step_4TY_cgMLST__chewbbaca(assembled, assigned_species[1], null)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD01_addThenDrop_lis_t2` — `missing_param`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 2
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    assigned_species = step_3TX_species__kmerfinder(assembled).assigned_species

    step_4TY_cgMLST__chewbbaca(assembled, assigned_species[1], null)

    step_4AN_AMR__abricate(assembled)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD01_addThenDrop_lis_t3` — `missing_param`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 3
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    assigned_species = step_3TX_species__kmerfinder(assembled).assigned_species
    step_4TY_cgMLST__chewbbaca(assembled, assigned_species[1], null)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    assigned_species = step_3TX_species__kmerfinder(assembled).assigned_species

    step_4TY_cgMLST__chewbbaca(assembled, assigned_species[1], null)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD02_addThenDrop_eco_t2` — `silent_no_op`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembled = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        trimmed
        
        assembled
        
    
}

workflow wf_species_cgmlst {
    
    take:
        
        assembled
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembled).assigned_species
        step_4TY_cgMLST__chewbbaca(assembled, assigned_species[1], null).alleles
    
    emit:
        
        assigned_species
        
    
}

workflow wf_amr {
    
    take:
        
        assembled
        
    
    main:
        step_4AN_AMR__abricate(assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    ch_rawreads = getSingleInput()

    ch_trimmed, ch_assembled = wf_trim_assemble(ch_rawreads)

    ch_assigned_species, ch_cgmlst_alleles = wf_species_cgmlst(ch_assembled)

    wf_amr(ch_assembled)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    assigned_species = step_3TX_species__kmerfinder(assembled).assigned_species

    step_4TY_cgMLST__chewbbaca(assembled, assigned_species[1], null)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD03_addThenDrop_sal_t1` — `missing_param`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 1
**Prompt:** cgMLST profile for Salmonella enterica from paired Illumina FASTQ.

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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    assigned_species = step_3TX_species__kmerfinder(assembled).assigned_species

    step_4TY_cgMLST__chewbbaca(assembled, assigned_species[1], null)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD03_addThenDrop_sal_t2` — `silent_no_op`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 2
**Prompt:** Also add ABRicate AMR screening in parallel.

**Steps (LLM):** `step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_assembly_and_species {
    
    take:
        
        trimmed
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmed).assembled
        assigned_species = step_3TX_species__kmerfinder(assembled).assigned_species
    
    emit:
        
        assembled
        
        assigned_species
        
    
}

workflow wf_cgmlst_and_amr {
    
    take:
        
        assembled
        
        assigned_species
        
    
    main:
        step_4TY_cgMLST__chewbbaca(assembled, assigned_species[1], '')
        step_4AN_AMR__abricate(assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled, assigned_species = wf_assembly_and_species(trimmed)
    wf_cgmlst_and_amr(assembled, assigned_species)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_3T_AD03_addThenDrop_sal_t3` — `missing_param`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 3
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    assigned_species = step_3TX_species__kmerfinder(assembled).assigned_species
    step_4TY_cgMLST__chewbbaca(assembled, assigned_species[1], null)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_RA01_replaceThenAdd_lis_t1` — `partial_dag`
**Conversation:** `MOD_3T_RA01_replaceThenAdd_lis` (replace) — turn 1
**Prompt:** Trim + assemble Listeria monocytogenes from paired Illumina FASTQ (fastp + SPAdes).

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
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
Only 5/6 expected processes appeared in the DAG
```

### `MOD_3T_RA01_replaceThenAdd_lis_t2` — `partial_dag`
**Conversation:** `MOD_3T_RA01_replaceThenAdd_lis` (replace) — turn 2
**Prompt:** Use Shovill instead of SPAdes.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__shovill`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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

        shovill_out = step_2AS_denovo__shovill(denovoInput)
    
    emit:
        
        assembled = shovill_out.assembly
        
        depleted
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_denovo(getSingleInput(), getHost())
}
```
**Error excerpt:**
```
Only 5/6 expected processes appeared in the DAG
```

### `MOD_3T_RA01_replaceThenAdd_lis_t3` — `file_not_found`
**Conversation:** `MOD_3T_RA01_replaceThenAdd_lis` (replace) — turn 3
**Prompt:** Now also run MLST on the assembly.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
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

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getHostUnkeyed; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    raw_reads = getSingleInput()
    host = getHostUnkeyed()

    depleted_reads = step_1PP_hostdepl__bowtie(raw_reads.combine(host))

    assembly = step_2AS_denovo__shovill(depleted_reads.depleted)

    step_4TY_MLST__mlst(assembly.assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_multi_turn/_shared_inputdir/2026/2026.LIS.246.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_RA02_replaceThenAdd_eco_t1` — `partial_dag`
**Conversation:** `MOD_3T_RA02_replaceThenAdd_eco` (replace) — turn 1
**Prompt:** Trim + assemble Escherichia coli from paired Illumina FASTQ (fastp + SPAdes).

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
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
Only 5/6 expected processes appeared in the DAG
```

### `MOD_3T_RA02_replaceThenAdd_eco_t2` — `partial_dag`
**Conversation:** `MOD_3T_RA02_replaceThenAdd_eco` (replace) — turn 2
**Prompt:** Use Shovill instead of SPAdes.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__shovill`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
        .set{ denovoInput }

        assembled = step_2AS_denovo__shovill(denovoInput)
    
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
Only 5/6 expected processes appeared in the DAG
```

### `MOD_3T_RA02_replaceThenAdd_eco_t3` — `missing_param`
**Conversation:** `MOD_3T_RA02_replaceThenAdd_eco` (replace) — turn 3
**Prompt:** Now also run MLST on the assembly.

**Steps (LLM):** `(none)`
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

### `MOD_3T_RA03_replaceThenAdd_sal_t1` — `partial_dag`
**Conversation:** `MOD_3T_RA03_replaceThenAdd_sal` (replace) — turn 1
**Prompt:** Trim + assemble Salmonella enterica from paired Illumina FASTQ (fastp + SPAdes).

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
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
Only 5/6 expected processes appeared in the DAG
```

### `MOD_3T_SA03_switchThenAdd_sal_to_eco_t2` — `missing_param`
**Conversation:** `MOD_3T_SA03_switchThenAdd_sal_to_eco` (switch_species) — turn 2
**Prompt:** Apply the same to Escherichia coli.

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

include { getSingleInput; getVCFs; optionalOrDefault; param } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        input
        
    
    main:
        multi_clustering__reportree(input, param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembly)
    module_surveillance(getVCFs())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: multi_clustering__reportree__summary_columns
```
