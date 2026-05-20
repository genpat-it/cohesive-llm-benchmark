#!/usr/bin/env python3.11
"""
Combinatorial expansion of the single-turn corpus from 50 to ~200.

Reuses the helpers from blueprints.py and adds 150 carefully picked,
non-redundant combinations across:

  - 3-step chains: trim x assembler x typing/AMR, varying species
  - long-read (chopper + flye) chains with typing
  - 4-step chains (one upstream + 3 downstream)
  - mono-step rare operations (filtering, hostdepl, downsampling variants)
  - parallel species ID + chain
  - cross-species sanity checks

Every blueprint is reachable through the same helpers as blueprints.py;
the validation harness treats them identically.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from harness.harness import Example   # noqa: E402

from dataset.blueprints import (   # noqa: E402
    PROCS, ASM_EMIT, _nf_header,
    _params_fastq, _params_assembly, _build_typing_call,
    mono_typing, mono_assembly, mono_species_id,
    trim_assembly, trim_assembly_typing,
    SPECIES_ID_REQUIRED_PARAMS,
)
import textwrap

# ---------------------------------------------------------------------------
# additional helpers
# ---------------------------------------------------------------------------
TRIMMERS = ["step_1PP_trimming__fastp",
            "step_1PP_trimming__trimmomatic"]   # chopper is long-read
ASSEMBLERS_ILLUMINA = [
    "step_2AS_denovo__spades",
    "step_2AS_denovo__shovill",
    "step_2AS_denovo__unicycler",
]
TYPING_ASM_INPUT = {
    "step_4TY_MLST__mlst":         "any",   # no species filter
    "step_4TY_cgMLST__chewbbaca":  {"listeria_monocytogenes",
                                    "escherichia_coli",
                                    "salmonella_enterica"},
    "step_4TY_flaA__flaA":         {"campylobacter_jejuni",
                                    "campylobacter_coli"},
    "step_4AN_AMR__staramr":       {"campylobacter_jejuni",
                                    "campylobacter_coli"},
    "step_4AN_AMR__abricate":      "any",
    "step_4AN_genes__prokka":      "any",
}


def is_species_compat(typing_step: str, species: str) -> bool:
    allowed = TYPING_ASM_INPUT.get(typing_step)
    if allowed == "any":
        return True
    return species in (allowed or set())


# Pretty-print helpers (lower-case + readable)
def _short(species: str) -> str:
    return {
        "listeria_monocytogenes":  "lis",
        "escherichia_coli":        "eco",
        "salmonella_enterica":     "sal",
        "campylobacter_jejuni":    "cam",
        "campylobacter_coli":      "cco",
    }.get(species, species[:3])


def _species_label(species: str) -> str:
    return species.replace("_", " ").title().replace("Coli", "coli").replace("Enterica", "enterica").replace("Monocytogenes", "monocytogenes").replace("Jejuni", "jejuni")


# ---------------------------------------------------------------------------
# 4-step builder (already in blueprints.py but inline here too for clarity)
# ---------------------------------------------------------------------------
def four_step(eid, prompt, trim, asm, typing1, typing2, cmp, genus_species, notes=""):
    c1 = _build_typing_call(typing1)
    c2 = _build_typing_call(typing2)
    emit = ASM_EMIT[asm]
    nf = _nf_header([trim, asm, typing1, typing2]) + textwrap.dedent(f"""
        workflow {{
            trimmed   = {trim}(getSingleInput()).trimmed
            assembled = {asm}(trimmed).{emit}
            {c1}
            {c2}
        }}
    """).strip() + "\n"
    return Example(
        eid=eid, category="4step", prompt=prompt,
        nextflow_code=nf,
        params=_params_fastq(cmp, genus_species),
        inputs=[f"fastq_paired:{cmp}"],
        expected_processes=PROCS[trim] + PROCS[asm] + PROCS[typing1] + PROCS[typing2],
        notes=notes,
    )


# 5-step builder: trim + asm + 3 downstream in parallel
def five_step(eid, prompt, trim, asm, downstream: list[str], cmp, genus_species, notes=""):
    calls = "\n            ".join(_build_typing_call(s) for s in downstream)
    emit = ASM_EMIT[asm]
    nf = _nf_header([trim, asm, *downstream]) + textwrap.dedent(f"""
        workflow {{
            trimmed   = {trim}(getSingleInput()).trimmed
            assembled = {asm}(trimmed).{emit}
            {calls}
        }}
    """).strip() + "\n"
    expected = PROCS[trim] + PROCS[asm] + sum(PROCS[s] for s in downstream)
    return Example(
        eid=eid, category="5step", prompt=prompt,
        nextflow_code=nf,
        params=_params_fastq(cmp, genus_species),
        inputs=[f"fastq_paired:{cmp}"],
        expected_processes=expected,
        notes=notes,
    )


# ---------------------------------------------------------------------------
# build_extended() — returns 150 new examples to append to blueprints.build_all()
# ---------------------------------------------------------------------------
def build_extended() -> list[Example]:
    L: list[Example] = []
    seen_eids: set[str] = set()

    def add(ex: Example):
        if ex.eid in seen_eids:
            raise ValueError(f"duplicate eid {ex.eid}")
        seen_eids.add(ex.eid)
        L.append(ex)

    species_supported_chewbbaca = ["listeria_monocytogenes", "escherichia_coli", "salmonella_enterica"]
    species_supported_flaa = ["campylobacter_jejuni"]
    species_any = ["listeria_monocytogenes", "escherichia_coli", "salmonella_enterica",
                   "campylobacter_jejuni"]

    cmp_counter = {"lis": 100, "eco": 100, "sal": 100, "cam": 100, "cco": 100}
    def make_cmp(species: str) -> str:
        s = _short(species)
        n = cmp_counter[s]
        cmp_counter[s] += 1
        return f"2026.{s.upper()}.{n}.1.1"

    # =========================================================================
    # K. More 3-step chains: trim x asm x typing/AMR/annotation x species (60)
    # =========================================================================
    typing_for_chains = [
        ("step_4TY_MLST__mlst",       "MLST typing"),
        ("step_4TY_cgMLST__chewbbaca","cgMLST allelic profiling"),
        ("step_4AN_AMR__abricate",    "ABRicate AMR screening"),
        ("step_4AN_genes__prokka",    "Prokka annotation"),
        ("step_4TY_flaA__flaA",       "flaA typing"),
        ("step_4AN_AMR__staramr",     "staramr AMR profiling"),
    ]

    k_idx = 0
    for trim in TRIMMERS:
        for asm in ASSEMBLERS_ILLUMINA:
            for typing_step, typing_label in typing_for_chains:
                for sp in species_any:
                    if not is_species_compat(typing_step, sp):
                        continue
                    k_idx += 1
                    if k_idx > 60:
                        break
                    cmp = make_cmp(sp)
                    trim_name = trim.rsplit("__", 1)[-1]
                    asm_name = asm.rsplit("__", 1)[-1]
                    add(trim_assembly_typing(
                        eid=f"K{k_idx:02d}_{typing_step.split('__')[-1]}_{_short(sp)}_{trim_name}_{asm_name}",
                        prompt=f"{typing_label} on {_species_label(sp)} from paired-end Illumina FASTQ ({trim_name} + {asm_name} + {typing_step.split('__')[-1]}).",
                        trim_step=trim, asm_step=asm, typing_step=typing_step,
                        cmp=cmp, genus_species=sp,
                        category=f"3step.K",
                        notes=f"combinatorial expansion: {trim_name} x {asm_name} x {typing_step.split('__')[-1]} x {_short(sp)}",
                    ))
                if k_idx > 60:
                    break
            if k_idx > 60:
                break
        if k_idx > 60:
            break

    # =========================================================================
    # L. 4-step chains: trim + asm + 2 downstream in parallel  (20)
    # =========================================================================
    l_combos = [
        # (typing1, typing2, species)
        ("step_4TY_MLST__mlst",       "step_4TY_cgMLST__chewbbaca",  "listeria_monocytogenes"),
        ("step_4TY_MLST__mlst",       "step_4TY_cgMLST__chewbbaca",  "escherichia_coli"),
        ("step_4TY_MLST__mlst",       "step_4TY_cgMLST__chewbbaca",  "salmonella_enterica"),
        ("step_4TY_MLST__mlst",       "step_4AN_AMR__abricate",      "listeria_monocytogenes"),
        ("step_4TY_MLST__mlst",       "step_4AN_AMR__abricate",      "escherichia_coli"),
        ("step_4TY_cgMLST__chewbbaca","step_4AN_AMR__abricate",      "listeria_monocytogenes"),
        ("step_4TY_cgMLST__chewbbaca","step_4AN_genes__prokka",      "listeria_monocytogenes"),
        ("step_4TY_cgMLST__chewbbaca","step_4AN_genes__prokka",      "salmonella_enterica"),
        ("step_4TY_MLST__mlst",       "step_4AN_genes__prokka",      "escherichia_coli"),
        ("step_4TY_MLST__mlst",       "step_4AN_genes__prokka",      "salmonella_enterica"),
        ("step_4AN_AMR__abricate",    "step_4AN_genes__prokka",      "listeria_monocytogenes"),
        ("step_4AN_AMR__abricate",    "step_4AN_genes__prokka",      "salmonella_enterica"),
        ("step_4TY_MLST__mlst",       "step_4TY_flaA__flaA",         "campylobacter_jejuni"),
        ("step_4TY_MLST__mlst",       "step_4AN_AMR__staramr",       "campylobacter_jejuni"),
        ("step_4TY_flaA__flaA",       "step_4AN_AMR__staramr",       "campylobacter_jejuni"),
        ("step_4TY_flaA__flaA",       "step_4AN_AMR__abricate",      "campylobacter_jejuni"),
        ("step_4AN_AMR__staramr",     "step_4AN_AMR__abricate",      "campylobacter_jejuni"),
        ("step_4AN_AMR__staramr",     "step_4AN_genes__prokka",      "campylobacter_jejuni"),
        ("step_4TY_flaA__flaA",       "step_4AN_genes__prokka",      "campylobacter_jejuni"),
        ("step_4TY_MLST__mlst",       "step_4AN_genes__prokka",      "listeria_monocytogenes"),
    ]
    for i, (t1, t2, sp) in enumerate(l_combos, start=1):
        cmp = make_cmp(sp)
        add(four_step(
            eid=f"L{i:02d}_{t1.split('__')[-1]}_{t2.split('__')[-1]}_{_short(sp)}",
            prompt=f"From paired Illumina FASTQ of {_species_label(sp)}: trim with fastp, assemble with SPAdes, then run {t1.split('__')[-1]} and {t2.split('__')[-1]} in parallel.",
            trim="step_1PP_trimming__fastp",
            asm="step_2AS_denovo__spades",
            typing1=t1, typing2=t2,
            cmp=cmp, genus_species=sp,
            notes="4-step: two downstream in parallel",
        ))

    # =========================================================================
    # M. 5-step chains: trim + asm + 3 downstream in parallel  (10)
    # =========================================================================
    m_combos = [
        (["step_4TY_MLST__mlst", "step_4TY_cgMLST__chewbbaca", "step_4AN_AMR__abricate"], "listeria_monocytogenes"),
        (["step_4TY_MLST__mlst", "step_4TY_cgMLST__chewbbaca", "step_4AN_genes__prokka"], "salmonella_enterica"),
        (["step_4TY_MLST__mlst", "step_4AN_AMR__abricate",     "step_4AN_genes__prokka"], "escherichia_coli"),
        (["step_4TY_MLST__mlst", "step_4AN_AMR__abricate",     "step_4AN_genes__prokka"], "listeria_monocytogenes"),
        (["step_4TY_MLST__mlst", "step_4TY_flaA__flaA",        "step_4AN_AMR__staramr"], "campylobacter_jejuni"),
        (["step_4TY_MLST__mlst", "step_4TY_flaA__flaA",        "step_4AN_AMR__abricate"], "campylobacter_jejuni"),
        (["step_4TY_flaA__flaA", "step_4AN_AMR__staramr",      "step_4AN_genes__prokka"], "campylobacter_jejuni"),
        (["step_4TY_MLST__mlst", "step_4AN_AMR__staramr",      "step_4AN_genes__prokka"], "campylobacter_jejuni"),
        (["step_4TY_cgMLST__chewbbaca", "step_4AN_AMR__abricate", "step_4AN_genes__prokka"], "listeria_monocytogenes"),
        (["step_4TY_cgMLST__chewbbaca", "step_4AN_AMR__abricate", "step_4AN_genes__prokka"], "escherichia_coli"),
    ]
    for i, (downstream, sp) in enumerate(m_combos, start=1):
        cmp = make_cmp(sp)
        names = "+".join(s.split("__")[-1] for s in downstream)
        add(five_step(
            eid=f"M{i:02d}_{names}_{_short(sp)}",
            prompt=f"Comprehensive typing+AMR+annotation pipeline for {_species_label(sp)} from paired Illumina FASTQ: trim, assemble, then run {', '.join(s.split('__')[-1] for s in downstream)} in parallel on the assembly.",
            trim="step_1PP_trimming__fastp",
            asm="step_2AS_denovo__spades",
            downstream=downstream,
            cmp=cmp, genus_species=sp,
            notes="5-step: three downstream in parallel",
        ))

    # =========================================================================
    # N. Cross-species sanity checks: same chain re-applied to many species (15)
    # =========================================================================
    canon_chain = ("step_1PP_trimming__fastp", "step_2AS_denovo__spades", "step_4TY_MLST__mlst")
    for i, sp in enumerate(species_any, start=1):
        cmp = make_cmp(sp)
        add(trim_assembly_typing(
            eid=f"N{i:02d}_canonical_mlst_{_short(sp)}",
            prompt=f"Canonical bacterial typing pipeline (fastp + SPAdes + mlst) on paired Illumina FASTQ of {_species_label(sp)}.",
            trim_step=canon_chain[0], asm_step=canon_chain[1], typing_step=canon_chain[2],
            cmp=cmp, genus_species=sp,
            category="3step.N",
            notes="cross-species canonical chain",
        ))

    # cgMLST cross-species (only on supported)
    for j, sp in enumerate(species_supported_chewbbaca, start=1):
        cmp = make_cmp(sp)
        add(trim_assembly_typing(
            eid=f"N0{j+4}_canonical_cgmlst_{_short(sp)}",
            prompt=f"Standard cgMLST pipeline (fastp + SPAdes + chewbbaca) on paired Illumina FASTQ of {_species_label(sp)}.",
            trim_step="step_1PP_trimming__fastp",
            asm_step="step_2AS_denovo__spades",
            typing_step="step_4TY_cgMLST__chewbbaca",
            cmp=cmp, genus_species=sp,
            category="3step.N",
            notes="cross-species cgMLST",
        ))

    # mono-typing from existing assembly, additional species (8)
    typing_assembly_combos = [
        ("step_4TY_MLST__mlst",         "campylobacter_jejuni"),
        ("step_4TY_MLST__mlst",         "salmonella_enterica"),
        ("step_4AN_AMR__abricate",      "listeria_monocytogenes"),
        ("step_4AN_AMR__abricate",      "salmonella_enterica"),
        ("step_4AN_AMR__abricate",      "campylobacter_jejuni"),
        ("step_4AN_genes__prokka",      "salmonella_enterica"),
        ("step_4AN_genes__prokka",      "campylobacter_jejuni"),
        ("step_4AN_genes__prokka",      "escherichia_coli"),
    ]
    for i, (st, sp) in enumerate(typing_assembly_combos, start=1):
        cmp = make_cmp(sp)
        add(mono_typing(
            eid=f"NA{i:02d}_{st.split('__')[-1]}_{_short(sp)}_assembly",
            prompt=f"Run {st.split('__')[-1]} on a pre-existing {_species_label(sp)} assembly.",
            step=st, cmp=cmp, genus_species=sp,
            category="mono-typing.N",
        ))

    # =========================================================================
    # O. More assembly variants (10)
    # =========================================================================
    assembly_only_extras = [
        ("step_2AS_denovo__spades",      "listeria_monocytogenes"),
        ("step_2AS_denovo__spades",      "salmonella_enterica"),
        ("step_2AS_denovo__spades",      "campylobacter_jejuni"),
        ("step_2AS_denovo__shovill",     "listeria_monocytogenes"),
        ("step_2AS_denovo__shovill",     "salmonella_enterica"),
        ("step_2AS_denovo__shovill",     "campylobacter_jejuni"),
        ("step_2AS_denovo__unicycler",   "listeria_monocytogenes"),
        ("step_2AS_denovo__unicycler",   "escherichia_coli"),
        ("step_2AS_denovo__unicycler",   "campylobacter_jejuni"),
        ("step_2AS_denovo__plasmidspades","escherichia_coli"),
    ]
    for i, (asm, sp) in enumerate(assembly_only_extras, start=1):
        cmp = make_cmp(sp)
        add(mono_assembly(
            eid=f"O{i:02d}_{asm.split('__')[-1]}_{_short(sp)}",
            prompt=f"De novo assembly with {asm.split('__')[-1]} from paired Illumina FASTQ of {_species_label(sp)}.",
            asm_step=asm, cmp=cmp,
            category="mono-assembly.O",
        ))

    # =========================================================================
    # P. Long-read Nanopore (chopper + flye) chains  (10)
    # =========================================================================
    p_combos = [
        ("step_4TY_MLST__mlst",       "listeria_monocytogenes"),
        ("step_4TY_MLST__mlst",       "salmonella_enterica"),
        ("step_4TY_MLST__mlst",       "escherichia_coli"),
        ("step_4TY_MLST__mlst",       "campylobacter_jejuni"),
        ("step_4AN_AMR__abricate",    "listeria_monocytogenes"),
        ("step_4AN_AMR__abricate",    "escherichia_coli"),
        ("step_4AN_AMR__abricate",    "salmonella_enterica"),
        ("step_4AN_genes__prokka",    "listeria_monocytogenes"),
        ("step_4TY_cgMLST__chewbbaca","listeria_monocytogenes"),
        ("step_4TY_cgMLST__chewbbaca","salmonella_enterica"),
    ]
    for i, (typing_step, sp) in enumerate(p_combos, start=1):
        cmp = make_cmp(sp)
        add(trim_assembly_typing(
            eid=f"P{i:02d}_chopper_flye_{typing_step.split('__')[-1]}_{_short(sp)}",
            prompt=f"Nanopore pipeline for {_species_label(sp)}: chopper trimming + Flye assembly + {typing_step.split('__')[-1]}.",
            trim_step="step_1PP_trimming__chopper",
            asm_step="step_2AS_denovo__flye",
            typing_step=typing_step,
            cmp=cmp, genus_species=sp,
            seq_type="nanopore",
            category="3step-nanopore.P",
        ))

    # =========================================================================
    # Q. Parallel branches: species ID + chain (10)
    # =========================================================================
    species_id_steps = ["step_3TX_species__kmerfinder", "step_3TX_species__mash"]
    q_idx = 0
    for sid in species_id_steps:
        for trim in ["step_1PP_trimming__fastp"]:
            for asm in ["step_2AS_denovo__spades", "step_2AS_denovo__shovill"]:
                for sp in ["listeria_monocytogenes", "escherichia_coli", "salmonella_enterica"]:
                    q_idx += 1
                    if q_idx > 10:
                        break
                    cmp = make_cmp(sp)
                    emit = ASM_EMIT[asm]
                    nf = _nf_header([sid, trim, asm]) + textwrap.dedent(f"""
                        workflow {{
                            raw = getSingleInput()
                            {sid}(raw)
                            trimmed   = {trim}(raw).trimmed
                            assembled = {asm}(trimmed).{emit}
                        }}
                    """).strip() + "\n"
                    p = _params_fastq(cmp)
                    p.update(SPECIES_ID_REQUIRED_PARAMS.get(sid, {}))
                    add(Example(
                        eid=f"Q{q_idx:02d}_{sid.split('__')[-1]}_{trim.split('__')[-1]}_{asm.split('__')[-1]}_{_short(sp)}",
                        category="3step-parallel.Q",
                        prompt=f"In parallel, identify the species with {sid.split('__')[-1]} and trim+assemble paired Illumina FASTQ of {_species_label(sp)} with {trim.split('__')[-1]} + {asm.split('__')[-1]}.",
                        nextflow_code=nf,
                        params=p,
                        inputs=[f"fastq_paired:{cmp}"],
                        expected_processes=PROCS[sid] + PROCS[trim] + PROCS[asm],
                        notes="species ID in parallel with trim+assembly",
                    ))
                if q_idx > 10: break
            if q_idx > 10: break
        if q_idx > 10: break

    # =========================================================================
    # R. More mono-step from FASTQ + db params (8)
    # =========================================================================
    extra_species_id = [
        ("step_3TX_species__kmerfinder", "campylobacter_jejuni"),
        ("step_3TX_species__kmerfinder", "salmonella_enterica"),
        ("step_3TX_species__mash",       "salmonella_enterica"),
        ("step_3TX_species__mash",       "escherichia_coli"),
        ("step_3TX_class__kraken2",      "listeria_monocytogenes"),
        ("step_3TX_class__kraken2",      "escherichia_coli"),
        ("step_3TX_class__kraken2",      "salmonella_enterica"),
        ("step_3TX_class__kraken2",      "campylobacter_jejuni"),
    ]
    for i, (sid, sp) in enumerate(extra_species_id, start=1):
        cmp = make_cmp(sp)
        add(mono_species_id(
            eid=f"R{i:02d}_{sid.split('__')[-1]}_{_short(sp)}",
            prompt=f"{sid.split('__')[-1]} on paired Illumina FASTQ of {_species_label(sp)}.",
            step=sid, cmp=cmp,
            category="mono-species-id.R",
        ))

    # =========================================================================
    # S. Trim-only + assembly-only (in isolation) (7)
    # =========================================================================
    trim_only_combos = [
        ("step_1PP_trimming__fastp",       "listeria_monocytogenes"),
        ("step_1PP_trimming__fastp",       "salmonella_enterica"),
        ("step_1PP_trimming__trimmomatic", "escherichia_coli"),
        ("step_1PP_trimming__trimmomatic", "campylobacter_jejuni"),
        ("step_1PP_trimming__chopper",     "listeria_monocytogenes"),
        ("step_1PP_trimming__chopper",     "salmonella_enterica"),
        ("step_1PP_trimming__chopper",     "campylobacter_jejuni"),
    ]
    for i, (trim, sp) in enumerate(trim_only_combos, start=1):
        cmp = make_cmp(sp)
        seq_type = "nanopore" if trim.endswith("chopper") else "illumina_paired"
        getter = "getInput" if trim != "step_1PP_trimming__chopper" else "getInput"
        nf = _nf_header([trim], use_getsingle=False) + textwrap.dedent(f"""
            workflow {{
                {trim}(getInput())
            }}
        """).strip() + "\n"
        kind = "fastq_paired" if seq_type == "illumina_paired" else "fastq_single"
        add(Example(
            eid=f"S{i:02d}_{trim.split('__')[-1]}_{_short(sp)}",
            category="mono-trim.S",
            prompt=f"{trim.split('__')[-1]} read trimming on {seq_type.replace('_', ' ')} FASTQ of {_species_label(sp)}.",
            nextflow_code=nf,
            params=_params_fastq(cmp, seq_type=seq_type),
            inputs=[f"{kind}:{cmp}"],
            expected_processes=PROCS[trim],
            notes="mono trimming",
        ))

    return L


if __name__ == "__main__":
    L = build_extended()
    print(f"Built {len(L)} extended examples")
    # check no duplicate IDs vs blueprints.build_all
    from dataset.blueprints import build_all
    base = build_all()
    base_ids = {e.eid for e in base}
    dupes = [e.eid for e in L if e.eid in base_ids]
    if dupes:
        print(f"DUPLICATE IDS with blueprints.build_all(): {dupes}")
    else:
        print("No duplicate IDs vs base 50.")
    total = len(base) + len(L)
    print(f"Combined total: {total}")
