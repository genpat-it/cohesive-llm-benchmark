# LLM multi-turn evaluation — detailed report

Total conversations: **159**  ·  total turns: **319**  ·  per-turn pass: **122/319**  ·  conversations fully passing: **33/159**

## Pass rate by modification kind (per turn)

| kind | turns | pass |
|----|-----:|-----:|
| `add` | 101 | 51 |
| `replace` | 95 | 34 |
| `drop` | 63 | 11 |
| `switch_species` | 60 | 26 |

## Error category breakdown

| Category | Count |
|----|----:|
| `file_not_found` | 121 |
| `none` | 118 |
| `missing_param` | 32 |
| `no_code` | 19 |
| `silent_no_op` | 17 |
| `arity_error` | 8 |
| `partial_dag` | 4 |

## Per-conversation outcome

| # | conv_id | kind | t1 | t2 | error category (failing turn) |
|---|---------|------|----|----|------------------------------|
| 1 | `MOD_M01_E02_add_mlst` | `add` | ✅ | ✅ |  |
| 2 | `MOD_M02_D01_add_chewbbaca` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 3 | `MOD_M03_B01_add_trimming` | `add` | ❌ | ❌ | t1: `missing_param` |
| 4 | `MOD_M04_A04_add_mlst_parallel` | `add` | ❌ | ❌ | t1: `silent_no_op` |
| 5 | `MOD_M05_E07_add_prokka` | `add` | ❌ | ❌ | t1: `file_not_found` |
| 6 | `MOD_M06_D01_replace_spades_with_shovill` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 7 | `MOD_M07_D03_replace_trimmomatic_with_fastp` | `replace` | ❌ | ❌ | t1: `silent_no_op` |
| 8 | `MOD_M08_E01_replace_spades_with_unicycler` | `replace` | ❌ | ✅ | t1: `file_not_found` |
| 9 | `MOD_M09_E07_replace_abricate_with_prokka` | `replace` | ✅ | ❌ | t2: `file_not_found` |
| 10 | `MOD_M10_A05_replace_cgmlst_with_mlst` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 11 | `MOD_M11_H01_drop_cgmlst` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 12 | `MOD_M12_D01_drop_assembly` | `drop` | ✅ | ✅ |  |
| 13 | `MOD_M13_I01_drop_kmerfinder` | `drop` | ✅ | ❌ | t2: `no_code` |
| 14 | `MOD_M14_E02_switch_species_to_salmonella` | `switch_species` | ❌ | ✅ | t1: `file_not_found` |
| 15 | `MOD_M15_A04_switch_species_to_ecoli` | `switch_species` | ❌ | ❌ | t1: `missing_param` |
| 16 | `MOD_M16_E07_switch_species_to_salmonella` | `switch_species` | ✅ | ❌ | t2: `file_not_found` |
| 17 | `MOD_M17_D05_switch_species_to_ecoli` | `switch_species` | ❌ | · | t1: `no_code` |
| 18 | `MOD_K01_add_mlst_to_chewbbaca_lis_spades` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 19 | `MOD_K02_add_mlst_to_chewbbaca_sal_spades` | `add` | ❌ | ❌ | t1: `file_not_found` |
| 20 | `MOD_K03_add_mlst_to_chewbbaca_eco_spades` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 21 | `MOD_K04_add_abricate_to_chewbbaca_lis_spades` | `add` | ✅ | ✅ |  |
| 22 | `MOD_K05_add_abricate_to_chewbbaca_sal_spades` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 23 | `MOD_K06_add_prokka_to_chewbbaca_lis_spades` | `add` | ✅ | ✅ |  |
| 24 | `MOD_K07_add_prokka_to_chewbbaca_sal_spades` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 25 | `MOD_K08_add_chewbbaca_to_mlst_lis_spades` | `add` | ✅ | ✅ |  |
| 26 | `MOD_K09_add_chewbbaca_to_mlst_eco_spades` | `add` | ✅ | ❌ | t2: `silent_no_op` |
| 27 | `MOD_K10_add_abricate_to_mlst_lis_spades` | `add` | ❌ | ❌ | t1: `missing_param` |
| 28 | `MOD_K11_add_abricate_to_mlst_eco_spades` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 29 | `MOD_K12_add_abricate_to_mlst_sal_spades` | `add` | ✅ | ✅ |  |
| 30 | `MOD_K13_add_prokka_to_mlst_lis_spades` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 31 | `MOD_K14_add_prokka_to_mlst_eco_spades` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 32 | `MOD_K15_add_prokka_to_mlst_sal_spades` | `add` | ✅ | ✅ |  |
| 33 | `MOD_K16_add_prokka_to_mlst_cam_spades` | `add` | ✅ | ✅ |  |
| 34 | `MOD_K17_add_prokka_to_abricate_lis_spades` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 35 | `MOD_K18_add_prokka_to_abricate_eco_spades` | `add` | ✅ | ✅ |  |
| 36 | `MOD_K19_add_mlst_to_abricate_sal_spades` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 37 | `MOD_K20_add_mlst_to_abricate_eco_spades` | `add` | ✅ | ✅ |  |
| 38 | `MOD_K21_add_mlst_to_flaA_cam_spades` | `add` | ✅ | ✅ |  |
| 39 | `MOD_K22_add_staramr_to_flaA_cam_spades` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 40 | `MOD_K23_add_abricate_to_flaA_cam_spades` | `add` | ❌ | · | t1: `no_code` |
| 41 | `MOD_K24_add_prokka_to_flaA_cam_spades` | `add` | ✅ | ❌ | t2: `arity_error` |
| 42 | `MOD_K25_add_mlst_to_staramr_cam_spades` | `add` | ✅ | ✅ |  |
| 43 | `MOD_K26_add_flaA_to_staramr_cam_spades` | `add` | ✅ | ❌ | t2: `file_not_found` |
| 44 | `MOD_K27_add_abricate_to_staramr_cam_spades` | `add` | ✅ | ✅ |  |
| 45 | `MOD_K28_add_prokka_to_staramr_cam_spades` | `add` | ❌ | ❌ | t1: `file_not_found` |
| 46 | `MOD_K29_add_flaA_to_mlst_cam_spades` | `add` | ✅ | ✅ |  |
| 47 | `MOD_K30_add_staramr_to_mlst_cam_spades` | `add` | ❌ | ❌ | t1: `file_not_found` |
| 48 | `MOD_K31_add_abricate_to_mlst_lis_shovill` | `add` | ❌ | ✅ | t1: `missing_param` |
| 49 | `MOD_K32_add_prokka_to_mlst_sal_shovill` | `add` | ❌ | · | t1: `no_code` |
| 50 | `MOD_K33_add_abricate_to_chewbbaca_lis_unicycler` | `add` | ❌ | · | t1: `no_code` |
| 51 | `MOD_K34_add_abricate_to_chewbbaca_sal_unicycler` | `add` | ✅ | ❌ | t2: `missing_param` |
| 52 | `MOD_K35_add_chewbbaca_to_mlst_eco_shovill` | `add` | ✅ | ✅ |  |
| 53 | `MOD_K36_add_chewbbaca_to_mlst_sal_shovill` | `add` | ❌ | ❌ | t1: `file_not_found` |
| 54 | `MOD_K37_add_abricate_to_mlst_lis_spades` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 55 | `MOD_K38_add_prokka_to_mlst_eco_spades` | `add` | ✅ | ✅ |  |
| 56 | `MOD_R01_replace_asm_spades_to_shovill_lis` | `replace` | ❌ | ✅ | t1: `missing_param` |
| 57 | `MOD_R02_replace_asm_spades_to_shovill_sal` | `replace` | ✅ | ❌ | t2: `file_not_found` |
| 58 | `MOD_R03_replace_asm_spades_to_shovill_eco` | `replace` | ❌ | ❌ | t1: `missing_param` |
| 59 | `MOD_R04_replace_asm_spades_to_shovill_cam` | `replace` | ❌ | · | t1: `no_code` |
| 60 | `MOD_R05_replace_asm_spades_to_unicycler_lis` | `replace` | ❌ | ❌ | t1: `missing_param` |
| 61 | `MOD_R06_replace_asm_spades_to_unicycler_sal` | `replace` | ✅ | ❌ | t2: `no_code` |
| 62 | `MOD_R07_replace_asm_spades_to_unicycler_cam` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 63 | `MOD_R08_replace_asm_shovill_to_spades_lis` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 64 | `MOD_R09_replace_asm_shovill_to_spades_eco` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 65 | `MOD_R10_replace_asm_shovill_to_unicycler_lis` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 66 | `MOD_R11_replace_asm_unicycler_to_spades_sal` | `replace` | ✅ | ✅ |  |
| 67 | `MOD_R12_replace_asm_unicycler_to_shovill_eco` | `replace` | ✅ | ❌ | t2: `file_not_found` |
| 68 | `MOD_RT01_replace_trim_fastp_to_trimmomatic_lis` | `replace` | ❌ | · | t1: `no_code` |
| 69 | `MOD_RT02_replace_trim_fastp_to_trimmomatic_eco` | `replace` | ❌ | ✅ | t1: `file_not_found` |
| 70 | `MOD_RT03_replace_trim_fastp_to_trimmomatic_sal` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 71 | `MOD_RT04_replace_trim_fastp_to_trimmomatic_cam` | `replace` | ✅ | ❌ | t2: `no_code` |
| 72 | `MOD_RT05_replace_trim_trimmomatic_to_fastp_lis` | `replace` | ❌ | ✅ | t1: `file_not_found` |
| 73 | `MOD_RT06_replace_trim_trimmomatic_to_fastp_sal` | `replace` | ✅ | ❌ | t2: `file_not_found` |
| 74 | `MOD_RTY01_replace_typing_mlst_to_chewbbaca_lis` | `replace` | ✅ | ✅ |  |
| 75 | `MOD_RTY02_replace_typing_mlst_to_chewbbaca_sal` | `replace` | ❌ | ✅ | t1: `file_not_found` |
| 76 | `MOD_RTY03_replace_typing_mlst_to_abricate_lis` | `replace` | ✅ | ✅ |  |
| 77 | `MOD_RTY04_replace_typing_mlst_to_abricate_sal` | `replace` | ✅ | ✅ |  |
| 78 | `MOD_RTY05_replace_typing_mlst_to_prokka_lis` | `replace` | ❌ | ✅ | t1: `file_not_found` |
| 79 | `MOD_RTY06_replace_typing_mlst_to_prokka_eco` | `replace` | ✅ | ✅ |  |
| 80 | `MOD_RTY07_replace_typing_chewbbaca_to_prokka_lis` | `replace` | ✅ | ✅ |  |
| 81 | `MOD_RTY08_replace_typing_chewbbaca_to_abricate_sal` | `replace` | ❌ | ✅ | t1: `file_not_found` |
| 82 | `MOD_RTY09_replace_typing_abricate_to_prokka_eco` | `replace` | ✅ | ✅ |  |
| 83 | `MOD_RTY10_replace_typing_prokka_to_abricate_sal` | `replace` | ✅ | ✅ |  |
| 84 | `MOD_RTY11_replace_typing_flaA_to_mlst_cam` | `replace` | ✅ | ✅ |  |
| 85 | `MOD_RTY12_replace_typing_staramr_to_abricate_cam` | `replace` | ❌ | ✅ | t1: `silent_no_op` |
| 86 | `MOD_RM01_replace_mono_mlst_to_chewbbaca_sal` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 87 | `MOD_RM02_replace_mono_mlst_to_chewbbaca_lis` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 88 | `MOD_RM03_replace_mono_chewbbaca_to_mlst_lis` | `replace` | ✅ | ✅ |  |
| 89 | `MOD_RM04_replace_mono_chewbbaca_to_mlst_sal` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 90 | `MOD_RM05_replace_mono_chewbbaca_to_abricate_lis` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 91 | `MOD_RM06_replace_mono_abricate_to_prokka_eco` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 92 | `MOD_RM07_replace_mono_abricate_to_mlst_sal` | `replace` | ❌ | ❌ | t1: `silent_no_op` |
| 93 | `MOD_RM08_replace_mono_flaA_to_staramr_cam` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 94 | `MOD_RM09_replace_mono_staramr_to_flaA_cam` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 95 | `MOD_RM10_replace_mono_staramr_to_mlst_cam` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 96 | `MOD_D01_drop_chewbbaca_keep_mlst_lis` | `drop` | ❌ | ❌ | t1: `file_not_found` |
| 97 | `MOD_D02_drop_chewbbaca_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 98 | `MOD_D03_drop_chewbbaca_keep_mlst_eco` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 99 | `MOD_D04_drop_mlst_keep_chewbbaca_lis` | `drop` | ✅ | ❌ | t2: `file_not_found` |
| 100 | `MOD_D05_drop_mlst_keep_chewbbaca_sal` | `drop` | ❌ | ❌ | t1: `file_not_found` |
| 101 | `MOD_D06_drop_abricate_keep_mlst_lis` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 102 | `MOD_D07_drop_abricate_keep_mlst_eco` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 103 | `MOD_D08_drop_abricate_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 104 | `MOD_D09_drop_prokka_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `partial_dag` |
| 105 | `MOD_D10_drop_prokka_keep_abricate_lis` | `drop` | ❌ | ❌ | t1: `arity_error` |
| 106 | `MOD_D11_drop_flaA_keep_mlst_cam` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 107 | `MOD_D12_drop_staramr_keep_mlst_cam` | `drop` | ❌ | ✅ | t1: `missing_param` |
| 108 | `MOD_DA01_drop_assembly_lis` | `drop` | ❌ | · | t1: `no_code` |
| 109 | `MOD_DA02_drop_assembly_eco` | `drop` | ❌ | · | t1: `no_code` |
| 110 | `MOD_DA03_drop_assembly_sal` | `drop` | ❌ | ❌ | t1: `file_not_found` |
| 111 | `MOD_DA04_drop_assembly_cam` | `drop` | ❌ | · | t1: `no_code` |
| 112 | `MOD_DM01_drop_mono_chewbbaca_keep_mlst_lis` | `drop` | ✅ | ❌ | t2: `file_not_found` |
| 113 | `MOD_DM02_drop_mono_chewbbaca_keep_mlst_sal` | `drop` | ✅ | ❌ | t2: `file_not_found` |
| 114 | `MOD_DM03_drop_mono_mlst_keep_chewbbaca_lis` | `drop` | ❌ | ❌ | t1: `file_not_found` |
| 115 | `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco` | `drop` | ❌ | ❌ | t1: `file_not_found` |
| 116 | `MOD_DM05_drop_mono_abricate_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 117 | `MOD_DM06_drop_mono_prokka_keep_mlst_lis` | `drop` | ❌ | ✅ | t1: `file_not_found` |
| 118 | `MOD_DM07_drop_mono_staramr_keep_mlst_cam` | `drop` | ❌ | ❌ | t1: `file_not_found` |
| 119 | `MOD_DM08_drop_mono_staramr_keep_flaA_cam` | `drop` | ✅ | ❌ | t2: `file_not_found` |
| 120 | `MOD_DM09_drop_mono_flaA_keep_staramr_cam` | `drop` | ❌ | ❌ | t1: `missing_param` |
| 121 | `MOD_DM10_drop_mono_flaA_keep_mlst_cam` | `drop` | ✅ | ❌ | t2: `file_not_found` |
| 122 | `MOD_DM11_drop_mono_abricate_keep_prokka_eco` | `drop` | ✅ | ❌ | t2: `file_not_found` |
| 123 | `MOD_DM12_drop_mono_prokka_keep_abricate_lis` | `drop` | ❌ | ❌ | t1: `arity_error` |
| 124 | `MOD_DM13_drop_mono_prokka_keep_mlst_sal` | `drop` | ❌ | ❌ | t1: `arity_error` |
| 125 | `MOD_DM14_drop_mono_abricate_keep_prokka_sal` | `drop` | ❌ | ❌ | t1: `arity_error` |
| 126 | `MOD_S01_cgmlst_retarget_lis_to_sal` | `switch_species` | ✅ | ✅ |  |
| 127 | `MOD_S02_cgmlst_retarget_lis_to_eco` | `switch_species` | ✅ | ❌ | t2: `file_not_found` |
| 128 | `MOD_S03_cgmlst_retarget_sal_to_lis` | `switch_species` | ✅ | ✅ |  |
| 129 | `MOD_S04_cgmlst_retarget_sal_to_eco` | `switch_species` | ✅ | ❌ | t2: `silent_no_op` |
| 130 | `MOD_S05_cgmlst_retarget_eco_to_lis` | `switch_species` | ❌ | ❌ | t1: `file_not_found` |
| 131 | `MOD_S06_cgmlst_retarget_eco_to_sal` | `switch_species` | ❌ | ❌ | t1: `partial_dag` |
| 132 | `MOD_SM01_mlst_retarget_lis_to_cam` | `switch_species` | ❌ | ✅ | t1: `file_not_found` |
| 133 | `MOD_SM02_mlst_retarget_sal_to_cam` | `switch_species` | ✅ | ❌ | t2: `file_not_found` |
| 134 | `MOD_SM03_mlst_retarget_eco_to_cam` | `switch_species` | ✅ | ✅ |  |
| 135 | `MOD_SM04_mlst_retarget_cam_to_lis` | `switch_species` | ✅ | ❌ | t2: `file_not_found` |
| 136 | `MOD_SM05_mlst_retarget_cam_to_sal` | `switch_species` | ✅ | ✅ |  |
| 137 | `MOD_SM06_mlst_retarget_cam_to_eco` | `switch_species` | ✅ | ✅ |  |
| 138 | `MOD_SMA01_mlst_mono_retarget_lis_to_sal` | `switch_species` | ❌ | ❌ | t1: `file_not_found` |
| 139 | `MOD_SMA02_mlst_mono_retarget_lis_to_eco` | `switch_species` | ❌ | ❌ | t1: `file_not_found` |
| 140 | `MOD_SMA03_mlst_mono_retarget_sal_to_lis` | `switch_species` | ❌ | ❌ | t1: `file_not_found` |
| 141 | `MOD_SMA04_mlst_mono_retarget_sal_to_eco` | `switch_species` | ❌ | ❌ | t1: `file_not_found` |
| 142 | `MOD_SMA05_mlst_mono_retarget_eco_to_lis` | `switch_species` | ❌ | ❌ | t1: `file_not_found` |
| 143 | `MOD_SMA06_mlst_mono_retarget_eco_to_sal` | `switch_species` | ❌ | ❌ | t1: `file_not_found` |
| 144 | `MOD_SMA07_mlst_mono_retarget_lis_to_cam` | `switch_species` | ❌ | ❌ | t1: `file_not_found` |
| 145 | `MOD_SMA08_mlst_mono_retarget_sal_to_cam` | `switch_species` | ❌ | ❌ | t1: `file_not_found` |
| 146 | `MOD_SMA09_mlst_mono_retarget_eco_to_cam` | `switch_species` | ❌ | ❌ | t1: `silent_no_op` |
| 147 | `MOD_SMA10_mlst_mono_retarget_cam_to_lis` | `switch_species` | ✅ | ❌ | t2: `no_code` |
| 148 | `MOD_3T01_addAdd_lis` | `add` | ✅ | ❌ | t2: `missing_param` |
| 149 | `MOD_3T02_addAdd_eco` | `add` | ❌ | ✅ | t1: `file_not_found` |
| 150 | `MOD_3T03_addAdd_sal` | `add` | ❌ | ❌ | t1: `missing_param` |
| 151 | `MOD_3T_AD01_addThenDrop_lis` | `add` | ❌ | ❌ | t1: `partial_dag` |
| 152 | `MOD_3T_AD02_addThenDrop_eco` | `add` | ❌ | ❌ | t1: `file_not_found` |
| 153 | `MOD_3T_AD03_addThenDrop_sal` | `add` | ❌ | ❌ | t1: `missing_param` |
| 154 | `MOD_3T_RA01_replaceThenAdd_lis` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 155 | `MOD_3T_RA02_replaceThenAdd_eco` | `replace` | ❌ | · | t1: `no_code` |
| 156 | `MOD_3T_RA03_replaceThenAdd_sal` | `replace` | ❌ | ❌ | t1: `file_not_found` |
| 157 | `MOD_3T_SA01_switchThenAdd_lis_to_sal` | `switch_species` | ✅ | ✅ |  |
| 158 | `MOD_3T_SA02_switchThenAdd_eco_to_lis` | `switch_species` | ✅ | ❌ | t2: `file_not_found` |
| 159 | `MOD_3T_SA03_switchThenAdd_sal_to_eco` | `switch_species` | ✅ | ✅ |  |

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trimming_assembly_cgmlst {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembly = step_2AS_denovo__spades(trimmed).assembled
        step_4TY_cgMLST__chewbbaca(assembly, 'listeria_monocytogenes', 'l_mono_chewie_1748_220623')
    
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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

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

// --- ENTRYPOINT ---
workflow {
    wf_trimming_assembly_cgmlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.4.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

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

include { extractKey } from '../functions/common.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
ERROR ~ missing required param: hosts_dir
```

### `MOD_M03_B01_add_trimming_t2` — `missing_param`
**Conversation:** `MOD_M03_B01_add_trimming` (add) — turn 2
**Prompt:** Add a fastp trimming step before the assembly.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades, step_1PP_trimming__fastp`
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

include { extractKey } from '../functions/common.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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

// --- ENTRYPOINT ---
workflow {
    trimmedReads = step_1PP_trimming__fastp(getSingleInput())
    module_denovo(trimmedReads.trimmed, getHost())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: hosts_dir
```

### `MOD_M04_A04_add_mlst_parallel_t1` — `silent_no_op`
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

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { parseMetadataFromFileName } from '../functions/common.nf'

// --- GLOBALS ---

def SPECIES_SCHEMA = [listeria_monocytogenes : ['l_mono_chewie_1748_220623'], escherichia_coli : ['e_coli_chewie_2360_210531'], salmonella_enterica : ['s_enterica_chewie_3255_210531']]

def SCHEMAS = [l_mono_chewie_1748_220623 : "/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip", e_coli_chewie_2360_210531 : "/schemas/Escherichia_coli_INNUENDO_wgMLST_2021-05-31T14_24_05.304225.zip", s_enterica_chewie_3255_210531 : "/schemas/Salmonella_enterica_INNUENDO_cgMLST_2021-05-31T20_28_21.350919.zip"]

def CHEWBBACA_SINGLE_END_PARAMS = [l_mono_chewie_1748_220623: ' --minimum-length 144 --st 0.1 --bsr 0.6 ', e_coli_chewie_2360_210531: ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', s_enterica_chewie_3255_210531: ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt ']

def CHEWBBACA_PAIRED_END_PARAMS = [l_mono_chewie_1748_220623: ' --minimum-length 144 ', e_coli_chewie_2360_210531: ' --minimum-length 0 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', s_enterica_chewie_3255_210531: ' --minimum-length 0 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt ']

// --- INLINE PROCESSES ---

process chewbbaca {
    container 'ghcr.io/genpat-it/chewbbaca-w-chewie-schemas:2.8.5--16b816c96d'
    
    input:
    
    tuple val(riscd_input), path(assembly)
    
    val genus_species
    
    val schema
    
    
    output:
    
    path '**'
    
    path("${base}_results_statistics.tsv"), emit: stats
    
    tuple path("${base}_results_alleles.tsv"), path('schema/'), emit: alleles
    
    tuple path("${base}_results_alleles.tsv"), path("${base}_new_alleles.txt"), val(schemaName), emit: alleles_with_new
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(assembly.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}_${METHOD}"
schemaName = getSchema(genus_species, schema)
schemaPath = SCHEMAS.get(schemaName)
newAlleleKey = assembly.getName().replaceAll('_', '-')
speciesSpecificParams = getExtraParams(schemaName)
"""
#!/bin/bash -euo pipefail
unzip ${schemaPath} -d schema > /dev/null
chmod -R 777 schema
mkdir input && cp ${assembly} input/
chewBBACA.py AlleleCall -i input -g schema -o results --cpu ${task.cpus} --force-continue --verbose ${speciesSpecificParams}
grep "${newAlleleKey}" schema/*.fasta -A1 -h | grep -v "\-\-" > ${base}_new_alleles.txt || echo "no INF alleles found"
mv results/*/results_alleles.tsv ${base}_results_alleles.tsv
mv results/*/results_contigsInfo.tsv ${base}_results_contigsInfo.tsv
mv results/*/results_statistics.tsv ${base}_results_statistics.tsv
"""
    """
}

process chewbbaca_check {
    container 'quay.io/biocontainers/python:3.9'
    
    input:
    
    path(chewbbacaStats)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    path("${base}_import_chewbbaca_check.csv"), emit: check
    
    
    script:
    """
md = parseMetadataFromFileName(chewbbacaStats.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
/scripts/chewieCheck.py --stat ${chewbbacaStats} > ${base}_import_chewbbaca_check.csv
"""
    """
}

process hashing {
    container 'ghcr.io/genpat-it/hashing:1.0--29180a232f'
    
    input:
    
    tuple path(chewbbaca_result), path(schema_path)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(chewbbaca_result.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
mask_matrix.py -i ${chewbbaca_result} -o masked_results.tsv
alleleprofile_hasher.py -p masked_results.tsv -d ${schema_path} -o ./_hashed_results.tsv
rm -Rf ${schema_path}/*
"""
    """
}

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

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'listeria_monocytogenes'

def schema = 'l_mono_chewie_1748_220623'

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
    assembly = getSingleInput()
    step_4TY_cgMLST__chewbbaca(assembly, genus_species, schema)
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.2.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_M05_E07_add_prokka_t1` — `file_not_found`
**Conversation:** `MOD_M05_E07_add_prokka` (add) — turn 1
**Prompt:** Resistance gene detection with ABRicate on Escherichia coli from Illumina paired FASTQ.

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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_assembly {
    
    take:
        
        reads
        
    
    main:
        unicycler(reads).scaffolds | assembly_filter | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow wf_species_confirmation {
    
    take:
        
        assembled
        
    
    main:
        kmerfinder(assembled)
        assigned_species = kmerfinder.out.check.map { [ it[0], getCalculatedSpecies(it[1]), getBacterialReferencePath(it[1]) ] }
    
    emit:
        
        assigned_species
        
    
}

workflow wf_resistance_gene_detection {
    
    take:
        
        assembled
        
    
    main:
        abricate(assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    reads = getSingleInput()
    wf_assembly(reads)
    wf_species_confirmation(wf_assembly.assembled)
    wf_resistance_gene_detection(wf_assembly.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.6.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_M05_E07_add_prokka_t2` — `missing_param`
**Conversation:** `MOD_M05_E07_add_prokka` (add) — turn 2
**Prompt:** Also annotate the assembly with Prokka.

**Steps (LLM):** `step_2AS_denovo__unicycler, step_3TX_species__kmerfinder, step_4AN_genes__prokka, step_4AN_AMR__abricate`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def kingdom = 'Bacteria'

def species = 'Escherichia coli'

def riscd_ref = '220308-020220308005121273-2AS_import-external'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_assembly_and_annotation {
    
    take:
        
        reads
        
    
    main:
        unicycler_out = step_2AS_denovo__unicycler(reads)
        assembly = unicycler_out.assembled
        step_3TX_species__kmerfinder(assembly)
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], kingdom, riscd_ref, '-', getEmpty() ] })
        step_4AN_AMR__abricate(assembly)
    
    emit:
        
        assembly = unicycler_out.assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_assembly_and_annotation(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_M06_D01_replace_spades_with_shovill_t1` — `file_not_found`
**Conversation:** `MOD_M06_D01_replace_spades_with_shovill` (replace) — turn 1
**Prompt:** From Illumina paired-end FASTQ of Listeria monocytogenes: trim with fastp and assemble with SPAdes.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.4.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_M06_D01_replace_spades_with_shovill_t2` — `silent_no_op`
**Conversation:** `MOD_M06_D01_replace_spades_with_shovill` (replace) — turn 2
**Prompt:** Use Shovill instead of SPAdes for the assembly.

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

include { extractKey; getRisCd; parseMetadataFromFileName } from '../functions/common.nf'

include { getSingleInput; isIlluminaPaired; isIonTorrent } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

process fastp {
    
    
    
    
    
    
    
    
    script:
    """
(r1,r2) = (reads instanceof java.util.Collection) ? reads : [reads, null]
md = parseMetadataFromFileName(r1.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}_${METHOD}"
riscd = getRisCd(md, ex, STEP, METHOD)
if (isIlluminaPaired(reads)) {
  """
    fastp --in1 ${r1} --out1 ${base}_R1.fastq.gz --in2 ${r2} --out2 ${base}_R2.fastq.gz \
    --unpaired1 ${base}_unpaired.fastq.gz --unpaired2 ${base}_unpaired.fastq.gz \
    --json ${base}_summary.json --html ${base}_summary.html --thread 8       """
} else if (isIonTorrent(reads)) {
  """
    fastp --in1 ${r1} --out1 ${base}_R1.fastq.gz  \
    --json ${base}_summary.json --html ${base}_summary.html --thread 8         
  """
}
    """
}

process shovill {
    
    
    
    
    
    
    
    
    script:
    """
(t1,t2) = (reads instanceof java.util.Collection) ? reads : [reads, null]
md = parseMetadataFromFileName(t1.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}_${METHOD}"
riscd = getRisCd(md, ex, STEP, METHOD)
"""
  shovill --outdir out --minlen 200 --cpus ${task.cpus} --ram ${task.memory.toGiga()} --R1 ${t1} --R2 ${t2}
  mv out/contigs.fa ${base}.fasta
"""
    """
}

process shovill_se {
    
    
    
    
    
    
    
    
    script:
    """
(t1,t2) = (reads instanceof java.util.Collection) ? reads : [reads, null]
md = parseMetadataFromFileName(t1.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}_${METHOD}"
riscd = getRisCd(md, ex, STEP, METHOD)
"""
  shovill-se --outdir out --minlen 200 --cpus ${task.cpus} --ram ${task.memory.toGiga()} --se ${t1} --opts '--sc --iontorrent' --kmers '31,33,55'
  mv out/contigs.fa ${base}.fasta
"""
    """
}

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__shovill {
    
    take:
        
        rawreads
        
    
    main:
        contigs_from_pe = shovill(rawreads).assembly
        contigs_from_se = shovill_se(rawreads).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }
        assembly = contigs
    
    emit:
        
        assembly
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__shovill(trimmed)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_M07_D03_replace_trimmomatic_with_fastp_t1` — `silent_no_op`
**Conversation:** `MOD_M07_D03_replace_trimmomatic_with_fastp` (replace) — turn 1
**Prompt:** Pipeline: trim with Trimmomatic, assemble with SPAdes. Illumina paired-end.

**Steps (LLM):** `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades`
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

include { extractKey; getRisCd; parseMetadataFromFileName } from '../functions/common.nf'

include { getInput; isIlluminaPaired; isIonTorrent } from '../functions/parameters.nf'

// --- GLOBALS ---

def trimmomatic_container = 'quay.io/biocontainers/trimmomatic:0.36--6'

def spades_container = 'quay.io/biocontainers/spades:3.11.1--py27_zlib1.2.8_0'

def fastqc_container = 'biocontainers/fastqc:v0.11.5_cv4'

def biopython_container = 'quay.io/biocontainers/biopython:1.78'

def python3_container = 'ghcr.io/genpat-it/python3:3.10.1--29cf21c1f1'

def quast_container = 'quay.io/biocontainers/quast:4.4--boost1.61_1'

// --- INLINE PROCESSES ---

process trimmomatic {
    container 'quay.io/biocontainers/trimmomatic:0.36--6'
    
    input:
    
    tuple val(riscd_input), path(reads)
    
    
    output:
    
    tuple val(riscd), path('*.fastq.gz'), emit: fastq
    
    path '{*trimmomatic.log,*.json}'
    
    path '*.sh', hidden: true
    
    
    script:
    """
(r1,r2) = (reads instanceof java.util.Collection) ? reads : [reads, null]
md = parseMetadataFromFileName(r1.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
riscd = getRisCd(md, ex, STEP, METHOD)
if (isIlluminaPaired(reads)) {
  """
    trimmomatic PE -threads 2 -phred33 $r1 $r2 ${base}_R1_trimmomatic.fastq.gz ${base}_R1_unpaired.fastq.gz ${base}_R2_trimmomatic.fastq.gz ${base}_R2_unpaired.fastq.gz ILLUMINACLIP:/usr/local/share/trimmomatic-0.36-6/adapters/NexteraPE-PE.fa:2:30:10 LEADING:25 TRAILING:25 SLIDINGWINDOW:20:25 MINLEN:36 2>> ${base}_trimmomatic.log;
    cat ${base}_R1_unpaired.fastq.gz ${base}_R2_unpaired.fastq.gz > ${base}_unpaired_trimmomatic.fastq.gz
    rm  ${base}_R1_unpaired.fastq.gz ${base}_R2_unpaired.fastq.gz
  """
} else if (isIonTorrent(reads)) {
  """
    trimmomatic SE -threads 2 -phred33 $r1 ${base}_R1_trimmomatic.fastq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:5:20 MINLEN:55 2>> ${base}_trimmomatic.log
  """
}
    """
}

process fastqc {
    container 'biocontainers/fastqc:v0.11.5_cv4'
    
    input:
    
    tuple val(riscd_input), path(reads)
    
    
    output:
    
    path '*'
    
    path '*.sh', hidden: true
    
    
    script:
    """
(r1,r2) = (reads instanceof java.util.Collection) ? reads : [reads, null]
md = parseMetadataFromFileName(r1.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
fastqc $reads > "${base}_fastqc.log" 2>&1
"""
    """
}

process sample_reads_check {
    container 'quay.io/biocontainers/biopython:1.78'
    
    input:
    
    tuple val(_), path(reads)
    
    tuple val(_), path(trimmed)
    
    
    output:
    
    path '*'
    
    path '*.sh', hidden: true
    
    
    script:
    """
(r1,r2) = (reads instanceof java.util.Collection) ? reads : [reads, null]
(t1,t2,u) = (trimmed instanceof java.util.Collection) ? trimmed : [trimmed, null, null]
md = parseMetadataFromFileName(r1.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
if (isIlluminaPaired(reads)) {
  """
  /scripts/SampleReadsCheck.py -n $base -R1 $r1 -R2 $r2 -T1 $t1 -T2 $t2 -U $u > ${base}_SRC_raw.log
  cat ${base}_SRC_raw.log > ${base}_SRC_treads.log;
  """
} else if (isIonTorrent(reads)) {
  """
  /scripts/SampleReadsCheck_ionTorrent.py -n $base -R1 $r1 -T1 $t1 > ${base}_SRC_raw.log
  """
}
    """
}

process denovo {
    container 'quay.io/biocontainers/spades:3.11.1--py27_zlib1.2.8_0'
    
    input:
    
    tuple val(riscd_input), path(reads)
    
    
    output:
    
    path '*'
    
    path("${base}_spades_scaffolds.fasta"), emit: scaffolds
    
    path '*.sh', hidden: true
    
    
    script:
    """
(t1,t2) = (reads instanceof java.util.Collection) ? reads : [reads, null]
md = parseMetadataFromFileName(t1.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
if (isIlluminaPaired(reads)) {
  """
  spades.py --only-assembler --careful -k 21,33,55,77 -t ${task.cpus}  -o spades -1 ${t1} -2 ${t2} > ${base}_spades.log 2>&1 ;
  mv spades/scaffolds.fasta ${base}_spades_scaffolds.fasta ;
  mv spades/contigs.fasta ${base}_spades_contigs.fasta ;
  """
} else if (isIonTorrent(reads)) {
  """
    spades.py --iontorrent --careful -o spades -s $t1 -t ${task.cpus}  > ${base}_spades.log 2>&1
    mv spades/scaffolds.fasta ${base}_spades_scaffolds.fasta ;
    mv spades/contigs.fasta ${base}_spades_contigs.fasta ;
  """
}
    """
}

process assembly_filter {
    container 'ghcr.io/genpat-it/python3:3.10.1--29cf21c1f1'
    
    input:
    
    path(scaffolds)
    
    
    output:
    
    tuple val(riscd), path("${base}_${METHOD}_scaffolds_L200.fasta"), emit: fasta
    
    path '*.sh', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(scaffolds.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
riscd = getRisCd(md, ex, STEP, METHOD)
"""
/scripts/AssemblyFilter.py -n ${base} -f ${scaffolds} -l 200 -c 0 ;
"""
    """
}

process quast {
    container 'quay.io/biocontainers/quast:4.4--boost1.61_1'
    
    input:
    
    tuple val(_), path(l200)
    
    
    output:
    
    path '*_quast.*'
    
    path '*.sh', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(l200.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
quast -m 200 --fast -o quast ${l200} > ${base}_quast.log ;
  cut -f1,14,15,16,17,18,19,20,21 quast/transposed_report.tsv > ${base}_quast.csv ;
"""
    """
}

// --- SUB WORKFLOWS ---

workflow step_1PP_trimming__trimmomatic {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = trimmomatic(rawreads).fastq;
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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__trimmomatic(getInput())
    step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_M07_D03_replace_trimmomatic_with_fastp_t2` — `no_code`
**Conversation:** `MOD_M07_D03_replace_trimmomatic_with_fastp` (replace) — turn 2
**Prompt:** Replace Trimmomatic with fastp.

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
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_M08_E01_replace_spades_with_unicycler_t1` — `file_not_found`
**Conversation:** `MOD_M08_E01_replace_spades_with_unicycler` (replace) — turn 1
**Prompt:** Classic MLST on Listeria monocytogenes from paired-end Illumina FASTQ (trim + assembly + MLST).

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.5.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_M09_E07_replace_abricate_with_prokka_t2` — `file_not_found`
**Conversation:** `MOD_M09_E07_replace_abricate_with_prokka` (replace) — turn 2
**Prompt:** Switch from ABRicate to Prokka annotation.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        trimmed
        
        assembled
        
    
}

workflow wf_annotate {
    
    take:
        
        assembled
        
    
    main:
        step_4AN_genes__prokka(assembled.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_and_assemble(getSingleInput())
    wf_annotate(wf_trim_and_assemble.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.6.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_M10_A05_replace_cgmlst_with_mlst_t1` — `file_not_found`
**Conversation:** `MOD_M10_A05_replace_cgmlst_with_mlst` (replace) — turn 1
**Prompt:** cgMLST allelic profile on an Escherichia coli assembly.

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

include { getAssembly } from '../functions/parameters.nf'

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

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getAssembly(), 'Escherichia coli', 'e_coli_chewie_2360_210531')
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.2.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_M10_A05_replace_cgmlst_with_mlst_t2` — `file_not_found`
**Conversation:** `MOD_M10_A05_replace_cgmlst_with_mlst` (replace) — turn 2
**Prompt:** Switch from cgMLST to classic 7-gene MLST.

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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.2.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_M11_H01_drop_cgmlst_t1` — `missing_param`
**Conversation:** `MOD_M11_H01_drop_cgmlst` (drop) — turn 1
**Prompt:** Run both MLST and cgMLST typing on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def genus_species = 'Listeria monocytogenes'

def schema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_typing {
    
    take:
        
        trimmed
        
    
    main:
        assembly = step_2AS_denovo__spades(trimmed).assembled
        species = step_3TX_species__kmerfinder(assembly).assigned_species
        step_4TY_MLST__mlst(assembly)
        step_4TY_cgMLST__chewbbaca(assembly, genus_species, schema)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_listeria_typing(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_M11_H01_drop_cgmlst_t2` — `no_code`
**Conversation:** `MOD_M11_H01_drop_cgmlst` (drop) — turn 2
**Prompt:** Drop the cgMLST step, only keep MLST.

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

### `MOD_M13_I01_drop_kmerfinder_t2` — `no_code`
**Conversation:** `MOD_M13_I01_drop_kmerfinder` (drop) — turn 2
**Prompt:** Drop the KmerFinder species ID. Keep only trim + assembly.

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
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Listeria monocytogenes'

def schema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

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

// --- ENTRYPOINT ---
workflow {
    step_1PP_trimming__fastp(getSingleInput())
    step_2AS_denovo__spades(step_1PP_trimming__fastp.out.trimmed)
    step_4TY_cgMLST__chewbbaca(step_2AS_denovo__spades.out.assembled, genus_species, schema)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.6.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_M15_A04_switch_species_to_ecoli_t1` — `missing_param`
**Conversation:** `MOD_M15_A04_switch_species_to_ecoli` (switch_species) — turn 1
**Prompt:** cgMLST allelic profile for Listeria monocytogenes from a pre-existing assembly.

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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def referenceCode = 'Listeria_monocytogenes'

def species = 'Listeria monocytogenes'

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

### `MOD_M15_A04_switch_species_to_ecoli_t2` — `file_not_found`
**Conversation:** `MOD_M15_A04_switch_species_to_ecoli` (switch_species) — turn 2
**Prompt:** Same thing but for Escherichia coli.

**Steps (LLM):** `step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

def genusSpecies = 'Escherichia coli'

def schema = 'ecoli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        assembly
        
    
    main:
        assembly.cross(assigned_species) { extractKey(it) }.multiMap {
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4AN_AMR__abricate(assembly)
        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, schema)
    
}

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.2.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_M16_E07_switch_species_to_salmonella_t2` — `file_not_found`
**Conversation:** `MOD_M16_E07_switch_species_to_salmonella` (switch_species) — turn 2
**Prompt:** Switch to Salmonella enterica.

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_resistance_gene_detection {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
        }.set { trAndRef }

        spades_out = step_2AS_denovo__spades(trAndRef.trimmed)
        step_4AN_AMR__abricate(spades_out.assembled)
    
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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_resistance_gene_detection(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.7.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_M17_D05_switch_species_to_ecoli_t1` — `no_code`
**Conversation:** `MOD_M17_D05_switch_species_to_ecoli` (switch_species) — turn 1
**Prompt:** Trim and de novo assembly (fastp + SPAdes) for a paired-end Illumina Campylobacter sample.

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
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_K01_add_mlst_to_chewbbaca_lis_spades_t2` — `file_not_found`
**Conversation:** `MOD_K01_add_mlst_to_chewbbaca_lis_spades` (add) — turn 2
**Prompt:** Now also run mlst in parallel on the same assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_4TY_MLST__mlst`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'listeria_monocytogenes'

def schema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trimming_assembly_typing {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads)
        assembly = step_2AS_denovo__spades(trimmed)
        step_4TY_cgMLST__chewbbaca(assembly, genus_species, schema)
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

workflow step_2AS_denovo__spades {
    
    take:
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

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
    wf_trimming_assembly_typing(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.200.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K02_add_mlst_to_chewbbaca_sal_spades_t1` — `file_not_found`
**Conversation:** `MOD_K02_add_mlst_to_chewbbaca_sal_spades` (add) — turn 1
**Prompt:** chewbbaca on Salmonella enterica from paired Illumina FASTQ (fastp + spades).

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

include { extractKey } from '../functions/common.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_denovo {
    
    take:
        
        trimmedReads
        
    
    main:
        trimmedReads.multiMap {
            trimmed: it
            genus_species: 'Salmonella enterica'
            schema: 's_enterica_chewie_3255_210531'
        }.set { prep }
        assembled = step_2AS_denovo__spades(prep.trimmed)
        step_4TY_cgMLST__chewbbaca(assembled, prep.genus_species, prep.schema)
    
    emit:
        
        assembled
        
    
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

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    module_denovo(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.200.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K02_add_mlst_to_chewbbaca_sal_spades_t2` — `file_not_found`
**Conversation:** `MOD_K02_add_mlst_to_chewbbaca_sal_spades` (add) — turn 2
**Prompt:** Now also run mlst in parallel on the same assembly.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_4TY_MLST__mlst, step_1PP_trimming__fastp`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def genus_species = 'Salmonella enterica'

def schema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_denovo_and_typing {
    
    take:
        
        trimmedReads
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmedReads)

        assembled.cross(genus_species, schema) { extractKey(it) }.multiMap {
            assembly: it[0]
            genus_species: it[1]
            schema: it[2]
        }.set { prep }

        step_4TY_cgMLST__chewbbaca(prep.assembly, prep.genus_species, prep.schema)
        step_4TY_MLST__mlst(prep.assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_denovo_and_typing(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.200.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K03_add_mlst_to_chewbbaca_eco_spades_t2` — `file_not_found`
**Conversation:** `MOD_K03_add_mlst_to_chewbbaca_eco_spades` (add) — turn 2
**Prompt:** Now also run mlst in parallel on the same assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_4TY_MLST__mlst`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def genus_species = 'Escherichia coli'

def schema = 'e_coli_chewie_2360_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
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
        
        assembled
        
    
    main:
        step_4TY_cgMLST__chewbbaca(assembled, genus_species, schema)
        step_4TY_MLST__mlst(assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_and_assemble(getSingleInput())
    wf_typing(wf_trim_and_assemble.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.200.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
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

// --- GLOBALS ---

def genus_species = 'Salmonella enterica'

def schema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

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

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = step_2AS_denovo__spades(trimmed)
    step_4TY_cgMLST__chewbbaca(assembled, genus_species, schema)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.201.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K07_add_prokka_to_chewbbaca_sal_spades_t1` — `file_not_found`
**Conversation:** `MOD_K07_add_prokka_to_chewbbaca_sal_spades` (add) — turn 1
**Prompt:** chewbbaca on Salmonella enterica from paired Illumina FASTQ (fastp + spades).

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_cgmlst {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            genus_species: 'Salmonella enterica'
            schema: 's_enterica_chewie_3255_210531'
        }.set { prep }

        assembly = step_2AS_denovo__spades(prep.trimmed).assembled
        step_4TY_cgMLST__chewbbaca(assembly, prep.genus_species, prep.schema)
    
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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast

        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

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

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_salmonella_cgmlst(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.202.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K09_add_chewbbaca_to_mlst_eco_spades_t2` — `silent_no_op`
**Conversation:** `MOD_K09_add_chewbbaca_to_mlst_eco_spades` (add) — turn 2
**Prompt:** Now also run chewbbaca in parallel on the same assembly.

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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

def genus_species = 'Escherichia_coli'

def schema = 'e_coli_chewie_2360_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_mlst_cgmlst {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        spades_out = step_2AS_denovo__spades(trAndRef.trimmed)
        step_4TY_MLST__mlst(spades_out.assembled)
        step_4TY_cgMLST__chewbbaca(spades_out.assembled, genus_species, schema)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_mlst_cgmlst(getSingleInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_K10_add_abricate_to_mlst_lis_spades_t1` — `missing_param`
**Conversation:** `MOD_K10_add_abricate_to_mlst_lis_spades` (add) — turn 1
**Prompt:** mlst on Listeria monocytogenes from paired Illumina FASTQ (fastp + spades).

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades, step_4TY_MLST__mlst`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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

        // [REMOVED BY PLAN] depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
        assembled = step_2AS_denovo__spades(denovoInput)

        step_4TY_MLST__mlst(assembled)
    
    emit:
        
        assembled
        
    
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

### `MOD_K10_add_abricate_to_mlst_lis_spades_t2` — `file_not_found`
**Conversation:** `MOD_K10_add_abricate_to_mlst_lis_spades` (add) — turn 2
**Prompt:** Now also run abricate in parallel on the same assembly.

**Steps (LLM):** `step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4TY_MLST__mlst, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey } from '../functions/common.nf'

include { getInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

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
        if (!params.skip_bestref_mapping) {
          trimmed.cross(assigned_species) { extractKey(it) }.multiMap {
            trimmed: it[0]
            species: it[1][1]
            referencePath: it[1][2]
          }.set { trimAndAndSpecies }
          step_2AS_mapping__bowtie(trimAndAndSpecies.trimmed, trimAndAndSpecies.referencePath)
        }

        step_4AN_AMR__abricate(assembly)

        assembly.cross(assigned_species) { extractKey(it) }.multiMap {
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getInput()).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    module_typing_bacteria(trimmed, assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.204.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K11_add_abricate_to_mlst_eco_spades_t2` — `file_not_found`
**Conversation:** `MOD_K11_add_abricate_to_mlst_eco_spades` (add) — turn 2
**Prompt:** Now also run abricate in parallel on the same assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_AMR__abricate`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast

        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    step_4TY_MLST__mlst(assembly)
    step_4AN_AMR__abricate(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.202.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K13_add_prokka_to_mlst_lis_spades_t2` — `file_not_found`
**Conversation:** `MOD_K13_add_prokka_to_mlst_lis_spades` (add) — turn 2
**Prompt:** Now also run prokka in parallel on the same assembly.

**Steps (LLM):** `step_4TY_MLST__mlst, step_4AN_genes__prokka, step_1PP_trimming__fastp, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def kingdom = 'Bacteria'

def riscd_ref = '220308-020220308005121273-2AS_import-external'

def reference = ''

def gb = ''

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_mlst_prokka {
    
    take:
        
        assembly
        
    
    main:
        step_4TY_MLST__mlst(assembly)
        step_4AN_genes__prokka([assembly[0], assembly[1], kingdom, riscd_ref, reference, gb])
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    wf_mlst_prokka(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.205.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K14_add_prokka_to_mlst_eco_spades_t2` — `file_not_found`
**Conversation:** `MOD_K14_add_prokka_to_mlst_eco_spades` (add) — turn 2
**Prompt:** Now also run prokka in parallel on the same assembly.

**Steps (LLM):** `step_4TY_MLST__mlst, step_4AN_genes__prokka, step_1PP_trimming__fastp, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def kingdom = 'Bacteria'

def riscd_ref = '220308-020220308005121273-2AS_import-external'

def reference = ''

def gb = ''

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_mlst_prokka {
    
    take:
        
        assembly
        
    
    main:
        step_4TY_MLST__mlst(assembly)
        step_4AN_genes__prokka([assembly[0], assembly[1], kingdom, riscd_ref, reference, gb])
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    wf_mlst_prokka(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.203.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    wf_trim_and_assemble(rawreads)
    step_4AN_AMR__abricate(wf_trim_and_assemble.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.206.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K19_add_mlst_to_abricate_sal_spades_t1` — `file_not_found`
**Conversation:** `MOD_K19_add_mlst_to_abricate_sal_spades` (add) — turn 1
**Prompt:** abricate on Salmonella enterica from paired Illumina FASTQ (fastp + spades).

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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_and_assemble(getSingleInput())
    step_4AN_AMR__abricate(wf_trim_and_assemble.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.205.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K22_add_staramr_to_flaA_cam_spades_t1` — `file_not_found`
**Conversation:** `MOD_K22_add_staramr_to_flaA_cam_spades` (add) — turn 1
**Prompt:** flaA on Campylobacter jejuni from paired Illumina FASTQ (fastp + spades).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_flaA__flaA`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_flaA__flaA(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'campylobacter'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_flaA__flaA {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        mlst_flaa(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    step_4TY_flaA__flaA(assembly, genus_species)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.202.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K23_add_abricate_to_flaA_cam_spades_t1` — `no_code`
**Conversation:** `MOD_K23_add_abricate_to_flaA_cam_spades` (add) — turn 1
**Prompt:** flaA on Campylobacter jejuni from paired Illumina FASTQ (fastp + spades).

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_flaA__flaA(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_K24_add_prokka_to_flaA_cam_spades_t2` — `arity_error`
**Conversation:** `MOD_K24_add_prokka_to_flaA_cam_spades` (add) — turn 2
**Prompt:** Now also run prokka in parallel on the same assembly.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_flaA__flaA, step_4AN_genes__prokka, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_flaA__flaA(assembled, param('genus_species'))
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def genus_species = 'Campylobacter jejuni'

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_analysis {
    
    take:
        
        trimmed
        
    
    main:
        assembly = step_2AS_denovo__spades(trimmed)

        assembly.multiMap {
          assembly: it
          genus_species: genus_species
        }.set { flaA_input }

        step_4TY_flaA__flaA(flaA_input.assembly, flaA_input.genus_species)

        assembly.multiMap {
          assembly: it
          kingdom: kingdom
        }.set { prokka_input }

        step_4AN_genes__prokka(prokka_input.assembly, prokka_input.kingdom)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_campylobacter_analysis(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_campylobacter_analysis:step_4AN_genes__prokka` declares 1 input channels but 2 were given
```

### `MOD_K26_add_flaA_to_staramr_cam_spades_t2` — `file_not_found`
**Conversation:** `MOD_K26_add_flaA_to_staramr_cam_spades` (add) — turn 2
**Prompt:** Now also run flaA in parallel on the same assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr, step_4TY_flaA__flaA`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__staramr(assembled, param('genus_species'))
    step_4TY_flaA__flaA(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def genusSpecies = 'Campylobacter jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembly = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        trimmed
        
        assembly
        
    
}

workflow wf_amr_and_typing {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_AMR__staramr(assembly, genusSpecies)
        step_4TY_flaA__flaA(assembly, genusSpecies)
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    wf_trim_and_assemble(rawreads)
    wf_amr_and_typing(wf_trim_and_assemble.assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.206.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K28_add_prokka_to_staramr_cam_spades_t1` — `file_not_found`
**Conversation:** `MOD_K28_add_prokka_to_staramr_cam_spades` (add) — turn 1
**Prompt:** staramr on Campylobacter jejuni from paired Illumina FASTQ (fastp + spades).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__staramr(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Campylobacter jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4AN_AMR__staramr {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        staramr(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = step_2AS_denovo__spades(trimmed)
    step_4AN_AMR__staramr(assembled, genus_species)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.208.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K28_add_prokka_to_staramr_cam_spades_t2` — `arity_error`
**Conversation:** `MOD_K28_add_prokka_to_staramr_cam_spades` (add) — turn 2
**Prompt:** Now also run prokka in parallel on the same assembly.

**Steps (LLM):** `step_4AN_AMR__staramr, step_4AN_genes__prokka, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def genusSpecies = 'Campylobacter jejuni'

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_amr_and_annotation {
    
    take:
        
        assembled
        
    
    main:
        assembled.multiMap {
            assembly: it
            genus_species: genusSpecies
            kingdom: kingdom
        }.set { prep }

        step_4AN_AMR__staramr(prep.assembly, prep.genus_species)
        step_4AN_genes__prokka(prep.assembly, prep.kingdom)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    wf_amr_and_annotation(assembled)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_amr_and_annotation:step_4AN_genes__prokka` declares 1 input channels but 2 were given
```

### `MOD_K30_add_staramr_to_mlst_cam_spades_t1` — `file_not_found`
**Conversation:** `MOD_K30_add_staramr_to_mlst_cam_spades` (add) — turn 1
**Prompt:** mlst on Campylobacter jejuni from paired Illumina FASTQ (fastp + spades).

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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        assembled
        
    
}

workflow wf_mlst_typing {
    
    take:
        
        assembled
        
    
    main:
        step_4TY_MLST__mlst(assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    wf_trim_and_assemble(rawreads)
    wf_mlst_typing(wf_trim_and_assemble.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.210.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K30_add_staramr_to_mlst_cam_spades_t2` — `file_not_found`
**Conversation:** `MOD_K30_add_staramr_to_mlst_cam_spades` (add) — turn 2
**Prompt:** Now also run staramr in parallel on the same assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_AMR__staramr`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_AMR__staramr(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput; param } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        assembled
        
    
}

workflow wf_mlst_and_amr {
    
    take:
        
        assembled
        
        genus_species
        
    
    main:
        step_4TY_MLST__mlst(assembled)
        step_4AN_AMR__staramr(assembled, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    wf_trim_and_assemble(rawreads).assembled | wf_mlst_and_amr(assembled, param('genus_species'))
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.210.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K31_add_abricate_to_mlst_lis_shovill_t1` — `missing_param`
**Conversation:** `MOD_K31_add_abricate_to_mlst_lis_shovill` (add) — turn 1
**Prompt:** mlst on Listeria monocytogenes from paired Illumina FASTQ (fastp + shovill).

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp, step_2AS_denovo__shovill`
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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

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
        // [REMOVED BY PLAN] assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species
            
            if (!params.skip_bestref_mapping) {
                trimmed.cross(assigned_species) { extractKey(it) }.multiMap {
                  trimmed: it[0]
                  species: it[1][1]
                  referencePath: it[1][2]
                }.set { trimAndAndSpecies }
            // [REMOVED BY PLAN] step_2AS_mapping__bowtie(trimAndAndSpecies.trimmed, trimAndAndSpecies.referencePath)
            } 

            // [REMOVED BY PLAN] step_4AN_AMR__abricate(assembly)

            // [REMOVED BY PLAN] step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

            assembly.cross(assigned_species) { extractKey(it) }.multiMap {
                assembly: it[0]
                species: it[1][1]
            }.set { assemblyAndSpecies }

            // [REMOVED BY PLAN] step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
            step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
            // [REMOVED BY PLAN] step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
            // [REMOVED BY PLAN] step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, '')
    
    emit:
        
        genus_species = assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
        assembly = step_2AS_denovo__shovill(trimmed).assembly
        module_typing_bacteria(trimmed, assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_K32_add_prokka_to_mlst_sal_shovill_t1` — `no_code`
**Conversation:** `MOD_K32_add_prokka_to_mlst_sal_shovill` (add) — turn 1
**Prompt:** mlst on Salmonella enterica from paired Illumina FASTQ (fastp + shovill).

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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_K33_add_abricate_to_chewbbaca_lis_unicycler_t1` — `no_code`
**Conversation:** `MOD_K33_add_abricate_to_chewbbaca_lis_unicycler` (add) — turn 1
**Prompt:** chewbbaca on Listeria monocytogenes from paired Illumina FASTQ (fastp + unicycler).

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__unicycler(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_K34_add_abricate_to_chewbbaca_sal_unicycler_t2` — `missing_param`
**Conversation:** `MOD_K34_add_abricate_to_chewbbaca_sal_unicycler` (add) — turn 2
**Prompt:** Now also run abricate in parallel on the same assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4AN_AMR__abricate, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__unicycler(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def schema = ''

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
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, schema)
    
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

### `MOD_K36_add_chewbbaca_to_mlst_sal_shovill_t1` — `file_not_found`
**Conversation:** `MOD_K36_add_chewbbaca_to_mlst_sal_shovill` (add) — turn 1
**Prompt:** mlst on Salmonella enterica from paired Illumina FASTQ (fastp + shovill).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__shovill {
    
    take:
        
        rawreads
        
    
    main:
        contigs_from_pe = shovill(rawreads).assembly
        contigs_from_se = shovill_se(rawreads).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }
    
    emit:
        
        assembly = contigs
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__shovill(trimmed)
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.208.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K36_add_chewbbaca_to_mlst_sal_shovill_t2` — `file_not_found`
**Conversation:** `MOD_K36_add_chewbbaca_to_mlst_sal_shovill` (add) — turn 2
**Prompt:** Now also run chewbbaca in parallel on the same assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill`
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

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'salmonella_enterica'

def schema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_typing {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
        chewbbaca(assembly, genus_species, schema)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__shovill(trimmed).assembly
    wf_salmonella_typing(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.208.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_K37_add_abricate_to_mlst_lis_spades_t1` — `file_not_found`
**Conversation:** `MOD_K37_add_abricate_to_mlst_lis_spades` (add) — turn 1
**Prompt:** mlst on Listeria monocytogenes from paired Illumina FASTQ (trimmomatic + spades).

**Steps (LLM):** `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_1PP_trimming__trimmomatic {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = trimmomatic(rawreads).fastq
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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__trimmomatic(getSingleInput())
    assembled = step_2AS_denovo__spades(trimmed)
    step_4TY_MLST__mlst(assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.209.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_R01_replace_asm_spades_to_shovill_lis_t1` — `missing_param`
**Conversation:** `MOD_R01_replace_asm_spades_to_shovill_lis` (replace) — turn 1
**Prompt:** Trim + assemble Listeria monocytogenes from paired Illumina FASTQ using fastp + spades.

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

include { extractKey } from '../functions/common.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
ERROR ~ missing required param: hosts_dir
```

### `MOD_R02_replace_asm_spades_to_shovill_sal_t2` — `file_not_found`
**Conversation:** `MOD_R02_replace_asm_spades_to_shovill_sal` (replace) — turn 2
**Prompt:** Replace spades with shovill.

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

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__shovill {
    
    take:
        
        trimmed
        
    
    main:
        contigs_from_pe = shovill(trimmed).assembly
        contigs_from_se = shovill_se(trimmed).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }
    
    emit:
        
        assembly = contigs
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    step_2AS_denovo__shovill(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.209.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_R03_replace_asm_spades_to_shovill_eco_t1` — `missing_param`
**Conversation:** `MOD_R03_replace_asm_spades_to_shovill_eco` (replace) — turn 1
**Prompt:** Trim + assemble Escherichia coli from paired Illumina FASTQ using fastp + spades.

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

include { extractKey } from '../functions/common.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
ERROR ~ missing required param: hosts_dir
```

### `MOD_R03_replace_asm_spades_to_shovill_eco_t2` — `no_code`
**Conversation:** `MOD_R03_replace_asm_spades_to_shovill_eco` (replace) — turn 2
**Prompt:** Replace spades with shovill.

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
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_R04_replace_asm_spades_to_shovill_cam_t1` — `no_code`
**Conversation:** `MOD_R04_replace_asm_spades_to_shovill_cam` (replace) — turn 1
**Prompt:** Trim + assemble Campylobacter jejuni from paired Illumina FASTQ using fastp + spades.

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
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_R05_replace_asm_spades_to_unicycler_lis_t1` — `missing_param`
**Conversation:** `MOD_R05_replace_asm_spades_to_unicycler_lis` (replace) — turn 1
**Prompt:** Trim + assemble Listeria monocytogenes from paired Illumina FASTQ using fastp + spades.

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

include { extractKey } from '../functions/common.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
ERROR ~ missing required param: hosts_dir
```

### `MOD_R05_replace_asm_spades_to_unicycler_lis_t2` — `missing_param`
**Conversation:** `MOD_R05_replace_asm_spades_to_unicycler_lis` (replace) — turn 2
**Prompt:** Replace spades with unicycler.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades, step_1PP_trimming__fastp, step_2AS_denovo__unicycler`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

def referenceCode = 'NC_045512.2'

def referencePath = "${params.assets_dir}/module_covid_emergency/NC_045512.fasta"

def referenceRiscd = '220308-020220308005121273-2AS_import-external'

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

        // [REMOVED BY PLAN] depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
        // [REMOVED BY PLAN] assembled = step_2AS_denovo__spades(denovoInput)
    
    emit:
        
        assembled
        
        depleted
        
    
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

workflow step_2AS_denovo__unicycler {
    
    take:
        
        data
        
    
    main:
        unicycler(data).scaffolds
        assembly_filter(unicycler.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__unicycler(trimmed)
    module_denovo(trimmed, getHost())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: hosts_dir
```

### `MOD_R06_replace_asm_spades_to_unicycler_sal_t2` — `no_code`
**Conversation:** `MOD_R06_replace_asm_spades_to_unicycler_sal` (replace) — turn 2
**Prompt:** Replace spades with unicycler.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_R07_replace_asm_spades_to_unicycler_cam_t1` — `file_not_found`
**Conversation:** `MOD_R07_replace_asm_spades_to_unicycler_cam` (replace) — turn 1
**Prompt:** Trim + assemble Campylobacter jejuni from paired Illumina FASTQ using fastp + spades.

**Steps (LLM):** `step_1PP_trimming__fastp`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_assembly {
    
    take:
        
        trimmed
        
    
    main:
        denovo(trimmed)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_campylobacter_assembly(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.212.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_R07_replace_asm_spades_to_unicycler_cam_t2` — `no_code`
**Conversation:** `MOD_R07_replace_asm_spades_to_unicycler_cam` (replace) — turn 2
**Prompt:** Replace spades with unicycler.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_R08_replace_asm_shovill_to_spades_lis_t1` — `file_not_found`
**Conversation:** `MOD_R08_replace_asm_shovill_to_spades_lis` (replace) — turn 1
**Prompt:** Trim + assemble Listeria monocytogenes from paired Illumina FASTQ using fastp + shovill.

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

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__shovill {
    
    take:
        
        rawreads
        
    
    main:
        contigs_from_pe = shovill(rawreads).assembly
        contigs_from_se = shovill_se(rawreads).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }
    
    emit:
        
        assembly = contigs
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__shovill(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.212.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_R08_replace_asm_shovill_to_spades_lis_t2` — `file_not_found`
**Conversation:** `MOD_R08_replace_asm_shovill_to_spades_lis` (replace) — turn 2
**Prompt:** Replace shovill with spades.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.212.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_R09_replace_asm_shovill_to_spades_eco_t1` — `file_not_found`
**Conversation:** `MOD_R09_replace_asm_shovill_to_spades_eco` (replace) — turn 1
**Prompt:** Trim + assemble Escherichia coli from paired Illumina FASTQ using fastp + shovill.

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

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__shovill {
    
    take:
        
        trimmed
        
    
    main:
        contigs_from_pe = shovill(trimmed).assembly
        contigs_from_se = shovill_se(trimmed).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }
        assembly = contigs
    
    emit:
        
        assembly
        
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    trimmed = step_1PP_trimming__fastp(rawreads)
    assembly = step_2AS_denovo__shovill(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.209.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_R09_replace_asm_shovill_to_spades_eco_t2` — `file_not_found`
**Conversation:** `MOD_R09_replace_asm_shovill_to_spades_eco` (replace) — turn 2
**Prompt:** Replace shovill with spades.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        denovo(trimmed)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.209.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_R10_replace_asm_shovill_to_unicycler_lis_t1` — `file_not_found`
**Conversation:** `MOD_R10_replace_asm_shovill_to_unicycler_lis` (replace) — turn 1
**Prompt:** Trim + assemble Listeria monocytogenes from paired Illumina FASTQ using fastp + shovill.

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

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__shovill {
    
    take:
        
        rawreads
        
    
    main:
        contigs_from_pe = shovill(rawreads).assembly
        contigs_from_se = shovill_se(rawreads).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }
    
    emit:
        
        assembly = contigs
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    step_2AS_denovo__shovill(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.213.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_R10_replace_asm_shovill_to_unicycler_lis_t2` — `file_not_found`
**Conversation:** `MOD_R10_replace_asm_shovill_to_unicycler_lis` (replace) — turn 2
**Prompt:** Replace shovill with unicycler.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__unicycler`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__unicycler {
    
    take:
        
        data
        
    
    main:
        unicycler(data).scaffolds
        assembly_filter(unicycler.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = step_2AS_denovo__unicycler(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.213.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_R12_replace_asm_unicycler_to_shovill_eco_t2` — `file_not_found`
**Conversation:** `MOD_R12_replace_asm_unicycler_to_shovill_eco` (replace) — turn 2
**Prompt:** Replace unicycler with shovill.

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

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__shovill {
    
    take:
        
        rawreads
        
    
    main:
        contigs_from_pe = shovill(rawreads).assembly
        contigs_from_se = shovill_se(rawreads).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }
    
    emit:
        
        assembly = contigs
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__shovill(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.210.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_RT01_replace_trim_fastp_to_trimmomatic_lis_t1` — `no_code`
**Conversation:** `MOD_RT01_replace_trim_fastp_to_trimmomatic_lis` (replace) — turn 1
**Prompt:** Trim + assemble Listeria monocytogenes from paired Illumina FASTQ using fastp + SPAdes.

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
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_RT02_replace_trim_fastp_to_trimmomatic_eco_t1` — `file_not_found`
**Conversation:** `MOD_RT02_replace_trim_fastp_to_trimmomatic_eco` (replace) — turn 1
**Prompt:** Trim + assemble Escherichia coli from paired Illumina FASTQ using fastp + SPAdes.

**Steps (LLM):** `step_2AS_denovo__spades, step_1PP_trimming__fastp`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_denovo {
    
    take:
        
        trimmedReads
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmedReads)
    
    emit:
        
        assembled
        
    
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

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    module_denovo(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.211.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_RT03_replace_trim_fastp_to_trimmomatic_sal_t1` — `file_not_found`
**Conversation:** `MOD_RT03_replace_trim_fastp_to_trimmomatic_sal` (replace) — turn 1
**Prompt:** Trim + assemble Salmonella enterica from paired Illumina FASTQ using fastp + SPAdes.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.212.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_RT03_replace_trim_fastp_to_trimmomatic_sal_t2` — `file_not_found`
**Conversation:** `MOD_RT03_replace_trim_fastp_to_trimmomatic_sal` (replace) — turn 2
**Prompt:** Replace fastp with trimmomatic.

**Steps (LLM):** `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_1PP_trimming__trimmomatic {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = trimmomatic(rawreads).fastq;
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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__trimmomatic(getSingleInput())
    step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.212.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_RT04_replace_trim_fastp_to_trimmomatic_cam_t2` — `no_code`
**Conversation:** `MOD_RT04_replace_trim_fastp_to_trimmomatic_cam` (replace) — turn 2
**Prompt:** Replace fastp with trimmomatic.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_RT05_replace_trim_trimmomatic_to_fastp_lis_t1` — `file_not_found`
**Conversation:** `MOD_RT05_replace_trim_trimmomatic_to_fastp_lis` (replace) — turn 1
**Prompt:** Trim + assemble Listeria monocytogenes from paired Illumina FASTQ using trimmomatic + SPAdes.

**Steps (LLM):** `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_1PP_trimming__trimmomatic {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = trimmomatic(rawreads).fastq;
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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__trimmomatic(getSingleInput())
    step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.215.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_RT06_replace_trim_trimmomatic_to_fastp_sal_t2` — `file_not_found`
**Conversation:** `MOD_RT06_replace_trim_trimmomatic_to_fastp_sal` (replace) — turn 2
**Prompt:** Replace trimmomatic with fastp.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.213.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_RTY02_replace_typing_mlst_to_chewbbaca_sal_t1` — `file_not_found`
**Conversation:** `MOD_RTY02_replace_typing_mlst_to_chewbbaca_sal` (replace) — turn 1
**Prompt:** mlst on Salmonella enterica from paired Illumina FASTQ (fastp + SPAdes + mlst).

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.214.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_RTY05_replace_typing_mlst_to_prokka_lis_t1` — `file_not_found`
**Conversation:** `MOD_RTY05_replace_typing_mlst_to_prokka_lis` (replace) — turn 1
**Prompt:** mlst on Listeria monocytogenes from paired Illumina FASTQ (fastp + SPAdes + mlst).

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_mlst {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
        }.set { trAndRef }

        assembly_out = step_2AS_denovo__spades(trAndRef.trimmed)
        step_4TY_MLST__mlst(assembly_out.assembled)
    
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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed
    wf_listeria_mlst(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.218.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_RTY08_replace_typing_chewbbaca_to_abricate_sal_t1` — `file_not_found`
**Conversation:** `MOD_RTY08_replace_typing_chewbbaca_to_abricate_sal` (replace) — turn 1
**Prompt:** chewbbaca on Salmonella enterica from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).

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

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

def STEP_1PP = '1PP_trimming'

def STEP_2AS = '2AS_denovo'

def STEP_4TY = '4TY_cgMLST'

def METHOD_1PP = 'fastp'

def METHOD_2AS = 'spades'

def METHOD_4TY = 'chewbbaca'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

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

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.216.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_RTY12_replace_typing_staramr_to_abricate_cam_t1` — `silent_no_op`
**Conversation:** `MOD_RTY12_replace_typing_staramr_to_abricate_cam` (replace) — turn 1
**Prompt:** staramr on Campylobacter jejuni from paired Illumina FASTQ (fastp + SPAdes + staramr).

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_AMR__staramr`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__staramr(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

// --- GLOBALS ---

def genus_species = 'Campylobacter jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_amr {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        spades_out = step_2AS_denovo__spades(trAndRef.trimmed)
        step_4AN_AMR__staramr(spades_out.assembled, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_campylobacter_amr(getSingleInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_RM01_replace_mono_mlst_to_chewbbaca_sal_t1` — `file_not_found`
**Conversation:** `MOD_RM01_replace_mono_mlst_to_chewbbaca_sal` (replace) — turn 1
**Prompt:** Run mlst on a pre-existing Salmonella enterica assembly.

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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.218.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM01_replace_mono_mlst_to_chewbbaca_sal_t2` — `silent_no_op`
**Conversation:** `MOD_RM01_replace_mono_mlst_to_chewbbaca_sal` (replace) — turn 2
**Prompt:** Use chewbbaca on that same assembly instead.

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

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { parseMetadataFromFileName } from '../functions/common.nf'

// --- GLOBALS ---

def SPECIES_SCHEMA = { listeria_monocytogenes: ['l_mono_chewie_1748_220623'], escherichia_coli: ['e_coli_chewie_2360_210531'], salmonella_enterica: ['s_enterica_chewie_3255_210531'] }

def SCHEMAS = { l_mono_chewie_1748_220623: '/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip', e_coli_chewie_2360_210531: '/schemas/Escherichia_coli_INNUENDO_wgMLST_2021-05-31T14_24_05.304225.zip', s_enterica_chewie_3255_210531: '/schemas/Salmonella_enterica_INNUENDO_cgMLST_2021-05-31T20_28_21.350919.zip' }

def CHEWBBACA_SINGLE_END_PARAMS = { l_mono_chewie_1748_220623: ' --minimum-length 144 --st 0.1 --bsr 0.6 ', e_coli_chewie_2360_210531: ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', s_enterica_chewie_3255_210531: ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt ' }

def CHEWBBACA_PAIRED_END_PARAMS = { l_mono_chewie_1748_220623: ' --minimum-length 144 ', e_coli_chewie_2360_210531: ' --minimum-length 0 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', s_enterica_chewie_3255_210531: ' --minimum-length 0 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt ' }

// --- INLINE PROCESSES ---

process chewbbaca {
    container 'ghcr.io/genpat-it/chewbbaca-w-chewie-schemas:2.8.5--16b816c96d'
    
    input:
    
    tuple val(riscd_input), path(assembly)
    
    val genus_species
    
    val schema
    
    
    output:
    
    path '**'
    
    path('${base}_results_statistics.tsv'), emit: stats
    
    tuple path('${base}_results_alleles.tsv'), path('schema/'), emit: alleles
    
    tuple path('${base}_results_alleles.tsv'), path('${base}_new_alleles.txt'), val(schemaName), emit: alleles_with_new
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(assembly.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}_${METHOD}"
schemaName = getSchema(genus_species, schema)
schemaPath = SCHEMAS.get(schemaName)
newAlleleKey = assembly.getName().replaceAll('_', '-')
speciesSpecificParams = getExtraParams(schemaName)
"""
#!/bin/bash -euo pipefail
unzip ${schemaPath} -d schema > /dev/null
chmod -R 777 schema
mkdir input && cp ${assembly} input/
chewBBACA.py AlleleCall -i input -g schema -o results --cpu ${task.cpus} --force-continue --verbose ${speciesSpecificParams}
grep "${newAlleleKey}" schema/*.fasta -A1 -h | grep -v "\-\-" > ${base}_new_alleles.txt || echo "no INF alleles found"
mv results/*/results_alleles.tsv ${base}_results_alleles.tsv
mv results/*/results_contigsInfo.tsv ${base}_results_contigsInfo.tsv
mv results/*/results_statistics.tsv ${base}_results_statistics.tsv
"""
    """
}

process chewbbaca_check {
    container 'quay.io/biocontainers/python:3.9'
    
    input:
    
    path(chewbbacaStats)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    path('${base}_import_chewbbaca_check.csv'), emit: check
    
    
    script:
    """
md = parseMetadataFromFileName(chewbbacaStats.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
/scripts/chewieCheck.py --stat ${chewbbacaStats} > ${base}_import_chewbbaca_check.csv
"""
    """
}

process hashing {
    container 'ghcr.io/genpat-it/hashing:1.0--29180a232f'
    
    input:
    
    tuple path(chewbbaca_result), path(schema_path)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(chewbbaca_result.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
mask_matrix.py -i ${chewbbaca_result} -o masked_results.tsv
alleleprofile_hasher.py -p masked_results.tsv -d ${schema_path} -o ./_hashed_results.tsv
rm -Rf ${schema_path}/*
"""
    """
}

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

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_RM02_replace_mono_mlst_to_chewbbaca_lis_t1` — `file_not_found`
**Conversation:** `MOD_RM02_replace_mono_mlst_to_chewbbaca_lis` (replace) — turn 1
**Prompt:** Run mlst on a pre-existing Listeria monocytogenes assembly.

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

include { getInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.220.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM02_replace_mono_mlst_to_chewbbaca_lis_t2` — `silent_no_op`
**Conversation:** `MOD_RM02_replace_mono_mlst_to_chewbbaca_lis` (replace) — turn 2
**Prompt:** Use chewbbaca on that same assembly instead.

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

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { parseMetadataFromFileName } from '../functions/common.nf'

// --- GLOBALS ---

def SPECIES_SCHEMA = [listeria_monocytogenes : ['l_mono_chewie_1748_220623'], escherichia_coli : ['e_coli_chewie_2360_210531'], salmonella_enterica : ['s_enterica_chewie_3255_210531']]

def SCHEMAS = [l_mono_chewie_1748_220623 : '/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip', e_coli_chewie_2360_210531 : '/schemas/Escherichia_coli_INNUENDO_wgMLST_2021-05-31T14_24_05.304225.zip', s_enterica_chewie_3255_210531 : '/schemas/Salmonella_enterica_INNUENDO_cgMLST_2021-05-31T20_28_21.350919.zip']

def CHEWBBACA_SINGLE_END_PARAMS = [l_mono_chewie_1748_220623 : ' --minimum-length 144 --st 0.1 --bsr 0.6 ', e_coli_chewie_2360_210531 : ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', s_enterica_chewie_3255_210531 : ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt ']

def CHEWBBACA_PAIRED_END_PARAMS = [l_mono_chewie_1748_220623 : ' --minimum-length 144 ', e_coli_chewie_2360_210531 : ' --minimum-length 0 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', s_enterica_chewie_3255_210531 : ' --minimum-length 0 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt ']

// --- INLINE PROCESSES ---

process chewbbaca {
    container 'ghcr.io/genpat-it/chewbbaca-w-chewie-schemas:2.8.5--16b816c96d'
    
    input:
    
    tuple val(riscd_input), path(assembly)
    
    val genus_species
    
    val schema
    
    
    output:
    
    path '**'
    
    path('${base}_results_statistics.tsv'), emit: stats
    
    tuple path('${base}_results_alleles.tsv'), path('schema/'), emit: alleles
    
    tuple path('${base}_results_alleles.tsv'), path('${base}_new_alleles.txt'), val(schemaName), emit: alleles_with_new
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(assembly.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}_${METHOD}"
schemaName = getSchema(genus_species, schema)
schemaPath = SCHEMAS.get(schemaName)
newAlleleKey = assembly.getName().replaceAll('_', '-')
speciesSpecificParams = getExtraParams(schemaName)
"""
#!/bin/bash -euo pipefail
unzip ${schemaPath} -d schema > /dev/null
chmod -R 777 schema
mkdir input && cp ${assembly} input/
chewBBACA.py AlleleCall -i input -g schema -o results --cpu ${task.cpus} --force-continue --verbose ${speciesSpecificParams}
grep "${newAlleleKey}" schema/*.fasta -A1 -h | grep -v "\-\-" > ${base}_new_alleles.txt || echo "no INF alleles found"
mv results/*/results_alleles.tsv ${base}_results_alleles.tsv
mv results/*/results_contigsInfo.tsv ${base}_results_contigsInfo.tsv
mv results/*/results_statistics.tsv ${base}_results_statistics.tsv
"""
    """
}

process chewbbaca_check {
    container 'quay.io/biocontainers/python:3.9'
    
    input:
    
    path(chewbbacaStats)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    path('${base}_import_chewbbaca_check.csv'), emit: check
    
    
    script:
    """
md = parseMetadataFromFileName(chewbbacaStats.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
/scripts/chewieCheck.py --stat ${chewbbacaStats} > ${base}_import_chewbbaca_check.csv
"""
    """
}

process hashing {
    container 'ghcr.io/genpat-it/hashing:1.0--29180a232f'
    
    input:
    
    tuple path(chewbbaca_result), path(schema_path)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(chewbbaca_result.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
mask_matrix.py -i ${chewbbaca_result} -o masked_results.tsv
alleleprofile_hasher.py -p masked_results.tsv -d ${schema_path} -o ./_hashed_results.tsv
rm -Rf ${schema_path}/*
"""
    """
}

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

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_RM04_replace_mono_chewbbaca_to_mlst_sal_t1` — `file_not_found`
**Conversation:** `MOD_RM04_replace_mono_chewbbaca_to_mlst_sal` (replace) — turn 1
**Prompt:** Run chewbbaca on a pre-existing Salmonella enterica assembly.

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

include { getInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Salmonella enterica'

def schema = 'Salmonella enterica'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
    
    main:
        chewbbaca_result = chewbbaca(assembly, genus_species, schema)
        hashing(chewbbaca_result.alleles)
        chewbbaca_check(chewbbaca_result.stats).check
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.219.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM04_replace_mono_chewbbaca_to_mlst_sal_t2` — `file_not_found`
**Conversation:** `MOD_RM04_replace_mono_chewbbaca_to_mlst_sal` (replace) — turn 2
**Prompt:** Use mlst on that same assembly instead.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
        mlst_profile = mlst.out
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.219.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM05_replace_mono_chewbbaca_to_abricate_lis_t1` — `file_not_found`
**Conversation:** `MOD_RM05_replace_mono_chewbbaca_to_abricate_lis` (replace) — turn 1
**Prompt:** Run chewbbaca on a pre-existing Listeria monocytogenes assembly.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Listeria monocytogenes'

def schema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
    
    main:
        chewbbaca_result = chewbbaca(assembly, genus_species, schema)
        chewbbaca_check(chewbbaca_result.stats).check
        hashing(chewbbaca_result.alleles)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.222.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM05_replace_mono_chewbbaca_to_abricate_lis_t2` — `file_not_found`
**Conversation:** `MOD_RM05_replace_mono_chewbbaca_to_abricate_lis` (replace) — turn 2
**Prompt:** Use abricate on that same assembly instead.

**Steps (LLM):** `step_4AN_AMR__abricate`
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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_AMR__abricate {
    
    take:
        
        assembly
        
    
    main:
        abricate(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4AN_AMR__abricate(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.222.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM06_replace_mono_abricate_to_prokka_eco_t1` — `file_not_found`
**Conversation:** `MOD_RM06_replace_mono_abricate_to_prokka_eco` (replace) — turn 1
**Prompt:** Run abricate on a pre-existing Escherichia coli assembly.

**Steps (LLM):** `(none)`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus = 'Escherichia'

def species = 'coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_abricate {
    
    take:
        
        assembly
        
    
    main:
        abricate(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_abricate(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.214.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM06_replace_mono_abricate_to_prokka_eco_t2` — `file_not_found`
**Conversation:** `MOD_RM06_replace_mono_abricate_to_prokka_eco` (replace) — turn 2
**Prompt:** Use prokka on that same assembly instead.

**Steps (LLM):** `step_4AN_genes__prokka`
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

include { getAssembly } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_genes__prokka {
    
    take:
        
        assembly
        
    
    main:
        assembly.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] }.set { prokkaIn }
        prokka(prokkaIn)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4AN_genes__prokka(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.214.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM07_replace_mono_abricate_to_mlst_sal_t1` — `silent_no_op`
**Conversation:** `MOD_RM07_replace_mono_abricate_to_mlst_sal` (replace) — turn 1
**Prompt:** Run abricate on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_4AN_AMR__abricate`
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

include { getInput } from '../functions/parameters.nf'

include { parseMetadataFromFileName } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

process abricate {
    container 'staphb/abricate:1.0.0'
    
    input:
    
    tuple val(riscd_input), path(assembly)
    
    
    output:
    
    path '*'
    
    path '*.sh', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(assembly.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
  abricate --db vfdb --csv ${assembly} > abricate.csv
  abricate ${assembly} -db vfdb &>> ${base}_abricate.log >> ${base}_abricate_calls.txt
  abricate --summary ${base}_abricate_calls.txt > ${base}_abricate.summary
"""
    """
}

// --- SUB WORKFLOWS ---

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4AN_AMR__abricate(getInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_RM07_replace_mono_abricate_to_mlst_sal_t2` — `file_not_found`
**Conversation:** `MOD_RM07_replace_mono_abricate_to_mlst_sal` (replace) — turn 2
**Prompt:** Use mlst on that same assembly instead.

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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.220.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM08_replace_mono_flaA_to_staramr_cam_t1` — `file_not_found`
**Conversation:** `MOD_RM08_replace_mono_flaA_to_staramr_cam` (replace) — turn 1
**Prompt:** Run flaA on a pre-existing Campylobacter jejuni assembly.

**Steps (LLM):** `step_4TY_flaA__flaA`
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

include { getAssembly; getGenusSpecies } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_flaA__flaA {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        mlst_flaa(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_flaA__flaA(getAssembly(), getGenusSpecies())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.216.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM08_replace_mono_flaA_to_staramr_cam_t2` — `no_code`
**Conversation:** `MOD_RM08_replace_mono_flaA_to_staramr_cam` (replace) — turn 2
**Prompt:** Use staramr on that same assembly instead.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `MOD_RM09_replace_mono_staramr_to_flaA_cam_t1` — `file_not_found`
**Conversation:** `MOD_RM09_replace_mono_staramr_to_flaA_cam` (replace) — turn 1
**Prompt:** Run staramr on a pre-existing Campylobacter jejuni assembly.

**Steps (LLM):** `step_4AN_AMR__staramr`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genusSpecies = 'Campylobacter_jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_AMR__staramr {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        staramr(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4AN_AMR__staramr(getSingleInput(), genusSpecies)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.217.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM09_replace_mono_staramr_to_flaA_cam_t2` — `file_not_found`
**Conversation:** `MOD_RM09_replace_mono_staramr_to_flaA_cam` (replace) — turn 2
**Prompt:** Use flaA on that same assembly instead.

**Steps (LLM):** `step_4TY_flaA__flaA`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genusSpecies = 'Campylobacter jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_flaA__flaA {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        mlst_flaa(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_flaA__flaA(getSingleInput(), genusSpecies)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.217.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM10_replace_mono_staramr_to_mlst_cam_t1` — `file_not_found`
**Conversation:** `MOD_RM10_replace_mono_staramr_to_mlst_cam` (replace) — turn 1
**Prompt:** Run staramr on a pre-existing Campylobacter jejuni assembly.

**Steps (LLM):** `step_4AN_AMR__staramr`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def GENUS_SPECIES = 'campylobacter_jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_AMR__staramr {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        staramr(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4AN_AMR__staramr(getSingleInput(), GENUS_SPECIES)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.218.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_RM10_replace_mono_staramr_to_mlst_cam_t2` — `file_not_found`
**Conversation:** `MOD_RM10_replace_mono_staramr_to_mlst_cam` (replace) — turn 2
**Prompt:** Use mlst on that same assembly instead.

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

include { getInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst_out = mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    assembly = getInput()
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.218.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_D01_drop_chewbbaca_keep_mlst_lis_t1` — `file_not_found`
**Conversation:** `MOD_D01_drop_chewbbaca_keep_mlst_lis` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca, step_4TY_MLST__mlst`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_assemble_typing {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__spades(trimmed).assembled
        species = step_3TX_species__kmerfinder(assembled).assigned_species
        step_4TY_cgMLST__chewbbaca(assembled, species[1], species[2])
        step_4TY_MLST__mlst(assembled)
    
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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_3TX_species__kmerfinder {
    
    take:
        
        data
        
    
    main:
        kmerfinder(data)
        assigned_species = kmerfinder.out.check.map { [ it[0], getCalculatedSpecies(it[1]), getBacterialReferencePath(it[1]) ] }
    
    emit:
        
        assigned_species
        
    
}

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
    wf_trim_assemble_typing(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.223.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_D01_drop_chewbbaca_keep_mlst_lis_t2` — `file_not_found`
**Conversation:** `MOD_D01_drop_chewbbaca_keep_mlst_lis` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_3TX_species__kmerfinder {
    
    take:
        
        data
        
    
    main:
        kmerfinder(data)
        assigned_species = kmerfinder.out.check.map { [ it[0], getCalculatedSpecies(it[1]), getBacterialReferencePath(it[1]) ] }
    
    emit:
        
        assigned_species
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    species = step_3TX_species__kmerfinder(assembly)
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.223.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_D02_drop_chewbbaca_keep_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_D02_drop_chewbbaca_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both chewbbaca and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__unicycler, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca, step_4TY_MLST__mlst, step_1PP_trimming__fastp`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def genus_species = 'Salmonella enterica'

def schema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_cgmlst_mlst {
    
    take:
        
        trimmed
        
    
    main:
        assembled = step_2AS_denovo__unicycler(trimmed).assembled
        species_out = step_3TX_species__kmerfinder(assembled).assigned_species
        step_4TY_cgMLST__chewbbaca(assembled, genus_species, schema)
        step_4TY_MLST__mlst(assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_cgmlst_mlst(step_1PP_trimming__fastp(getSingleInput()).trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D02_drop_chewbbaca_keep_mlst_sal_t2` — `missing_param`
**Conversation:** `MOD_D02_drop_chewbbaca_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

**Steps (LLM):** `step_2AS_denovo__unicycler, step_3TX_species__kmerfinder, step_4TY_MLST__mlst, step_1PP_trimming__fastp`
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

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_mlst {
    
    take:
        
        trimmed
        
    
    main:
        unicycler_out = step_2AS_denovo__unicycler(trimmed)

        kmerfinder_out = step_3TX_species__kmerfinder(unicycler_out.assembled)

        step_4TY_MLST__mlst(kmerfinder_out.assigned_species)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())

    wf_salmonella_mlst(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

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

### `MOD_D03_drop_chewbbaca_keep_mlst_eco_t2` — `missing_param`
**Conversation:** `MOD_D03_drop_chewbbaca_keep_mlst_eco` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

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

### `MOD_D04_drop_mlst_keep_chewbbaca_lis_t2` — `file_not_found`
**Conversation:** `MOD_D04_drop_mlst_keep_chewbbaca_lis` (drop) — turn 2
**Prompt:** Drop mlst, keep only chewbbaca.

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

// --- GLOBALS ---

def genus_species = 'Listeria monocytogenes'

def schema = 'listeria_monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

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

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    step_4TY_cgMLST__chewbbaca(assembly, genus_species, schema)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.224.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_D05_drop_mlst_keep_chewbbaca_sal_t1` — `file_not_found`
**Conversation:** `MOD_D05_drop_mlst_keep_chewbbaca_sal` (drop) — turn 1
**Prompt:** Run both mlst and chewbbaca on Salmonella enterica from paired Illumina FASTQ.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def SPECIES_SCHEMA = ['s_enterica_chewie_3255_210531']

def SCHEMAS = ['/schemas/Salmonella_enterica_INNUENDO_cgMLST_2021-05-31T20_28_21.350919.zip']

def CHEWBBACA_PAIRED_END_PARAMS = ['--minimum-length 0 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt']

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

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

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    step_4TY_MLST__mlst(assembly)
    step_4TY_cgMLST__chewbbaca(assembly, 'salmonella_enterica', 's_enterica_chewie_3255_210531')
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.222.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_D05_drop_mlst_keep_chewbbaca_sal_t2` — `file_not_found`
**Conversation:** `MOD_D05_drop_mlst_keep_chewbbaca_sal` (drop) — turn 2
**Prompt:** Drop mlst, keep only chewbbaca.

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Salmonella enterica'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__spades(trimmed).assembled
    
    emit:
        
        trimmed
        
        assembled
        
    
}

workflow wf_cgmlst {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        step_4TY_cgMLST__chewbbaca(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    wf_trim_and_assemble(rawreads)
    wf_cgmlst(wf_trim_and_assemble.assembled, genus_species)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.222.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_D06_drop_abricate_keep_mlst_lis_t1` — `missing_param`
**Conversation:** `MOD_D06_drop_abricate_keep_mlst_lis` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4AN_AMR__abricate, step_4TY_MLST__mlst, step_1PP_trimming__fastp`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_amr_mlst {
    
    take:
        
        trimmed
        
    
    main:
        assembly = step_2AS_denovo__spades(trimmed).assembled
        species = step_3TX_species__kmerfinder(assembly).assigned_species
        step_4AN_AMR__abricate(assembly)
        step_4TY_MLST__mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_listeria_amr_mlst(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D06_drop_abricate_keep_mlst_lis_t2` — `file_not_found`
**Conversation:** `MOD_D06_drop_abricate_keep_mlst_lis` (drop) — turn 2
**Prompt:** Drop abricate, keep only mlst.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_3TX_species__kmerfinder {
    
    take:
        
        data
        
    
    main:
        kmerfinder(data)
        assigned_species = kmerfinder.out.check.map { [ it[0], getCalculatedSpecies(it[1]), getBacterialReferencePath(it[1]) ] }
    
    emit:
        
        assigned_species
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    step_3TX_species__kmerfinder(assembly)
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.225.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_D07_drop_abricate_keep_mlst_eco_t1` — `missing_param`
**Conversation:** `MOD_D07_drop_abricate_keep_mlst_eco` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Escherichia coli from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_4AN_AMR__abricate, step_4TY_MLST__mlst`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_analyze {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        trimmed.cross(trimmed) { extractKey(it) }.multiMap {
          trimmed: it[0]
          reference: it[1]
        }.set { trAndRef }

        assigned_species = step_3TX_species__kmerfinder(trAndRef.trimmed).assigned_species
        step_4AN_AMR__abricate(trAndRef.trimmed)
        step_4TY_MLST__mlst(trAndRef.trimmed)
    
    emit:
        
        trimmed
        
        assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_and_analyze(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D07_drop_abricate_keep_mlst_eco_t2` — `missing_param`
**Conversation:** `MOD_D07_drop_abricate_keep_mlst_eco` (drop) — turn 2
**Prompt:** Drop abricate, keep only mlst.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4TY_MLST__mlst, step_1PP_trimming__fastp`
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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_mlst {
    
    take:
        
        trimmed
        
    
    main:
        step_3TX_species__kmerfinder(trimmed)
        step_4TY_MLST__mlst(trimmed)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_ecoli_mlst(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D08_drop_abricate_keep_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_D08_drop_abricate_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both abricate and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

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

### `MOD_D08_drop_abricate_keep_mlst_sal_t2` — `missing_param`
**Conversation:** `MOD_D08_drop_abricate_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop abricate, keep only mlst.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4TY_MLST__mlst, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

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
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    module_typing_bacteria(trimmed, assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D09_drop_prokka_keep_mlst_sal_t1` — `partial_dag`
**Conversation:** `MOD_D09_drop_prokka_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both prokka and mlst on Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_4AN_genes__prokka, step_4TY_MLST__mlst`
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

include { getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_prokka_and_mlst {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] })
        step_4TY_MLST__mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_prokka_and_mlst(getSingleInput())
}
```
**Error excerpt:**
```
Only 2/8 expected processes appeared in the DAG
```

### `MOD_D09_drop_prokka_keep_mlst_sal_t2` — `file_not_found`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.224.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_D10_drop_prokka_keep_abricate_lis_t1` — `arity_error`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_assembly_and_annotation {
    
    take:
        
        reads
        
    
    main:
        spades_out = step_2AS_denovo__spades(reads)

        spades_out.assembled.multiMap {
            assembly: it
            kingdom: 'Bacteria'
            riscd_ref: '-'
            reference: getEmpty()
        }.set { prokka_in }

        step_4AN_genes__prokka(prokka_in)

        spades_out.assembled.multiMap {
            assembly: it
        }.set { abricate_in }

        step_4AN_AMR__abricate(abricate_in)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_assembly_and_annotation(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_assembly_and_annotation:step_4AN_genes__prokka` declares 1 input channels but 4 were given
```

### `MOD_D10_drop_prokka_keep_abricate_lis_t2` — `file_not_found`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_2AS_denovo__spades {
    
    take:
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    reads = getSingleInput()
    spades_out = step_2AS_denovo__spades(reads)
    step_4AN_AMR__abricate(spades_out.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.226.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

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

### `MOD_D11_drop_flaA_keep_mlst_cam_t2` — `missing_param`
**Conversation:** `MOD_D11_drop_flaA_keep_mlst_cam` (drop) — turn 2
**Prompt:** Drop flaA, keep only mlst.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { getInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast

        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getInput()).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    module_typing_bacteria(trimmed, assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_D12_drop_staramr_keep_mlst_cam_t1` — `missing_param`
**Conversation:** `MOD_D12_drop_staramr_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both staramr and mlst on Campylobacter jejuni from paired Illumina FASTQ.

**Steps (LLM):** `step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder`
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

include { extractKey } from '../functions/common.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def GENUS_SPECIES = 'Campylobacter jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_amr_mlst {
    
    take:
        
        assembly
        
        assigned_species
        
    
    main:
        assembly.cross(assigned_species) { extractKey(it) }.multiMap {
            assembly: it[0]
            genus_species: it[1][1]
        }.set { amr_mlst_input }

        step_4AN_AMR__staramr(amr_mlst_input.assembly, amr_mlst_input.genus_species)
        step_4TY_MLST__mlst(amr_mlst_input.assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species
    wf_amr_mlst(assembly, assigned_species)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_DA01_drop_assembly_lis_t1` — `no_code`
**Conversation:** `MOD_DA01_drop_assembly_lis` (drop) — turn 1
**Prompt:** Trim + assemble Listeria monocytogenes from paired Illumina FASTQ (fastp + SPAdes).

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
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_DA02_drop_assembly_eco_t1` — `no_code`
**Conversation:** `MOD_DA02_drop_assembly_eco` (drop) — turn 1
**Prompt:** Trim + assemble Escherichia coli from paired Illumina FASTQ (fastp + SPAdes).

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
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_DA03_drop_assembly_sal_t1` — `file_not_found`
**Conversation:** `MOD_DA03_drop_assembly_sal` (drop) — turn 1
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.225.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_DA03_drop_assembly_sal_t2` — `silent_no_op`
**Conversation:** `MOD_DA03_drop_assembly_sal` (drop) — turn 2
**Prompt:** Drop the assembly step and just trim the reads.

**Steps (LLM):** `step_1PP_trimming__fastp`
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

include { extractKey; getRisCd; parseMetadataFromFileName } from '../functions/common.nf'

include { getInput; isIlluminaPaired; isIonTorrent } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

process fastp {
    container 'ghcr.io/genpat-it/fastp:0.23.1--e4ac3df4c5'
    
    input:
    
    tuple val(riscd_input), path(reads)
    
    
    output:
    
    path '*'
    
    tuple val(riscd), path('*.fastq.gz'), emit: trimmed
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
(r1,r2) = (reads instanceof java.util.Collection) ? reads : [reads, null]
md = parseMetadataFromFileName(r1.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}_${METHOD}"
riscd = getRisCd(md, ex, STEP, METHOD)
if (isIlluminaPaired(reads)) {
  """
    fastp --in1 ${r1} --out1 ${base}_R1.fastq.gz --in2 ${r2} --out2 ${base}_R2.fastq.gz \
    --unpaired1 ${base}_unpaired.fastq.gz --unpaired2 ${base}_unpaired.fastq.gz \
    --json ${base}_summary.json --html ${base}_summary.html --thread 8
  """
} else if (isIonTorrent(reads)) {
  """
    fastp --in1 ${r1} --out1 ${base}_R1.fastq.gz  \
    --json ${base}_summary.json --html ${base}_summary.html --thread 8
  """
}
    """
}

// --- SUB WORKFLOWS ---

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

// --- ENTRYPOINT ---
workflow {
    step_1PP_trimming__fastp(getInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_DA04_drop_assembly_cam_t1` — `no_code`
**Conversation:** `MOD_DA04_drop_assembly_cam` (drop) — turn 1
**Prompt:** Trim + assemble Campylobacter jejuni from paired Illumina FASTQ (fastp + SPAdes).

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
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_DM01_drop_mono_chewbbaca_keep_mlst_lis_t2` — `file_not_found`
**Conversation:** `MOD_DM01_drop_mono_chewbbaca_keep_mlst_lis` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.228.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM02_drop_mono_chewbbaca_keep_mlst_sal_t2` — `file_not_found`
**Conversation:** `MOD_DM02_drop_mono_chewbbaca_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop chewbbaca, keep only mlst.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.226.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM03_drop_mono_mlst_keep_chewbbaca_lis_t1` — `file_not_found`
**Conversation:** `MOD_DM03_drop_mono_mlst_keep_chewbbaca_lis` (drop) — turn 1
**Prompt:** Run both mlst and chewbbaca on a pre-existing Listeria monocytogenes assembly.

**Steps (LLM):** `step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Listeria monocytogenes'

def schema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_typing {
    
    take:
        
        assembly
        
    
    main:
        step_4TY_MLST__mlst(assembly)
        step_4TY_cgMLST__chewbbaca(assembly, genus_species, schema)
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

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

// --- ENTRYPOINT ---
workflow {
    wf_listeria_typing(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.229.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM03_drop_mono_mlst_keep_chewbbaca_lis_t2` — `silent_no_op`
**Conversation:** `MOD_DM03_drop_mono_mlst_keep_chewbbaca_lis` (drop) — turn 2
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

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'

// --- GLOBALS ---

def SPECIES_SCHEMA = [listeria_monocytogenes: ['l_mono_chewie_1748_220623'], escherichia_coli: ['e_coli_chewie_2360_210531'], salmonella_enterica: ['s_enterica_chewie_3255_210531']]

def SCHEMAS = [l_mono_chewie_1748_220623: '/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip', e_coli_chewie_2360_210531: '/schemas/Escherichia_coli_INNUENDO_wgMLST_2021-05-31T14_24_05.304225.zip', s_enterica_chewie_3255_210531: '/schemas/Salmonella_enterica_INNUENDO_cgMLST_2021-05-31T20_28_21.350919.zip']

def CHEWBBACA_SINGLE_END_PARAMS = [l_mono_chewie_1748_220623: ' --minimum-length 144 --st 0.1 --bsr 0.6 ', e_coli_chewie_2360_210531: ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', s_enterica_chewie_3255_210531: ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt ']

def CHEWBBACA_PAIRED_END_PARAMS = [l_mono_chewie_1748_220623: ' --minimum-length 144 ', e_coli_chewie_2360_210531: ' --minimum-length 0 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', s_enterica_chewie_3255_210531: ' --minimum-length 0 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt ']

// --- INLINE PROCESSES ---

process chewbbaca {
    container 'ghcr.io/genpat-it/chewbbaca-w-chewie-schemas:2.8.5--16b816c96d'
    
    input:
    
    tuple val(riscd_input), path(assembly)
    
    val genus_species
    
    val schema
    
    
    output:
    
    path '**'
    
    path('${base}_results_statistics.tsv'), emit: stats
    
    tuple path('${base}_results_alleles.tsv'), path('schema/'), emit: alleles
    
    tuple path('${base}_results_alleles.tsv'), path('${base}_new_alleles.txt'), val(schemaName), emit: alleles_with_new
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
#!/bin/bash -euo pipefail
unzip ${schemaPath} -d schema > /dev/null
chmod -R 777 schema
mkdir input && cp ${assembly} input/
chewBBACA.py AlleleCall -i input -g schema -o results --cpu ${task.cpus} --force-continue --verbose ${speciesSpecificParams}
grep "${newAlleleKey}" schema/*.fasta -A1 -h | grep -v "\-\-" > ${base}_new_alleles.txt || echo "no INF alleles found"
mv results/*/results_alleles.tsv ${base}_results_alleles.tsv
mv results/*/results_contigsInfo.tsv ${base}_results_contigsInfo.tsv
mv results/*/results_statistics.tsv ${base}_results_statistics.tsv
    """
}

process chewbbaca_check {
    container 'quay.io/biocontainers/python:3.9'
    
    input:
    
    path(chewbbacaStats)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    path('${base}_import_chewbbaca_check.csv'), emit: check
    
    
    script:
    """
/scripts/chewieCheck.py --stat ${chewbbacaStats} > ${base}_import_chewbbaca_check.csv
    """
}

process hashing {
    container 'ghcr.io/genpat-it/hashing:1.0--29180a232f'
    
    input:
    
    tuple path(chewbbaca_result), path(schema_path)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
mask_matrix.py -i ${chewbbaca_result} -o masked_results.tsv
alleleprofile_hasher.py -p masked_results.tsv -d ${schema_path} -o ./_hashed_results.tsv
rm -Rf ${schema_path}/*
    """
}

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

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco_t1` — `file_not_found`
**Conversation:** `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco` (drop) — turn 1
**Prompt:** Run both mlst and chewbbaca on a pre-existing Escherichia coli assembly.

**Steps (LLM):** `step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Escherichia coli'

def schema = 'e_coli_chewie_2360_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly).view { mlst_out }
    
}

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
    
    main:
        chewbbaca(assembly, genus_species, schema).view { chewbbaca_out }
    
}

// --- ENTRYPOINT ---
workflow {
    assembly = getAssembly()
    step_4TY_MLST__mlst(assembly)
    step_4TY_cgMLST__chewbbaca(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.218.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM04_drop_mono_mlst_keep_chewbbaca_eco_t2` — `silent_no_op`
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

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'

// --- GLOBALS ---

def SPECIES_SCHEMA = {'listeria_monocytogenes': ['l_mono_chewie_1748_220623'], 'escherichia_coli': ['e_coli_chewie_2360_210531'], 'salmonella_enterica': ['s_enterica_chewie_3255_210531']}

def SCHEMAS = {'l_mono_chewie_1748_220623': '/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip', 'e_coli_chewie_2360_210531': '/schemas/Escherichia_coli_INNUENDO_wgMLST_2021-05-31T14_24_05.304225.zip', 's_enterica_chewie_3255_210531': '/schemas/Salmonella_enterica_INNUENDO_cgMLST_2021-05-31T20_28_21.350919.zip'}

def CHEWBBACA_SINGLE_END_PARAMS = {'l_mono_chewie_1748_220623': ' --minimum-length 144 --st 0.1 --bsr 0.6 ', 'e_coli_chewie_2360_210531': ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', 's_enterica_chewie_3255_210531': ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt '}

def CHEWBBACA_PAIRED_END_PARAMS = {'l_mono_chewie_1748_220623': ' --minimum-length 144 ', 'e_coli_chewie_2360_210531': ' --minimum-length 0 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', 's_enterica_chewie_3255_210531': ' --minimum-length 0 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt '}

// --- INLINE PROCESSES ---

process chewbbaca {
    container 'ghcr.io/genpat-it/chewbbaca-w-chewie-schemas:2.8.5--16b816c96d'
    
    input:
    
    tuple val(riscd_input), path(assembly)
    
    val genus_species
    
    val schema
    
    
    output:
    
    path '**'
    
    path('${base}_results_statistics.tsv'), emit: stats
    
    tuple path('${base}_results_alleles.tsv'), path('schema/'), emit: alleles
    
    tuple path('${base}_results_alleles.tsv'), path('${base}_new_alleles.txt'), val(schemaName), emit: alleles_with_new
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
#!/bin/bash -euo pipefail
        unzip ${schemaPath} -d schema > /dev/null
        chmod -R 777 schema
        mkdir input && cp ${assembly} input/
        chewBBACA.py AlleleCall -i input -g schema -o results --cpu ${task.cpus} --force-continue --verbose ${speciesSpecificParams}
        grep "${newAlleleKey}" schema/*.fasta -A1 -h | grep -v "\-\-" > ${base}_new_alleles.txt || echo "no INF alleles found"
        mv results/*/results_alleles.tsv ${base}_results_alleles.tsv
        mv results/*/results_contigsInfo.tsv ${base}_results_contigsInfo.tsv
        mv results/*/results_statistics.tsv ${base}_results_statistics.tsv
    """
}

process chewbbaca_check {
    container 'quay.io/biocontainers/python:3.9'
    
    input:
    
    path(chewbbacaStats)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    path('${base}_import_chewbbaca_check.csv'), emit: check
    
    
    script:
    """
/scripts/chewieCheck.py --stat ${chewbbacaStats} > ${base}_import_chewbbaca_check.csv
    """
}

process hashing {
    container 'ghcr.io/genpat-it/hashing:1.0--29180a232f'
    
    input:
    
    tuple path(chewbbaca_result), path(schema_path)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
mask_matrix.py -i ${chewbbaca_result} -o masked_results.tsv
        alleleprofile_hasher.py -p masked_results.tsv -d ${schema_path} -o ./_hashed_results.tsv
        rm -Rf ${schema_path}/*
    """
}

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

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_DM05_drop_mono_abricate_keep_mlst_sal_t1` — `missing_param`
**Conversation:** `MOD_DM05_drop_mono_abricate_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both abricate and mlst on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_4AN_AMR__abricate, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    asm = getInput()
    step_4AN_AMR__abricate(asm)
    step_4TY_MLST__mlst(asm)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

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

### `MOD_DM05_drop_mono_abricate_keep_mlst_sal_t2` — `file_not_found`
**Conversation:** `MOD_DM05_drop_mono_abricate_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop abricate, keep only mlst.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.227.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM06_drop_mono_prokka_keep_mlst_lis_t1` — `file_not_found`
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

include { getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_analysis {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] })
        step_4TY_MLST__mlst(prokka_out)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_listeria_analysis(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.230.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM07_drop_mono_staramr_keep_mlst_cam_t1` — `file_not_found`
**Conversation:** `MOD_DM07_drop_mono_staramr_keep_mlst_cam` (drop) — turn 1
**Prompt:** Run both staramr and mlst on a pre-existing Campylobacter jejuni assembly.

**Steps (LLM):** `step_4AN_AMR__staramr, step_4TY_MLST__mlst`
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

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_analysis {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_AMR__staramr(assembly, 'Campylobacter jejuni')
        step_4TY_MLST__mlst(staramr_out)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_campylobacter_analysis(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.222.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM07_drop_mono_staramr_keep_mlst_cam_t2` — `arity_error`
**Conversation:** `MOD_DM07_drop_mono_staramr_keep_mlst_cam` (drop) — turn 2
**Prompt:** Drop staramr, keep only mlst.

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

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

def genusSpecies = 'Campylobacter jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_mlst_typing {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap {
            assembly: it
            genus_species: genusSpecies
        }.set { mlst_input }

        step_4TY_MLST__mlst(mlst_input.assembly, mlst_input.genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    assembly = getSingleInput()
    wf_mlst_typing(assembly)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_mlst_typing:step_4TY_MLST__mlst` declares 1 input channels but 2 were given
```

### `MOD_DM08_drop_mono_staramr_keep_flaA_cam_t2` — `file_not_found`
**Conversation:** `MOD_DM08_drop_mono_staramr_keep_flaA_cam` (drop) — turn 2
**Prompt:** Drop staramr, keep only flaA.

**Steps (LLM):** `step_4TY_flaA__flaA`
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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

def genusSpecies = 'campylobacter'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_flaA__flaA {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        mlst_flaa(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_flaA__flaA(getAssembly(), genusSpecies)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.223.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM09_drop_mono_flaA_keep_staramr_cam_t1` — `missing_param`
**Conversation:** `MOD_DM09_drop_mono_flaA_keep_staramr_cam` (drop) — turn 1
**Prompt:** Run both flaA and staramr on a pre-existing Campylobacter jejuni assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

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

### `MOD_DM09_drop_mono_flaA_keep_staramr_cam_t2` — `missing_param`
**Conversation:** `MOD_DM09_drop_mono_flaA_keep_staramr_cam` (drop) — turn 2
**Prompt:** Drop flaA, keep only staramr.

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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { extractKey } from '../functions/common.nf'

include { getAssembly } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

// --- GLOBALS ---

def KMERFINDER_SPECIES_DIR = '${params.step_3TX_species__kmerfinder__db}'

def KMERFINDER_REFERENCE_DIR = '${KMERFINDER_SPECIES_DIR}/Bacteria/Fasta/'

def GENUS_ALLOWED = ['campylobacter']

def POINFINDER_ORGANISM = {campylobacter: 'campylobacter'}

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

        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
    
    emit:
        
        genus_species = assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_DM10_drop_mono_flaA_keep_mlst_cam_t2` — `file_not_found`
**Conversation:** `MOD_DM10_drop_mono_flaA_keep_mlst_cam` (drop) — turn 2
**Prompt:** Drop flaA, keep only mlst.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.225.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM11_drop_mono_abricate_keep_prokka_eco_t2` — `file_not_found`
**Conversation:** `MOD_DM11_drop_mono_abricate_keep_prokka_eco` (drop) — turn 2
**Prompt:** Drop abricate, keep only prokka.

**Steps (LLM):** `step_4AN_genes__prokka`
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

include { getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_genes__prokka {
    
    take:
        
        assembly
        
    
    main:
        assembly.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] }.set { prokkaIn }
        prokka(prokkaIn)
    
}

// --- ENTRYPOINT ---
workflow {
    assembly = getSingleInput()
    step_4AN_genes__prokka(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.219.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

def referenceCode = 'NC_045512.2'

def referencePath = "${params.assets_dir}/module_covid_emergency/NC_045512.fasta"

def referenceRiscd = '220308-020220308005121273-2AS_import-external'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_prokka_and_abricate {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap {
            assembly: it
            kingdom: 'Bacteria'
            riscd_ref: '-'
            reference: getEmpty()
        }.set { prokkaIn }

        step_4AN_genes__prokka(prokkaIn)
        step_4AN_AMR__abricate(prokkaIn)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_prokka_and_abricate(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_prokka_and_abricate:step_4AN_genes__prokka` declares 1 input channels but 4 were given
```

### `MOD_DM12_drop_mono_prokka_keep_abricate_lis_t2` — `file_not_found`
**Conversation:** `MOD_DM12_drop_mono_prokka_keep_abricate_lis` (drop) — turn 2
**Prompt:** Drop prokka, keep only abricate.

**Steps (LLM):** `step_4AN_AMR__abricate`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_AMR__abricate {
    
    take:
        
        assembly
        
    
    main:
        abricate(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4AN_AMR__abricate(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.231.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM13_drop_mono_prokka_keep_mlst_sal_t1` — `arity_error`
**Conversation:** `MOD_DM13_drop_mono_prokka_keep_mlst_sal` (drop) — turn 1
**Prompt:** Run both prokka and mlst on a pre-existing Salmonella enterica assembly.

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

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_analysis {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap {
            assembly: it
            kingdom: kingdom
        }.set { prokka_input }

        step_4AN_genes__prokka(prokka_input.assembly, prokka_input.kingdom)
        step_4TY_MLST__mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_analysis(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_salmonella_analysis:step_4AN_genes__prokka` declares 1 input channels but 2 were given
```

### `MOD_DM13_drop_mono_prokka_keep_mlst_sal_t2` — `file_not_found`
**Conversation:** `MOD_DM13_drop_mono_prokka_keep_mlst_sal` (drop) — turn 2
**Prompt:** Drop prokka, keep only mlst.

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

include { getInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.228.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_DM14_drop_mono_abricate_keep_prokka_sal_t1` — `arity_error`
**Conversation:** `MOD_DM14_drop_mono_abricate_keep_prokka_sal` (drop) — turn 1
**Prompt:** Run both abricate and prokka on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_4AN_AMR__abricate, step_4AN_genes__prokka`
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

include { getAssembly } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_amr_and_annotation {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap {
            assembly: it
            kingdom: kingdom
        }.set { prep }

        step_4AN_AMR__abricate(prep.assembly)
        step_4AN_genes__prokka(prep.assembly, prep.kingdom)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_amr_and_annotation(getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_amr_and_annotation:step_4AN_genes__prokka` declares 1 input channels but 2 were given
```

### `MOD_DM14_drop_mono_abricate_keep_prokka_sal_t2` — `file_not_found`
**Conversation:** `MOD_DM14_drop_mono_abricate_keep_prokka_sal` (drop) — turn 2
**Prompt:** Drop abricate, keep only prokka.

**Steps (LLM):** `step_4AN_genes__prokka`
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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_genes__prokka {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap {
            riscd: it[0]
            scaffolds200: it[1]
            kingdom: it[2]
            riscd_ref: it[3]
            reference: it[4]
            gb: it[5]
        }.set { prokka_input }

        prokka(prokka_input.riscd, prokka_input.scaffolds200, prokka_input.kingdom, prokka_input.riscd_ref, prokka_input.reference, prokka_input.gb)
    
}

// --- ENTRYPOINT ---
workflow {
    assembly = getAssembly()
    step_4AN_genes__prokka(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.229.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_S02_cgmlst_retarget_lis_to_eco_t2` — `file_not_found`
**Conversation:** `MOD_S02_cgmlst_retarget_lis_to_eco` (switch_species) — turn 2
**Prompt:** Apply the same pipeline to Escherichia coli.

**Steps (LLM):** `step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def genus_species = 'Escherichia coli'

def schema = 'e_coli_chewie_2360_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        trimmed.cross(assembly) { extractKey(it) }.multiMap {
          trimmed: it[0]
          assembly: it[1]
        }.set { trimAndAssembly }

        step_4AN_AMR__abricate(trimAndAssembly.assembly)

        step_4AN_genes__prokka(trimAndAssembly.assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

        trimAndAssembly.assembly.cross(genus_species) { extractKey(it) }.multiMap {
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, schema)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    module_typing_bacteria(trimmed, assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.220.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_S04_cgmlst_retarget_sal_to_eco_t2` — `silent_no_op`
**Conversation:** `MOD_S04_cgmlst_retarget_sal_to_eco` (switch_species) — turn 2
**Prompt:** Apply the same pipeline to Escherichia coli.

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { extractKey } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

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
        trimmed.cross(assembly) { extractKey(it) }.multiMap {
          trimmed: it[0]
          assembly: it[1]
        }.set { trimAndAssembly }

        step_4TY_cgMLST__chewbbaca(trimAndAssembly.assembly, trimAndAssembly.assembly)
    
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

### `MOD_S05_cgmlst_retarget_eco_to_lis_t1` — `file_not_found`
**Conversation:** `MOD_S05_cgmlst_retarget_eco_to_lis` (switch_species) — turn 1
**Prompt:** cgMLST pipeline for Escherichia coli from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_ecoli {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            genus_species: 'Escherichia coli'
            schema: params.schema
        }.set { prep }

        spades_out = step_2AS_denovo__spades(prep.trimmed)
        step_4TY_cgMLST__chewbbaca(spades_out.assembled, prep.genus_species, prep.schema)
    
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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast

        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

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

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed
    wf_cgmlst_ecoli(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.222.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_S05_cgmlst_retarget_eco_to_lis_t2` — `arity_error`
**Conversation:** `MOD_S05_cgmlst_retarget_eco_to_lis` (switch_species) — turn 2
**Prompt:** Apply the same pipeline to Listeria monocytogenes.

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trimming_assembly_cgmlst {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembly = step_2AS_denovo__spades(trimmed).assembled
        step_4TY_cgMLST__chewbbaca(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trimming_assembly_cgmlst(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_trimming_assembly_cgmlst:step_4TY_cgMLST__chewbbaca` declares 3 input channels but 2 were given
```

### `MOD_S06_cgmlst_retarget_eco_to_sal_t1` — `partial_dag`
**Conversation:** `MOD_S06_cgmlst_retarget_eco_to_sal` (switch_species) — turn 1
**Prompt:** cgMLST pipeline for Escherichia coli from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Escherichia coli'

def schema = 'e_coli_chewie_2360_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_pipeline {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            genus_species: genus_species
            schema: schema
        }.set { trAndRef }

        assembly = step_2AS_denovo__spades(trAndRef.trimmed)
        step_4TY_cgMLST__chewbbaca(assembly.assembled, trAndRef.genus_species, trAndRef.schema)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_cgmlst_pipeline(getSingleInput())
}
```
**Error excerpt:**
```
Only 6/9 expected processes appeared in the DAG
```

### `MOD_S06_cgmlst_retarget_eco_to_sal_t2` — `file_not_found`
**Conversation:** `MOD_S06_cgmlst_retarget_eco_to_sal` (switch_species) — turn 2
**Prompt:** Apply the same pipeline to Salmonella enterica.

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

// --- GLOBALS ---

def SPECIES_SCHEMA = ['e_coli_chewie_2360_210531', 's_enterica_chewie_3255_210531']

def SCHEMAS = ['/schemas/Escherichia_coli_INNUENDO_wgMLST_2021-05-31T14_24_05.304225.zip', '/schemas/Salmonella_enterica_INNUENDO_cgMLST_2021-05-31T20_28_21.350919.zip']

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

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

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    step_4TY_cgMLST__chewbbaca(assembly, 'Escherichia coli', 'e_coli_chewie_2360_210531')
    step_4TY_cgMLST__chewbbaca(assembly, 'Salmonella enterica', 's_enterica_chewie_3255_210531')
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.233.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_SM01_mlst_retarget_lis_to_cam_t1` — `file_not_found`
**Conversation:** `MOD_SM01_mlst_retarget_lis_to_cam` (switch_species) — turn 1
**Prompt:** MLST pipeline for Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__spades, step_1PP_trimming__fastp`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_mlst {
    
    take:
        
        trimmed
        
    
    main:
        assembly = step_2AS_denovo__spades(trimmed).assembled
        mlst(assembly)
        mlst_type = mlst.out
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_listeria_mlst(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.236.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_SM02_mlst_retarget_sal_to_cam_t2` — `file_not_found`
**Conversation:** `MOD_SM02_mlst_retarget_sal_to_cam` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Campylobacter jejuni.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.227.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_SM04_mlst_retarget_cam_to_lis_t2` — `file_not_found`
**Conversation:** `MOD_SM04_mlst_retarget_cam_to_lis` (switch_species) — turn 2
**Prompt:** Re-run the same pipeline on Listeria monocytogenes.

**Steps (LLM):** `step_2AS_denovo__unicycler, step_4TY_MLST__mlst, step_1PP_trimming__fastp`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_mlst {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
        }.set { trAndRef }

        assembly_out = step_2AS_denovo__unicycler(trAndRef.trimmed)
        step_4TY_MLST__mlst(assembly_out.assembled)
    
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

workflow step_2AS_denovo__unicycler {
    
    take:
        
        data
        
    
    main:
        unicycler(data).scaffolds
        assembly_filter(unicycler.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_listeria_mlst(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.237.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_SMA01_mlst_mono_retarget_lis_to_sal_t1` — `file_not_found`
**Conversation:** `MOD_SMA01_mlst_mono_retarget_lis_to_sal` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Listeria monocytogenes assembly.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.238.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA01_mlst_mono_retarget_lis_to_sal_t2` — `file_not_found`
**Conversation:** `MOD_SMA01_mlst_mono_retarget_lis_to_sal` (switch_species) — turn 2
**Prompt:** Same thing but for Salmonella enterica.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.236.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA02_mlst_mono_retarget_lis_to_eco_t1` — `file_not_found`
**Conversation:** `MOD_SMA02_mlst_mono_retarget_lis_to_eco` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Listeria monocytogenes assembly.

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

include { getInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
        mlst_results = mlst.out
    
}

// --- ENTRYPOINT ---
workflow {
    assembly = getInput()
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.239.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA02_mlst_mono_retarget_lis_to_eco_t2` — `file_not_found`
**Conversation:** `MOD_SMA02_mlst_mono_retarget_lis_to_eco` (switch_species) — turn 2
**Prompt:** Same thing but for Escherichia coli.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.226.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA03_mlst_mono_retarget_sal_to_lis_t1` — `file_not_found`
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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.237.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA03_mlst_mono_retarget_sal_to_lis_t2` — `file_not_found`
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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.240.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA04_mlst_mono_retarget_sal_to_eco_t1` — `file_not_found`
**Conversation:** `MOD_SMA04_mlst_mono_retarget_sal_to_eco` (switch_species) — turn 1
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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.238.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA04_mlst_mono_retarget_sal_to_eco_t2` — `file_not_found`
**Conversation:** `MOD_SMA04_mlst_mono_retarget_sal_to_eco` (switch_species) — turn 2
**Prompt:** Same thing but for Escherichia coli.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.227.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA05_mlst_mono_retarget_eco_to_lis_t1` — `file_not_found`
**Conversation:** `MOD_SMA05_mlst_mono_retarget_eco_to_lis` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Escherichia coli assembly.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.228.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA05_mlst_mono_retarget_eco_to_lis_t2` — `silent_no_op`
**Conversation:** `MOD_SMA05_mlst_mono_retarget_eco_to_lis` (switch_species) — turn 2
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

include { getAssembly } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap { it }.set { input }
        step_4TY_MLST__mlst(input)
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getAssembly())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_SMA06_mlst_mono_retarget_eco_to_sal_t1` — `file_not_found`
**Conversation:** `MOD_SMA06_mlst_mono_retarget_eco_to_sal` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Escherichia coli assembly.

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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.229.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA06_mlst_mono_retarget_eco_to_sal_t2` — `file_not_found`
**Conversation:** `MOD_SMA06_mlst_mono_retarget_eco_to_sal` (switch_species) — turn 2
**Prompt:** Same thing but for Salmonella enterica.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.239.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA07_mlst_mono_retarget_lis_to_cam_t1` — `file_not_found`
**Conversation:** `MOD_SMA07_mlst_mono_retarget_lis_to_cam` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Listeria monocytogenes assembly.

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

include { getInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.242.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA07_mlst_mono_retarget_lis_to_cam_t2` — `silent_no_op`
**Conversation:** `MOD_SMA07_mlst_mono_retarget_lis_to_cam` (switch_species) — turn 2
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { optionalOrDefault; param } from '../functions/parameters.nf'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    main:
        include { getVCFs;param;optionalOrDefault } from '../functions/parameters.nf'
        include { taskMemory;getEmpty } from '../functions/common.nf'

        if (getReportreeInputType() == 'alleles') {
          include { multi_clustering__reportree } from "../multi/multi_clustering__reportree_alleles"
          include { getAlleles as inputFn } from "../multi/multi_clustering__reportree_alleles"
        } else if (getReportreeInputType() == 'alignment') {
          include { multi_clustering__reportree } from "../multi/multi_clustering__reportree_alignment"
          include { getInput as inputFn } from '../functions/parameters.nf'
        } else {
          include { multi_clustering__reportree } from "../multi/multi_clustering__reportree_vcf"
          include { getVCFs as inputFn } from '../functions/parameters.nf'
        }

        def getReportreeInputType() {
            def res = param('multi_clustering__reportree__input')
            if (!(res in ['alleles', 'vcf', 'alignment'])) {
                exit 2, "params (multi_clustering__reportree__input) not valid"
            }
            return res
        }

        workflow {
            multi_clustering__reportree(inputFn(),  param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
        }
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance()
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_SMA08_mlst_mono_retarget_sal_to_cam_t1` — `file_not_found`
**Conversation:** `MOD_SMA08_mlst_mono_retarget_sal_to_cam` (switch_species) — turn 1
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

include { getInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst_out = mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.240.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA08_mlst_mono_retarget_sal_to_cam_t2` — `file_not_found`
**Conversation:** `MOD_SMA08_mlst_mono_retarget_sal_to_cam` (switch_species) — turn 2
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

include { getInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst_out = mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    assembly = getInput()
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.233.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA09_mlst_mono_retarget_eco_to_cam_t1` — `silent_no_op`
**Conversation:** `MOD_SMA09_mlst_mono_retarget_eco_to_cam` (switch_species) — turn 1
**Prompt:** MLST on a pre-existing Escherichia coli assembly.

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

include { optionalOrDefault; param } from '../functions/parameters.nf'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    main:
        if (getReportreeInputType() == 'alleles') {
          include { multi_clustering__reportree } from "../multi/multi_clustering__reportree_alleles"
          include { getAlleles as inputFn } from "../multi/multi_clustering__reportree_alleles"
        } else if (getReportreeInputType() == 'alignment') {
          include { multi_clustering__reportree } from "../multi/multi_clustering__reportree_alignment"
          include { getInput as inputFn } from '../functions/parameters.nf'
        } else {
          include { multi_clustering__reportree } from "../multi/multi_clustering__reportree_vcf"
          include { getVCFs as inputFn } from '../functions/parameters.nf'
        }

        def getReportreeInputType() {
            def res = param('multi_clustering__reportree__input')
            if (!(res in ['alleles', 'vcf', 'alignment'])) {
                exit 2, "params (multi_clustering__reportree__input) not valid"
            }
            return res
        }

        workflow {
            multi_clustering__reportree(inputFn(),  param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
        }
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance()
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_SMA09_mlst_mono_retarget_eco_to_cam_t2` — `file_not_found`
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

include { getInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.CAM.234.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `MOD_SMA10_mlst_mono_retarget_cam_to_lis_t2` — `no_code`
**Conversation:** `MOD_SMA10_mlst_mono_retarget_cam_to_lis` (switch_species) — turn 2
**Prompt:** Same thing but for Listeria monocytogenes.

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
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_3T01_addAdd_lis_t2` — `missing_param`
**Conversation:** `MOD_3T01_addAdd_lis` (add) — turn 2
**Prompt:** Now also run MLST on the assembly.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades, step_4TY_MLST__mlst`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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

        // [REMOVED BY PLAN] depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
        assembled = step_2AS_denovo__spades(denovoInput)

        step_4TY_MLST__mlst(assembled)
    
    emit:
        
        assembled
        
    
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

### `MOD_3T01_addAdd_lis_t3` — `file_not_found`
**Conversation:** `MOD_3T01_addAdd_lis` (add) — turn 3
**Prompt:** Also add cgMLST in parallel.

**Steps (LLM):** `step_2AS_denovo__spades, step_1PP_trimming__fastp, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Listeria monocytogenes'

def schema = 'default'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_denovo {
    
    take:
        
        trimmedReads
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmedReads)
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
    
    main:
        chewbbaca(assembly, genus_species, schema)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    module_denovo(trimmed)
    step_4TY_MLST__mlst(module_denovo.assembled)
    step_4TY_cgMLST__chewbbaca(module_denovo.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.244.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T02_addAdd_eco_t1` — `file_not_found`
**Conversation:** `MOD_3T02_addAdd_eco` (add) — turn 1
**Prompt:** From paired Illumina FASTQ of Escherichia coli: trim with fastp and assemble with SPAdes.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.231.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T03_addAdd_sal_t1` — `missing_param`
**Conversation:** `MOD_3T03_addAdd_sal` (add) — turn 1
**Prompt:** From paired Illumina FASTQ of Salmonella enterica: trim with fastp and assemble with SPAdes.

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

include { extractKey } from '../functions/common.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
ERROR ~ missing required param: hosts_dir
```

### `MOD_3T03_addAdd_sal_t2` — `missing_param`
**Conversation:** `MOD_3T03_addAdd_sal` (add) — turn 2
**Prompt:** Now also run MLST on the assembly.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_1PP_trimming__fastp`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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

        // [REMOVED BY PLAN] depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }
        assembled = step_2AS_denovo__spades(denovoInput)

        step_4TY_MLST__mlst(assembled)
    
    emit:
        
        assembled
        
    
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

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    module_denovo(trimmed, getHost())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: hosts_dir
```

### `MOD_3T_AD01_addThenDrop_lis_t1` — `partial_dag`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 1
**Prompt:** cgMLST profile for Listeria monocytogenes from paired Illumina FASTQ.

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_listeria {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        spades_out = step_2AS_denovo__spades(trAndRef.trimmed)
        step_4TY_cgMLST__chewbbaca(spades_out.assembled, 'Listeria monocytogenes', 'l_mono_chewie_1748_220623')
    
}

// --- ENTRYPOINT ---
workflow {
    wf_cgmlst_listeria(getSingleInput())
}
```
**Error excerpt:**
```
Only 6/9 expected processes appeared in the DAG
```

### `MOD_3T_AD01_addThenDrop_lis_t2` — `silent_no_op`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 2
**Prompt:** Also add ABRicate AMR screening in parallel.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
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

include { extractKey } from '../functions/common.nf'

include { getReference; getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_cgmlst_amr {
    
    take:
        
        trimmed
        
        abricateDb
        
        schema
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            abricateDb: abricateDb
            schema: schema
        }.set { prep }

        assembly = step_2AS_denovo__spades(prep.trimmed)
        step_4TY_cgMLST__chewbbaca(assembly.assembled, 'listeria_monocytogenes', schema)
        step_4AN_AMR__abricate(assembly.assembled)
    
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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

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

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    abricateDb = getReference('abricate')
    schema = getReference('schema')
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_listeria_cgmlst_amr(trimmed, abricateDb, schema)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_3T_AD01_addThenDrop_lis_t3` — `partial_dag`
**Conversation:** `MOD_3T_AD01_addThenDrop_lis` (add) — turn 3
**Prompt:** Actually, drop the ABRicate step.

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Listeria monocytogenes'

def schema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_pipeline {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            genus_species: genus_species
            schema: schema
        }.set { trAndRef }

        spades_out = step_2AS_denovo__spades(trAndRef.trimmed)
        step_4TY_cgMLST__chewbbaca(spades_out.assembled, genus_species, schema)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_cgmlst_pipeline(getSingleInput())
}
```
**Error excerpt:**
```
Only 6/9 expected processes appeared in the DAG
```

### `MOD_3T_AD02_addThenDrop_eco_t1` — `file_not_found`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 1
**Prompt:** cgMLST profile for Escherichia coli from paired Illumina FASTQ.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def referenceCode = 'Escherichia_coli'

def referencePath = "${params.assets_dir}/Escherichia_coli_reference.fasta"

def referenceRiscd = '220308-020220308005121273-2AS_import-external'

def schema = 'e_coli_chewie_2360_210531'

def genusSpecies = 'Escherichia_coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_pipeline {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        bowtie2(trAndRef.trimmed, trAndRef.reference)
        samtools(bowtie2.out.sam)
        consensus = seqio(samtools.out.fq).consensus

        chewbbaca(consensus, genusSpecies, schema)
    
}

workflow wf_trimming {
    
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

// --- ENTRYPOINT ---
workflow {
    trimmed = wf_trimming(getSingleInput()).trimmed
    wf_cgmlst_pipeline(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.232.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_AD02_addThenDrop_eco_t2` — `file_not_found`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 2
**Prompt:** Also add ABRicate AMR screening in parallel.

**Steps (LLM):** `step_2AS_mapping__bowtie, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
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

include { extractDsRef; extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def referenceCode = 'NC_045512.2'

def referencePath = "${params.assets_dir}/module_covid_emergency/NC_045512.fasta"

def referenceRiscd = '220308-020220308005121273-2AS_import-external'

def schema = 'e_coli_chewie_2360_210531'

def genus_species = 'escherichia_coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_amr {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        bowtie_out = step_2AS_mapping__bowtie(trAndRef.trimmed, trAndRef.reference)
        step_4TY_cgMLST__chewbbaca(bowtie_out.consensus, genus_species, schema)
        step_4AN_AMR__abricate(bowtie_out.consensus)
    
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

workflow step_2AS_mapping__bowtie {
    
    take:
        
        reads
        
        reference
        
    
    main:
        bowtie2(reads, reference)
        samtools(bowtie2.out.sam)
        consensus = seqio(samtools.out.fq).consensus

        coverage_minmax(samtools.out.bam, 'bowtie')
        coverage_minmax.out.coverage_depth | coverage_plot

        coverage = samtools_depth(samtools.out.bam, 'bowtie').coverage
        coverage.cross(consensus) { extractDsRef(it) }.map {
            return [ it[0][0], it[1][1], it[0][1] ]
        }.set { coverageRefAndConsensus }
        coverageBasic = coverage_check(coverageRefAndConsensus, 'bowtie').coverage_basic

        crossedChecks = coverage_minmax.out.coverage_extra.cross(coverageBasic) { it[0] + "-" + it[1] }
        .map { [ it[0][0], it[0][1], it[0][2], it[1][2] ] }
        coverage_check_group(coverage_check_merge(crossedChecks, 'bowtie').coverage_merged | groupTuple, 'bowtie')
    
    emit:
        
        consensus
        
    
}

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

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_cgmlst_amr(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.232.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_AD02_addThenDrop_eco_t3` — `file_not_found`
**Conversation:** `MOD_3T_AD02_addThenDrop_eco` (add) — turn 3
**Prompt:** Actually, drop the ABRicate step.

**Steps (LLM):** `step_2AS_mapping__bowtie, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp`
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

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def genus_species = 'Escherichia coli'

def schema = 'e_coli_chewie_2360_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_profiling {
    
    take:
        
        trimmed
        
        reference
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        consensus = step_2AS_mapping__bowtie(trAndRef.trimmed, trAndRef.reference).consensus
        step_4TY_cgMLST__chewbbaca(consensus, genus_species, schema)
    
}

workflow wf_trimming {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

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
    wf_trimming(getSingleInput()).trimmed.cross(getReference('fa')) { extractKey(it) }.multiMap {
        trimmed: it[0]
        reference: it[1][1..3]
    }.set { trAndRef }

    wf_cgmlst_profiling(trAndRef.trimmed, trAndRef.reference)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.232.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_AD03_addThenDrop_sal_t1` — `missing_param`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 1
**Prompt:** cgMLST profile for Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__unicycler, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp`
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

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def genus_species = 'Salmonella enterica'

def schema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_cgmlst {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        assembly = step_2AS_denovo__unicycler(trAndRef.trimmed)

        species_out = step_3TX_species__kmerfinder(assembly)

        step_4TY_cgMLST__chewbbaca(assembly, genus_species, schema)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_salmonella_cgmlst(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD03_addThenDrop_sal_t2` — `missing_param`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 2
**Prompt:** Also add ABRicate AMR screening in parallel.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def genus_species = 'Salmonella enterica'

def schema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_preprocess_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__unicycler(trimmed).assembled
    
    emit:
        
        trimmed
        
        assembled
        
    
}

workflow wf_species_confirmation {
    
    take:
        
        assembled
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembled).assigned_species
    
    emit:
        
        assigned_species
        
    
}

workflow wf_cgmlst_amr {
    
    take:
        
        assembled
        
    
    main:
        step_4TY_cgMLST__chewbbaca(assembled, genus_species, schema)
        step_4AN_AMR__abricate(assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    wf_preprocess_assemble(rawreads)
    wf_species_confirmation(wf_preprocess_assemble.assembled)
    wf_cgmlst_amr(wf_preprocess_assemble.assembled)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `MOD_3T_AD03_addThenDrop_sal_t3` — `silent_no_op`
**Conversation:** `MOD_3T_AD03_addThenDrop_sal` (add) — turn 3
**Prompt:** Actually, drop the ABRicate step.

**Steps (LLM):** `step_2AS_denovo__unicycler, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp`
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

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_salmonella {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        unicycler_out = step_2AS_denovo__unicycler(trAndRef.trimmed)
        assembly_filter(unicycler_out.scaffolds).fasta | quast

        kmerfinder_out = step_3TX_species__kmerfinder(assembly_filter.out.fasta)

        step_4TY_cgMLST__chewbbaca(kmerfinder_out.assigned_species, 'Salmonella enterica', 's_enterica_chewie_3255_210531')
    
}

workflow wf_cgmlst_salmonella {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        unicycler_out = step_2AS_denovo__unicycler(trAndRef.trimmed)
        assembly_filter(unicycler_out.scaffolds).fasta | quast

        kmerfinder_out = step_3TX_species__kmerfinder(assembly_filter.out.fasta)

        step_4TY_cgMLST__chewbbaca(kmerfinder_out.assigned_species, 'Salmonella enterica', 's_enterica_chewie_3255_210531')
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_cgmlst_salmonella(trimmed)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `MOD_3T_RA01_replaceThenAdd_lis_t1` — `file_not_found`
**Conversation:** `MOD_3T_RA01_replaceThenAdd_lis` (replace) — turn 1
**Prompt:** Trim + assemble Listeria monocytogenes from paired Illumina FASTQ (fastp + SPAdes).

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        denovo(trimmed)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.246.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_RA01_replaceThenAdd_lis_t2` — `file_not_found`
**Conversation:** `MOD_3T_RA01_replaceThenAdd_lis` (replace) — turn 2
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

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__shovill {
    
    take:
        
        trimmed
        
    
    main:
        contigs_from_pe = shovill(trimmed).assembly
        contigs_from_se = shovill_se(trimmed).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }
    
    emit:
        
        assembly = contigs
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    step_2AS_denovo__shovill(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.246.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_RA01_replaceThenAdd_lis_t3` — `file_not_found`
**Conversation:** `MOD_3T_RA01_replaceThenAdd_lis` (replace) — turn 3
**Prompt:** Now also run MLST on the assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__shovill {
    
    take:
        
        rawreads
        
    
    main:
        contigs_from_pe = shovill(rawreads).assembly
        contigs_from_se = shovill_se(rawreads).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }
    
    emit:
        
        assembly = contigs
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.246.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_RA02_replaceThenAdd_eco_t1` — `no_code`
**Conversation:** `MOD_3T_RA02_replaceThenAdd_eco` (replace) — turn 1
**Prompt:** Trim + assemble Escherichia coli from paired Illumina FASTQ (fastp + SPAdes).

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
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `MOD_3T_RA03_replaceThenAdd_sal_t1` — `file_not_found`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    step_2AS_denovo__spades(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.243.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
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

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__shovill {
    
    take:
        
        rawreads
        
    
    main:
        contigs_from_pe = shovill(rawreads).assembly
        contigs_from_se = shovill_se(rawreads).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }
    
    emit:
        
        assembly = contigs
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__shovill(trimmed).assembly
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.243.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_RA03_replaceThenAdd_sal_t3` — `file_not_found`
**Conversation:** `MOD_3T_RA03_replaceThenAdd_sal` (replace) — turn 3
**Prompt:** Now also run MLST on the assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__shovill {
    
    take:
        
        rawreads
        
    
    main:
        contigs_from_pe = shovill(rawreads).assembly
        contigs_from_se = shovill_se(rawreads).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
          checkm(contigs)
        }
        assembly = contigs
    
    emit:
        
        assembly
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.243.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `MOD_3T_SA02_switchThenAdd_eco_to_lis_t2` — `file_not_found`
**Conversation:** `MOD_3T_SA02_switchThenAdd_eco_to_lis` (switch_species) — turn 2
**Prompt:** Apply the same to Listeria monocytogenes.

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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        
        data
        
    
    main:
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.248.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```
