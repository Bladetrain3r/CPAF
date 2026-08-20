"""
Lab ch07 -- the phase-locking threshold and the derived 1/sqrt(2) (Ch 7, iter 6).

Two oscillators reduce exactly to one equation for their phase difference,

    dpsi/dt = Δω - 2K sin(psi),

which locks (fixed point) iff K >= Kc = |Δω|/2 — a saddle-node bifurcation.
On the stable branch the pair coherence is R = |cos(psi*/2)|, which at onset
is exactly 1/sqrt(2) ≈ 0.7071: the architecture's hand-picked ~0.7 coherence
threshold, DERIVED. This lab probes one (Δω, K) live and sweeps K across the
threshold, with noise smearing the sharp bifurcation into a stochastic one.

The probe integrates the FULL two-oscillator system (iter 6 check 1 verified
it matches the 1-D reduction); the sweep integrates the reduction, vectorized
over K, exactly as verification/iter6_locking_threshold.py does.
"""
import numpy as np

from ksomheb import order_parameter
from .common import getp, rounded, slider

INV_SQRT2 = 1.0 / np.sqrt(2.0)

LAB = {
    "id": "ch07",
    "nav": "Ch 7 · Locking",
    "title": "The locking threshold: Kc = |Δω|/2 and the 1/√2 onset",
    "chapter": "textbook/07_grounding_the_threshold.md",
    "witness": "verification/iter6_locking_threshold.py",
    "claim": "Two oscillators lock iff K ≥ Kc = |Δω|/2 (saddle-node); the "
             "coherence at onset is exactly 1/√2 ≈ 0.7071 — a derived value "
             "for the ~0.7 threshold. Exact for N=2 [AN]@pair; the global "
             "N-oscillator transition has no special 0.7.",
    "blurb": "The smallest system with a sharp noise/deviation boundary: two "
             "oscillators that either drift past each other forever or lock "
             "into a fixed phase relationship. The threshold isn't tuned — "
             "it falls out of the algebra.",
    "notice": [
        "Below Kc the phase difference ψ climbs forever (drift): the pair "
        "coherence R oscillates and averages low. This is CPAF 'noise' — "
        "no persistent relation.",
        "Cross Kc and ψ flattens onto a horizontal line: locked. The pair "
        "holds a fixed phase offset — a persistent deviation, the seed of "
        "an interaction.",
        "At onset the locked branch STARTS at R = 1/√2, not at 0 — the "
        "coherence jumps. That discontinuity is why a ~0.7 threshold "
        "separates locked from drifting pairs.",
        "Nudge Δω up with K fixed and watch locking break at exactly "
        "K = |Δω|/2 — the threshold moves with the disagreement.",
        "Add noise: the sweep's sharp corner smears into a soft shoulder "
        "(stochastic bifurcation) — real systems cross thresholds "
        "probabilistically.",
    ],
    "renderer": "labs/ch07.js",
    "controls": [
        slider("dw", "Δω detuning", 0.05, 1.5, 0.005, 0.19),
        slider("K", "coupling K", 0.0, 1.5, 0.005, 0.12),
        slider("noise", "phase noise σ (probe)", 0.0, 0.5, 0.01, 0.0),
        slider("T", "probe duration T", 100, 800, 50, 300),
        slider("seed", "random seed", 1, 99, 1, 7),
    ],
    "presets": [
        {"label": "drifting (K = 0.7·Kc)", "set": {"dw": 0.19, "K": 0.065}},
        {"label": "at onset (K ≈ Kc)", "set": {"dw": 0.19, "K": 0.095}},
        {"label": "locked (K = 2·Kc)", "set": {"dw": 0.19, "K": 0.19}},
    ],
}

DT = 0.01
MAX_FRAMES = 600
SWEEP_NOISES = [0.0, 0.15, 0.4]
SWEEP_POINTS = 31


