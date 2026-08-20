/* Renderer for ch07 — the locking threshold Kc = |Δω|/2 and the 1/√2 onset. */
"use strict";
window.Renderers.ch07 = function (viz, lab, st) {
  const pairCv = el("canvas", { width: 300, height: 300 });
  const psiCv = el("canvas", { width: 420, height: 300 });
  const sweepCv = el("canvas", { width: 760, height: 260 });
  const playerRow = el("div", {});
  const verdict = el("div", { class: "verdict" }, "—");

  viz.append(el("div", { class: "panels" },
    el("div", { class: "card" },
      el("h3", {}, "The pair — phases on the circle"), pairCv, playerRow, verdict),
    el("div", { class: "card" },
      el("h3", {}, "Phase difference ψ(t) — drift vs lock"), psiCv,
      el("div", { class: "note" },
        "Climbing staircase = drifting past each other. Horizontal line = locked.")),
    el("div", { class: "card wide" },
      el("h3", {}, "Coherence R vs K/Kc — the 1/√2 onset"), sweepCv,
      el("div", { class: "note", html:
        "Solid: analytic locked branch |cos(ψ*/2)|. Dots: simulated steady " +
        "R at three noise levels (0, 0.15, 0.4) — noise smears the sharp corner. " +
        "Gold marker: the current probe." }))));

  let res = null;
  const player = UI.makePlayer(playerRow, drawFrame);

  function drawFrame(i) {
    if (!res?.probe) return;
    const pr = res.probe;
    const x = pairCv.getContext("2d"), W = pairCv.width, H = pairCv.height;
    const cx = W / 2, cy = H / 2, R = Math.min(W, H) * 0.42;
    x.clearRect(0, 0, W, H);
    x.strokeStyle = "#2a313c";
    x.beginPath(); x.arc(cx, cy, R, 0, 2 * Math.PI); x.stroke();
    const pts = [[pr.theta1[i], "#4aa3ff"], [pr.theta2[i], "#d62728"]]
      .map(([a, c]) => {
        const px = cx + R * Math.cos(a), py = cy - R * Math.sin(a);
        x.fillStyle = c;
        x.beginPath(); x.arc(px, py, 7, 0, 2 * Math.PI); x.fill();
        return [px, py];
      });
    x.strokeStyle = "#8b97a6"; x.setLineDash([3, 3]);
    x.beginPath(); x.moveTo(pts[0][0], pts[0][1]); x.lineTo(pts[1][0], pts[1][1]);
    x.stroke(); x.setLineDash([]);
    x.fillStyle = "#8b97a6"; x.font = "12px system-ui";
    x.fillText(`R = ${pr.R[i].toFixed(3)}`, 10, 18);
    const psiWrapped = ((pr.psi[i] % (2 * Math.PI)) + 2 * Math.PI) % (2 * Math.PI);
    x.fillText(`ψ mod 2π = ${psiWrapped.toFixed(2)}`, 10, 34);

    UI.plot(psiCv, {
      series: [{ xs: pr.ts, ys: pr.psi, color: "#4aa3ff", label: "ψ (unwrapped)" }],
      x0: 0, x1: pr.ts[pr.ts.length - 1],
      playhead: pr.ts[i], xlabel: "time",
    });
  }

  function drawSweep() {
    if (!res?.sweep) return;
    const Kc = res.Kc;
    const norm = xs => xs.map(k => k / Kc);
    const series = [{ xs: norm(res.branch.Ks), ys: res.branch.R,
                      color: "#e6edf3", width: 2, label: "analytic branch" }];
    const cols = { "0": "#4aa3ff", "0.15": "#e08a1e", "0.4": "#d62728" };
    for (const [nz, ys] of Object.entries(res.sweep.curves)) {
      series.push({ xs: norm(res.sweep.Ks), ys, color: cols[nz] || "#8b97a6",
                    width: 1, label: "σ=" + nz });
    }
    const points = [];
    if (res.probe) {
      points.push({ x: st.params.K / Kc, y: res.probe.R_steady,
                    color: "#ffce54", r: 5 });
    }
    UI.plot(sweepCv, {
      series, points,
      hlines: [{ y: res.inv_sqrt2, color: "#2a9d5c", label: "1/√2 ≈ 0.707" }],
      vlines: [{ x: 1, color: "#d62728", label: "Kc = |Δω|/2" }],
      x0: 0.3, x1: 1.8, y0: 0.4, y1: 1.02, xlabel: "K / Kc",
    });
  }

  return {
    modeFor(id) { return (id === "K" || id === "noise") ? "probe" : "both"; },
    update(result, params) {
      res = result;
      drawSweep();
      if (res.probe) {
        const locked = res.probe.drift < 1e-2;
        verdict.textContent = locked
          ? `LOCKED — drift ≈ 0, steady R = ${res.probe.R_steady.toFixed(3)}`
          : `DRIFTING — drift rate ${res.probe.drift.toFixed(3)}, ` +
            `mean R = ${res.probe.R_steady.toFixed(3)}`;
        verdict.style.color = locked ? "var(--cold)" : "var(--hot)";
        player.setFrames(res.probe.ts.length);
      }
      st.dom.derived.innerHTML =
        `Kc = |Δω|/2 = <b>${res.Kc.toFixed(4)}</b> · ` +
        `K/Kc = <b>${(params.K / res.Kc).toFixed(2)}</b> · ` +
        `prediction: <b>${res.locked_pred ? "locked" : "drifting"}</b> ` +
        `(noise-free)`;
    },
  };
};
