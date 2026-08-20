"""
Lab ch01 -- the Kuramoto synchronization transition (textbook Ch 1, iter 1).

Sweep the uniform coupling K and watch the steady-state order parameter r
stay flat below Kc and rise past it; probe a single K to see the phasors do
it live. Same experiment as verification/iter1_kuramoto_transition.py with
interactive parameters.

Provenance note on the stepper: iteration 1 integrates the full N x N form
via ksomheb.kuramoto_step. For a UNIFORM all-to-all coupling that RHS is
algebraically identical to the mean-field form

    dtheta_i/dt = omega_i + K * r * sin(psi - theta_i)

(the j = i term contributes sin(0) = 0, so the zeroed diagonal changes
nothing). We use the mean-field form here because it is O(N) per step,
which makes slider-speed sweeps possible; selfcheck.py verifies the two
steppers agree to floating-point tolerance on random states. This identity
is exact algebra, not an approximation -- the dynamics are the same.
"""
import numpy as np

from ksomheb import order_parameter
from .common import getp, rounded, slider

LAB = {
    "id": "ch01",
    "nav": "Ch 1 · Transition",
    "title": "The Kuramoto synchronization transition",
    "chapter": "textbook/01_phase_oscillators.md",
    "witness": "verification/iter1_kuramoto_transition.py",
    "claim": "Steady-state r stays low below Kc = 2/(π·g(0)) ≈ 1.596·σ and "
             "rises sharply above it (mean-field theory, Gaussian frequencies).",
    "blurb": "Everything in K-SOM-Heb sits on the order parameter r. Before "
             "trusting any learning, check the foundation: sweep the fixed "
             "coupling K and find the phase transition where a scattered "
             "population snaps into synchrony.",
    "notice": [
        "Below Kc the curve hugs r ≈ 0 (finite-N noise keeps it slightly "
        "above): no amount of time produces order there — coupling is simply "
        "too weak against the frequency spread σ.",
        "The rise past Kc is steep but continuous — for large N this is a "
        "genuine phase transition, the first 'more is different' moment of "
        "the book.",
        "Drag σ up and the whole transition slides right (Kc = 1.596·σ): "
        "more disagreement needs more coupling to overcome.",
        "Probe a K just below and just above Kc and watch the phasor ring: "
        "the gold arrow (length r) either wanders near the centre or grows "
        "and drags the dots into a clump.",
    ],
    "renderer": "labs/ch01.js",
    "controls": [
        slider("N", "N oscillators", 50, 300, 10, 200),
        slider("sigma", "σ frequency spread", 0.2, 1.5, 0.05, 1.0),
        slider("K_probe", "probe coupling K", 0.0, 4.0, 0.05, 1.0),
        slider("seed", "random seed", 1, 99, 1, 42),
    ],
    "presets": [
        {"label": "just below Kc", "set": {"K_probe": 1.2}},
        {"label": "just above Kc", "set": {"K_probe": 2.0}},
        {"label": "deep sync", "set": {"K_probe": 3.5}},
    ],
}

DT = 0.05
SWEEP_POINTS = 25
SWEEP_KMAX = 4.0
SETTLE, MEASURE = 1200, 600
PROBE_STEPS, PROBE_REC = 2400, 5
DISPLAY_CAP = 120  # phases sent for animation; r is computed over all N


def _draw(seed, N, sigma):
    rng = np.random.RandomState(int(seed))
    omega = rng.normal(0.0, sigma, N)
    omega -= omega.mean()
    theta0 = rng.uniform(0, 2 * np.pi, N)
    return omega, theta0


def _meanfield_step(theta, omega, K, dt):
    """Exact uniform-coupling form of ksomheb.kuramoto_step (see docstring).

    theta may be (N,) or batched (M, N); K scalar or (M, 1).
    """
    z = np.exp(1j * theta).mean(axis=-1, keepdims=True)
    r, psi = np.abs(z), np.angle(z)
    return theta + (omega + K * r * np.sin(psi - theta)) * dt


def run(params):
    spec = LAB["controls"]
    N = int(getp(params, spec, "N"))
    sigma = getp(params, spec, "sigma")
    K_probe = getp(params, spec, "K_probe")
    seed = int(getp(params, spec, "seed"))
    mode = params.get("mode", "both")

    Kc = 2.0 * sigma * np.sqrt(2.0 / np.pi)
    out = {"Kc_theory": round(float(Kc), 4)}

    if mode in ("both", "sweep"):
        omega, theta0 = _draw(seed, N, sigma)
        Ks = np.linspace(0.0, SWEEP_KMAX, SWEEP_POINTS)
        theta = np.tile(theta0, (SWEEP_POINTS, 1))
        Kcol = Ks[:, None]
        for _ in range(SETTLE):
            theta = _meanfield_step(theta, omega, Kcol, DT)
        acc = np.zeros(SWEEP_POINTS)
        for _ in range(MEASURE):
            theta = _meanfield_step(theta, omega, Kcol, DT)
            acc += np.abs(np.exp(1j * theta).mean(axis=1))
        out["sweep"] = {"Ks": rounded(Ks, 3),
                        "r": rounded(acc / MEASURE, 4)}

    if mode in ("both", "probe"):
        omega, theta = _draw(seed + 1, N, sigma)
        show = np.linspace(0, N - 1, min(N, DISPLAY_CAP)).astype(int)
        frames, rs = [], []
        for t in range(PROBE_STEPS):
            theta = _meanfield_step(theta, omega, K_probe, DT)
            if t % PROBE_REC == 0:
                r, _ = order_parameter(theta)
                rs.append(r)
                frames.append(np.mod(theta[show], 2 * np.pi))
        out["probe"] = {
            "K": round(float(K_probe), 3),
            "dt_frame": DT * PROBE_REC,
            "phases": [rounded(f, 3) for f in frames],
            "r": rounded(rs, 4),
            "shown": int(len(show)),
        }

    return out
