"""
Iteration 1 -- Does the base dynamics synchronize like Kuramoto theory says?

Everything in K-SOM-Heb sits on top of the Kuramoto order parameter r. Before
trusting the Hebbian layer, we check the foundation: with fixed, uniform
all-to-all coupling of strength K, the steady-state r should stay near 0 while
K is small and rise sharply past a critical coupling Kc -- the classic
synchronization phase transition.

Mean-field theory (N -> infinity, frequencies drawn from a symmetric unimodal
density g) predicts onset at:

    Kc = 2 / (pi * g(0))

For Gaussian natural frequencies N(0, sigma^2), g(0) = 1/(sigma*sqrt(2*pi)),
so Kc = 2 * sigma * sqrt(2/pi) ~= 1.596 * sigma.

We sweep K, integrate to steady state, time-average r, and compare the
empirical onset to this prediction.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ksomheb import order_parameter, kuramoto_step

np.random.seed(42)

N = 400
sigma = 1.0
omega = np.random.normal(0.0, sigma, N)
omega -= omega.mean()                     # remove drift -> work in mean frame

Kc_theory = 2.0 * sigma * np.sqrt(2.0 / np.pi)

dt = 0.05
T_settle = 2000                            # steps discarded (transient)
T_measure = 1000                           # steps averaged (steady state)

Ks = np.linspace(0.0, 4.0, 21)
r_of_K = []
for K in Ks:
    theta = np.random.uniform(0, 2 * np.pi, N)
    Kmat = np.full((N, N), K)
    np.fill_diagonal(Kmat, 0.0)
    for _ in range(T_settle):
        theta = kuramoto_step(theta, omega, Kmat, dt)
    acc = 0.0
    for _ in range(T_measure):
        theta = kuramoto_step(theta, omega, Kmat, dt)
        acc += order_parameter(theta)[0]
    r_of_K.append(acc / T_measure)
r_of_K = np.array(r_of_K)

# Empirical onset: first K where steady r crosses a small threshold.
thresh = 0.25
above = np.where(r_of_K > thresh)[0]
Kc_emp = Ks[above[0]] if len(above) else float("nan")

print(f"{'K':>6} | {'steady-state r':>14}")
print("-" * 25)
for K, r in zip(Ks, r_of_K):
    bar = "#" * int(round(r * 30))
    mark = "  <- Kc(theory)" if abs(K - Kc_theory) < (Ks[1] - Ks[0]) / 2 else ""
    print(f"{K:6.2f} | {r:6.3f} {bar}{mark}")
print()
print(f"Kc (mean-field theory) = {Kc_theory:.3f}")
print(f"Kc (empirical, r>{thresh}) ~ {Kc_emp:.3f}")
print(f"r stays low (incoherent) below Kc and rises above it: "
      f"{r_of_K[Ks < Kc_theory*0.7].max():.3f} -> {r_of_K[Ks > Kc_theory*1.5].min():.3f}")

# ---- plot ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(Ks, r_of_K, "o-", color="#1f77b4", label="measured steady-state r")
    ax.axvline(Kc_theory, color="#d62728", ls="--",
               label=f"Kc theory = {Kc_theory:.2f}")
    ax.set_xlabel("coupling strength K")
    ax.set_ylabel("order parameter r")
    ax.set_title(f"Kuramoto synchronization transition (N={N}, Gaussian freqs)")
    ax.set_ylim(-0.02, 1.02)
    ax.legend()
    ax.grid(alpha=0.3)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter1_kuramoto_transition.png")
    fig.tight_layout()
    fig.savefig(out, dpi=110)
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
