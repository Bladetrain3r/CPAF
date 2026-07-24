"""
Iteration 12 -- The sign of an interaction: latent vs active as a discriminant.

Ziggy's conjecture: latent vs active interaction is "a sort of sign problem."
It is -- precisely. The two-oscillator locked state solves

    sin(psi*) = Dw / (2K)                       (iter 6)

which has a REAL solution iff |Dw/(2K)| <= 1. Define the locking discriminant

    Disc(K) = 1 - (Dw / (2K))^2

  Disc > 0  -> psi* real     -> ACTIVE interaction  (locked; a deviation)   [K > Kc]
  Disc = 0  -> psi* = pi/2   -> the threshold Kc; onset coherence 1/sqrt(2) [K = Kc]
  Disc < 0  -> psi* complex  -> LATENT interaction  (channel only, no dev.) [K < Kc]

Below Kc the locked offset is complex:
    psi* = pi/2 - i * arccosh(Dw / 2K)
-- the phase relationship exists in analytic continuation but is NOT realized on
the real circle. Its imaginary part arccosh(Dw/2K) measures "how latent" the
interaction is (0 at threshold, growing as coupling weakens). The SIGN of the
discriminant -- equivalently, the realness of psi* -- is the latent/active
discriminator. That is the sign problem, made exact.

NB: this is the sign of the DISCRIMINANT (K vs Kc), NOT the sign of the coupling
K itself. K >= 0 throughout (D1/D5); the attractive/repulsive sign of the
coupling is a separate axis we did not take. Non-negative coupling, signed
discriminant.

Checks (analytic backbone + simulated realization):
 1. sign(Disc) flips at Kc = |Dw|/2, and Disc = 0 there.
 2. Above Kc the simulated pair settles to a REAL fixed offset matching Re(psi*);
    below Kc it never settles (drifts) -- the offset is unrealized (latent).
 3. Im(psi*) = arccosh(Dw/2K) > 0 below Kc and -> 0 at Kc (quantifies latency).
 4. At Kc: psi* = pi/2 and coherence R = |cos(psi*/2)| = 1/sqrt(2) (ties to iter 6).
"""
import numpy as np

INV_SQRT2 = 1.0 / np.sqrt(2.0)

# positive detuning for a clean stable branch psi* in (0, pi/2)
f1, f2 = 1.20, 1.00
Dw = 2 * np.pi * (f1 - f2)                 # > 0
Kc = abs(Dw) / 2
print(f"Dw = {Dw:.4f}   Kc = |Dw|/2 = {Kc:.4f}   1/sqrt(2) = {INV_SQRT2:.4f}\n")

def discriminant(K):
    return 1.0 - (Dw / (2.0 * K)) ** 2

def psi_star(K):
    """Stable locked offset. Real (arcsin) above Kc; complex below."""
    arg = Dw / (2.0 * K)
    if arg <= 1.0:
        return complex(np.arcsin(arg), 0.0)          # real: active
    return complex(np.pi / 2.0, -np.arccosh(arg))     # complex: latent

def simulate_offset(K, T=600.0, dt=0.002):
    """Reduced 1-D dynamics dpsi/dt = Dw - 2K sin(psi) (deterministic, no noise).
    Returns (drift_rate, settled_offset_in_(-pi,pi])."""
    psi = 0.3
    n = int(T / dt); burn = int(0.7 * n)
    start = None
    for k in range(n):
        psi += (Dw - 2 * K * np.sin(psi)) * dt
        if k == burn:
            start = psi
    drift = abs(psi - start) / (T - burn * dt)        # rad/time over the tail
    offset = (psi + np.pi) % (2 * np.pi) - np.pi       # wrap to (-pi, pi]
    return drift, offset

# ---- sweep ----
Ks = np.array([0.3, 0.5, 0.7, 0.9, 1.0, 1.1, 1.3, 1.6, 2.0, 3.0]) * Kc
print(f"{'K/Kc':>5} | {'Disc':>7} | {'Re psi*':>8} | {'Im psi*':>8} | "
      f"{'sim drift':>9} | {'sim offset':>10} | class")
print("-" * 78)
rows = []
for K in Ks:
    D = discriminant(K)
    ps = psi_star(K)
    drift, off = simulate_offset(K)
    realized = drift < 1e-3
    cls = "ACTIVE" if D >= 0 else "latent"
    rows.append((K, D, ps, drift, off, realized))
    print(f"{K/Kc:5.2f} | {D:7.3f} | {ps.real:8.3f} | {ps.imag:8.3f} | "
          f"{drift:9.4f} | {off:10.3f} | {cls}")

