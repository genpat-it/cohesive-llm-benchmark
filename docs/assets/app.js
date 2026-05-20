// Shared helpers for the cohesive-llm-benchmark static site.

const DATA = {
  SINGLE_TURN_DATASET: "data/dataset_50.jsonl",
  MULTI_TURN_DATASET: "data/dataset_modifications.jsonl",
  SINGLE_TURN_VERDICTS: "data/example_run_verdicts.jsonl",
  MULTI_TURN_VERDICTS: "data/example_run_verdicts_modifications.jsonl",
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