def _probe(dw, K, noise, T, seed):
    """Full two-oscillator sim (matches the reduction: iter 6 check 1)."""
    rng = np.random.RandomState(seed)
    p1, p2 = rng.uniform(0, 2 * np.pi, 2)
    n = int(T / DT)
    rec = max(1, n // MAX_FRAMES)
    psi_un = p1 - p2
    t1, t2, psis, Rs, ts = [], [], [], [], []
    for k in range(n):
        d1 = (0.5 * dw + K * np.sin(p2 - p1)) * DT
        d2 = (-0.5 * dw + K * np.sin(p1 - p2)) * DT
        if noise:
            d1 += noise * np.sqrt(DT) * rng.randn()
            d2 += noise * np.sqrt(DT) * rng.randn()
        p1 += d1
        p2 += d2
        psi_un += d1 - d2
        if k % rec == 0:
            ts.append(k * DT)
            t1.append(p1 % (2 * np.pi))
            t2.append(p2 % (2 * np.pi))
            psis.append(psi_un)
            Rs.append(order_parameter([p1, p2])[0])
    burn = int(0.7 * len(psis))
    drift = (abs(psis[-1] - psis[burn])
             / max((len(psis) - 1 - burn) * rec * DT, 1e-9))
    R_steady = float(np.mean(Rs[burn:]))
    return {"ts": rounded(ts, 2), "theta1": rounded(t1, 3),
            "theta2": rounded(t2, 3), "psi": rounded(psis, 3),
            "R": rounded(Rs, 4), "drift": round(float(drift), 4),
            "R_steady": round(R_steady, 4)}


def _sweep(dw, T, seed):
    """Reduced dynamics dpsi = (Δω − 2K sinψ)dt + √2·σ dW, vectorized over K.

    Same integrator as iter 6's integrate_psi (the √2 because two independent
    phase noises combine in the difference); returns mean steady-state R(K)
    at the iter-6 noise levels.
    """
    Kc = dw / 2.0
    Ks = np.linspace(0.3 * Kc, 1.8 * Kc, SWEEP_POINTS)
    n = int(T / DT)
    burn = int(0.7 * n)
    curves = {}
    for nz in SWEEP_NOISES:
        rng = np.random.RandomState(seed)
        psi = rng.uniform(0, 2 * np.pi, SWEEP_POINTS)
        amp = nz * np.sqrt(2.0)
        acc = np.zeros(SWEEP_POINTS)
        cnt = 0
        for k in range(n):
            dpsi = (dw - 2 * Ks * np.sin(psi)) * DT
            if nz:
                dpsi += amp * np.sqrt(DT) * rng.randn(SWEEP_POINTS)
            psi += dpsi
            if k > burn:
                acc += np.abs(np.cos(psi / 2.0))
                cnt += 1
        curves[f"{nz:g}"] = rounded(acc / cnt, 4)
    return {"Ks": rounded(Ks, 4), "curves": curves}


def _branch(dw):
    """Analytic locked branch R(K) = |cos(ψ*/2)|, ψ* = arcsin(Δω/2K)."""
    Kc = dw / 2.0
    Kg = np.linspace(1.0 * Kc, 3.0 * Kc, 120)
    R = np.abs(np.cos(np.arcsin(np.clip(dw / (2 * Kg), -1, 1)) / 2.0))
    return {"Ks": rounded(Kg, 4), "R": rounded(R, 4)}


def run(params):
    spec = LAB["controls"]
    dw = getp(params, spec, "dw")
    K = getp(params, spec, "K")
    noise = getp(params, spec, "noise")
    T = getp(params, spec, "T")
    seed = int(getp(params, spec, "seed"))
    mode = params.get("mode", "both")

    Kc = dw / 2.0
    out = {"Kc": round(float(Kc), 4), "inv_sqrt2": round(INV_SQRT2, 4),
           "locked_pred": bool(K >= Kc)}
    if mode in ("both", "probe"):
        out["probe"] = _probe(dw, K, noise, T, seed)
    if mode in ("both", "sweep"):
        out["sweep"] = _sweep(dw, min(T, 400), seed)
        out["branch"] = _branch(dw)
    return out
