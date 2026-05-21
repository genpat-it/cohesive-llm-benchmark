#!/usr/bin/env python3.11
"""
Multi-sample workflow blueprints.

These exercise the `multi/multi_*` workflows of cohesive-ngsmanager:
clustering (grapetree, cfsan, vcf2mst, reportree*), pangenome (panaroo),
alignment (snippycore).

Multi-sample inputs are passed via the `params.input` array (one
{cmp, riscd} entry per sample) so getInput()/getVCFs()/etc. collects
across samples.

Each blueprint:
  - generates the workflow {} code that calls the multi workflow
  - declares the right input layouts so the harness materialises the
    expected per-sample result files (GFF for panaroo, .vcf for vcf2mst,
    cgMLST allele tsv for grapetree, ...)
  - supplies any required params (metadata/geodata paths, kmers_size, ...)
"""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from harness.harness import Example   # noqa: E402

# ---------------------------------------------------------------------------
# Helpers: tiny placeholder files for metadata/geodata that params point at
# ---------------------------------------------------------------------------
_PLACEHOLDER_META = "/tmp/_bench_meta.csv"
_PLACEHOLDER_GEO  = "/tmp/_bench_geo.tsv"


# Placeholder values for the many param('multi_clustering__reportree__...') calls.
# In nextflow.config these are all defaulted to '', which makes the strict
# param() helper exit 2 -- so we explicitly pass non-empty stubs.
REPORTREE_STUB_PARAMS = {
    "multi_clustering__reportree__summary_columns":      "strain,date",
    "multi_clustering__reportree__summary_sample_column":"strain",
    "multi_clustering__reportree__summary_geo_column":   "region",
    "multi_clustering__reportree__summary_date_aliases": "none_alias/none_alias",
    "multi_clustering__reportree__thr":                  "single",
    "multi_clustering__reportree__loci_called":          "0.99",
    "multi_clustering__reportree__site_inclusion":       "0.99",
    "multi_clustering__reportree__HC_threshold":         "single",
    "multi_clustering__reportree__report_threshold":     "0",
    "multi_clustering__reportree__nomenclature":         "",
    "multi_clustering__reportree__sample_of_interest":   "",
    "multi_clustering__reportree__zoom_cluster_of_interest": "",
    "multi_clustering__reportree__extra":                "",
}


def _placeholder_files() -> None:
    """Materialise minimal metadata + geodata files so param('metadata')/...
    can be passed as a path that exists."""
    from pathlib import Path as _P
    m = _P(_PLACEHOLDER_META)
    if not m.exists():
        m.write_text("strain,date,region,country\nsample1,2024-01-01,EU,IT\n")
    g = _P(_PLACEHOLDER_GEO)
    if not g.exists():
        g.write_text("country\tregion\tlatitude\tlongitude\nIT\tEU\t42.0\t12.0\n")


# ---------------------------------------------------------------------------
# blueprint helpers
# ---------------------------------------------------------------------------
def _multi_header(*includes, **named) -> str:
    """workflow header including the multi-workflow(s).

    Positional args: <workflow_name> (file basename == workflow basename).
    Keyword args: <workflow_name>="<file_basename>" -- used when the workflow
    exported by a file has a *different* name from the file itself
    (e.g. multi_clustering__reportree_alleles.nf exports
    'multi_clustering__reportree').
    """
    inc_lines = [f"include {{ {x} }} from '../multi/{x}'" for x in includes]
    inc_lines += [f"include {{ {wf} }} from '../multi/{fn}'" for wf, fn in named.items()]
    return ("nextflow.enable.dsl=2\n\n"
            + "include { getInput; getVCFs; param; optionalOrDefault; getReferenceUnkeyed } from '../functions/parameters.nf'\n"
            + "\n".join(inc_lines) + "\n")


def _input_array(cmps: list[str], riscd: str) -> list[dict]:
    return [{"cmp": c, "riscd": riscd} for c in cmps]


