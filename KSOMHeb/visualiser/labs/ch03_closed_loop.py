"""
Lab ch03 -- the closed loop: bistability from global reward (Ch 3, iter 3).

The reward is computed live from the system's own synchrony, R = r - r_baseline,
closing the loop coupling -> synchrony -> reward -> coupling. Positive feedback
commits: the same rule with the same parameters either runs away to saturated
coupling or strips itself bare, decided by where the initial coupling K0 puts
r relative to the baseline. This is the successor of the original JS
visualiser, now driven directly by ksomheb.update_ksom_heb -- the verified
implementation, not a port.

The whole trajectory is computed here and the browser animates/scrubs it,
so you can rewind through the tipping point. Optionally a fixed-coupling
control run (same K0, no learning) is returned for overlay -- iter 3's
check 3: the adaptive run brackets its control on both sides.
"""
import numpy as np

from ksomheb import kuramoto_step, order_parameter, update_ksom_heb
from .common import getp, pack_unit_u8, rounded, slider, toggle

LAB = {
    "id": "ch03",
    "nav": "Ch 3 · Closed loop",
    "title": "Closing the loop: runaway or collapse",
    "chapter": "textbook/03_closing_the_loop.md",
    "witness": "verification/iter3_closed_loop.py",
    "claim": "Global reward R = r − r_baseline creates bistability: initial "
             "coupling above the tipping point runs away to saturated K and "
             "locked synchrony; below it, coupling is stripped and the "
             "population scatters. Global reward commits; it does not regulate.",
    "blurb": "Phases AND coupling evolve together for the first time. Flip "
             "the initial coupling K₀ across the tipping point and watch the "
             "same learning rule choose opposite fates.",
    "notice": [
        "Supercritical start (K₀ = 1.2 > Kc): r beats the baseline, reward "
        "is positive, coupling grows, which raises r further — the loop "
        "commits and K piles into the K_max clamp (heatmap saturates).",
        "Subcritical start (K₀ = 0.4): r sits below baseline, negative "
        "reward strips coupling, r falls further — the same rule erases "
        "the network. Scrub back and find the moment it was still close.",
        "Turn on the fixed-K control: the adaptive run ends ABOVE its "
        "control in the runaway regime and BELOW it in collapse — learning "
        "amplifies whichever side of the baseline you start on.",
        "The plasticity story: mean K moves fast early, then freezes at "
        "either extreme. Learning happens in the transition, not at the "
        "fixed points.",
        "There is no per-pair credit assignment here — that failure is the "
        "point, and it is what Ch 4–5 (reward modes, competition) fix.",
    ],
    "renderer": "labs/ch03.js",
    "controls": [
        slider("eta", "η learning rate", 0.001, 0.05, 0.001, 0.01),
        slider("lam", "λ decay rate", 0.0002, 0.01, 0.0002, 0.001),
        slider("K_max", "K_max coupling cap", 0.5, 4.0, 0.1, 2.0),
        slider("r_baseline", "r_baseline (reward zero)", 0.0, 0.9, 0.02, 0.3),
        slider("N", "N oscillators", 10, 120, 2, 60),
        slider("sigma", "σ frequency spread", 0.05, 1.5, 0.05, 0.5),
        slider("K0", "initial coupling K₀", 0.0, 3.0, 0.05, 1.2),
        slider("dt", "dt step", 0.01, 0.1, 0.01, 0.05),
        slider("steps", "steps", 2000, 60000, 1000, 12000),
        slider("seed", "random seed", 1, 99, 1, 11),
        toggle("control", "overlay fixed-K control run", True,
               "same K₀, learning off — iter 3 check 3"),
    ],
    "presets": [
        {"label": "↑ Supercritical", "set": {"K0": 1.2}},
        {"label": "↓ Subcritical", "set": {"K0": 0.4}},
    ],
}

MAX_FRAMES = 600
MAX_KSNAPS = 48


def run(params):
    spec = LAB["controls"]
    p = {c["id"]: getp(params, spec, c["id"]) for c in spec}
    N = int(p["N"])
    steps = int(p["steps"])
    seed = int(p["seed"])

    rng = np.random.RandomState(seed)
    omega = rng.normal(0.0, p["sigma"], N)
    omega -= omega.mean()
    theta0 = rng.uniform(0, 2 * np.pi, N)
    K0 = np.full((N, N), p["K0"])
    np.fill_diagonal(K0, 0.0)
    off = ~np.eye(N, dtype=bool)

    rec = max(1, steps // MAX_FRAMES)
    n_frames = steps // rec
    ksnap_every = max(1, int(np.ceil(n_frames / MAX_KSNAPS)))

    def simulate(adaptive):
        theta, K = theta0.copy(), K0.copy()
        ts, rs, meanK, fsat, phases, ksnaps = [], [], [], [], [], []
        for t in range(steps):
            if adaptive:
                r, _ = order_parameter(theta)
                theta, K = update_ksom_heb(
                    theta, omega, K, reward=r - p["r_baseline"],
                    dt=p["dt"], eta=p["eta"], lam=p["lam"], K_max=p["K_max"])
            else:
                theta = kuramoto_step(theta, omega, K, p["dt"])
            if t % rec == 0:
                r, _ = order_parameter(theta)
                ts.append(t * p["dt"])
                rs.append(r)
                meanK.append(K[off].mean())
                fsat.append((K[off] >= p["K_max"] - 1e-6).mean())
                if adaptive:
                    phases.append(np.mod(theta, 2 * np.pi))
                    if (len(ts) - 1) % ksnap_every == 0:
                        ksnaps.append(pack_unit_u8(K / p["K_max"]))
        return ts, rs, meanK, fsat, phases, ksnaps

    ts, rs, meanK, fsat, phases, ksnaps = simulate(adaptive=True)
    out = {
        "params": {k: (bool(v) if isinstance(v, bool) else round(float(v), 5))
                   for k, v in p.items()},
        "Kc_theory": round(float(1.596 * p["sigma"]), 4),
        "R_sat": round(float(p["K_max"] * p["lam"] / p["eta"]), 4),
        "N": N,
        "dt_frame": p["dt"] * rec,
        "ts": rounded(ts, 2),
        "r": rounded(rs, 4),
        "meanK": rounded(meanK, 4),
        "fracSat": rounded(fsat, 4),
        "phases": [rounded(f, 3) for f in phases],
        "Ksnaps": {"every": ksnap_every, "data": ksnaps},
    }
    if p["control"]:
        _, rs_c, meanK_c, _, _, _ = simulate(adaptive=False)
        out["control"] = {"r": rounded(rs_c, 4), "meanK": rounded(meanK_c, 4)}
    return out
