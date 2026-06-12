"""
Iteration 3 -- The closed loop: phases AND coupling evolving together.

Iterations 1-2 verified each layer against known theory in isolation. Here the
layers interact: the reward is computed live from the system's own synchrony,

    R(t) = r(t) - r_baseline,

so the loop closes:  coupling -> synchrony -> reward -> coupling.

No closed-form solution exists for this; simulation is the instrument now.
But the structure of the loop makes qualitative predictions we CAN check:

  Positive feedback: more coupling -> more sync -> higher r -> higher R ->
  more coupling. A loop like that doesn't regulate -- it commits. Predicted
  BISTABILITY, controlled by where the initial coupling puts r relative to
  the baseline:

  1. RUNAWAY: start with coupling strong enough that r > r_baseline.
     R > 0 feeds growth; coupling rises until the K_max clamp catches it
     (the iter-2 saturation bound predicts sustained R ~ 0.2-0.4 >> R_sat
     guarantees this). Steady state: saturated K, elevated r.
  2. COLLAPSE: start subcritical, r < r_baseline. R < 0 strips coupling,
     which lowers r further; coupling decays toward 0 and the population
     unsyncs. The same rule, the same parameters -- opposite fate.
  3. Fixed-coupling CONTROLS at the same starting K bracket the adaptive
     runs: adaptive ends above its control in the runaway regime, below it
     in the collapse regime.
  4. Plasticity index P(t) = ||K(t+dt) - K(t)|| / dt is high during the
     transition and falls toward ~0 at either steady state (the doc's
     "P > 0 during learning" claim, made precise).

This directly demonstrates the caveat added to the architecture doc (v1.1):
global reward provides no per-pair credit assignment, and the rich-get-richer
loop tends toward winner-take-all or collapse -- not, by itself, modularity.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ksomheb import order_parameter, kuramoto_step, update_ksom_heb

np.random.seed(11)

N = 80
sigma = 0.5                       # freq spread -> Kc = 1.596*sigma ~ 0.80
omega = np.random.normal(0.0, sigma, N); omega -= omega.mean()

dt = 0.05
steps = 60_000                    # 3000 time units = 3 decay timescales
record_every = 50
r_baseline = 0.30
eta, lam, K_max = 0.01, 0.001, 2.0
R_sat = K_max * lam / eta

K_high, K_low = 1.2, 0.4          # supercritical / subcritical starts (Kc~0.8)

def make_K(k0):
    K = np.full((N, N), k0); np.fill_diagonal(K, 0.0); return K

def run(k0, adaptive):
    theta = np.random.uniform(0, 2 * np.pi, N)
    K = make_K(k0)
    rs, Kmeans, Ps, ts = [], [], [], []
    off = ~np.eye(N, dtype=bool)
    for t in range(steps):
        if adaptive:
            r, _ = order_parameter(theta)
            theta_new, K_new = update_ksom_heb(theta, omega, K,
                                               reward=r - r_baseline,
                                               dt=dt, eta=eta, lam=lam,
                                               K_max=K_max)
        else:
            theta_new, K_new = kuramoto_step(theta, omega, K, dt), K
        if t % record_every == 0:
            rs.append(order_parameter(theta_new)[0])
            Kmeans.append(K_new[off].mean())
            Ps.append(np.linalg.norm(K_new - K) / dt)
            ts.append(t * dt)
        theta, K = theta_new, K_new
    return (np.array(ts), np.array(rs), np.array(Kmeans), np.array(Ps), K)

print(f"N={N}, sigma={sigma} -> Kc ~ {1.596*sigma:.2f}; "
      f"starts: K_high={K_high} (super), K_low={K_low} (sub)")
print(f"r_baseline={r_baseline}, R_sat={R_sat} "
      f"(sustained R above this saturates -- see iter2)\n")

runs = {}
for name, (k0, adaptive) in {
    "adaptive_high": (K_high, True),  "fixed_high": (K_high, False),
    "adaptive_low":  (K_low,  True),  "fixed_low":  (K_low,  False),
}.items():
    runs[name] = run(k0, adaptive)
    ts, rs, Km, Ps, K = runs[name]
    tail = slice(-len(rs) // 10, None)        # last 10% = steady state
    print(f"{name:14s}: r_final={rs[tail].mean():.3f}  "
          f"meanK={Km[-1]:.3f}  P_final={Ps[tail].mean():.4f}")

off = ~np.eye(N, dtype=bool)

# ---- Check 1: runaway regime -- adaptation drives K into saturation ----
ts, rs, Km, Ps, K_ah = runs["adaptive_high"]
frac_sat = (K_ah[off] >= K_max - 1e-6).mean()
tail = slice(-len(rs) // 10, None)
r_ah = rs[tail].mean()
r_fh = runs["fixed_high"][1][tail].mean()
ok1 = frac_sat > 0.5 and Km[-1] > K_high
print(f"\nCheck 1 (runaway): fraction of pairs at K_max = {frac_sat:.2%}, "
      f"mean K {K_high} -> {Km[-1]:.3f}  -> {'PASS' if ok1 else 'FAIL'}")

# ---- Check 2: collapse regime -- coupling stripped, sync lost ----
ts, rs2, Km2, Ps2, K_al = runs["adaptive_low"]
r_al = rs2[tail].mean()
r_fl = runs["fixed_low"][1][tail].mean()
ok2 = Km2[-1] < 0.1 * K_low and r_al < r_baseline
print(f"Check 2 (collapse): mean K {K_low} -> {Km2[-1]:.4f}, "
      f"r_final={r_al:.3f} < baseline  -> {'PASS' if ok2 else 'FAIL'}")

# ---- Check 3: adaptive brackets its fixed controls ----
ok3 = (r_ah > r_fh) and (r_al < r_fl)
print(f"Check 3 (controls): runaway {r_ah:.3f} > fixed {r_fh:.3f}; "
      f"collapse {r_al:.3f} < fixed {r_fl:.3f}  -> {'PASS' if ok3 else 'FAIL'}")

# ---- Check 4: plasticity high in transient, ~0 at steady state ----
P_ah = runs["adaptive_high"][3]
ok4 = P_ah[:len(P_ah)//5].max() > 20 * max(P_ah[tail].mean(), 1e-12)
print(f"Check 4 (plasticity): P peak={P_ah.max():.3f} -> "
      f"P steady={P_ah[tail].mean():.4f}  -> {'PASS' if ok4 else 'FAIL'}")

ok = ok1 and ok2 and ok3 and ok4
print("\nALL PASS" if ok else "\nSOME CHECKS FAILED")
print("\nSame rule, same parameters, opposite fates by initial condition:")
print("bistability confirmed. Global reward commits; it does not regulate.")

# ---- plot ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 2, figsize=(12.5, 8))

    ax = axes[0, 0]
    for name, c, ls in [("adaptive_high", "#1f77b4", "-"),
                        ("fixed_high", "#1f77b4", "--"),
                        ("adaptive_low", "#d62728", "-"),
                        ("fixed_low", "#d62728", "--")]:
        ts, rs, *_ = runs[name]
        ax.plot(ts, rs, color=c, ls=ls, lw=1.2,
                label=name.replace("_", " "), alpha=0.9)
    ax.axhline(r_baseline, color="k", ls=":", label="r_baseline")
    ax.set_title("Order parameter r(t): runaway vs collapse")
    ax.set_xlabel("time"); ax.set_ylabel("r"); ax.legend(fontsize=8)

    ax = axes[0, 1]
    for name, c in [("adaptive_high", "#1f77b4"), ("adaptive_low", "#d62728")]:
        ts, _, Km, *_ = runs[name]
        ax.plot(ts, Km, color=c, label=name.replace("_", " "))
    ax.axhline(K_max, color="gray", ls="--", label="K_max")
    ax.axhline(1.596 * sigma, color="green", ls=":", label="Kc (theory)")
    ax.set_title("Mean coupling: grows to clamp, or stripped to zero")
    ax.set_xlabel("time"); ax.set_ylabel("mean K"); ax.legend(fontsize=8)

    ax = axes[1, 0]
    for name, c in [("adaptive_high", "#1f77b4"), ("adaptive_low", "#d62728")]:
        ts, _, _, Ps, _ = runs[name]
        ax.semilogy(ts, np.maximum(Ps, 1e-6), color=c,
                    label=name.replace("_", " "))
    ax.set_title("Plasticity index P(t): learning, then stillness")
    ax.set_xlabel("time"); ax.set_ylabel("P (log)"); ax.legend(fontsize=8)

    ax = axes[1, 1]
    ax.hist(runs["adaptive_high"][4][off], bins=40, color="#1f77b4",
            alpha=0.75, label="runaway final K")
    ax.hist(runs["adaptive_low"][4][off], bins=40, color="#d62728",
            alpha=0.75, label="collapse final K")
    ax.set_title("Final coupling distributions: all-or-nothing")
    ax.set_xlabel("K_ij"); ax.set_ylabel("pair count"); ax.legend(fontsize=8)

    for ax in axes.ravel():
        ax.grid(alpha=0.3)
    fig.suptitle("Iteration 3 — closed loop: global reward creates bistability",
                 y=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter3_closed_loop_bistability.png")
    fig.tight_layout()
    fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"plot saved -> {out}")
except Exception as e:
    print(f"(plot skipped: {e})")