# ---- checks ----
print()
# 1. discriminant sign flips at Kc
below = [r for r in rows if r[0] < Kc - 1e-9]
above = [r for r in rows if r[0] > Kc + 1e-9]
c1 = all(r[1] < 0 for r in below) and all(r[1] > 0 for r in above) \
     and abs(discriminant(Kc)) < 1e-9
print(f"Check 1 (sign(Disc) flips at Kc; Disc(Kc)={discriminant(Kc):.2e}): "
      f"all K<Kc have Disc<0, all K>Kc have Disc>0  -> {'PASS' if c1 else 'FAIL'}")

# 2. active -> realized real offset (matches Re psi*); latent -> never settles
active_ok = all(r[5] and abs(((r[4]-r[2].real+np.pi) % (2*np.pi)) - np.pi) < 1e-2
                for r in above)
latent_ok = all((not r[5]) for r in below)
c2 = active_ok and latent_ok
print(f"Check 2 (active settles to Re psi*, latent never settles): "
      f"active realized & matched = {active_ok}, latent all drifting = {latent_ok}"
      f"  -> {'PASS' if c2 else 'FAIL'}")

# 3. Im(psi*) > 0 below Kc, monotone, -> 0 at Kc
ims_below = [r[2].imag for r in below]                 # negative (we stored -arccosh)
c3 = all(im < 0 for im in ims_below) and abs(psi_star(Kc).imag) < 1e-6 \
     and abs(psi_star(0.5 * Kc).imag) > abs(psi_star(0.9 * Kc).imag)
print(f"Check 3 (Im psi* nonzero below Kc, ->0 at Kc, grows as K falls): "
      f"Im at 0.5Kc={psi_star(0.5*Kc).imag:.3f}, 0.9Kc={psi_star(0.9*Kc).imag:.3f}, "
      f"Kc={psi_star(Kc).imag:.3f}  -> {'PASS' if c3 else 'FAIL'}")

# 4. threshold: psi*=pi/2, R = 1/sqrt2
ps_c = psi_star(Kc)
R_onset = abs(np.cos(ps_c / 2.0))
c4 = abs(ps_c.real - np.pi/2) < 1e-6 and abs(ps_c.imag) < 1e-6 \
     and abs(R_onset - INV_SQRT2) < 1e-6
print(f"Check 4 (at Kc: psi*=pi/2, R=1/sqrt2): psi*={ps_c.real:.4f}"
      f"{ps_c.imag:+.4f}i, R={R_onset:.4f}  -> {'PASS' if c4 else 'FAIL'}")

allok = c1 and c2 and c3 and c4
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED")
print("\nVerdict: latent vs active interaction IS a sign problem -- the sign of")
print("the locking discriminant Disc = 1 - (Dw/2K)^2. Active interactions have a")
print("REAL locked phase-offset (realized on the circle: a deviation); latent")
print("interactions have a COMPLEX offset (unrealized -- a channel only). The")
print("threshold Kc is the zero of the discriminant, where the offset becomes")
print("real at exactly psi*=pi/2 (coherence 1/sqrt2). 'How latent' = |Im psi*| =")
print("arccosh(Dw/2K). Sign of discriminant, NOT sign of coupling.")

# ---- plot ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    Kg = np.linspace(0.3 * Kc, 3 * Kc, 400)
    D = np.array([discriminant(K) for K in Kg])
    Im = np.array([abs(psi_star(K).imag) for K in Kg])
    fig, ax = plt.subplots(figsize=(8.4, 5))
    ax.axhline(0, color="k", lw=0.8)
    ax.axvspan(Kg[0] / Kc, 1.0, color="#f4d06f", alpha=0.30,
               label="latent (Disc<0, ψ* complex)")
    ax.axvspan(1.0, Kg[-1] / Kc, color="#bfe3c0", alpha=0.40,
               label="active (Disc>0, ψ* real)")
    ax.plot(Kg / Kc, D, color="#1f77b4", lw=2, label="discriminant  1−(Δω/2K)²")
    ax.plot(Kg / Kc, Im, color="#d62728", lw=2, ls="--",
            label="|Im ψ*| = arccosh(Δω/2K)  (latency)")
    ax.axvline(1.0, color="k", ls=":", alpha=0.7)
    ax.plot([1.0], [0.0], "o", color="k")
    ax.annotate("Kc: sign flip\nψ*=π/2, R=1/√2", xy=(1.0, 0.0), xytext=(1.25, -0.6),
                fontsize=8, arrowprops=dict(arrowstyle="->", color="#555"))
    ax.set_xlabel("K / Kc"); ax.set_ylabel("value")
    ax.set_title("Iter 12 — an interaction's sign: latent (complex ψ*) vs "
                 "active (real ψ*)", fontsize=10.5)
    ax.legend(fontsize=8, loc="upper left"); ax.grid(alpha=0.3)
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter12_interaction_sign.png")
    fig.tight_layout(); fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
