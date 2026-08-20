/* Renderer for ch03 — the closed loop: runaway vs collapse. */
"use strict";
window.Renderers.ch03 = function (viz, lab, st) {
  const stat = id => el("div", { class: "v", id }, "—");
  const sR = stat(), sRw = stat(), sK = stat(), sSat = stat();
  const phasorCv = el("canvas", { width: 320, height: 320 });
  const heatCv = el("canvas", { width: 320, height: 320, class: "pix" });
  const tsCv = el("canvas", { width: 760, height: 210 });
  const playerRow = el("div", {});
  const regime = el("div", { class: "verdict" }, "—");

  viz.append(
    el("div", { class: "stats" },
      el("div", { class: "stat" }, el("div", { class: "k" }, "order r"), sR),
      el("div", { class: "stat" }, el("div", { class: "k" }, "reward R"), sRw),
      el("div", { class: "stat" }, el("div", { class: "k" }, "mean K"), sK),
      el("div", { class: "stat" }, el("div", { class: "k" }, "% at K_max"), sSat)),
    el("div", { class: "panels" },
      el("div", { class: "card" },
        el("h3", {}, "Phasors — the order parameter"), phasorCv),
      el("div", { class: "card" },
        el("h3", {}, "Coupling matrix K (heatmap)"), heatCv),
      el("div", { class: "card wide" },
        el("h3", {}, "r(t) and mean K(t)"), tsCv, playerRow, regime)));

  let res = null;
  let ksnapCache = [];
  const player = UI.makePlayer(playerRow, drawFrame);

  function drawFrame(i) {
    if (!res) return;
    const p = res.params;
    UI.phasors(phasorCv, res.phases[i], "r = " + res.r[i].toFixed(3));
    const snap = ksnapCache[Math.min(Math.floor(i / res.Ksnaps.every),
                                     ksnapCache.length - 1)];
    if (snap) UI.heatmap(heatCv, snap, res.N);
    sR.textContent = res.r[i].toFixed(3);
    sRw.textContent = (res.r[i] - p.r_baseline).toFixed(3);
    sK.textContent = res.meanK[i].toFixed(3);
    sSat.textContent = (res.fracSat[i] * 100).toFixed(0) + "%";
    const fsat = res.fracSat[i], mK = res.meanK[i];
    if (fsat > 0.6) {
      regime.textContent = "RUNAWAY — coupling saturated at K_max, sync locked in";
      regime.style.color = "var(--cold)";
    } else if (mK < 0.05) {
      regime.textContent = "COLLAPSE — coupling stripped, oscillators scattering";
      regime.style.color = "var(--hot)";
    } else {
      regime.textContent = "in transition…";
      regime.style.color = "var(--mut)";
    }
    const series = [
      { xs: res.ts, ys: res.meanK.map(v => v / p.K_max), color: "#2a9d5c",
        label: "meanK/K_max" },
      { xs: res.ts, ys: res.r, color: "#4aa3ff", label: "r" },
    ];
    if (res.control) {
      series.push({ xs: res.ts, ys: res.control.r, color: "#4aa3ff",
                    dash: "dash", width: 1, label: "r (fixed-K control)" });
    }
    UI.plot(tsCv, {
      series,
      hlines: [{ y: p.r_baseline, color: "#8b97a6", label: "r_baseline" }],
      x0: 0, x1: res.ts[res.ts.length - 1], y0: 0, y1: 1,
      playhead: res.ts[i], xlabel: "time",
    });
  }

  return {
    update(result) {
      res = result;
      ksnapCache = res.Ksnaps.data.map(UI.decodeU8);
      st.dom.derived.innerHTML =
        `Kc(theory) ≈ 1.596·σ = <b>${res.Kc_theory.toFixed(2)}</b><br>` +
        `R_sat = K_max·λ/η = <b>${res.R_sat.toFixed(2)}</b> — sustained ` +
        `reward above this saturates coupling (iter 2 bound).`;
      player.setFrames(res.phases.length);
    },
  };
};
