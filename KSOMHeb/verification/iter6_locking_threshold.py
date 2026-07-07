"""
Iteration 6 -- The phase-locking transition, and a *derived* coherence threshold.

Origin: a two-oscillator "entangle/disentangle" demo (Opus3/GPT3-era, preserved
as twoosc_entangle_demo.py). This iteration makes its implicit claim rigorous:
that two coupled oscillators undergo a sharp transition from drifting (noise) to
locked (coherent) at a critical coupling -- and that the order parameter at that
onset is exactly 1/sqrt(2), which is a *derived* value for the ~0.7 coherence
threshold the architecture otherwise picks by hand.

The reduction (why N=2 is exactly solvable)
-------------------------------------------
Full pair:  phi1' = w1 + K sin(phi2-phi1),  phi2' = w2 + K sin(phi1-phi2).
Let psi = phi1 - phi2 and Dw = w1 - w2. Subtracting collapses two equations to ONE:

    dpsi/dt = Dw - 2K sin(psi)

A locked state is a fixed point (dpsi/dt = 0): sin(psi*) = Dw/(2K). Real solution
exists iff |Dw/(2K)| <= 1, i.e.

    K >= Kc = |Dw| / 2                         (saddle-node bifurcation)

Stable branch has psi* in (-pi/2, pi/2), so the coherence R = |cos(psi*/2)| lies
in (1/sqrt(2), 1]. At onset (K = Kc) psi* = +-pi/2 and

    R_onset = |cos(pi/4)| = 1/sqrt(2) ~= 0.7071

Since our per-pair synchrony S_ij IS this R, a pair can phase-lock only when
S_ij > 1/sqrt(2). That is the derived threshold.

Checks:
  1. The 1-D reduction reproduces the full 2-oscillator order parameter.
  2. Empirical Kc (drift rate -> 0) equals |Dw|/2, across several detunings.
  3. Locked-branch R matches |cos(psi*/2)|; R at onset = 1/sqrt(2).
  4. Below Kc the phase drifts (noise); above Kc it locks (deviation).
  5. Noise smears the sharp threshold (stochastic bifurcation).
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ksomheb import order_parameter   # for the full-sim cross-check

INV_SQRT2 = 1.0 / np.sqrt(2.0)

# ---------- integrators ----------
def integrate_psi(Dw, K, T=800.0, dt=0.01, noise=0.0, seed=0):
    """Reduced 1-D phase-difference dynamics dpsi = (Dw - 2K sin psi) dt + noise.
    Returns (drift_rate, mean_R) measured over the last 30% (steady state)."""
    rng = np.random.RandomState(seed)
    psi = rng.uniform(0, 2 * np.pi)
    n = int(T / dt)
    burn = int(0.7 * n)
    # sqrt(2) because two independent phase noises combine in the difference
    amp = noise * np.sqrt(2.0)
    psi_unwrap = psi
    prev = psi
    start_val = None; start_t = None
    Rsum = 0.0; cnt = 0
    for k in range(n):
        dpsi = (Dw - 2 * K * np.sin(psi)) * dt
        if noise:
            dpsi += amp * np.sqrt(dt) * rng.randn()
        psi += dpsi
        # track unwrapped psi for drift rate
        psi_unwrap += dpsi
        if k == burn:
            start_val = psi_unwrap; start_t = k * dt
        if k > burn:
            Rsum += abs(np.cos(psi / 2.0)); cnt += 1
    drift = abs(psi_unwrap - start_val) / (n * dt - start_t)
    return drift, Rsum / max(cnt, 1)

def integrate_full(w1, w2, K, T=800.0, dt=0.01, seed=0):
    """Full two-oscillator sim; returns steady-state mean order parameter."""
    rng = np.random.RandomState(seed)
    p1 = rng.uniform(0, 2 * np.pi); p2 = rng.uniform(0, 2 * np.pi)
    n = int(T / dt); burn = int(0.7 * n)
    Rsum = 0.0; cnt = 0
    for k in range(n):
        d1 = w1 + K * np.sin(p2 - p1)
        d2 = w2 + K * np.sin(p1 - p2)
        p1 += d1 * dt; p2 += d2 * dt
        if k > burn:
            Rsum += order_parameter([p1, p2])[0]; cnt += 1
    return Rsum / cnt

# ---------- setup (the demo's numbers) ----------
w1, w2 = 2 * np.pi * 1.00, 2 * np.pi * 1.03
Dw = w1 - w2
Kc = abs(Dw) / 2
print(f"demo detuning |Dw| = {abs(Dw):.4f}  ->  Kc = |Dw|/2 = {Kc:.4f}")
print(f"predicted R at locking onset = 1/sqrt(2) = {INV_SQRT2:.4f}\n")

# ---------- Check 1: reduction reproduces the full sim ----------
print("Check 1 -- 1-D reduction vs full two-oscillator sim (mean R):")
red_ok = True
for K in [0.12, 0.2, 0.5, 1.0]:
    _, R_red = integrate_psi(Dw, K)
    R_full = integrate_full(w1, w2, K)
    ok = abs(R_red - R_full) < 0.02
    red_ok &= ok
    print(f"  K={K:4.2f}: reduced R={R_red:.3f}  full R={R_full:.3f}  "
          f"{'ok' if ok else 'MISMATCH'}")
print(f"  -> {'PASS' if red_ok else 'FAIL'}\n")

# ---------- Check 2: Kc = |Dw|/2 across detunings ----------
print("Check 2 -- empirical Kc (drift rate collapses) vs |Dw|/2:")
kc_ok = True
for Dw_test in [abs(Dw), 0.40, 0.80]:
    Ks = np.linspace(0.2 * Dw_test / 2, 2.0 * Dw_test / 2, 40)
    drifts = [integrate_psi(Dw_test, K)[0] for K in Ks]
    # empirical Kc = first K whose drift rate is essentially zero
    locked = np.where(np.array(drifts) < 1e-3)[0]
    Kc_emp = Ks[locked[0]] if len(locked) else float("nan")
    Kc_the = Dw_test / 2
    ok = abs(Kc_emp - Kc_the) < (Ks[1] - Ks[0]) * 1.5
    kc_ok &= ok
    print(f"  |Dw|={Dw_test:.3f}: Kc_emp={Kc_emp:.4f}  Kc_theory={Kc_the:.4f}  "
          f"{'ok' if ok else 'MISMATCH'}")
print(f"  -> {'PASS' if kc_ok else 'FAIL'}\n")

# ---------- Check 3: locked-branch R and the 1/sqrt(2) onset ----------
print("Check 3 -- locked-branch R = |cos(psi*/2)|, onset = 1/sqrt(2):")
branch_ok = True
onset_R = abs(np.cos(np.arcsin(np.clip(Dw / (2 * Kc), -1, 1)) / 2))
print(f"  analytic R at K=Kc: {onset_R:.4f}  (target {INV_SQRT2:.4f})  "
      f"{'ok' if abs(onset_R-INV_SQRT2)<1e-3 else 'MISMATCH'}")
branch_ok &= abs(onset_R - INV_SQRT2) < 1e-3
for K in [0.10, 0.12, 0.2, 0.5, 1.0]:
    _, R_emp = integrate_psi(Dw, K)
    psi_star = np.arcsin(np.clip(Dw / (2 * K), -1, 1))
    R_ana = abs(np.cos(psi_star / 2))
    ok = abs(R_emp - R_ana) < 0.02 and R_emp > INV_SQRT2 - 1e-3
    branch_ok &= ok
    print(f"  K={K:4.2f} (K/Kc={K/Kc:5.2f}): R_emp={R_emp:.3f}  R_analytic={R_ana:.3f}  "
          f"{'ok' if ok else 'MISMATCH'}")
print(f"  -> {'PASS' if branch_ok else 'FAIL'}\n")

# ---------- Check 4: drift below Kc, lock above ----------
drift_below = integrate_psi(Dw, 0.5 * Kc)[0]
drift_above = integrate_psi(Dw, 2.0 * Kc)[0]
c4 = drift_below > 0.05 and drift_above < 1e-3
print(f"Check 4 -- drift below Kc = {drift_below:.4f} (nonzero), "
      f"above Kc = {drift_above:.2e} (~0)  -> {'PASS' if c4 else 'FAIL'}\n")

# ---------- Check 5: noise smears the threshold ----------
print("Check 5 -- noise softens the sharp transition:")
Ks = np.linspace(0.3 * Kc, 1.3 * Kc, 25)
curves = {}
for nz in [0.0, 0.15, 0.4]:
    curves[nz] = np.array([integrate_psi(Dw, K, noise=nz, seed=3)[1] for K in Ks])
# sharpness = max slope of R vs K; noise should reduce it
def sharpness(c): return np.max(np.abs(np.diff(c)) / np.diff(Ks))
s0, s1, s2 = sharpness(curves[0.0]), sharpness(curves[0.15]), sharpness(curves[0.4])
c5 = s0 > s1 > s2
print(f"  max slope of R(K): noise 0.0 -> {s0:.2f},  0.15 -> {s1:.2f},  "
      f"0.4 -> {s2:.2f}  (should decrease)  -> {'PASS' if c5 else 'FAIL'}\n")

allok = red_ok and kc_ok and branch_ok and c4 and c5
print("ALL PASS" if allok else "SOME CHECKS FAILED")
print("\nVerdict: the two-oscillator system undergoes a genuine saddle-node")
print("(phase-locking) bifurcation at Kc = |Dw|/2 -- a sharp threshold from")
print("drifting 'noise' to locked 'deviation'. The coherence at onset is exactly")
print("1/sqrt(2) ~= 0.707, giving a DERIVED per-pair threshold (S_ij > 1/sqrt2 to")
print("lock) that matches the architecture's hand-picked r >= 0.7. Caveat: exact")
print("for N=2; the global N-oscillator transition is continuous with no special")
print("0.7. Noise smears the bifurcation into a stochastic one.")

# ---------- plot ----------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.6))

    # left: R vs K/Kc, analytic branch + the 1/sqrt2 onset
    Kg = np.linspace(0.3 * Kc, 3 * Kc, 200)
    R_ana = np.where(Kg >= Kc,
                     np.abs(np.cos(np.arcsin(np.clip(Dw / (2 * Kg), -1, 1)) / 2)),
                     np.nan)
    ax[0].plot(Kg / Kc, R_ana, color="#1f77b4", lw=2, label="locked branch |cos(ψ*/2)|")
    ax[0].axvline(1.0, color="#d62728", ls="--", label="Kc = |Δω|/2")
    ax[0].axhline(INV_SQRT2, color="#2a9d5c", ls=":", label="1/√2 ≈ 0.707 (onset)")
    ax[0].plot([1.0], [INV_SQRT2], "o", color="#2a9d5c")
    ax[0].set_xlabel("K / Kc"); ax[0].set_ylabel("order parameter R")
    ax[0].set_title("Locking transition: R jumps to 1/√2 at Kc, then → 1")
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)

    # right: noise smearing
    for nz, c in zip([0.0, 0.15, 0.4], ["#1f77b4", "#e08a1e", "#d62728"]):
        ax[1].plot(Ks / Kc, curves[nz], "-o", ms=3, color=c, label=f"noise σ={nz}")
    ax[1].axvline(1.0, color="k", ls="--", alpha=0.5, label="Kc")
    ax[1].axhline(INV_SQRT2, color="#2a9d5c", ls=":", alpha=0.7)
    ax[1].set_xlabel("K / Kc"); ax[1].set_ylabel("mean R")
    ax[1].set_title("Noise smears the sharp threshold (stochastic bifurcation)")
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3)

    fig.suptitle("Iteration 6 — phase-locking threshold and the derived 1/√2 coherence bound",
                 y=1.02)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter6_locking_threshold.png")
    fig.tight_layout(); fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
