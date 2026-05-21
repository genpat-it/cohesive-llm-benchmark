# Why an LLM, given a finite framework?

> *Paper-ready prose answering the strongest reviewer objection to this
> benchmark. Roughly 700 words. Drop into the manuscript's Related Work
> / Methodology / Discussion as needed.*

## The objection

A sharp reviewer will ask: *"`cohesive-ngsmanager` is a finite framework
with a known set of steps, parameters, and valid compositions. You can
in principle enumerate every valid pipeline combinatorially and build a
domain-specific language plus an ontology (EDAM, OBI, NCIt) for
grounding natural-language queries. A retriever over that enumeration,
augmented by an ontology, would be deterministic, cheaper, and free of
hallucination. Why use an LLM at all?"*

The objection is real. We address it in five steps: a concession, four
arguments that survive the concession, and one reframing.

## Concession

For the head of the prompt distribution — single-shot, well-specified,
canonically-phrased requests that map cleanly to a single enumerated
pipeline — we accept that a retriever over a generator's output,
augmented by a domain ontology, would outperform a general-purpose LLM
on every operational axis (cost, latency, determinism, refusal
behaviour). We do not claim LLMs supersede such systems on this regime.

## Arguments

**(1) The prompt space is open even when the pipeline space is closed.**
A finite catalog of pipelines admits an unbounded space of natural-
language prompts: synonyms (*"MLST"*, *"sequence typing"*, *"7-gene
typing"*), surface variants (*"campilobacter"*, *"C. jejuni"*,
*"Campy"*), code-mixing (Italian/English/Spanish in clinical labs), and
implicit intent (*"check whether it's the outbreak strain"*). A
retrieval baseline requires every variant in a synonyms list, which
presupposes that the user already knows the framework's canonical
vocabulary — defeating the purpose of natural-language interfaces.
LLMs handle surface variation by virtue of their pretraining; we
measure the residual error rate, we do not eliminate it.

**(2) Frameworks evolve.** `cohesive-ngsmanager`, like any production
bioinformatics platform, ships new steps, new species filters, and new
parameters with every release. A combinatorial enumerator must be
rebuilt and re-described per release, with human-written canonical
descriptions for every new pipeline. The cost scales with the catalog.
An LLM that has read the framework source can in principle adapt
without retraining a retriever; whether it actually does is empirically
testable, and the version-pinning machinery in this benchmark
(`metadata.json` per run, framework commit, dataset commit) is what
makes that test possible longitudinally.

**(3) Tacit biomedical knowledge the framework does not encode.** The
framework lists ~60 steps; it does not encode that `fastp` is adapter-
trimming, that `unicycler` performs no internal trimming, or that
*Listeria* (gram-positive cultured isolates) makes a poor case for
host-depletion against the human genome. The LLM brings this knowledge
from pretraining on biomedical corpora — for free. Empirical evidence:
of 200 single-turn prompts, the LLM spontaneously inserts upstream
best-practice steps in 18 cases (tag `extras-best-practice`),
producing pipelines that are bioinformatically sound but absent from
the literal prompt. A retriever cannot interpolate; a generator+
ontology approach would require explicit ontology engineering of
"best-practice" relations as a second framework. We quantify this gap.

**(4) Multi-turn refinement is not a retrieval problem.** The most
common real interaction is incremental edit: *"now add MLST"*,
*"swap unicycler for shovill"*, *"actually I'm doing nanopore"*. That
is a stateful operation over a structured artifact with conversational
memory — program synthesis, not nearest-neighbour lookup. Our 159-
conversation multi-turn corpus measures this directly; the conversation
-level fully-passing rate (136/159 = 85.5%) versus single-turn pass
rate (185/200 = 92.5%) **quantifies state degradation in pipeline-
generation tasks** in a way the field has not had before.

## Reframing — the contribution is the protocol

We do not argue that LLMs replace combinatorial generation. We argue
that the `nextflow -stub-run`-validated benchmark protocol — with
verdict tagging, version pinning, full chat-log transparency, and a
unified manifest (`docs/data/benchmark.json`) — is the right way to
measure *any* natural-language → pipeline system. The protocol applies
equally to retrievers, hybrid retriever+LLM systems, generator+
ontology+grounding-LLM systems, and agentic decomposers. The
deterministic generator (`blueprints.py`) **is** the ground truth in
our methodology — by design, not by accident.

This reframing dissolves the objection. The reviewer's "why an LLM?"
becomes "what NL system best serves users on top of this protocol?" —
which is the very question this benchmark exists to answer for any
candidate system, including the generator+ontology system the reviewer
proposes. We invite that comparison.
