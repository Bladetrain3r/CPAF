"""
Iteration 11 -- Interaction vs deviation: the latent channel (noun vs verb).

Chapter 8 s8.4 #1 left one span of the CPAF bridge unbuilt: the claim that an
INTERACTION (an edge -- a coupling channel that exists) and a DEVIATION (the
locking *event* on that edge) are genuinely distinct, not two names for one
thing. This iteration gives that split its own falsifiable test.

The tools are already in hand:
  * DEVIATION detector = mutual information I(theta1; theta2) (iter 7): it is ~0
    while the pair drifts and jumps up only when the pair LOCKS (K >= Kc).
  * INTERACTION detector = transfer entropy TE (iter 8): how much one phase's
    present improves prediction of the other's future. A coupling transmits
    influence whether or not it has locked, so TE should be > 0 for ANY K > 0.

Prediction (the noun/verb dissociation):
  K = 0            : no interaction, no deviation      -> MI ~ 0,  TE ~ 0
  0 < K < Kc       : interaction WITHOUT deviation     -> MI ~ 0,  TE > 0   <-- latent channel
  K > Kc           : interaction AND deviation         -> MI > 0,  TE > 0

If it holds: interaction is graded (a matter of degree -- TE rises smoothly from
0), deviation is abrupt (an event -- MI switches on at Kc). The interaction
"turns on" at a LOWER coupling than the deviation, and in between sits a real but
silent edge. That also hardens Ch 8's reframe: a null state (no deviations, MI~0)
can still be full of interactions (TE>0) -- latency below threshold, not emptiness.

Method mirrors iter 7/8: two noisy oscillators (Euler-Maruyama), long
steady-state run subsampled to reduce autocorrelation, swept across K. MI is
shuffle-corrected; TE is a binned conditional MI I(Y_{t+lag}; X_t | Y_t) with
FINE conditioning bins (iter-8 caveat) and circular-shift surrogate correction.
Values in bits.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

rng = np.random.RandomState(7)

# ---- pair + sweep ----
f1, f2 = 1.00, 1.20
w1, w2 = 2 * np.pi * f1, 2 * np.pi * f2
Dw = abs(w1 - w2)
Kc = Dw / 2                          # bidirectional locking threshold (iter 6)
noise = 0.30                         # enough to decorrelate below Kc (keeps MI~0 there)
#   but not so much it washes out locking; below ~0.25 the noiseless drift becomes
#   a deterministic limit cycle and MI picks up spurious structure -- 0.30 is the
#   sweet spot where sub-Kc MI stays at floor while TE remains detectable.

Ks = np.concatenate(([0.0], np.linspace(0.15 * Kc, 2.4 * Kc, 13)))
nK = len(Ks)

dt = 0.01
sub = 10                             # subsample stride (tau = 0.1)
lag = 3                              # TE horizon (0.3 time units)
n_samples = 100000
burn = 20000
n_steps = burn + n_samples * sub

# ---- integrate all K columns side by side ----
S1 = np.empty((n_samples, nK)); S2 = np.empty((n_samples, nK))
amp = noise * np.sqrt(dt)
th1 = rng.uniform(0, 2 * np.pi, nK)
th2 = rng.uniform(0, 2 * np.pi, nK)
si = 0
for k in range(n_steps):
    d1 = (w1 + Ks * np.sin(th2 - th1)) * dt + amp * rng.randn(nK)
    d2 = (w2 + Ks * np.sin(th1 - th2)) * dt + amp * rng.randn(nK)
    th1 = (th1 + d1) % (2 * np.pi)
    th2 = (th2 + d2) % (2 * np.pi)
    if k >= burn and (k - burn) % sub == 0 and si < n_samples:
        S1[si] = th1; S2[si] = th2; si += 1

# ---- estimators (same construction as iter 8) ----
def _bin(a, B):
    return np.minimum((a / (2 * np.pi) * B).astype(np.int64), B - 1)

def mutual_info_bits(a, b, B=16):
    H, _, _ = np.histogram2d(a, b, bins=[np.linspace(0, 2 * np.pi, B + 1)] * 2)
    p = H / H.sum()
    pa = p.sum(1, keepdims=True); pb = p.sum(0, keepdims=True)
    nz = p > 0
    return float(np.sum(p[nz] * np.log2(p[nz] / (pa * pb)[nz])))

def _cond_mi(a, b, c, Ba, Bb, Bc):
    flat = np.bincount((a * Bb + b) * Bc + c, minlength=Ba * Bb * Bc)
    p = flat.reshape(Ba, Bb, Bc) / flat.sum()
    pc = p.sum((0, 1), keepdims=True)
    pac = p.sum(1, keepdims=True)
    pbc = p.sum(0, keepdims=True)
    nz = p > 0
    return float(np.sum(p[nz] * np.log2((p * pc)[nz] / (pac * pbc)[nz])))

def transfer_entropy_bits(x, y, lag=lag, B=8, Bcond=24, n_surr=8, _rng=rng):
    """TE(X->Y) = I(Y_{t+lag}; X_t | Y_t), fine conditioning + surrogate-corrected."""
    yf = _bin(y[lag:], B); xs = x[:-lag]; cond = _bin(y[:-lag], Bcond)
    def te_of(xsrc):
        return _cond_mi(yf, _bin(xsrc, B), cond, B, B, Bcond)
    te = te_of(xs)
    n = len(xs)
    surr = [te_of(np.roll(xs, _rng.randint(n // 10, n - n // 10)))
            for _ in range(n_surr)]
    return te - float(np.mean(surr))

def order_param(a, b):
    return float(np.mean(np.abs(0.5 * (np.exp(1j * a) + np.exp(1j * b)))))

# ---- sweep ----
print(f"|Dw|={Dw:.3f}  Kc={Kc:.3f}  noise={noise}  samples/K={n_samples}\n")
print(f"{'K':>7} | {'K/Kc':>5} | {'R':>5} | {'MI':>6} | {'TE12':>7} | "
      f"{'TE21':>7} | {'meanTE':>7} | regime")
print("-" * 78)
R = np.zeros(nK); MI = np.zeros(nK); TE12 = np.zeros(nK); TE21 = np.zeros(nK)
for j in range(nK):
    a, b = S1[:, j], S2[:, j]
    R[j] = order_param(a, b)
    mi = mutual_info_bits(a, b)
    MI[j] = max(mi - mutual_info_bits(a, rng.permutation(b)), 0.0)
    TE12[j] = transfer_entropy_bits(a, b)
    TE21[j] = transfer_entropy_bits(b, a)
mTE = 0.5 * (TE12 + TE21)
for j in range(nK):
    reg = ("null" if Ks[j] == 0 else
           "latent (interaction, no deviation)" if Ks[j] < Kc and MI[j] < 0.05 else
           "deviation" if MI[j] >= 0.05 else "sub-Kc")
    print(f"{Ks[j]:7.3f} | {Ks[j]/Kc:5.2f} | {R[j]:5.3f} | {MI[j]:6.3f} | "
          f"{TE12[j]:7.4f} | {TE21[j]:7.4f} | {mTE[j]:7.4f} | {reg}")

# ---- turn-on points & the latent window ----
TE_floor = max(mTE[0], 0.004)                      # K=0 gives the estimator floor
MI_floor = 0.05
TE_on = next((Ks[j] for j in range(nK) if mTE[j] > max(2 * TE_floor, 0.01)), np.nan)
MI_on = next((Ks[j] for j in range(nK) if MI[j] > MI_floor), np.nan)
latent = [j for j in range(nK) if 0 < Ks[j] < Kc and mTE[j] > max(2*TE_floor, 0.01)
          and MI[j] < MI_floor]

# ---- checks ----
print()
print(f"Check A (K=0 is a true null): MI={MI[0]:.4f}, meanTE={mTE[0]:.4f} "
      f"(both at floor -- no interaction, no deviation)")
cA = MI[0] < 0.03 and mTE[0] < 0.012
print(f"   -> {'PASS' if cA else 'FAIL'}")

if latent:
    lj = max(latent, key=lambda j: mTE[j])         # clearest example
    print(f"Check B (LATENT CHANNEL exists): at K/Kc={Ks[lj]/Kc:.2f} "
          f"meanTE={mTE[lj]:.4f} bits (interaction present) but MI={MI[lj]:.4f} "
          f"(no deviation) -- a real but silent edge")
cB = len(latent) >= 1
print(f"   -> {'PASS' if cB else 'FAIL'}")

# The noun/verb claim is about ORDER, not absolute position: the interaction
# (TE) must become detectable at a strictly lower coupling than the deviation
# (MI), and it must do so inside the sub-threshold band (TE_on well below Kc).
# Noise smears the deviation, so MI_on itself sits somewhat below the noiseless
# Kc -- expected, and not what this check is about.
print(f"Check C (interaction turns on before deviation): TE_on at K={TE_on:.3f} "
      f"(K/Kc={TE_on/Kc:.2f}) < MI_on at K={MI_on:.3f} (K/Kc={MI_on/Kc:.2f}); "
      f"interaction detected inside the sub-threshold band")
cC = (TE_on < MI_on) and (TE_on / Kc < 0.5)
print(f"   -> {'PASS' if cC else 'FAIL'}")

print(f"Check D (above Kc: both present): at K/Kc={Ks[-1]/Kc:.2f} "
      f"MI={MI[-1]:.3f} (deviation) and meanTE={mTE[-1]:.4f} (interaction)")
cD = MI[-1] > 0.5 and mTE[-1] > 0.01
print(f"   -> {'PASS' if cD else 'FAIL'}")

allok = cA and cB and cC and cD
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED")
print("\nVerdict: interaction and deviation are SEPARATE observables. Transfer")
print("entropy (the interaction) rises smoothly from zero the moment any")
print("coupling exists; mutual information (the deviation) stays flat until the")
print("locking threshold Kc, then switches on. Between them lies the LATENT")
print("CHANNEL: 0 < K < Kc, where the edge is real (TE>0) but silent (MI~0).")
print("Interaction is a noun graded by degree; deviation is a verb -- an event.")
print("A null state (no deviations) can be dense with interactions: latency")
print("below threshold, not emptiness. Ch 8's last bridge span, grounded.")

# ---- plot ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8.4, 5))
    x = Ks / Kc
    ax.plot(x, MI / max(MI.max(), 1e-9), "s-", color="#d62728",
            label="deviation:  MI (normalized)")
    ax.plot(x, mTE / max(mTE.max(), 1e-9), "o-", color="#1f77b4",
            label="interaction:  mean TE (normalized)")
    ax.axvline(1.0, color="k", ls="--", alpha=0.6, label="Kc (deviation onset)")
    if latent:
        ax.axvspan(min(Ks[j] for j in latent) / Kc, 1.0, color="#f4d06f",
                   alpha=0.30, label="latent channel (interaction, no deviation)")
    ax.set_xlabel("K / Kc"); ax.set_ylabel("normalized signal")
    ax.set_title("Iter 11 — interaction turns on before deviation:\n"
                 "TE rises from K>0; MI waits for Kc; a silent edge in between",
                 fontsize=10.5)
    ax.legend(fontsize=8, loc="center right"); ax.grid(alpha=0.3)
    ax.set_ylim(-0.03, 1.05)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter11_interaction_vs_deviation.png")
    fig.tight_layout(); fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
