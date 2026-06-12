"""
Iteration 2 -- Does the Hebbian coupling rule behave as the math predicts?

We isolate the learning rule by FREEZING the phases (no Kuramoto step), so
S_ij and R are constants and the coupling ODE becomes a plain linear
first-order equation per pair:

    dK_ij/dt = eta * S_ij * R - lam * K_ij

Known closed-form solution (same math as an RC circuit charging):

    K_ij(t) = K* + (K_ij(0) - K*) * exp(-lam * t),   K* = eta * S_ij * R / lam

Predictions checked here:
  1. Each K_ij relaxes exponentially to its own fixed point K* = eta*S*R/lam,
     with time constant tau = 1/lam -- pairs with higher synchrony S earn
     proportionally stronger equilibrium coupling. (This is the
     "fire together, wire together" gradient the v1.0 bug destroyed: with
     S identically 1, every pair would share ONE fixed point.)
  2. If K* exceeds K_max the trajectory clamps at K_max.
  3. Negative reward (R < 0): synchronized pairs are driven to the floor at 0;
     zero-synchrony pairs decay passively as K0 * exp(-lam*t) regardless of R
     (this is the pure-Hebbian property: no anti-phase repulsion, only decay).

FINDING (saturation bound): the doc's heuristic parameters give a gain of
eta/lam = 10, so the unclamped fixed point is K* = 10 * S * R. Any sustained
reward R > K_max * lam / eta = 0.2 pushes well-synchronized pairs past K_max,
where the clamp erases the synchrony gradient -- all strong pairs read 2.0.
Differentiated ("informative") coupling requires operating with sustained
reward below that bound, or a larger lam / smaller eta. First run of this
script used R = 1 and hit exactly this: nearly every pair saturated.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ksomheb import local_synchrony

np.random.seed(7)

eta, lam, K_max, dt = 0.01, 0.001, 2.0, 0.01

# Frozen phases chosen to give a spread of pairwise synchronies.
theta = np.array([0.0, 0.4, 1.2, 2.4, np.pi])
N = len(theta)
S = local_synchrony(theta)

R_sat = K_max * lam / eta             # saturation bound on sustained reward
print(f"gain eta/lam = {eta/lam:.0f}; saturation bound R_sat = "
      f"K_max*lam/eta = {R_sat}\n")

def integrate(K0, R, n_steps):
    """Euler-integrate dK/dt = eta*S*R - lam*K with phases frozen."""
    K = K0.copy()
    trace = [K.copy()]
    for _ in range(n_steps):
        dK = eta * (S * R) - lam * K
        K = np.clip(K + dK * dt, 0.0, K_max)
        trace.append(K.copy())
    return K, np.array(trace)

tau = 1.0 / lam                       # time constant of the decay, in time units
n_steps = int(6 * tau / dt)           # 6 tau ~ within 0.25% of equilibrium
t_axis = np.arange(n_steps + 1) * dt

print(f"tau = 1/lam = {tau:.0f} time units; integrating 6 tau "
      f"({n_steps} Euler steps at dt={dt})\n")

# ---- Check 1: relaxation to per-pair fixed point (R inside valid range) ----
R = 0.15                              # below R_sat -> K* = 1.5*S stays under K_max
K0 = np.full((N, N), 0.5); np.fill_diagonal(K0, 0.0)
K_end, trace1 = integrate(K0, R, n_steps)
K_star = eta * S * R / lam

print(f"Check 1: K -> K* = eta*S*R/lam (R={R} < R_sat, start K=0.5)")
print(f"{'pair':>6} | {'S_ij':>6} | {'K* pred':>8} | {'K final':>8} | {'err':>8}")
pairs = [(0, 1), (0, 2), (0, 3), (0, 4)]
for (i, j) in pairs:
    print(f"  ({i},{j}) | {S[i,j]:6.3f} | {K_star[i,j]:8.4f} | "
          f"{K_end[i,j]:8.4f} | {abs(K_end[i,j]-K_star[i,j]):8.1e}")
off = ~np.eye(N, dtype=bool)
# After 6 tau the remaining transient is |K0 - K*| * e^-6 per pair.
err1 = np.abs(K_end - K_star)[off].max()
bound1 = np.abs(K0 - K_star)[off].max() * np.exp(-6)
ok1 = err1 < bound1 * 1.1 + 1e-6
print(f"  max |K_final - K*| = {err1:.2e} "
      f"(analytic transient bound {bound1:.2e})  -> "
      f"{'PASS' if ok1 else 'FAIL'}")

# Check the whole trajectory against the closed form, not just the endpoint.
i, j = 0, 2
analytic = K_star[i, j] + (K0[i, j] - K_star[i, j]) * np.exp(-lam * t_axis)
traj_err = np.abs(trace1[:, i, j] - analytic).max()
ok1b = traj_err < 1e-3
print(f"  trajectory vs closed form (pair (0,2)): max err = {traj_err:.2e}  -> "
      f"{'PASS' if ok1b else 'FAIL'}\n")

# ---- Check 2: clamp at K_max when K* > K_max (the saturation regime) ----
R_big = 1.0                           # > R_sat: K* = 10*S, saturates strong pairs
K_end2, trace2 = integrate(K0, R_big, n_steps)
sat_pairs = K_star_big = eta * S * R_big / lam > K_max
ok2 = (np.isclose(K_end2[0, 1], K_max) and K_end2.max() <= K_max + 1e-12
       and np.isclose(K_end2[0, 3], K_max))   # even moderate-S pair saturates
print(f"Check 2: sustained R={R_big} (> R_sat={R_sat}) -> clamp erases gradient")
print(f"  K(0,1) [S=0.98] final = {K_end2[0,1]:.4f}")
print(f"  K(0,3) [S=0.36] final = {K_end2[0,3]:.4f}   <- indistinguishable!")
print(f"  global max = {K_end2.max():.4f} <= K_max  -> "
      f"{'PASS' if ok2 else 'FAIL'}\n")

# ---- Check 3: negative reward -- synced pairs floor at 0, S=0 pair decays ----
R_neg = -1.0
K_end3, trace3 = integrate(K0, R_neg, n_steps)
synced_ok = K_end3[0, 1] < 1e-9 and K_end3[0, 2] < 1e-9
passive_pred = K0[0, 4] * np.exp(-lam * n_steps * dt)   # S=0: decay only
passive_ok = abs(K_end3[0, 4] - passive_pred) < 1e-4
ok3 = synced_ok and passive_ok
print(f"Check 3: R={R_neg} (below-baseline performance)")
print(f"  synced pairs driven to floor: K(0,1)={K_end3[0,1]:.2e}, "
      f"K(0,2)={K_end3[0,2]:.2e}")
print(f"  S=0 pair decays passively:    K(0,4)={K_end3[0,4]:.4e} "
      f"vs analytic K0*e^-6={passive_pred:.4e}")
print(f"  (pure-Hebbian property: zero-synchrony pairs feel no reward at all)")
print(f"  -> {'PASS' if ok3 else 'FAIL'}\n")

print("ALL PASS" if (ok1 and ok1b and ok2 and ok3) else "SOME CHECKS FAILED")

# ---- plot (decimated traces) ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    step = 200
    td = t_axis[::step]
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.2), sharey=True)
    colors = plt.cm.viridis(np.linspace(0.15, 0.9, len(pairs)))

    ax = axes[0]
    for (i, j), c in zip(pairs, colors):
        ax.plot(td, trace1[::step, i, j], color=c, label=f"S={S[i,j]:.2f}")
        ax.axhline(K_star[i, j], color=c, ls=":", alpha=0.7)
    ax.set_title(f"R={R} (< R_sat): each pair → its own K* = ηSR/λ")
    ax.set_xlabel("time"); ax.set_ylabel("coupling K_ij")
    ax.legend(title="pair synchrony", fontsize=8, loc="upper right")

    ax = axes[1]
    for (i, j), c in zip(pairs, colors):
        ax.plot(td, trace2[::step, i, j], color=c)
    ax.axhline(K_max, color="#d62728", ls="--", label=f"K_max = {K_max}")
    ax.set_title(f"R={R_big} (> R_sat): clamp erases the S gradient")
    ax.set_xlabel("time"); ax.legend(loc="center right")

    ax = axes[2]
    for (i, j), c in zip(pairs, colors):
        ax.plot(td, trace3[::step, i, j], color=c)
    ax.axhline(0, color="#d62728", ls="--", label="floor = 0")
    ax.set_title("R = −1: synced pairs floor; S=0 pair only decays")
    ax.set_xlabel("time"); ax.legend(loc="upper right")

    for ax in axes:
        ax.grid(alpha=0.3)
    fig.suptitle("Iteration 2 — Hebbian rule in isolation (phases frozen)",
                 y=1.02)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter2_hebbian_fixed_point.png")
    fig.tight_layout()
    fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"plot saved -> {out}")
except Exception as e:
    print(f"(plot skipped: {e})")
