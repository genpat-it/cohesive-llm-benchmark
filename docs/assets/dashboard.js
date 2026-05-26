/* Dashboard SPA: cross-model KPI + drill-down.
 * Reads docs/data/dashboard.json (pre-computed) for the aggregate charts,
 * and lazy-loads the augmented verdicts of the currently selected model when
 * the user opens the drill-down table.
 *
 * URL hash carries the selected state so links are shareable:
 *   #model=labs-devstral-small-2512&corpus=multi&error=silent_no_op&species=ecoli
 */

const SPECIES_ORDER = ["listeria", "ecoli", "salmonella", "campylobacter", "other"];

const STATE = {
  dashboard: null,         // dashboard.json
  modelKey: null,          // index key into STATE.dashboard.models
  cachedVerdicts: {},      // { run_id: rows[] }
  filters: {
    corpus: "multi",
    outcome: "",
    error: "",
    species: "",
    kind: "",
    tag: "",
    text: "",
  },
  selected: null,          // currently-open detail row
};

const CHARTS = {};

/* ----- helpers ----- */
function $(id) { return document.getElementById(id); }
function el(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "className") node.className = v;
    else if (k === "onClick") node.addEventListener("click", v);
    else if (v != null) node.setAttribute(k, v);
  }
  for (const c of children) {
    if (c == null) continue;
    node.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
  }
  return node;
}
function pct(n, d) { return d ? Math.round(100 * n / d) : 0; }
function speciesOf(id) {
  const low = (id || "").toLowerCase();
  if (/_lis(_|$)|listeria/.test(low)) return "listeria";
  if (/_eco(_|$)|ecoli/.test(low)) return "ecoli";
  if (/_sal(_|$)|salmonella/.test(low)) return "salmonella";
  if (/_cam(_|$)|campylobacter/.test(low)) return "campylobacter";
  return "other";
}

