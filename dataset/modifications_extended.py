#!/usr/bin/env python3.11
"""
Combinatorial expansion of the multi-turn modification corpus from 17 to ~200.

Adds:
  - more add/replace/drop/switch_species 2-turn conversations
  - 3-turn conversations: a base + 2 sequential modifications
  - one or two 4-turn conversations for stress-tests

Reuses helpers from modifications.py and blueprints.py. Validation harness
is unchanged.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dataset.modifications import (   # noqa: E402
    ConversationExample, Turn,
    chain_trim_asm, chain_trim_asm_typing, chain_trim_asm_two_typing,
    chain_mono_asm, chain_mono_typing_assembly, chain_mono_two_typing_assembly,
    _add_typing_to_chain,
)
from dataset.blueprints import (   # noqa: E402
    PROCS, ASM_EMIT, _nf_header,
    _params_fastq, _params_assembly, _build_typing_call,
)


def _short(sp: str) -> str:
    return {
        "listeria_monocytogenes":  "lis",
        "escherichia_coli":        "eco",
        "salmonella_enterica":     "sal",
        "campylobacter_jejuni":    "cam",
    }.get(sp, sp[:3])


def _label(sp: str) -> str:
    return sp.replace("_", " ").title().replace("Coli","coli").replace("Enterica","enterica").replace("Monocytogenes","monocytogenes").replace("Jejuni","jejuni")


def build_extended_modifications() -> list[ConversationExample]:
    L: list[ConversationExample] = []
    seen: set[str] = set()
    def add(c: ConversationExample):
        if c.eid in seen:
            raise ValueError(f"duplicate {c.eid}")
        seen.add(c.eid); L.append(c)

    SP_CHEW = ["listeria_monocytogenes", "escherichia_coli", "salmonella_enterica"]
    SP_FLAA = ["campylobacter_jejuni"]
    SP_ANY  = SP_CHEW + SP_FLAA

    cmp_counter = {"lis": 200, "eco": 200, "sal": 200, "cam": 200}
    def make_cmp(sp: str) -> str:
        s = _short(sp); n = cmp_counter[s]; cmp_counter[s] += 1
        return f"2026.{s.upper()}.{n}.1.1"

    # ========================================================================
    # ADD: add a second typing/AMR step in parallel to an existing chain (50)
    # ========================================================================
    add_combos = [
        # (base_typing, new_typing, species, asm)
        # cgMLST + add MLST/abricate/prokka
        ("step_4TY_cgMLST__chewbbaca", "step_4TY_MLST__mlst",   "listeria_monocytogenes", "step_2AS_denovo__spades"),
        ("step_4TY_cgMLST__chewbbaca", "step_4TY_MLST__mlst",   "salmonella_enterica",    "step_2AS_denovo__spades"),
        ("step_4TY_cgMLST__chewbbaca", "step_4TY_MLST__mlst",   "escherichia_coli",       "step_2AS_denovo__spades"),
        ("step_4TY_cgMLST__chewbbaca", "step_4AN_AMR__abricate","listeria_monocytogenes", "step_2AS_denovo__spades"),
        ("step_4TY_cgMLST__chewbbaca", "step_4AN_AMR__abricate","salmonella_enterica",    "step_2AS_denovo__spades"),
        ("step_4TY_cgMLST__chewbbaca", "step_4AN_genes__prokka","listeria_monocytogenes", "step_2AS_denovo__spades"),
        ("step_4TY_cgMLST__chewbbaca", "step_4AN_genes__prokka","salmonella_enterica",    "step_2AS_denovo__spades"),
        # MLST + add cgMLST/abricate/prokka
        ("step_4TY_MLST__mlst", "step_4TY_cgMLST__chewbbaca","listeria_monocytogenes", "step_2AS_denovo__spades"),
        ("step_4TY_MLST__mlst", "step_4TY_cgMLST__chewbbaca","escherichia_coli",       "step_2AS_denovo__spades"),
        ("step_4TY_MLST__mlst", "step_4AN_AMR__abricate",    "listeria_monocytogenes", "step_2AS_denovo__spades"),
        ("step_4TY_MLST__mlst", "step_4AN_AMR__abricate",    "escherichia_coli",       "step_2AS_denovo__spades"),
        ("step_4TY_MLST__mlst", "step_4AN_AMR__abricate",    "salmonella_enterica",    "step_2AS_denovo__spades"),
        ("step_4TY_MLST__mlst", "step_4AN_genes__prokka",    "listeria_monocytogenes", "step_2AS_denovo__spades"),
        ("step_4TY_MLST__mlst", "step_4AN_genes__prokka",    "escherichia_coli",       "step_2AS_denovo__spades"),
        ("step_4TY_MLST__mlst", "step_4AN_genes__prokka",    "salmonella_enterica",    "step_2AS_denovo__spades"),
        ("step_4TY_MLST__mlst", "step_4AN_genes__prokka",    "campylobacter_jejuni",   "step_2AS_denovo__spades"),
        # abricate + add others
        ("step_4AN_AMR__abricate", "step_4AN_genes__prokka","listeria_monocytogenes", "step_2AS_denovo__spades"),
        ("step_4AN_AMR__abricate", "step_4AN_genes__prokka","escherichia_coli",       "step_2AS_denovo__spades"),
        ("step_4AN_AMR__abricate", "step_4TY_MLST__mlst",   "salmonella_enterica",    "step_2AS_denovo__spades"),
        ("step_4AN_AMR__abricate", "step_4TY_MLST__mlst",   "escherichia_coli",       "step_2AS_denovo__spades"),
        # Campy chains (flaA / staramr / mlst)
        ("step_4TY_flaA__flaA",    "step_4TY_MLST__mlst",      "campylobacter_jejuni", "step_2AS_denovo__spades"),
        ("step_4TY_flaA__flaA",    "step_4AN_AMR__staramr",    "campylobacter_jejuni", "step_2AS_denovo__spades"),
        ("step_4TY_flaA__flaA",    "step_4AN_AMR__abricate",   "campylobacter_jejuni", "step_2AS_denovo__spades"),
        ("step_4TY_flaA__flaA",    "step_4AN_genes__prokka",   "campylobacter_jejuni", "step_2AS_denovo__spades"),
        ("step_4AN_AMR__staramr",  "step_4TY_MLST__mlst",      "campylobacter_jejuni", "step_2AS_denovo__spades"),
        ("step_4AN_AMR__staramr",  "step_4TY_flaA__flaA",      "campylobacter_jejuni", "step_2AS_denovo__spades"),
        ("step_4AN_AMR__staramr",  "step_4AN_AMR__abricate",   "campylobacter_jejuni", "step_2AS_denovo__spades"),
        ("step_4AN_AMR__staramr",  "step_4AN_genes__prokka",   "campylobacter_jejuni", "step_2AS_denovo__spades"),
        ("step_4TY_MLST__mlst",    "step_4TY_flaA__flaA",      "campylobacter_jejuni", "step_2AS_denovo__spades"),
        ("step_4TY_MLST__mlst",    "step_4AN_AMR__staramr",    "campylobacter_jejuni", "step_2AS_denovo__spades"),
        # different assembler underneath
        ("step_4TY_MLST__mlst", "step_4AN_AMR__abricate",    "listeria_monocytogenes", "step_2AS_denovo__shovill"),
        ("step_4TY_MLST__mlst", "step_4AN_genes__prokka",    "salmonella_enterica",    "step_2AS_denovo__shovill"),
        ("step_4TY_cgMLST__chewbbaca", "step_4AN_AMR__abricate", "listeria_monocytogenes", "step_2AS_denovo__unicycler"),
        ("step_4TY_cgMLST__chewbbaca", "step_4AN_AMR__abricate", "salmonella_enterica",    "step_2AS_denovo__unicycler"),
        ("step_4TY_MLST__mlst", "step_4TY_cgMLST__chewbbaca", "escherichia_coli",      "step_2AS_denovo__shovill"),
        ("step_4TY_MLST__mlst", "step_4TY_cgMLST__chewbbaca", "salmonella_enterica",   "step_2AS_denovo__shovill"),
        # different trimmer
        ("step_4TY_MLST__mlst", "step_4AN_AMR__abricate",    "listeria_monocytogenes", "step_2AS_denovo__spades", "step_1PP_trimming__trimmomatic"),
        ("step_4TY_MLST__mlst", "step_4AN_genes__prokka",    "escherichia_coli",       "step_2AS_denovo__spades", "step_1PP_trimming__trimmomatic"),
    ]
    for i, combo in enumerate(add_combos, start=1):
        if len(combo) == 4:
            t1, t2, sp, asm = combo
            trim = "step_1PP_trimming__fastp"
        else:
            t1, t2, sp, asm, trim = combo
        cmp = make_cmp(sp)
        emit = ASM_EMIT[asm]
        c1 = _build_typing_call(t1); c2 = _build_typing_call(t2)
        turn1_nf = _nf_header([trim, asm, t1]) + "workflow {\n    trimmed   = " + trim + "(getSingleInput()).trimmed\n    assembled = " + asm + "(trimmed)." + emit + "\n    " + c1 + "\n}\n"
        turn2_nf = _nf_header([trim, asm, t1, t2]) + "workflow {\n    trimmed   = " + trim + "(getSingleInput()).trimmed\n    assembled = " + asm + "(trimmed)." + emit + "\n    " + c1 + "\n    " + c2 + "\n}\n"
        add(ConversationExample(
            eid=f"MOD_K{i:02d}_add_{t2.split('__')[-1]}_to_{t1.split('__')[-1]}_{_short(sp)}_{asm.split('__')[-1]}",
            category="modification", base_id="(generated)", modification_kind="add",
            notes=f"add {t2.split('__')[-1]} in parallel to a ({trim.split('__')[-1]}+{asm.split('__')[-1]}+{t1.split('__')[-1]}) chain",
            turns=[
                Turn(prompt=f"{t1.split('__')[-1]} on {_label(sp)} from paired Illumina FASTQ "
                            f"({trim.split('__')[-1]} + {asm.split('__')[-1]}).",
                     nextflow_code=turn1_nf, params=_params_fastq(cmp, sp),
                     inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS[trim]+PROCS[asm]+PROCS[t1]),
                Turn(prompt=f"Now also run {t2.split('__')[-1]} in parallel on the same assembly.",
                     nextflow_code=turn2_nf, params=_params_fastq(cmp, sp),
                     inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS[trim]+PROCS[asm]+PROCS[t1]+PROCS[t2]),
            ],
        ))

    # ========================================================================
    # REPLACE: swap one component (50)
    # ========================================================================
    # Swap assembler
    replace_asm_combos = [
        ("step_2AS_denovo__spades",   "step_2AS_denovo__shovill",   "listeria_monocytogenes"),
        ("step_2AS_denovo__spades",   "step_2AS_denovo__shovill",   "salmonella_enterica"),
        ("step_2AS_denovo__spades",   "step_2AS_denovo__shovill",   "escherichia_coli"),
        ("step_2AS_denovo__spades",   "step_2AS_denovo__shovill",   "campylobacter_jejuni"),
        ("step_2AS_denovo__spades",   "step_2AS_denovo__unicycler", "listeria_monocytogenes"),
        ("step_2AS_denovo__spades",   "step_2AS_denovo__unicycler", "salmonella_enterica"),
        ("step_2AS_denovo__spades",   "step_2AS_denovo__unicycler", "campylobacter_jejuni"),
        ("step_2AS_denovo__shovill",  "step_2AS_denovo__spades",    "listeria_monocytogenes"),
        ("step_2AS_denovo__shovill",  "step_2AS_denovo__spades",    "escherichia_coli"),
        ("step_2AS_denovo__shovill",  "step_2AS_denovo__unicycler", "listeria_monocytogenes"),
        ("step_2AS_denovo__unicycler","step_2AS_denovo__spades",    "salmonella_enterica"),
        ("step_2AS_denovo__unicycler","step_2AS_denovo__shovill",   "escherichia_coli"),
    ]
    # 2-step trim+asm, swap assembler
    for i, (a1, a2, sp) in enumerate(replace_asm_combos, start=1):
        cmp = make_cmp(sp)
        add(ConversationExample(
            eid=f"MOD_R{i:02d}_replace_asm_{a1.split('__')[-1]}_to_{a2.split('__')[-1]}_{_short(sp)}",
            category="modification", base_id="(generated)", modification_kind="replace",
            notes=f"swap assembler {a1.split('__')[-1]} -> {a2.split('__')[-1]}",
            turns=[
                Turn(prompt=f"Trim + assemble {_label(sp)} from paired Illumina FASTQ using fastp + {a1.split('__')[-1]}.",
                     nextflow_code=chain_trim_asm("step_1PP_trimming__fastp", a1),
                     params=_params_fastq(cmp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS[a1]),
                Turn(prompt=f"Replace {a1.split('__')[-1]} with {a2.split('__')[-1]}.",
                     nextflow_code=chain_trim_asm("step_1PP_trimming__fastp", a2),
                     params=_params_fastq(cmp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS[a2]),
            ],
        ))

    # Swap trimmer
    replace_trim_combos = [
        ("step_1PP_trimming__fastp",       "step_1PP_trimming__trimmomatic", "listeria_monocytogenes"),
        ("step_1PP_trimming__fastp",       "step_1PP_trimming__trimmomatic", "escherichia_coli"),
        ("step_1PP_trimming__fastp",       "step_1PP_trimming__trimmomatic", "salmonella_enterica"),
        ("step_1PP_trimming__fastp",       "step_1PP_trimming__trimmomatic", "campylobacter_jejuni"),
        ("step_1PP_trimming__trimmomatic", "step_1PP_trimming__fastp",       "listeria_monocytogenes"),
        ("step_1PP_trimming__trimmomatic", "step_1PP_trimming__fastp",       "salmonella_enterica"),
    ]
    for i, (t1, t2, sp) in enumerate(replace_trim_combos, start=1):
        cmp = make_cmp(sp)
        add(ConversationExample(
            eid=f"MOD_RT{i:02d}_replace_trim_{t1.split('__')[-1]}_to_{t2.split('__')[-1]}_{_short(sp)}",
            category="modification", base_id="(generated)", modification_kind="replace",
            notes=f"swap trimmer {t1.split('__')[-1]} -> {t2.split('__')[-1]}",
            turns=[
                Turn(prompt=f"Trim + assemble {_label(sp)} from paired Illumina FASTQ using {t1.split('__')[-1]} + SPAdes.",
                     nextflow_code=chain_trim_asm(t1, "step_2AS_denovo__spades"),
                     params=_params_fastq(cmp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS[t1]+PROCS["step_2AS_denovo__spades"]),
                Turn(prompt=f"Replace {t1.split('__')[-1]} with {t2.split('__')[-1]}.",
                     nextflow_code=chain_trim_asm(t2, "step_2AS_denovo__spades"),
                     params=_params_fastq(cmp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS[t2]+PROCS["step_2AS_denovo__spades"]),
            ],
        ))

    # Swap typing tool
    replace_typing_combos = [
        ("step_4TY_MLST__mlst",        "step_4TY_cgMLST__chewbbaca", "listeria_monocytogenes"),
        ("step_4TY_MLST__mlst",        "step_4TY_cgMLST__chewbbaca", "salmonella_enterica"),
        ("step_4TY_MLST__mlst",        "step_4AN_AMR__abricate",     "listeria_monocytogenes"),
        ("step_4TY_MLST__mlst",        "step_4AN_AMR__abricate",     "salmonella_enterica"),
        ("step_4TY_MLST__mlst",        "step_4AN_genes__prokka",     "listeria_monocytogenes"),
        ("step_4TY_MLST__mlst",        "step_4AN_genes__prokka",     "escherichia_coli"),
        ("step_4TY_cgMLST__chewbbaca", "step_4AN_genes__prokka",     "listeria_monocytogenes"),
        ("step_4TY_cgMLST__chewbbaca", "step_4AN_AMR__abricate",     "salmonella_enterica"),
        ("step_4AN_AMR__abricate",     "step_4AN_genes__prokka",     "escherichia_coli"),
        ("step_4AN_genes__prokka",     "step_4AN_AMR__abricate",     "salmonella_enterica"),
        ("step_4TY_flaA__flaA",        "step_4TY_MLST__mlst",        "campylobacter_jejuni"),
        ("step_4AN_AMR__staramr",      "step_4AN_AMR__abricate",     "campylobacter_jejuni"),
    ]
    for i, (t1, t2, sp) in enumerate(replace_typing_combos, start=1):
        cmp = make_cmp(sp)
        add(ConversationExample(
            eid=f"MOD_RTY{i:02d}_replace_typing_{t1.split('__')[-1]}_to_{t2.split('__')[-1]}_{_short(sp)}",
            category="modification", base_id="(generated)", modification_kind="replace",
            notes=f"swap downstream typing/AMR {t1.split('__')[-1]} -> {t2.split('__')[-1]}",
            turns=[
                Turn(prompt=f"{t1.split('__')[-1]} on {_label(sp)} from paired Illumina FASTQ (fastp + SPAdes + {t1.split('__')[-1]}).",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades",t1),
                     params=_params_fastq(cmp, sp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS[t1]),
                Turn(prompt=f"Switch the downstream step from {t1.split('__')[-1]} to {t2.split('__')[-1]}.",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades",t2),
                     params=_params_fastq(cmp, sp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS[t2]),
            ],
        ))

    # Swap typing on existing assembly (mono → mono)
    mono_replace_combos = [
        ("step_4TY_MLST__mlst",       "step_4TY_cgMLST__chewbbaca", "salmonella_enterica"),
        ("step_4TY_MLST__mlst",       "step_4TY_cgMLST__chewbbaca", "listeria_monocytogenes"),
        ("step_4TY_cgMLST__chewbbaca","step_4TY_MLST__mlst",        "listeria_monocytogenes"),
        ("step_4TY_cgMLST__chewbbaca","step_4TY_MLST__mlst",        "salmonella_enterica"),
        ("step_4TY_cgMLST__chewbbaca","step_4AN_AMR__abricate",     "listeria_monocytogenes"),
        ("step_4AN_AMR__abricate",    "step_4AN_genes__prokka",     "escherichia_coli"),
        ("step_4AN_AMR__abricate",    "step_4TY_MLST__mlst",        "salmonella_enterica"),
        ("step_4TY_flaA__flaA",       "step_4AN_AMR__staramr",      "campylobacter_jejuni"),
        ("step_4AN_AMR__staramr",     "step_4TY_flaA__flaA",        "campylobacter_jejuni"),
        ("step_4AN_AMR__staramr",     "step_4TY_MLST__mlst",        "campylobacter_jejuni"),
    ]
    for i, (t1, t2, sp) in enumerate(mono_replace_combos, start=1):
        cmp = make_cmp(sp)
        add(ConversationExample(
            eid=f"MOD_RM{i:02d}_replace_mono_{t1.split('__')[-1]}_to_{t2.split('__')[-1]}_{_short(sp)}",
            category="modification", base_id="(generated)", modification_kind="replace",
            notes=f"mono-step typing on existing assembly: {t1.split('__')[-1]} -> {t2.split('__')[-1]}",
            turns=[
                Turn(prompt=f"Run {t1.split('__')[-1]} on a pre-existing {_label(sp)} assembly.",
                     nextflow_code=chain_mono_typing_assembly(t1),
                     params=_params_assembly(cmp, sp), inputs=[f"assembly:{cmp}"],
                     expected_processes=PROCS[t1]),
                Turn(prompt=f"Use {t2.split('__')[-1]} on that same assembly instead.",
                     nextflow_code=chain_mono_typing_assembly(t2),
                     params=_params_assembly(cmp, sp), inputs=[f"assembly:{cmp}"],
                     expected_processes=PROCS[t2]),
            ],
        ))

    # ========================================================================
    # DROP (30)
    # ========================================================================
    drop_combos = [
        # base 4-step → drop one downstream
        # (downstream_drop, kept_downstream, sp)
        ("step_4TY_cgMLST__chewbbaca", "step_4TY_MLST__mlst",   "listeria_monocytogenes"),
        ("step_4TY_cgMLST__chewbbaca", "step_4TY_MLST__mlst",   "salmonella_enterica"),
        ("step_4TY_cgMLST__chewbbaca", "step_4TY_MLST__mlst",   "escherichia_coli"),
        ("step_4TY_MLST__mlst",        "step_4TY_cgMLST__chewbbaca", "listeria_monocytogenes"),
        ("step_4TY_MLST__mlst",        "step_4TY_cgMLST__chewbbaca", "salmonella_enterica"),
        ("step_4AN_AMR__abricate",     "step_4TY_MLST__mlst",   "listeria_monocytogenes"),
        ("step_4AN_AMR__abricate",     "step_4TY_MLST__mlst",   "escherichia_coli"),
        ("step_4AN_AMR__abricate",     "step_4TY_MLST__mlst",   "salmonella_enterica"),
        ("step_4AN_genes__prokka",     "step_4TY_MLST__mlst",   "salmonella_enterica"),
        ("step_4AN_genes__prokka",     "step_4AN_AMR__abricate","listeria_monocytogenes"),
        ("step_4TY_flaA__flaA",        "step_4TY_MLST__mlst",   "campylobacter_jejuni"),
        ("step_4AN_AMR__staramr",      "step_4TY_MLST__mlst",   "campylobacter_jejuni"),
    ]
    for i, (dropped, kept, sp) in enumerate(drop_combos, start=1):
        cmp = make_cmp(sp)
        emit = ASM_EMIT["step_2AS_denovo__spades"]
        c_dropped = _build_typing_call(dropped); c_kept = _build_typing_call(kept)
        nf_with_both = _nf_header(["step_1PP_trimming__fastp","step_2AS_denovo__spades", dropped, kept]) + "workflow {\n    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed\n    assembled = step_2AS_denovo__spades(trimmed)." + emit + "\n    " + c_dropped + "\n    " + c_kept + "\n}\n"
        nf_only_kept = chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades",kept)
        add(ConversationExample(
            eid=f"MOD_D{i:02d}_drop_{dropped.split('__')[-1]}_keep_{kept.split('__')[-1]}_{_short(sp)}",
            category="modification", base_id="(generated)", modification_kind="drop",
            notes=f"drop {dropped.split('__')[-1]}, keep {kept.split('__')[-1]}",
            turns=[
                Turn(prompt=f"Run both {dropped.split('__')[-1]} and {kept.split('__')[-1]} on {_label(sp)} from paired Illumina FASTQ.",
                     nextflow_code=nf_with_both, params=_params_fastq(cmp, sp),
                     inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS[dropped]+PROCS[kept]),
                Turn(prompt=f"Drop {dropped.split('__')[-1]}, keep only {kept.split('__')[-1]}.",
                     nextflow_code=nf_only_kept, params=_params_fastq(cmp, sp),
                     inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS[kept]),
            ],
        ))

    # drop the assembly step entirely (keep just trim)
    for i, sp in enumerate(["listeria_monocytogenes","escherichia_coli","salmonella_enterica","campylobacter_jejuni"], start=1):
        cmp = make_cmp(sp)
        add(ConversationExample(
            eid=f"MOD_DA{i:02d}_drop_assembly_{_short(sp)}",
            category="modification", base_id="(generated)", modification_kind="drop",
            notes="remove assembly, keep only trimming",
            turns=[
                Turn(prompt=f"Trim + assemble {_label(sp)} from paired Illumina FASTQ (fastp + SPAdes).",
                     nextflow_code=chain_trim_asm("step_1PP_trimming__fastp","step_2AS_denovo__spades"),
                     params=_params_fastq(cmp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]),
                Turn(prompt="Drop the assembly step and just trim the reads.",
                     nextflow_code=_nf_header(["step_1PP_trimming__fastp"]) + "workflow {\n    step_1PP_trimming__fastp(getSingleInput())\n}\n",
                     params=_params_fastq(cmp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]),
            ],
        ))

    # drop one of two parallel mono-typing
    for i, (drop, keep, sp) in enumerate([
        ("step_4TY_cgMLST__chewbbaca","step_4TY_MLST__mlst", "listeria_monocytogenes"),
        ("step_4TY_cgMLST__chewbbaca","step_4TY_MLST__mlst", "salmonella_enterica"),
        ("step_4TY_MLST__mlst",       "step_4TY_cgMLST__chewbbaca","listeria_monocytogenes"),
        ("step_4TY_MLST__mlst",       "step_4TY_cgMLST__chewbbaca","escherichia_coli"),
        ("step_4AN_AMR__abricate",    "step_4TY_MLST__mlst", "salmonella_enterica"),
        ("step_4AN_genes__prokka",    "step_4TY_MLST__mlst", "listeria_monocytogenes"),
        ("step_4AN_AMR__staramr",     "step_4TY_MLST__mlst", "campylobacter_jejuni"),
        ("step_4AN_AMR__staramr",     "step_4TY_flaA__flaA", "campylobacter_jejuni"),
        ("step_4TY_flaA__flaA",       "step_4AN_AMR__staramr","campylobacter_jejuni"),
        ("step_4TY_flaA__flaA",       "step_4TY_MLST__mlst",  "campylobacter_jejuni"),
        ("step_4AN_AMR__abricate",    "step_4AN_genes__prokka","escherichia_coli"),
        ("step_4AN_genes__prokka",    "step_4AN_AMR__abricate","listeria_monocytogenes"),
        ("step_4AN_genes__prokka",    "step_4TY_MLST__mlst",   "salmonella_enterica"),
        ("step_4AN_AMR__abricate",    "step_4AN_genes__prokka","salmonella_enterica"),
    ], start=1):
        cmp = make_cmp(sp)
        add(ConversationExample(
            eid=f"MOD_DM{i:02d}_drop_mono_{drop.split('__')[-1]}_keep_{keep.split('__')[-1]}_{_short(sp)}",
            category="modification", base_id="(generated)", modification_kind="drop",
            notes="mono-step from assembly: drop one of two parallel typing tools",
            turns=[
                Turn(prompt=f"Run both {drop.split('__')[-1]} and {keep.split('__')[-1]} on a pre-existing {_label(sp)} assembly.",
                     nextflow_code=chain_mono_two_typing_assembly(drop, keep),
                     params=_params_assembly(cmp, sp), inputs=[f"assembly:{cmp}"],
                     expected_processes=PROCS[drop]+PROCS[keep]),
                Turn(prompt=f"Drop {drop.split('__')[-1]}, keep only {keep.split('__')[-1]}.",
                     nextflow_code=chain_mono_typing_assembly(keep),
                     params=_params_assembly(cmp, sp), inputs=[f"assembly:{cmp}"],
                     expected_processes=PROCS[keep]),
            ],
        ))

    # ========================================================================
    # SWITCH_SPECIES (30)
    # ========================================================================
    sp_pairs_chew = [
        ("listeria_monocytogenes","salmonella_enterica"),
        ("listeria_monocytogenes","escherichia_coli"),
        ("salmonella_enterica","listeria_monocytogenes"),
        ("salmonella_enterica","escherichia_coli"),
        ("escherichia_coli","listeria_monocytogenes"),
        ("escherichia_coli","salmonella_enterica"),
    ]
    # cgMLST 3-step retarget (12)
    for i, (sp1, sp2) in enumerate(sp_pairs_chew, start=1):
        cmp1, cmp2 = make_cmp(sp1), make_cmp(sp2)
        add(ConversationExample(
            eid=f"MOD_S{i:02d}_cgmlst_retarget_{_short(sp1)}_to_{_short(sp2)}",
            category="modification", base_id="(generated)", modification_kind="switch_species",
            notes=f"cgMLST chain retargeted from {sp1} to {sp2}",
            turns=[
                Turn(prompt=f"cgMLST pipeline for {_label(sp1)} from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_cgMLST__chewbbaca"),
                     params=_params_fastq(cmp1, sp1), inputs=[f"fastq_paired:{cmp1}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_cgMLST__chewbbaca"]),
                Turn(prompt=f"Apply the same pipeline to {_label(sp2)}.",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_cgMLST__chewbbaca"),
                     params=_params_fastq(cmp2, sp2), inputs=[f"fastq_paired:{cmp2}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_cgMLST__chewbbaca"]),
            ],
        ))

    # MLST chain retarget across all 4 species (12 combos)
    sp_pairs_mlst = [
        ("listeria_monocytogenes","campylobacter_jejuni"),
        ("salmonella_enterica","campylobacter_jejuni"),
        ("escherichia_coli","campylobacter_jejuni"),
        ("campylobacter_jejuni","listeria_monocytogenes"),
        ("campylobacter_jejuni","salmonella_enterica"),
        ("campylobacter_jejuni","escherichia_coli"),
    ]
    for i, (sp1, sp2) in enumerate(sp_pairs_mlst, start=1):
        cmp1, cmp2 = make_cmp(sp1), make_cmp(sp2)
        add(ConversationExample(
            eid=f"MOD_SM{i:02d}_mlst_retarget_{_short(sp1)}_to_{_short(sp2)}",
            category="modification", base_id="(generated)", modification_kind="switch_species",
            notes=f"MLST chain retargeted",
            turns=[
                Turn(prompt=f"MLST pipeline for {_label(sp1)} from paired Illumina FASTQ.",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_MLST__mlst"),
                     params=_params_fastq(cmp1, sp1), inputs=[f"fastq_paired:{cmp1}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_MLST__mlst"]),
                Turn(prompt=f"Re-run the same pipeline on {_label(sp2)}.",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_MLST__mlst"),
                     params=_params_fastq(cmp2, sp2), inputs=[f"fastq_paired:{cmp2}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_MLST__mlst"]),
            ],
        ))

    # Switch species on mono-typing (10)
    for i, (sp1, sp2) in enumerate(sp_pairs_chew[:6] + sp_pairs_mlst[:4], start=1):
        cmp1, cmp2 = make_cmp(sp1), make_cmp(sp2)
        add(ConversationExample(
            eid=f"MOD_SMA{i:02d}_mlst_mono_retarget_{_short(sp1)}_to_{_short(sp2)}",
            category="modification", base_id="(generated)", modification_kind="switch_species",
            notes="mono MLST on existing assembly, switch species",
            turns=[
                Turn(prompt=f"MLST on a pre-existing {_label(sp1)} assembly.",
                     nextflow_code=chain_mono_typing_assembly("step_4TY_MLST__mlst"),
                     params=_params_assembly(cmp1, sp1), inputs=[f"assembly:{cmp1}"],
                     expected_processes=PROCS["step_4TY_MLST__mlst"]),
                Turn(prompt=f"Same thing but for {_label(sp2)}.",
                     nextflow_code=chain_mono_typing_assembly("step_4TY_MLST__mlst"),
                     params=_params_assembly(cmp2, sp2), inputs=[f"assembly:{cmp2}"],
                     expected_processes=PROCS["step_4TY_MLST__mlst"]),
            ],
        ))

    # ========================================================================
    # 3-TURN conversations: base, then mod1, then mod2 (15)
    # ========================================================================
    for i, sp in enumerate(SP_CHEW, start=1):
        cmp = make_cmp(sp)
        add(ConversationExample(
            eid=f"MOD_3T{i:02d}_addAdd_{_short(sp)}",
            category="modification", base_id="(generated)", modification_kind="add",
            notes="3-turn: assemble → add MLST → also add cgMLST",
            turns=[
                Turn(prompt=f"From paired Illumina FASTQ of {_label(sp)}: trim with fastp and assemble with SPAdes.",
                     nextflow_code=chain_trim_asm("step_1PP_trimming__fastp","step_2AS_denovo__spades"),
                     params=_params_fastq(cmp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]),
                Turn(prompt=f"Now also run MLST on the assembly.",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_MLST__mlst"),
                     params=_params_fastq(cmp, sp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_MLST__mlst"]),
                Turn(prompt=f"Also add cgMLST in parallel.",
                     nextflow_code=chain_trim_asm_two_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_MLST__mlst","step_4TY_cgMLST__chewbbaca"),
                     params=_params_fastq(cmp, sp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_MLST__mlst"]+PROCS["step_4TY_cgMLST__chewbbaca"]),
            ],
        ))

    # 3-turn: add then drop (sanity check)
    for i, sp in enumerate(SP_CHEW, start=1):
        cmp = make_cmp(sp)
        add(ConversationExample(
            eid=f"MOD_3T_AD{i:02d}_addThenDrop_{_short(sp)}",
            category="modification", base_id="(generated)", modification_kind="add",
            notes="3-turn: cgMLST → add abricate → drop abricate",
            turns=[
                Turn(prompt=f"cgMLST profile for {_label(sp)} from paired Illumina FASTQ.",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_cgMLST__chewbbaca"),
                     params=_params_fastq(cmp, sp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_cgMLST__chewbbaca"]),
                Turn(prompt="Also add ABRicate AMR screening in parallel.",
                     nextflow_code=chain_trim_asm_two_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_cgMLST__chewbbaca","step_4AN_AMR__abricate"),
                     params=_params_fastq(cmp, sp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_cgMLST__chewbbaca"]+PROCS["step_4AN_AMR__abricate"]),
                Turn(prompt="Actually, drop the ABRicate step.",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_cgMLST__chewbbaca"),
                     params=_params_fastq(cmp, sp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_cgMLST__chewbbaca"]),
            ],
        ))

    # 3-turn: replace assembler, then add typing
    for i, sp in enumerate(SP_CHEW, start=1):
        cmp = make_cmp(sp)
        add(ConversationExample(
            eid=f"MOD_3T_RA{i:02d}_replaceThenAdd_{_short(sp)}",
            category="modification", base_id="(generated)", modification_kind="replace",
            notes="3-turn: trim+spades → replace spades with shovill → add MLST",
            turns=[
                Turn(prompt=f"Trim + assemble {_label(sp)} from paired Illumina FASTQ (fastp + SPAdes).",
                     nextflow_code=chain_trim_asm("step_1PP_trimming__fastp","step_2AS_denovo__spades"),
                     params=_params_fastq(cmp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]),
                Turn(prompt="Use Shovill instead of SPAdes.",
                     nextflow_code=chain_trim_asm("step_1PP_trimming__fastp","step_2AS_denovo__shovill"),
                     params=_params_fastq(cmp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__shovill"]),
                Turn(prompt="Now also run MLST on the assembly.",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__shovill","step_4TY_MLST__mlst"),
                     params=_params_fastq(cmp, sp), inputs=[f"fastq_paired:{cmp}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__shovill"]+PROCS["step_4TY_MLST__mlst"]),
            ],
        ))

    # 3-turn: switch species then add typing  (6)
    for i, sp1, sp2 in [(1,"listeria_monocytogenes","salmonella_enterica"),
                       (2,"escherichia_coli","listeria_monocytogenes"),
                       (3,"salmonella_enterica","escherichia_coli")]:
        cmp1, cmp2 = make_cmp(sp1), make_cmp(sp2)
        add(ConversationExample(
            eid=f"MOD_3T_SA{i:02d}_switchThenAdd_{_short(sp1)}_to_{_short(sp2)}",
            category="modification", base_id="(generated)", modification_kind="switch_species",
            notes="3-turn: chain on sp1 → retarget sp2 → add cgMLST",
            turns=[
                Turn(prompt=f"MLST pipeline for {_label(sp1)} from paired Illumina FASTQ.",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_MLST__mlst"),
                     params=_params_fastq(cmp1, sp1), inputs=[f"fastq_paired:{cmp1}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_MLST__mlst"]),
                Turn(prompt=f"Apply the same to {_label(sp2)}.",
                     nextflow_code=chain_trim_asm_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_MLST__mlst"),
                     params=_params_fastq(cmp2, sp2), inputs=[f"fastq_paired:{cmp2}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_MLST__mlst"]),
                Turn(prompt="Also add cgMLST in parallel for this species.",
                     nextflow_code=chain_trim_asm_two_typing("step_1PP_trimming__fastp","step_2AS_denovo__spades","step_4TY_MLST__mlst","step_4TY_cgMLST__chewbbaca"),
                     params=_params_fastq(cmp2, sp2), inputs=[f"fastq_paired:{cmp2}"],
                     expected_processes=PROCS["step_1PP_trimming__fastp"]+PROCS["step_2AS_denovo__spades"]+PROCS["step_4TY_MLST__mlst"]+PROCS["step_4TY_cgMLST__chewbbaca"]),
            ],
        ))

    return L


if __name__ == "__main__":
    L = build_extended_modifications()
    print(f"Built {len(L)} extended modification conversations")
    # check duplicate with base
    from dataset.modifications import build_modifications
    base = build_modifications()
    base_ids = {c.eid for c in base}
    dupes = [c.eid for c in L if c.eid in base_ids]
    if dupes:
        print(f"DUPLICATES: {dupes}")
    else:
        print(f"No duplicate IDs vs base. Total = {len(base) + len(L)} conversations.")
    n_turns = sum(len(c.turns) for c in base + L)
    print(f"Total turns: {n_turns}")