# ---------------------------------------------------------------------------
def build_multi_workflows() -> list[Example]:
    _placeholder_files()
    L: list[Example] = []

    # -- panaroo: take = input (gff files from prokka) -----------------------
    panaroo_cmps = ["2026.MULTI.PANGE.1.1", "2026.MULTI.PANGE.2.1",
                    "2026.MULTI.PANGE.3.1"]
    riscd_gff = "260224-99999-4AN_genes-prokka"
    L.append(Example(
        eid="X01_multi_pangenome_panaroo_listeria",
        category="multi.pangenome",
        prompt="Pangenome analysis with panaroo across multiple Listeria monocytogenes assemblies, each previously annotated with Prokka.",
        nextflow_code=_multi_header("multi_pangenome__panaroo") + textwrap.dedent("""
            workflow {
                multi_pangenome__panaroo(getInput())
            }
        """).strip() + "\n",
        params={
            "cmp": panaroo_cmps[0],
            "input": _input_array(panaroo_cmps, riscd_gff),
            "genus_species": "listeria_monocytogenes",
        },
        inputs=[f"gff:{c}" for c in panaroo_cmps],
        expected_processes=1,   # just `panaroo`
        notes="multi-sample pangenome from 3 prokka-annotated assemblies",
    ))

    # -- vcf2mst: take = input (vcf files) -----------------------------------
    vcf_cmps = ["2026.MULTI.VCF.1.1", "2026.MULTI.VCF.2.1", "2026.MULTI.VCF.3.1"]
    riscd_vcf = "260224-99999-2AS_mapping-snippy"
    L.append(Example(
        eid="X02_multi_clustering_vcf2mst",
        category="multi.clustering",
        prompt="Build a minimum spanning tree from per-sample VCF files using vcf2mst (multi-sample clustering).",
        nextflow_code=_multi_header("multi_clustering__vcf2mst") + textwrap.dedent("""
            workflow {
                getVCFs()
                    .map { it[1] }
                    .collect()
                    .set { inputSet }
                multi_clustering__vcf2mst(inputSet)
            }
        """).strip() + "\n",
        params={
            "cmp": vcf_cmps[0],
            "input": _input_array(vcf_cmps, riscd_vcf),
        },
        inputs=[f"vcf:{c}" for c in vcf_cmps],
        expected_processes=2,   # vcf2mst + dists
        notes="multi-sample MST from snippy VCFs",
    ))

    # -- grapetree: take = (input, metadata, geodata) ------------------------
    # NOTE: grapetree also reads several `multi_clustering__reportree__*`
    # params at file-include time (shared metadata logic), so we have to
    # pass the same reportree stubs even for grapetree.
    allele_cmps = ["2026.MULTI.GRAPE.1.1", "2026.MULTI.GRAPE.2.1",
                   "2026.MULTI.GRAPE.3.1"]
    riscd_alleles = "260224-99999-4TY_cgMLST-chewbbaca"
    L.append(Example(
        eid="X03_multi_clustering_grapetree_listeria",
        category="multi.clustering",
        prompt="cgMLST-based clustering of multiple Listeria monocytogenes samples with grapetree, after their allelic profiles were generated.",
        nextflow_code=_multi_header("multi_clustering__grapetree") + textwrap.dedent("""
            workflow {
                multi_clustering__grapetree(getInput(), param('metadata'), param('geodata'))
            }
        """).strip() + "\n",
        params={
            "cmp": allele_cmps[0],
            "input": _input_array(allele_cmps, riscd_alleles),
            "metadata": _PLACEHOLDER_META,
            "geodata":  _PLACEHOLDER_GEO,
            **REPORTREE_STUB_PARAMS,
        },
        inputs=[f"alleles:{c}" for c in allele_cmps],
        expected_processes=2,   # extract_cgMLST + dists  (grapetree, augur try real cmd)
        notes="multi-sample grapetree from cgMLST allele profiles",
    ))

    # -- reportree_alleles ---------------------------------------------------
    L.append(Example(
        eid="X04_multi_clustering_reportree_alleles_listeria",
        category="multi.clustering",
        prompt="ReporTree clustering on the allelic profiles of several Listeria samples.",
        nextflow_code=_multi_header(
            multi_clustering__reportree="multi_clustering__reportree_alleles"
        ) + textwrap.dedent("""
            workflow {
                multi_clustering__reportree(getInput(),
                                            param('metadata'),
                                            param('geodata'),
                                            optionalOrDefault('multi_clustering__reportree__nomenclature', ''))
            }
        """).strip() + "\n",
        params={
            "cmp": allele_cmps[0],
            "input": _input_array(allele_cmps, riscd_alleles),
            "metadata": _PLACEHOLDER_META,
            "geodata":  _PLACEHOLDER_GEO,
            **REPORTREE_STUB_PARAMS,
        },
        inputs=[f"alleles:{c}" for c in allele_cmps],
        expected_processes=1,
        notes="reportree (allelic) across 3 Listeria samples",
    ))

    # -- reportree_vcf -------------------------------------------------------
    L.append(Example(
        eid="X05_multi_clustering_reportree_vcf",
        category="multi.clustering",
        prompt="ReporTree clustering of multiple samples starting from their VCFs.",
        nextflow_code=_multi_header(
            multi_clustering__reportree="multi_clustering__reportree_vcf"
        ) + textwrap.dedent("""
            workflow {
                multi_clustering__reportree(getVCFs(),
                                            param('metadata'),
                                            param('geodata'),
                                            optionalOrDefault('multi_clustering__reportree__nomenclature', ''))
            }
        """).strip() + "\n",
        params={
            "cmp": vcf_cmps[0],
            "input": _input_array(vcf_cmps, riscd_vcf),
            "metadata": _PLACEHOLDER_META,
            "geodata":  _PLACEHOLDER_GEO,
            **REPORTREE_STUB_PARAMS,
        },
        inputs=[f"vcf:{c}" for c in vcf_cmps],
        expected_processes=1,
        notes="reportree (vcf-based) across 3 samples",
    ))

    return L


if __name__ == "__main__":
    L = build_multi_workflows()
    print(f"Built {len(L)} multi-workflow blueprints")
    for ex in L:
        print(f"  {ex.eid}  ({ex.category})")