/* ----- URL state sync ----- */
function readHash() {
  const h = location.hash.replace(/^#/, "");
  if (!h) return {};
  return Object.fromEntries(new URLSearchParams(h));
}
function writeHash() {
  const p = new URLSearchParams();
  if (STATE.modelKey) p.set("model", STATE.modelKey);
  for (const [k, v] of Object.entries(STATE.filters)) {
    if (v) p.set(k, v);
  }
  if (STATE.selected) p.set("row", STATE.selected);
  const newHash = "#" + p.toString();
  if (newHash !== location.hash) history.replaceState(null, "", location.pathname + newHash);
}

/* ----- main ----- */
async function init() {
  // load aggregate
  const r = await fetch("data/dashboard.json");
  STATE.dashboard = await r.json();
  $("data-stamp").textContent = STATE.dashboard.generated_at;

  // populate model picker
  const sel = $("model-picker");
  STATE.dashboard.models.forEach((m, i) => {
    sel.appendChild(el("option", { value: m.key }, m.model_name));
  });

  // apply hash / defaults
  const hash = readHash();
  STATE.modelKey = hash.model || STATE.dashboard.models[0].key;
  sel.value = STATE.modelKey;
  for (const k of Object.keys(STATE.filters)) {
    if (hash[k]) STATE.filters[k] = hash[k];
  }
  // sync filter inputs from STATE
  $("f-corpus").value = STATE.filters.corpus;
  $("f-outcome").value = STATE.filters.outcome;
  $("f-species").value = STATE.filters.species;
  $("f-kind").value = STATE.filters.kind;
  $("f-tag").value = STATE.filters.tag;
  $("f-text").value = STATE.filters.text;

  // wire change handlers
  sel.addEventListener("change", () => { STATE.modelKey = sel.value; onModelChange(); });
  $("f-corpus").addEventListener("change", e => { STATE.filters.corpus = e.target.value; onFilterChange(); });
  $("f-outcome").addEventListener("change", e => { STATE.filters.outcome = e.target.value; onFilterChange(); });
  $("f-error").addEventListener("change", e => { STATE.filters.error = e.target.value; onFilterChange(); });
  $("f-species").addEventListener("change", e => { STATE.filters.species = e.target.value; onFilterChange(); });
  $("f-kind").addEventListener("change", e => { STATE.filters.kind = e.target.value; onFilterChange(); });
  $("f-tag").addEventListener("change", e => { STATE.filters.tag = e.target.value; onFilterChange(); });
  $("f-text").addEventListener("input", e => { STATE.filters.text = e.target.value; onFilterChange(); });

  // detail panel close
  $("detail-close").addEventListener("click", closeDetail);
  $("detail-overlay").addEventListener("click", closeDetail);

  await onModelChange();
}

function currentModel() {
  return STATE.dashboard.models.find(m => m.key === STATE.modelKey);
}

async function onModelChange() {
  renderKpis();
  renderPickerMeta();
  renderErrorChart();
  renderKindChart();
  populateErrorFilter();
  renderPassRatesChart();   // cross-model, redrawn for highlight
  renderHeatmap();
  await loadVerdictsAndRenderTable();
  writeHash();
}

async function onFilterChange() {
  await loadVerdictsAndRenderTable();
  writeHash();
}

/* ----- KPIs ----- */
function renderKpis() {
  const m = currentModel();
  const st = m.single_turn?.headline;
  const mtTurns = m.multi_turn?.headline?.turns;
  const mtConvs = m.multi_turn?.headline?.convs;
  $("kpi-st-pct").textContent = st ? `${st.pct}%` : "—";
  $("kpi-st-frac").textContent = st ? `${st.passed} / ${st.total}` : "no single-turn data";
  $("kpi-mt-pct").textContent = mtTurns ? `${mtTurns.pct}%` : "—";
  $("kpi-mt-frac").textContent = mtTurns ? `${mtTurns.passed} / ${mtTurns.total}` : "no multi-turn data";
  $("kpi-conv-pct").textContent = mtConvs ? `${mtConvs.pct}%` : "—";
  $("kpi-conv-frac").textContent = mtConvs ? `${mtConvs.full_pass} / ${mtConvs.total} convs` : "";

  // silent_no_op rate (multi-turn, since that is what we discuss most)
  const sno = m.multi_turn?.by_error?.silent_no_op || 0;
  const denom = mtTurns?.total || 0;
  $("kpi-sno-pct").textContent = denom ? `${pct(sno, denom)}%` : "—";
  $("kpi-sno-frac").textContent = denom ? `${sno} of ${denom} turns` : "";
}

function renderPickerMeta() {
  const m = currentModel();
  const meta = [];
  if (m.single_run_id) meta.push(`single: <code>${m.single_run_id}</code>`);
  if (m.multi_run_id)  meta.push(`multi: <code>${m.multi_run_id}</code>`);
  $("picker-meta").innerHTML = meta.join(" · ");
}

/* ----- error filter dropdown ----- */
function populateErrorFilter() {
  const m = currentModel();
  const corpus = STATE.filters.corpus;
  const errors = corpus === "single" ? (m.single_turn?.by_error || {}) : (m.multi_turn?.by_error || {});
  const sel = $("f-error");
  const prev = STATE.filters.error;
  sel.innerHTML = '<option value="">all</option>';
  for (const k of Object.keys(errors)) {
    sel.appendChild(el("option", { value: k }, `${k} (${errors[k]})`));
  }
  sel.value = prev;
}

/* ----- charts ----- */
function destroyChart(key) {
  if (CHARTS[key]) { CHARTS[key].destroy(); delete CHARTS[key]; }
}

function renderPassRatesChart() {
  destroyChart("passRates");
  const labels = STATE.dashboard.models.map(m => m.model_name);
  const stPct = STATE.dashboard.models.map(m => m.single_turn?.headline?.pct || 0);
  const mtPct = STATE.dashboard.models.map(m => m.multi_turn?.headline?.turns?.pct || 0);
  const convPct = STATE.dashboard.models.map(m => m.multi_turn?.headline?.convs?.pct || 0);
  const highlightIdx = STATE.dashboard.models.findIndex(m => m.key === STATE.modelKey);
  const accent = (base, ix) => labels.map((_, i) => i === highlightIdx ? base : base + "80");
  CHARTS.passRates = new Chart($("chart-pass-rates"), {
    type: "bar",
    data: {
      labels,
      datasets: [
        { label: "single-turn",  data: stPct,   backgroundColor: accent("#0B3A5E") },
        { label: "multi-turn turns", data: mtPct, backgroundColor: accent("#1d5887") },
        { label: "conv full-pass", data: convPct, backgroundColor: accent("#27AE60") },
      ],
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { position: "bottom" } },
      scales: { y: { beginAtZero: true, max: 100, ticks: { callback: v => v + "%" } } },
    },
  });
}

