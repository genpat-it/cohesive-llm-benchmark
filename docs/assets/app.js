// Shared helpers for the cohesive-llm-benchmark static site.

const DATA = {
  SINGLE_TURN_DATASET: "data/dataset_50.jsonl",
  MULTI_TURN_DATASET: "data/dataset_modifications.jsonl",
  // Augmented verdicts carry verdict_tags + llm_full_reply + llm_turn_logs.
  SINGLE_TURN_VERDICTS: "data/example_run_mistral_verdicts_augmented.jsonl",
  MULTI_TURN_VERDICTS: "data/example_run_mistral_multi_turn_verdicts_augmented.jsonl",
  SINGLE_TURN_METADATA: "data/example_run_metadata.json",
  MULTI_TURN_METADATA: "data/example_run_metadata_multi_turn.json",
  FULL_SINGLE_VERDICTS: "data/llm_full_200_verdicts_augmented.jsonl",
  FULL_MULTI_VERDICTS:  "data/llm_full_multi_turn_verdicts_augmented.jsonl",
};

/* --- jsonl loader -------------------------------------------------------- */
async function loadJsonl(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`fetch ${url}: ${r.status}`);
  const txt = await r.text();
  return txt.split("\n").filter(l => l.trim()).map(l => JSON.parse(l));
}

