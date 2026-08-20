/* CPAF interactive companion — tab shell, controls, playback & plot helpers.
   The browser only renders: all model integration happens server-side in the
   labs (see ../serve.py), which call the verified ksomheb.py. */
"use strict";
const TAU = Math.PI * 2;

/* ---------------- tiny DOM helpers ---------------- */
function el(tag, attrs = {}, ...kids) {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") n.className = v;
    else if (k === "html") n.innerHTML = v;
    else if (k.startsWith("on")) n.addEventListener(k.slice(2), v);
    else n.setAttribute(k, v);
  }
  for (const kid of kids) n.append(kid);
  return n;
}
const fmtVal = (v, step) => {
  const d = Math.max(0, -Math.floor(Math.log10(step) + 1e-9));
  return (+v).toFixed(Math.min(d, 4));
};

/* ---------------- shared rendering helpers ---------------- */
const UI = {
  /* Decode a base64 uint8 payload (quantized K heatmap). */
  decodeU8(b64) {
    const s = atob(b64), a = new Uint8Array(s.length);
    for (let i = 0; i < s.length; i++) a[i] = s.charCodeAt(i);
    return a;
  },

  /* Same viridis-ish ramp as the legacy visualiser: v in [0,1] -> [r,g,b]. */
  heatColor(v) {
    return [Math.round(40 + 215 * Math.pow(v, 1.4)),
            Math.round(20 + 200 * v),
            Math.round(80 + 120 * (1 - v))];
  },

  /* Draw an N x N uint8 matrix (0..255) as a nearest-neighbour heatmap. */
  heatmap(canvas, u8, N) {
    const x = canvas.getContext("2d");
    const img = x.createImageData(N, N);
    for (let i = 0; i < N * N; i++) {
      const [r, g, b] = UI.heatColor(u8[i] / 255), o = i * 4;
      img.data[o] = r; img.data[o + 1] = g; img.data[o + 2] = b; img.data[o + 3] = 255;
    }
    const tmp = document.createElement("canvas");
    tmp.width = N; tmp.height = N;
    tmp.getContext("2d").putImageData(img, 0, 0);
    x.imageSmoothingEnabled = false;
    x.clearRect(0, 0, canvas.width, canvas.height);
    x.drawImage(tmp, 0, 0, canvas.width, canvas.height);
  },

  /* Phasor ring: dots on the unit circle + the order-parameter arrow. */
  phasors(canvas, phases, label) {
    const x = canvas.getContext("2d"), W = canvas.width, H = canvas.height;
    const cx = W / 2, cy = H / 2, R = Math.min(W, H) * 0.42;
    x.clearRect(0, 0, W, H);
    x.strokeStyle = "#2a313c";
    x.beginPath(); x.arc(cx, cy, R, 0, TAU); x.stroke();
    let zr = 0, zi = 0;
    for (const a of phases) {
      zr += Math.cos(a); zi += Math.sin(a);
      x.fillStyle = "rgba(74,163,255,0.8)";
      x.beginPath();
      x.arc(cx + R * Math.cos(a), cy - R * Math.sin(a), 3, 0, TAU);
      x.fill();
    }
    zr /= phases.length; zi /= phases.length;
    const r = Math.hypot(zr, zi), psi = Math.atan2(zi, zr);
    const ax = cx + R * r * Math.cos(psi), ay = cy - R * r * Math.sin(psi);
    x.strokeStyle = "#ffce54"; x.lineWidth = 3;
    x.beginPath(); x.moveTo(cx, cy); x.lineTo(ax, ay); x.stroke();
    x.lineWidth = 1; x.fillStyle = "#ffce54";
    x.beginPath(); x.arc(ax, ay, 4, 0, TAU); x.fill();
    if (label) {
      x.fillStyle = "#8b97a6"; x.font = "12px system-ui";
      x.fillText(label, 10, 18);
    }
  },

  /* Generic 2-D line plot with gridlines, h/v guide lines, points, playhead. */
  plot(canvas, o) {
    const x = canvas.getContext("2d"), W = canvas.width, H = canvas.height;
    const ml = o.ml ?? 40, mr = 10, mt = 8, mb = 22;
    const pw = W - ml - mr, ph = H - mt - mb;
    let x0 = o.x0, x1 = o.x1, y0 = o.y0, y1 = o.y1;
    if (x0 === undefined || y0 === undefined) {
      let xs = [], ys = [];
      for (const s of o.series || []) { xs = xs.concat(s.xs); ys = ys.concat(s.ys); }
      for (const p of o.points || []) { xs.push(p.x); ys.push(p.y); }
      if (x0 === undefined) { x0 = Math.min(...xs); x1 = Math.max(...xs); }
      if (y0 === undefined) {
        y0 = Math.min(...ys); y1 = Math.max(...ys);
        const pad = (y1 - y0 || 1) * 0.08; y0 -= pad; y1 += pad;
      }
    }
    const X = v => ml + (v - x0) / (x1 - x0 || 1) * pw;
    const Y = v => mt + ph - (v - y0) / (y1 - y0 || 1) * ph;
    x.clearRect(0, 0, W, H);
    x.font = "10.5px system-ui";
    x.strokeStyle = "#222a34"; x.fillStyle = "#66707e";
    for (let g = 0; g <= 4; g++) {
      const vy = y0 + g / 4 * (y1 - y0), py = Y(vy);
      x.beginPath(); x.moveTo(ml, py); x.lineTo(W - mr, py); x.stroke();
      x.fillText((+vy.toFixed(2)).toString(), 4, py + 3);
    }
    const lastTick = o.xlabel ? 4 : 5;   // leave room for the axis label
    for (let g = 0; g <= lastTick; g++) {
      const vx = x0 + g / 5 * (x1 - x0);
      x.fillText((+vx.toFixed(2)).toString(), X(vx) - 8, H - 7);
    }
    const dashOf = d => d === "dash" ? [5, 4] : d === "dot" ? [2, 3] : [];
    for (const h of o.hlines || []) {
      x.strokeStyle = h.color; x.setLineDash(dashOf(h.dash ?? "dot"));
      x.beginPath(); x.moveTo(ml, Y(h.y)); x.lineTo(W - mr, Y(h.y)); x.stroke();
      x.setLineDash([]);
      if (h.label) { x.fillStyle = h.color; x.fillText(h.label, ml + 4, Y(h.y) - 4); }
    }
    for (const v of o.vlines || []) {
      x.strokeStyle = v.color; x.setLineDash(dashOf(v.dash ?? "dash"));
      x.beginPath(); x.moveTo(X(v.x), mt); x.lineTo(X(v.x), mt + ph); x.stroke();
      x.setLineDash([]);
      if (v.label) { x.fillStyle = v.color; x.fillText(v.label, X(v.x) + 4, mt + 12); }
    }
    for (const s of o.series || []) {
      x.strokeStyle = s.color; x.lineWidth = s.width ?? 1.5;
      x.setLineDash(dashOf(s.dash));
      x.beginPath();
      let started = false;
      for (let i = 0; i < s.xs.length; i++) {
        const px = X(s.xs[i]), py = Y(Math.max(y0, Math.min(y1, s.ys[i])));
        started ? x.lineTo(px, py) : x.moveTo(px, py);
        started = true;
      }
      x.stroke(); x.setLineDash([]); x.lineWidth = 1;
    }
    for (const p of o.points || []) {
      x.fillStyle = p.color;
      x.beginPath(); x.arc(X(p.x), Y(p.y), p.r ?? 3.5, 0, TAU); x.fill();
    }
    if (o.playhead !== undefined) {
      x.strokeStyle = "#e6edf3"; x.globalAlpha = 0.55;
      x.beginPath(); x.moveTo(X(o.playhead), mt); x.lineTo(X(o.playhead), mt + ph);
      x.stroke(); x.globalAlpha = 1;
    }
    let lx = W - mr - 8;
    for (const s of (o.series || []).slice().reverse()) {
      if (!s.label) continue;
      x.fillStyle = s.color;
      lx -= x.measureText(s.label).width + 14;
      x.fillText(s.label, lx, mt + 12);
    }
    if (o.xlabel) { x.fillStyle = "#66707e"; x.fillText(o.xlabel, W - mr - x.measureText(o.xlabel).width, H - 7); }
  },

  /* Playback engine: play/pause + scrub + speed over a frame index range. */
  makePlayer(container, onFrame) {
    let n = 0, i = 0, playing = false, speed = 1, last = 0, accum = 0, raf = 0;
    const FPS = 30;
    const btn = el("button", { class: "act primary" }, "Play");
    const scrub = el("input", { type: "range", min: 0, max: 0, step: 1, value: 0 });
    const tlab = el("span", { class: "t" }, "—");
    const sel = el("select", {},
      ...[0.5, 1, 2, 4].map(s => el("option", { value: s, ...(s === 1 ? { selected: "" } : {}) }, s + "×")));
    container.classList.add("player");
    container.append(btn, scrub, sel, tlab);

    function show(idx) {
      i = Math.max(0, Math.min(n - 1, idx));
      scrub.value = i;
      tlab.textContent = `frame ${i + 1}/${n}`;
      onFrame(i);
    }
    function tick(ts) {
      if (!playing) return;
      accum += (ts - last) / 1000 * FPS * speed; last = ts;
      if (accum >= 1) {
        const adv = Math.floor(accum); accum -= adv;
        if (i + adv >= n - 1) { show(n - 1); pause(); return; }
        show(i + adv);
      }
      raf = requestAnimationFrame(tick);
    }
    function play() {
      if (n === 0) return;
      if (i >= n - 1) i = 0;
      playing = true; btn.textContent = "Pause"; btn.classList.remove("primary");
      last = performance.now(); accum = 0;
      raf = requestAnimationFrame(tick);
    }
    function pause() {
      playing = false; btn.textContent = "Play"; btn.classList.add("primary");
      cancelAnimationFrame(raf);
    }
    btn.addEventListener("click", () => playing ? pause() : play());
    scrub.addEventListener("input", () => { pause(); show(+scrub.value); });
    sel.addEventListener("change", () => speed = +sel.value);
    return {
      setFrames(count, { autoplay = true } = {}) {
        n = count; scrub.max = Math.max(0, n - 1);
        pause(); show(0);
        if (autoplay) play();
      },
      seek: show, pause,
      get index() { return i; },
    };
  },
};