function renderErrorChart() {
  destroyChart("errors");
  const m = currentModel();
  const corpus = STATE.filters.corpus;
  const errors = corpus === "single" ? (m.single_turn?.by_error || {}) : (m.multi_turn?.by_error || {});
  const entries = Object.entries(errors).sort((a, b) => b[1] - a[1]);
  const colors = { none: "#27AE60", silent_no_op: "#C0392B", missing_param: "#D3681B",
                   no_code: "#7f8c8d", file_not_found: "#9b59b6", arity_error: "#e67e22",
                   ngsmanager_naming: "#16a085", partial_dag: "#f39c12",
                   channel_emit: "#8e44ad", unknown: "#555" };
  $("err-model-label").textContent = `${m.model_name} · ${corpus}-turn`;
  CHARTS.errors = new Chart($("chart-errors"), {
    type: "doughnut",
    data: {
      labels: entries.map(e => e[0]),
      datasets: [{
        data: entries.map(e => e[1]),
        backgroundColor: entries.map(e => colors[e[0]] || "#888"),
      }],
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { position: "right" } },
    },
  });
}

function renderKindChart() {
  destroyChart("kinds");
  const m = currentModel();
  const by = m.multi_turn?.by_kind || {};
  const labels = Object.keys(by);
  const totals = labels.map(k => by[k].total);
  const passed = labels.map(k => by[k].passed);
  CHARTS.kinds = new Chart($("chart-kinds"), {
    type: "bar",
    data: {
      labels,
      datasets: [
        { label: "total",  data: totals, backgroundColor: "#cfd8e3" },
        { label: "passed", data: passed, backgroundColor: "#1d5887" },
      ],
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { position: "bottom" } },
      scales: { y: { beginAtZero: true } },
    },
  });
}

function renderHeatmap() {
  const host = $("heatmap");
  host.innerHTML = "";
  // col labels (species)
  host.appendChild(el("div", { className: "hm-col-label" }, ""));   // corner
  for (const sp of SPECIES_ORDER) host.appendChild(el("div", { className: "hm-col-label" }, sp));

  for (const m of STATE.dashboard.models) {
    host.appendChild(el("div", { className: "hm-row-label" }, m.model_name));
    const by = m.multi_turn?.by_species || {};
    for (const sp of SPECIES_ORDER) {
      const cell = by[sp];
      let rate = null, text = "—";
      if (cell && cell.total) {
        const sno = cell.silent_no_op || 0;
        rate = sno / cell.total;
        text = `${Math.round(100 * rate)}% (${sno}/${cell.total})`;
      }
      const bg = rate == null ? "#e6e8eb" : `hsl(${(1 - rate) * 100}, 65%, ${50 - rate * 20}%)`;
      const cellEl = el("div", { className: "hm-cell" }, text);
      cellEl.style.background = bg;
      if (rate == null) cellEl.style.color = "#7d848d";
      host.appendChild(cellEl);
    }
  }
}

/* ----- table + verdicts loader ----- */
async function loadVerdictsAndRenderTable() {
  const m = currentModel();
  const corpus = STATE.filters.corpus;
  // toggle kind filter visibility
  $("kind-wrap").style.display = corpus === "multi" ? "" : "none";

  const runId = corpus === "single" ? m.single_run_id : m.multi_run_id;
  if (!runId) {
    renderTable([]);
    return;
  }
  if (!STATE.cachedVerdicts[runId]) {
    const fname = corpus === "single"
      ? `data/${runId}_verdicts_augmented.jsonl`
      : `data/${runId}_verdicts_modifications_augmented.jsonl`;
    try {
      const rows = await loadJsonl(fname);
      // attach derived species so filters are uniform
      for (const r of rows) r._species = speciesOf(r.conv_id || r.id);
      STATE.cachedVerdicts[runId] = rows;
    } catch (e) {
      STATE.cachedVerdicts[runId] = [];
      console.warn("verdicts load failed:", fname, e);
    }
  }
  populateErrorFilter();
  renderErrorChart();
  renderTable(STATE.cachedVerdicts[runId]);
}

function passOf(r) { return !!r.semantic_valid; }

function applyFilters(rows) {
  const f = STATE.filters;
  return rows.filter(r => {
    if (f.outcome === "pass" && !passOf(r)) return false;
    if (f.outcome === "fail" && passOf(r))  return false;
    if (f.error && r.error_category !== f.error) return false;
    if (f.species && r._species !== f.species) return false;
    if (f.kind && r.modification_kind !== f.kind) return false;
    if (f.tag && !(r.verdict_tags || []).includes(f.tag)) return false;
    if (f.text) {
      const t = f.text.toLowerCase();
      const hay = `${r.id || ""} ${r.conv_id || ""} ${r.prompt || ""} ${(r.called_steps || []).join(" ")}`.toLowerCase();
      if (!hay.includes(t)) return false;
    }
    return true;
  });
}

