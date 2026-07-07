"""
Iteration 4 -- Does the coupling matrix become a modular "memory"?

The doc claims "connectivity IS memory" and that "functional networks emerge
from experience." Iteration 3 showed a global reward yields an all-or-nothing K
(one bit). The doc's proposed rescue is heterogeneous (local/hybrid) reward.
This iteration tests both the rescue and the underlying claim -- and finds the
claim does not hold for the pure-Hebbian dynamics as specified.

Setup: hidden structure. N oscillators in two frequency clusters
    group A: omega ~ +Delta,   group B: omega ~ -Delta   (+ small jitter),
Delta large enough that, LEFT ALONE, A and B cannot cross-entrain (their
cross-cluster synchrony is low) while within-group oscillators lock tightly.
Ground-truth module = group membership (used only for scoring).

Two findings, each with a control:

(1) Reward mode is nearly irrelevant to the learned structure. A per-node
    reward R_i multiplies ALL of node i's links equally, so it cancels out of
    the within/cross coupling ratio:
        K*_within/K*_cross = (S_within*R)/(S_cross*R) = S_within/S_cross.
    Only S_ij carries per-pair information. Control: an S==1 ablation (the v1.0
    bug) erases even the weak structure that exists -> contrast collapses to 1.

(2) The architecture does NOT recover the hidden modules. All-to-all Hebbian
    coupling with positive reward is self-reinforcing: as long as cross-links
    survive, they ENTRAIN the two clusters, which raises cross-synchrony, which
    (Hebbian) keeps the cross-links alive. The system homogenizes toward ONE
    global module (or collapses), rather than differentiating into two.
    Control/smoking gun: cross-cluster synchrony measured with the clusters
    ISOLATED (cross-coupling forced to 0) is far lower than in the coupled
    steady state -- entrainment inflates it and prevents modularization.

Conclusion for CPAF: modularity Q is not a reliable emergent metric here.
Recovering pre-existing modules would need an extra ingredient the doc does not
specify (coupling competition/normalization, a distance/anti-Hebbian term, or
genuinely per-PAIR reward) -- flagged, not silently assumed.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ksomheb import (order_parameter, kuramoto_step, local_synchrony,
                     update_ksom_heb, local_field_coherence, modularity,
                     reward_matrix)

np.random.seed(23)

N = 60
half = N // 2
groups = np.array([0] * half + [1] * (N - half))
Delta = 1.4
jitter = 0.12
omega = np.where(groups == 0, +Delta, -Delta) + np.random.normal(0, jitter, N)

dt = 0.05
steps = 50_000
r_baseline = 0.10
eta, lam, K_max = 0.01, 0.005, 2.0   # coupled (non-collapsing) regime
alpha = 0.5
K0 = 0.8

within = (groups[:, None] == groups[None, :]).copy()
cross = ~within
np.fill_diagonal(within, False)
block_mask = within | np.eye(N, dtype=bool)     # keep only within-group links

def make_K(block_diagonal=False):
    K = np.full((N, N), K0)
    np.fill_diagonal(K, 0.0)
    if block_diagonal:
        K[cross] = 0.0
    return K

def run(mode):
    rng = np.random.RandomState(1)
    theta = rng.uniform(0, 2 * np.pi, N)
    # "isolated" reference keeps a static block-diagonal coupling: the two
    # clusters run side by side with NO cross-links, so we can read off the
    # cross-synchrony the frequency gap alone permits.
    isolated = (mode == "isolated")
    K = make_K(block_diagonal=isolated)
    for t in range(steps):
        if isolated:
            theta = kuramoto_step(theta, omega, K, dt)   # coupling frozen
            continue
        if mode == "local":
            reward = local_field_coherence(theta, K) - r_baseline
        elif mode == "hybrid":
            rg = order_parameter(theta)[0] - r_baseline
            rl = local_field_coherence(theta, K) - r_baseline
            reward = alpha * rg + (1 - alpha) * rl
        else:  # global, ablation
            reward = order_parameter(theta)[0] - r_baseline
        if mode == "ablation":
            theta = kuramoto_step(theta, omega, K, dt)
            dK = eta * (1.0 * reward_matrix(reward)) - lam * K   # S == 1
            np.fill_diagonal(dK, 0.0)
            K = np.clip(K + dK * dt, 0.0, K_max)
        else:
            theta, K = update_ksom_heb(theta, omega, K, reward,
                                       dt=dt, eta=eta, lam=lam, K_max=K_max)
    return theta, K

def report(mode, theta, K):
    S = local_synchrony(theta)
    w, c = K[within].mean(), K[cross].mean()
    contrast = w / c if c > 1e-9 else float("inf")
    Sc = S[cross].mean()
    Q = modularity(K, groups)
    print(f"{mode:8s}| K_within={w:5.3f} K_cross={c:5.3f} within/cross={contrast:5.2f}"
          f"  S_within={S[within].mean():.3f} S_cross={Sc:.3f}  Q={Q:+.3f}")
    return dict(mode=mode, within=w, cross=c, contrast=contrast, Sc=Sc, Q=Q, K=K)

print(f"N={N} (2x{half}), Delta={Delta}, baseline={r_baseline}, "
      f"regime eta/lam={eta/lam:.0f}\n")
res = {}
for mode in ("global", "local", "hybrid", "ablation", "isolated"):
    theta, K = run(mode)
    res[mode] = report(mode, theta, K)

g, l, h, a, iso = (res[m] for m in ("global", "local", "hybrid", "ablation", "isolated"))
real = [g, l, h]

# ---- checks ----
# 1. Reward mode barely changes the structure (contrast spread tiny).
spread = max(m["contrast"] for m in real) - min(m["contrast"] for m in real)
ok1 = spread < 0.25
# 2. S==1 ablation erases even the weak structure -> contrast ~ 1, Q ~ 0.
ok2 = a["contrast"] < 1.05 and abs(a["Q"]) < 0.02
# 3. Modules are NOT recovered: coupled cross-synchrony is inflated far above
#    the isolated reference -> entrainment prevents modularization.
ok3 = min(m["Sc"] for m in real) > 1.8 * iso["Sc"]
# 4. The realized modular contrast stays weak (<1.5), nowhere near the
#    within/cross separation the isolated frequency structure would allow.
ok4 = max(m["contrast"] for m in real) < 1.5

print()
print(f"Check 1 (reward mode ~irrelevant: contrast spread {spread:.3f} < 0.25)   -> "
      f"{'PASS' if ok1 else 'FAIL'}")
print(f"Check 2 (S==1 ablation erases structure: contrast~1, Q~0)          -> "
      f"{'PASS' if ok2 else 'FAIL'}")
print(f"Check 3 (entrainment inflates cross-sync: coupled S_cross {min(m['Sc'] for m in real):.2f}"
      f" > 1.8x isolated {iso['Sc']:.2f}) -> {'PASS' if ok3 else 'FAIL'}")
print(f"Check 4 (modules NOT recovered: best contrast {max(m['contrast'] for m in real):.2f} < 1.5) -> "
      f"{'PASS' if ok4 else 'FAIL'}")
allok = ok1 and ok2 and ok3 and ok4
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED")
print("\nVerdict: the doc's 'functional modules emerge' claim does NOT hold for")
print("pure Hebbian all-to-all coupling. Reward mode is a red herring for")
print("modularity (it cancels from the within/cross ratio); the only per-pair")
print("signal is S_ij, and self-entrainment drives cross-S up until the two")
print("clusters merge into one module. CPAF should not treat modularity Q as an")
print("emergent given -- it needs coupling competition or per-pair credit first.")

# ---- plot ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 5, figsize=(18, 3.9))
    order = ("isolated", "global", "local", "hybrid", "ablation")
    labels = {"isolated": "isolated ref\n(no cross-links)",
              "ablation": "ablation\n(S==1, v1.0 bug)"}
    for ax, mode in zip(axes, order):
        R = res[mode]
        im = ax.imshow(R["K"], cmap="viridis", vmin=0, vmax=K_max)
        title = labels.get(mode, mode)
        ax.set_title(f"{title}\nw/c={R['contrast']:.2f}, Sc={R['Sc']:.2f}, "
                     f"Q={R['Q']:+.2f}", fontsize=9)
        ax.axhline(half - 0.5, color="w", lw=0.6, alpha=0.5)
        ax.axvline(half - 0.5, color="w", lw=0.6, alpha=0.5)
        ax.set_xticks([]); ax.set_yticks([])
    fig.colorbar(im, ax=axes[-1], fraction=0.046, label="K_ij")
    fig.suptitle("Iteration 4 — Hebbian coupling homogenizes (one module), it "
                 "does not recover the two hidden clusters", y=1.04)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter4_reward_modes_modularity.png")
    fig.tight_layout()
    fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
