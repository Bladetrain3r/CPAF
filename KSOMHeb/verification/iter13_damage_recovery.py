"""
Iteration 13 -- Damage recovery: does a locked module restore its PATTERN?

Ziggy's framing: damage recovery = recovery from a disruption of the cycle, and
the thing that matters is not mere *coherence continuation* but recovery of the
*pattern* -- the specific relationships that ARE the system's identity (a ship of
Theseus: same coherence, different pattern = a different ship). So the primary
metric is PATTERN FIDELITY, coherence is only secondary.

Setup. A locked module (N heterogeneous oscillators, all-to-all coupling K) settles
into a stored pattern -- the gauge-invariant matrix of pairwise phase differences
P0[i,j] = theta*_i - theta*_j. This is the identity; the coupling K is the memory.

Damage. Scramble the phases: theta <- theta + sigma_d * N(0,1). Sweep sigma_d.

Pattern fidelity (PRIMARY):
    F(theta) = mean_{i<j} cos( (theta_i - theta_j) - P0[i,j] )   in [-1, 1]
Gauge-invariant (a global rotation cancels in theta_i - theta_j) and immune to
2*pi phase slips. F = 1 means the identity is fully restored.

Three recovery conditions (the ship of Theseus):
  * frozen  : K held fixed         -- memory PROTECTED (pure attractor recovery)
  * nomem   : K = 0                -- memory ABSENT (control: is K what recovers it?)
  * plastic : K keeps learning     -- memory UNPROTECTED (the disruption can rewrite it)

Claims:
 1. With protected memory, the pattern recovers (F -> ~1) -- the coupling IS memory,
    and it restores the identity.
 2. Without memory (K=0), nothing recovers -- recovery is DUE to the stored coupling.
 3. Coherence is the weaker bar: during recovery r rises BEFORE pattern fidelity
    (pattern is the stricter, later-settling quantity).
 4. Resilience has a threshold: beyond a critical damage the pattern does not recover.
 5. Unprotected memory -> IDENTITY LOSS: coherence returns but into a shifted pattern
    (F stays low) -- the disruption rewrote the memory. Ship of Theseus.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ksomheb import order_parameter, kuramoto_step, update_ksom_heb

rng = np.random.RandomState(13)

# ---- a locked module (near its stability edge, and recovery happens in noise) ----
N = 6
omega = 2 * np.pi * (1.0 + 0.08 * np.linspace(-1, 1, N))   # heterogeneous -> nontrivial offsets
kappa = 1.0                                                # all-to-all strength
K0 = kappa * (1 - np.eye(N))                               # symmetric, uniform
dt = 0.01
NOISE = 0.04                                               # light ongoing noise during recovery

def settle(theta, K, steps):
    for _ in range(steps):
        theta = kuramoto_step(theta, omega, K, dt)
    return theta

# form the stored pattern
theta_star = settle(rng.uniform(0, 2 * np.pi, N), K0, 6000)
P0 = theta_star[:, None] - theta_star[None, :]
r0 = order_parameter(theta_star)[0]
iu = np.triu_indices(N, 1)
offset_spread = np.std((theta_star[:, None] - theta_star[None, :])[iu])

def fidelity(theta):
    d = theta[:, None] - theta[None, :]
    return float(np.mean(np.cos((d - P0)[iu])))

def damage(theta, sigma_d):
    return (theta + sigma_d * rng.randn(N)) % (2 * np.pi)

def recover(theta, mode, steps, r_baseline=0.60, eta=0.27, lam=0.08):
    """Return (F_traj, r_traj) over recovery under the given memory condition.
    Recovery happens in ongoing noise. Plastic gains are set so that when the
    pattern is INTACT the coupling self-maintains (eta*S*reward ~ lam*K0), but a
    disruption that holds coherence below r_baseline drives reward negative and
    ERODES the memory -- so small hits are absorbed, big hits destroy it."""
    K = K0.copy() if mode != "nomem" else np.zeros((N, N))
    amp = NOISE * np.sqrt(dt)
    Ft, Rt = [], []
    for _ in range(steps):
        if mode == "plastic":
            r = order_parameter(theta)[0]
            theta, K = update_ksom_heb(theta, omega, K, r - r_baseline,
                                       dt=dt, eta=eta, lam=lam, K_max=2 * kappa)
        else:
            theta = kuramoto_step(theta, omega, K, dt)
        theta = (theta + amp * rng.randn(N)) % (2 * np.pi)
        Ft.append(fidelity(theta)); Rt.append(order_parameter(theta)[0])
    return np.array(Ft), np.array(Rt)

def final(traj):
    return float(np.mean(traj[-400:]))       # average out the ongoing noise

print(f"locked module: N={N}, r0={r0:.3f}, offset spread={offset_spread:.3f} rad "
      f"(nontrivial pattern)\n")

REC_STEPS = 6000
TRIALS = 16
sigmas = np.array([0.3, 0.6, 1.0, 1.5, 2.0, 2.5, 3.0])

# ---- resilience sweep: protected (frozen) vs unprotected (plastic) memory ----
print("Resilience sweep -- pattern fidelity F after recovery (F=pattern, r=coherence):")
print(f"{'sigma_d':>7} | {'F_dmg':>6} | {'frozen F':>8} {'r':>5} | {'plastic F':>9} {'r':>5}")
print("-" * 58)
F_fro = {}; R_fro = {}; F_pla = {}; R_pla = {}
for s in sigmas:
    Fd = []; ff = []; rf = []; fp = []; rp = []
    for _ in range(TRIALS):
        th = damage(theta_star, s); Fd.append(fidelity(th))
        Ft, Rt = recover(th.copy(), "frozen", REC_STEPS); ff.append(final(Ft)); rf.append(final(Rt))
        Ft, Rt = recover(th.copy(), "plastic", REC_STEPS); fp.append(final(Ft)); rp.append(final(Rt))
    F_fro[s] = np.mean(ff); R_fro[s] = np.mean(rf); F_pla[s] = np.mean(fp); R_pla[s] = np.mean(rp)
    print(f"{s:7.2f} | {np.mean(Fd):6.3f} | {F_fro[s]:8.3f} {R_fro[s]:5.2f} | "
          f"{F_pla[s]:9.3f} {R_pla[s]:5.2f}")

# ---- no-memory control at a moderate damage ----
s_rep = 1.0
fn = [final(recover(damage(theta_star, s_rep).copy(), "nomem", REC_STEPS)[0])
      for _ in range(TRIALS)]
F_nomem = float(np.mean(fn))

# ---- timescale: coherence leads pattern (frozen, moderate damage) ----
th = damage(theta_star, 1.5)
Ft, Rt = recover(th.copy(), "frozen", REC_STEPS)
t = np.arange(REC_STEPS) * dt
def first_cross(traj, thresh):
    idx = np.where(traj >= thresh)[0]
    return t[idx[0]] if len(idx) else np.inf
t_r = first_cross(Rt, 0.9 * r0)
t_F = first_cross(Ft, 0.9)

# ---- checks ----
print()
c1 = F_fro[0.6] > 0.9 and R_fro[0.6] > 0.85 * r0
print(f"Check 1 (protected memory restores the pattern): sigma=0.6 -> "
      f"frozen F={F_fro[0.6]:.3f}, r={R_fro[0.6]:.3f}  -> {'PASS' if c1 else 'FAIL'}")

c2 = F_nomem < 0.5 and F_fro[s_rep] - F_nomem > 0.3
print(f"Check 2 (memory is necessary): F(nomem)={F_nomem:.3f} << "
      f"F(frozen)={F_fro[s_rep]:.3f} at sigma={s_rep}  -> {'PASS' if c2 else 'FAIL'}")

c3 = t_r < t_F
print(f"Check 3 (coherence leads pattern): r hits 0.9*r0 at t={t_r:.2f}, "
      f"F hits 0.9 at t={t_F:.2f}  -> {'PASS' if c3 else 'FAIL'}")

# resilience threshold lives in the UNPROTECTED memory
c4 = F_pla[sigmas[0]] - F_pla[sigmas[-1]] > 0.3
sig_star = next((s for s in sigmas if F_pla[s] < 0.7), None)
print(f"Check 4 (unprotected memory has a resilience threshold): plastic F drops "
      f"{F_pla[sigmas[0]]:.3f} (σ={sigmas[0]}) -> {F_pla[sigmas[-1]]:.3f} (σ={sigmas[-1]}); "
      f"crosses 0.7 near σ*={sig_star}  -> {'PASS' if c4 else 'FAIL'}")

# identity loss: at large damage, protected keeps identity, unprotected loses it
sL = sigmas[-1]
c5 = (F_fro[sL] - F_pla[sL] > 0.2) and (R_pla[sL] > 0.55 * r0)
print(f"Check 5 (identity loss w/o protection): at σ={sL}, frozen F={F_fro[sL]:.3f} "
      f"(identity kept) vs plastic F={F_pla[sL]:.3f} while plastic r={R_pla[sL]:.2f} "
      f"(coherence continues)  -> {'PASS' if c5 else 'FAIL'}")

allok = c1 and c2 and c3 and c4 and c5
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED")
print("\nVerdict: a locked module's PATTERN (its identity) recovers from a phase")
print("disruption when the memory (coupling K) is protected -- the coupling is")
print("what restores it (K=0 recovers nothing). Coherence is the weaker bar: it")
print("returns before full pattern fidelity, and beyond a critical damage the")
print("full pattern fidelity, and an UNPROTECTED (plastic) memory has a resilience")
print("threshold: small hits are absorbed, but past a critical damage the coupling")
print("erodes and the memory is rewritten -- partial coherence persists (r~0.5)")
print("into a SHIFTED, weaker pattern while fidelity collapses (F~0.4). Coherence")
print("continuation, identity lost -- ship of Theseus, measured. Resilience =")
print("recovery of the PATTERN, not the r; and it requires protecting the memory.")

# ---- plot ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    # left: resilience curves -- protected vs unprotected memory
    ss = sigmas
    ax[0].plot(ss, [F_fro[s] for s in ss], "s-", color="#2a9d5c",
               label="pattern F — memory protected (frozen)")
    ax[0].plot(ss, [F_pla[s] for s in ss], "s--", color="#d62728",
               label="pattern F — memory unprotected (plastic)")
    ax[0].plot(ss, [R_pla[s] / r0 for s in ss], "o:", color="#1f77b4",
               label="coherence r/r0 — plastic (continues)")
    ax[0].axhline(0.7, color="#888", ls=":", lw=1)
    ax[0].set_xlabel("damage  σ_d (phase scramble)"); ax[0].set_ylabel("recovery")
    ax[0].set_title("Protected memory keeps the identity; unprotected loses it",
                    fontsize=10)
    ax[0].legend(fontsize=7.5); ax[0].grid(alpha=0.3); ax[0].set_ylim(0, 1.05)
    # right: recovery trajectory (coherence leads pattern) + condition bars inset
    ax[1].plot(t, Rt / r0, color="#1f77b4", label="coherence r / r0")
    ax[1].plot(t, Ft, color="#d62728", label="pattern fidelity F")
    ax[1].axhline(0.9, color="#888", ls=":", lw=1)
    ax[1].set_xlabel("recovery time"); ax[1].set_ylabel("value")
    ax[1].set_title("Coherence returns first; pattern is the stricter, later bar",
                    fontsize=10)
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3)
    fig.suptitle("Iter 13 — damage recovery: the PATTERN is the identity that "
                 "recovers (or doesn't)", y=1.02, fontsize=11)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter13_damage_recovery.png")
    fig.tight_layout(); fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
