/* Renderer for ch01 — Kuramoto synchronization transition. */
"use strict";
window.Renderers.ch01 = function (viz, lab, st) {
  const sweepCv = el("canvas", { width: 420, height: 300 });
  const phasorCv = el("canvas", { width: 300, height: 300 });
  const rCv = el("canvas", { width: 420, height: 110 });
  const playerRow = el("div", {});
  const readout = el("div", { class: "note" }, "—");

  viz.append(el("div", { class: "panels" },
    el("div", { class: "card" },
      el("h3", {}, "Steady-state r vs coupling K (sweep)"), sweepCv,
      el("div", { class: "note", html:
        "Each point: settle 60 time units, then average r over 30 more. " +
        "Red dashed line: K<sub>c</sub> = 1.596·σ (mean-field theory)." })),
    el("div", { class: "card" },
      el("h3", {}, "Probe run at chosen K — phasors"), phasorCv,
      playerRow, readout),
    el("div", { class: "card wide" },
      el("h3", {}, "Probe run — r(t)"), rCv)));

  let res = null, params = null;
  const player = UI.makePlayer(playerRow, drawFrame);

  function drawFrame(i) {
    if (!res?.probe) return;
    const pr = res.probe;
    UI.phasors(phasorCv, pr.phases[i],
      `K = ${pr.K}   r = ${pr.r[i].toFixed(3)}` +
      (pr.shown < pr.phases[i].length ? "" : ""));
    const ts = pr.r.map((_, k) => k * pr.dt_frame);
    UI.plot(rCv, {
      series: [{ xs: ts, ys: pr.r, color: "#4aa3ff", label: "r(t)" }],
      y0: 0, y1: 1, x0: 0, x1: ts[ts.length - 1],
      hlines: [], playhead: i * pr.dt_frame, xlabel: "time",
    });
  }

  function drawSweep() {
    if (!res?.sweep) return;
    const marker = [];
    if (res.probe) {
      // put the probe marker on the sweep curve: interpolate r at K_probe
      const { Ks, r } = res.sweep;
      const K = res.probe.K;
      let y = r[r.length - 1];
      for (let i = 1; i < Ks.length; i++) {
        if (K <= Ks[i]) {
          const f = (K - Ks[i - 1]) / (Ks[i] - Ks[i - 1] || 1);
          y = r[i - 1] + f * (r[i] - r[i - 1]);
          break;
        }
      }
      marker.push({ x: K, y, color: "#ffce54", r: 5 });
    }
    UI.plot(sweepCv, {
      series: [{ xs: res.sweep.Ks, ys: res.sweep.r, color: "#4aa3ff",
                 label: "steady-state r", width: 2 }],
      points: marker,
      vlines: [{ x: res.Kc_theory, color: "#d62728",
                 label: "Kc = " + res.Kc_theory.toFixed(2) }],
      x0: 0, x1: res.sweep.Ks[res.sweep.Ks.length - 1], y0: 0, y1: 1,
      xlabel: "K",
    });
  }

  return {
    modeFor(id) { return id === "K_probe" ? "probe" : "both"; },
    update(result, p) {
      res = result; params = p;
      drawSweep();
      if (res.probe) {
        const above = res.probe.K >= res.Kc_theory;
        readout.textContent =
          `K ${above ? "≥" : "<"} Kc(${res.Kc_theory.toFixed(2)}): expect ` +
          (above ? "partial synchrony — the gold arrow grows and holds."
                 : "incoherence — the arrow stays short and wanders.") +
          (res.probe.shown < params.N
            ? ` (showing ${res.probe.shown} of ${params.N} phases; r uses all)` : "");
        player.setFrames(res.probe.phases.length);
      }
      st.dom.derived.innerHTML =
        `Kc(theory) = 1.596·σ = <b>${res.Kc_theory.toFixed(3)}</b>`;
    },
  };
};