/* ---------------- lab shell ---------------- */
const Renderers = window.Renderers = {};
const labState = {};

async function runLab(id, mode) {
  const st = labState[id];
  const stage = st.dom.stage;
  stage.classList.add("loading");
  st.dom.err.style.display = "none";
  try {
    const body = { ...st.params };
    if (mode) body.mode = mode;
    const resp = await fetch("/api/run/" + id, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    const data = await resp.json();
    if (!resp.ok) throw new Error(data.error || resp.statusText);
    st.result = { ...(st.result || {}), ...data };
    st.view.update(st.result, st.params);
  } catch (e) {
    st.dom.err.textContent = "run failed: " + e.message;
    st.dom.err.style.display = "block";
  } finally {
    stage.classList.remove("loading");
  }
}

function buildControls(lab, st, container) {
  const inputs = {};
  container.append(el("h2", {}, "Parameters"));
  for (const c of lab.controls) {
    if (c.type === "toggle") {
      const cb = el("input", { type: "checkbox", ...(c.value ? { checked: "" } : {}) });
      cb.addEventListener("change", () => {
        st.params[c.id] = cb.checked;
        runLab(lab.id, st.view.modeFor?.(c.id));
      });
      const row = el("div", { class: "row" },
        el("label", {}, el("span", {}, c.label + " "), cb));
      if (c.note) row.append(el("div", { class: "subnote" }, c.note));
      container.append(row);
      inputs[c.id] = { set: v => { cb.checked = v; } };
      st.params[c.id] = c.value;
      continue;
    }
    const val = el("b", {}, fmtVal(c.value, c.step));
    const inp = el("input", { type: "range", min: c.min, max: c.max, step: c.step, value: c.value });
    inp.addEventListener("input", () => val.textContent = fmtVal(inp.value, c.step));
    inp.addEventListener("change", () => {
      st.params[c.id] = +inp.value;
      runLab(lab.id, st.view.modeFor?.(c.id));
    });
    const row = el("div", { class: "row" },
      el("label", {}, el("span", {}, c.label), val), inp);
    if (c.note) row.append(el("div", { class: "subnote" }, c.note));
    container.append(row);
    inputs[c.id] = { set: v => { inp.value = v; val.textContent = fmtVal(v, c.step); } };
    st.params[c.id] = c.value;
  }
  if (lab.presets?.length) {
    const btns = el("div", { class: "btns" });
    for (const pr of lab.presets) {
      btns.append(el("button", { class: "act", onclick: () => {
        for (const [k, v] of Object.entries(pr.set)) {
          st.params[k] = v;
          inputs[k]?.set(v);
        }
        runLab(lab.id);
      } }, pr.label));
    }
    container.append(el("h2", { style: "margin-top:18px" }, "Presets"), btns);
  }
  const derived = el("div", { class: "derived" });
  container.append(derived);
  st.dom.derived = derived;
}

function buildLabPanel(lab, root) {
  const st = labState[lab.id] = { params: {}, result: null, dom: {} };
  const controls = el("aside", { class: "controls" });
  const err = el("div", { class: "errbar" });
  const viz = el("div", { class: "viz" });
  const notice = el("details", { class: "notice", open: "" },
    el("summary", {}, "What to notice"),
    el("ul", {}, ...lab.notice.map(t => el("li", {}, t))));
  const prov = el("div", { class: "provenance" },
    el("span", { class: "chip" }, "📖 " + lab.chapter),
    el("span", { class: "chip" }, "🧪 witness: " + lab.witness),
    el("span", { class: "chip" }, "⚙ dynamics: ksomheb.py"),
    el("span", { class: "claim" }, lab.claim));
  const stage = el("div", { class: "stage" },
    el("div", { class: "stage-head" },
      el("h2", {}, lab.title), el("p", {}, lab.blurb)),
    err, viz, notice, prov,
    el("div", { class: "busy" }, "computing…"));
  st.dom = { stage, err, viz };
  root.append(controls, stage);
  st.view = Renderers[lab.id](viz, lab, st);
  buildControls(lab, st, controls);
  return st;
}

function loadScript(src) {
  return new Promise((res, rej) => {
    const s = document.createElement("script");
    s.src = src; s.onload = res;
    s.onerror = () => rej(new Error("failed to load " + src));
    document.head.append(s);
  });
}

async function boot() {
  const man = await (await fetch("/api/manifest")).json();
  await Promise.all(man.labs.map(l => loadScript("/static/" + l.renderer)));
  const tabs = document.querySelector("nav.tabs");
  const main = document.querySelector("main");
  const panels = { about: document.getElementById("panel-about") };
  const buttons = {};

  function activate(id) {
    for (const [k, p] of Object.entries(panels)) p.hidden = k !== id;
    for (const [k, b] of Object.entries(buttons)) b.classList.toggle("active", k === id);
    if (id !== "about" && !labState[id].result) runLab(id);
  }

  buttons.about = el("button", { class: "active", onclick: () => activate("about") }, "About");
  tabs.append(buttons.about);
  for (const lab of man.labs) {
    const panel = el("section", { class: "lab", hidden: "" });
    main.append(panel);
    panels[lab.id] = panel;
    buildLabPanel(lab, panel);
    buttons[lab.id] = el("button", { onclick: () => activate(lab.id) }, lab.nav);
    tabs.append(buttons[lab.id]);
  }
  const rows = man.labs.map(l =>
    `<tr><td>${l.nav}</td><td><code>${l.chapter}</code></td><td><code>${l.witness}</code></td></tr>`).join("");
  document.getElementById("about-labmap").innerHTML =
    `<tr><th>tab</th><th>textbook chapter</th><th>verified witness</th></tr>${rows}`;
}

boot();