function renderTable(allRows) {
  const tbody = document.querySelector("#tbl tbody");
  tbody.innerHTML = "";
  const rows = applyFilters(allRows);
  $("row-stat").textContent = `${rows.length} / ${allRows.length} rows`;
  for (const r of rows) {
    const tr = el("tr", { className: "row-clickable" });
    const id = r.id || `${r.conv_id}_t${r.turn_index}`;
    const kind = r.modification_kind || r.category || "";
    const ok = passOf(r);
    const tagsCell = el("td");
    for (const t of r.verdict_tags || []) {
      tagsCell.appendChild(el("span", { className: `tag tag-${t}` }, t));
      tagsCell.appendChild(document.createTextNode(" "));
    }
    tr.appendChild(el("td", {}, id));
    tr.appendChild(el("td", {}, kind));
    tr.appendChild(el("td", {}, r._species || ""));
    const outcome = el("span", { className: `pill ${ok ? "pass" : "fail"}` }, ok ? "PASS" : "FAIL");
    const outCell = el("td"); outCell.appendChild(outcome);
    tr.appendChild(outCell);
    tr.appendChild(el("td", {}, r.error_category || ""));
    tr.appendChild(tagsCell);
    tr.addEventListener("click", () => openDetail(r, id));
    tbody.appendChild(tr);
  }
}

/* ----- detail panel ----- */
function openDetail(r, id) {
  STATE.selected = id;
  const body = $("detail-body");
  body.innerHTML = "";
  body.appendChild(el("h2", {}, id));
  body.appendChild(el("div", { className: "kpi-sub" },
    `${currentModel().model_name} · ${STATE.filters.corpus}-turn`));
  const tags = r.verdict_tags || [];
  if (tags.length) {
    const row = el("div", { className: "detail-tag-row" });
    for (const t of tags) row.appendChild(el("span", { className: `tag tag-${t}` }, t));
    body.appendChild(row);
  }
  const meta = el("table", { className: "bench" });
  const tbody = el("tbody");
  const kv = (k, v) => {
    const tr = el("tr");
    tr.appendChild(el("td", {}, k));
    tr.appendChild(el("td", {}, v == null ? "—" : String(v)));
    tbody.appendChild(tr);
  };
  kv("outcome", passOf(r) ? "PASS" : "FAIL");
  kv("error_category", r.error_category);
  kv("syntax_valid", r.syntax_valid);
  kv("species", r._species);
  if (r.modification_kind) kv("modification_kind", r.modification_kind);
  if (r.base_id) kv("base_id", r.base_id);
  kv("expected_processes", r.expected_processes);
  kv("n_processes",       r.n_processes);
  kv("called_steps",      (r.called_steps || []).join(", "));
  kv("missing_steps",     (r.missing_steps || []).join(", "));
  kv("extra_steps",       (r.extra_steps   || []).join(", "));
  kv("hallucinated_steps",(r.hallucinated_steps || []).join(", "));
  meta.appendChild(tbody);
  body.appendChild(meta);

  body.appendChild(blockTitle("Prompt"));
  body.appendChild(el("pre", { className: "reply" }, r.prompt || "—"));

  body.appendChild(blockTitle("Ground-truth .nf"));
  body.appendChild(el("pre", { className: "code" }, r.ground_truth_code || "—"));

  body.appendChild(blockTitle("LLM-generated .nf"));
  body.appendChild(el("pre", { className: "code" }, r.nextflow_code || r.llm_reply_excerpt || "—"));

  if (r.llm_full_reply) {
    body.appendChild(blockTitle("LLM full reply"));
    body.appendChild(el("pre", { className: "reply" }, r.llm_full_reply));
  }
  if (r.error_detail) {
    body.appendChild(blockTitle("Error detail"));
    body.appendChild(el("pre", { className: "reply" }, r.error_detail));
  }

  $("detail-panel").classList.add("open");
  $("detail-overlay").classList.add("open");
  writeHash();
}

function blockTitle(label) {
  const s = el("section", { className: "detail-block" });
  s.appendChild(el("h4", {}, label));
  return s.children[0] ? s : (s.appendChild(el("h4", {}, label)), s);
}

function closeDetail() {
  STATE.selected = null;
  $("detail-panel").classList.remove("open");
  $("detail-overlay").classList.remove("open");
  writeHash();
}

/* boot */
init().catch(err => {
  console.error(err);
  $("dash-main")?.appendChild(el("p", { style: "color:red" }, "Dashboard failed to load: " + err.message));
});