/* --- escape -------------------------------------------------------------- */
function esc(s) {
  return (s == null ? "" : String(s))
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

/* --- category pill ------------------------------------------------------- */
function passPill(b) {
  if (b === null || b === undefined) return `<span class="pill muted">—</span>`;
  return b ? `<span class="pill pass">PASS</span>` : `<span class="pill fail">FAIL</span>`;
}

/* --- format steps ------------------------------------------------------- */
function fmtSteps(arr) {
  if (!arr || !arr.length) return "<em>none</em>";
  return arr.map(s => `<code>${esc(s)}</code>`).join(", ");
}

/* --- verdict tags chips ------------------------------------------------- */
const TAG_TITLE = {
  "literal-match":          "LLM steps match the ground truth exactly",
  "extras-best-practice":   "LLM added upstream best-practice steps (trimming, species-id, host-depletion, ...)",
  "extras-irrelevant":      "LLM added steps that are not a common best-practice add-on",
  "missing-steps":          "LLM left out required ground-truth steps",
  "hallucinated":           "LLM used step/include names that don't exist in the framework",
  "upstream-rate-limited":  "Upstream API (Mistral) returned a 429 rate-limit error -- not a model quality failure",
};
function tagChips(tags) {
  if (!tags || !tags.length) return "";
  return tags.map(t =>
    `<span class="tag ${esc(t)}" title="${esc(TAG_TITLE[t] || t)}">${esc(t)}</span>`
  ).join("");
}

/* --- summary numbers ---------------------------------------------------- */
function summaryStats(verdicts) {
  const n = verdicts.length;
  const pass = verdicts.filter(v => v.semantic_valid).length;
  const code = verdicts.filter(v => v.nextflow_code).length;
  const syntax = verdicts.filter(v => v.syntax_valid).length;
  const halluc = verdicts.filter(v => v.hallucinated_steps && v.hallucinated_steps.length).length;
  return {
    total: n,
    code,
    syntax,
    semantic: pass,
    pct: n ? Math.round((pass / n) * 100) : 0,
    hallucinated: halluc,
  };
}

/* --- error category breakdown ------------------------------------------- */
function errorBreakdown(verdicts) {
  const c = {};
  for (const v of verdicts) {
    const k = v.error_category || "—";
    c[k] = (c[k] || 0) + 1;
  }
  return Object.entries(c).sort((a, b) => b[1] - a[1]);
}

/* --- metadata banner ---------------------------------------------------- */
async function loadMeta(url) {
  try { const r = await fetch(url); return r.ok ? await r.json() : null; }
  catch (e) { return null; }
}

function commitLink(remote, sha, branch) {
  if (!sha) return "";
  let url = remote;
  if (url) {
    // normalise git@ → https
    url = url.replace(/^git@github\.com:/, "https://github.com/").replace(/\.git$/, "");
    if (url.includes("github.com")) url += `/commit/${sha}`;
  }
  const short = sha.slice(0, 7);
  const label = branch ? `${short} (${branch})` : short;
  return url ? `<a href="${esc(url)}" target="_blank"><code>${esc(label)}</code></a>` : `<code>${esc(label)}</code>`;
}

function metaBanner(meta, dataset_name) {
  if (!meta) return "";
  const b = meta.bench || {}, f = meta.framework || {}, l = meta.llm || {};
  return `
    <div class="meta-banner">
      <div class="meta-title">Pinned version of this run · <span class="meta-time">${esc(meta.run_started_at || "?")}</span></div>
      <div class="meta-grid">
        <div><span class="meta-key">LLM</span>
          ${l.name ? `<code>${esc(l.name)}</code>` : ""}
          ${l.model ? ` · model <code>${esc(l.model)}</code>` : ""}
          ${l.commit ? ` · ${commitLink(l.remote, l.commit, l.branch)}` : ""}
        </div>
        <div><span class="meta-key">Framework</span> ${commitLink(f.remote, f.commit, f.branch) || "?"}</div>
        <div><span class="meta-key">Bench</span> ${commitLink(b.remote, b.commit, b.branch) || "?"}</div>
        <div><span class="meta-key">Dataset</span> <code>${esc(meta.dataset || dataset_name || "?")}</code></div>
      </div>
      ${meta.notes ? `<div class="meta-notes">${esc(meta.notes)}</div>` : ""}
    </div>`;
}

/* --- reproduce commands for an example ---------------------------------- */
function escShell(s) {
  return String(s).replace(/'/g, "'\\''");
}

function reproduceSnippet(d) {
  // Heuristic 1: detect if it's a mono-step from FASTQ → can use ngsmanager_run.sh CLI
  const steps = d.called_steps || d.ground_truth_steps || [];
  const isMonoStep = steps.length === 1;
  const monoStep = isMonoStep ? steps[0] : null;
  const usesFastqPaired = d.params && d.params.seq_type === "illumina_paired";

  // Pretty params.json (one-line per key)
  const paramsStr = JSON.stringify(d.params || {}, null, 2);

  // Always: bare nextflow snippet — works for every example
  let bare = `# 1) Make sure NGSMANAGER_DIR points at your cohesive-ngsmanager checkout\n`
           + `export NGSMANAGER_DIR=/path/to/cohesive-ngsmanager\n\n`
           + `# 2) Save the ground-truth pipeline\n`
           + `cat > "$NGSMANAGER_DIR/pipelines/${esc(d.id || "this")}.nf" <<'EOF'\n`
           + `${(d.ground_truth_code || "").trimEnd()}\nEOF\n\n`
           + `# 3) Save params + run nextflow stub-run\n`
           + `cat > /tmp/${esc(d.id || "params")}_params.json <<'EOF'\n${paramsStr}\nEOF\n`
           + `\ncd "$NGSMANAGER_DIR"\nnextflow run pipelines/${esc(d.id || "this")}.nf -stub-run \\\n  -params-file /tmp/${esc(d.id || "params")}_params.json`;

  // Optional: ngsmanager_run.sh shortcut for mono-step FASTQ examples
  let cli = "";
  if (isMonoStep && usesFastqPaired) {
    const gs = d.params.genus_species ? ` --genus_species ${escShell(d.params.genus_species)}` : "";
    cli = `# Requires cohesive-ngsmanager-cli (https://github.com/genpat-it/cohesive-ngsmanager-cli)\n`
        + `./ngsmanager_run.sh \\\n  cohesive-ngsmanager/steps/${esc(monoStep)}.nf \\\n  sample_R1.fastq.gz sample_R2.fastq.gz${gs}`;
  } else if (isMonoStep && d.params && d.params.input) {
    cli = `# (Mono-step on an existing assembly — supply via ngsmanager_run.sh or feed the .nf directly above.)`;
  }

  return `
    <details class="reproduce">
      <summary>Reproduce this example on the command line</summary>
      <div class="reproduce-body">
        <div class="reproduce-section">
          <div class="reproduce-label">Bare nextflow stub-run (works for every example)</div>
          <pre>${esc(bare)}</pre>
        </div>
        ${cli ? `<div class="reproduce-section">
          <div class="reproduce-label">Or via the ngsmanager-cli wrapper</div>
          <pre>${esc(cli)}</pre>
        </div>` : ""}
      </div>
    </details>`;
}
