"""
Iteration 8 -- Interaction vs common cause (is the edge what carries the info?)

Iteration 7 grounded CPAF's "information" as the mutual information born at a
locking event. But MI has a known blind spot (Ch 8 s8.4 #3): it sees
*correlation*, not *causation*. Two oscillators driven by a shared hidden
source Z carry high MI with NO coupling between them -- the information is
real, but the edge it seems to sit on doesn't exist. The candidate fix is a
*directed* measure, transfer entropy:

    TE(X -> Y) = I( Y_{t+tau} ; X_t | Y_t )

-- how much X's present tells us about Y's future *beyond what Y's own past
already says*. This iteration tests four claims, and the honest headline is
that the naive fix only half-works:

  (A) MI is blind to the graph. A genuinely coupled pair, an uncoupled
      common-driven pair, and a one-way-coupled pair all carry MI of the same
      order. MI cannot distinguish these three different graphs.

  (B) Pairwise TE is ALSO fooled by a hidden common cause. Each driven
      oscillator is a second noisy sensor of Z, so oscillator 1's present
      genuinely improves prediction of oscillator 2's future -- real
      predictive transfer over a nonexistent edge. TE(common-drive) comes out
      the same order as TE(coupled). TE measures *prediction*, not causation.

  (C) CONDITIONAL TE resolves it -- a double dissociation. Conditioning on
      the source, TE(1 -> 2 | Z) for the common-driven pair collapses to ~0,
      while the coupled pair's TE is untouched by conditioning on the (for
      it, irrelevant) Z. The edge is certified exactly when the confounder is
      *observed*.

  (D) TE is directional where MI cannot be. With a one-way coupling
      (1 -> 2 only -- the architecture's asymmetric-K_ij extension),
      TE(2 -> 1) is statistically zero while TE(1 -> 2) is large; MI is
      symmetric and reads the same as the bidirectional case.

Method. Three two-oscillator scenarios integrated side by side (Euler-
Maruyama, same noise), long steady-state runs subsampled to reduce
autocorrelation. TE from binned phases: a conditional MI over the triple
(Y_{t+lag}, X_t, Y_t), with the conditioning variable binned FINE (Bcond=24)
-- coarse conditioning leaks sub-bin information about Y_t through the
correlated X_t and fakes transfer (we measured this: at Bcond=8 the one-way
null direction reads 0.11 bits; at 24 it reads ~0.000). All estimates
bias-corrected by subtracting the mean over circularly time-shifted
surrogates of the source (destroys directed pairing, preserves marginals and
autocorrelation). Values in bits.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

rng = np.random.RandomState(4)

# ---- three scenarios, integrated side by side (columns) ----
# 0: genuine coupling   (bidirectional K > Kc, no drive)
# 1: common cause       (K = 0 both ways; both entrained by hidden source Z)
# 2: one-way coupling   (1 -> 2 only; asymmetric K_ij)
SCEN = ["coupled 1<->2", "common drive Z->1,Z->2", "one-way 1->2"]

f1, f2, fz = 1.00, 1.20, 1.10
w1, w2, wz = 2 * np.pi * f1, 2 * np.pi * f2, 2 * np.pi * fz
Dw = abs(w1 - w2)                    # pair detuning
Kc_pair = Dw / 2                     # bidirectional locking threshold (iter 6)
noise = 0.60                         # strong noise: entropy for TE to move

K12 = np.array([2.5 * Kc_pair, 0.0, 0.0])       # influence of 2 on 1
K21 = np.array([2.5 * Kc_pair, 0.0, 2.5 * Dw])  # influence of 1 on 2
#   a one-way (driven) pair locks at K >= |Dw|, twice the bidirectional Kc
Kz = np.array([0.0, 3.0 * 2 * np.pi * 0.10, 0.0])  # drive on BOTH 1 and 2
#   entrainment to Z needs Kz >= |w_i - wz| = 2*pi*0.10; 3x that locks both

dt = 0.01
sub = 10                             # subsample stride (tau = sub*dt = 0.1)
lag = 3                              # TE horizon: 3 samples = 0.3 time units
n_samples = 100000
burn = 20000
n_steps = burn + n_samples * sub

S1 = np.empty((n_samples, 3)); S2 = np.empty((n_samples, 3))
SZ = np.empty(n_samples)             # the hidden source (common-drive column)
amp = noise * np.sqrt(dt)            # Euler-Maruyama noise increment
th1 = rng.uniform(0, 2 * np.pi, 3)
th2 = rng.uniform(0, 2 * np.pi, 3)
thz = rng.uniform(0, 2 * np.pi, 3)
si = 0
for k in range(n_steps):
    d1 = (w1 + K12 * np.sin(th2 - th1) + Kz * np.sin(thz - th1)) * dt \
        + amp * rng.randn(3)
    d2 = (w2 + K21 * np.sin(th1 - th2) + Kz * np.sin(thz - th2)) * dt \
        + amp * rng.randn(3)
    dz = wz * dt + amp * rng.randn(3)        # source: noisy, undriven
    th1 = (th1 + d1) % (2 * np.pi)
    th2 = (th2 + d2) % (2 * np.pi)
    thz = (thz + dz) % (2 * np.pi)
    if k >= burn and (k - burn) % sub == 0 and si < n_samples:
        S1[si] = th1; S2[si] = th2; SZ[si] = thz[1]; si += 1

# ---- estimators (binned; surrogate bias-corrected) ----
def _bin(a, B):
    return np.minimum((a / (2 * np.pi) * B).astype(np.int64), B - 1)

def mutual_info_bits(a, b, B=16):
    H, _, _ = np.histogram2d(a, b, bins=[np.linspace(0, 2 * np.pi, B + 1)] * 2)
    p = H / H.sum()
    pa = p.sum(1, keepdims=True); pb = p.sum(0, keepdims=True)
    nz = p > 0
    return float(np.sum(p[nz] * np.log2(p[nz] / (pa * pb)[nz])))

def _cond_mi(a, b, c, Ba, Bb, Bc):
    """I(A;B|C) over integer-coded triples."""
    flat = np.bincount((a * Bb + b) * Bc + c, minlength=Ba * Bb * Bc)
    p = flat.reshape(Ba, Bb, Bc) / flat.sum()
    pc = p.sum((0, 1), keepdims=True)
    pac = p.sum(1, keepdims=True)
    pbc = p.sum(0, keepdims=True)
    nz = p > 0
    return float(np.sum(p[nz] * np.log2((p * pc)[nz] / (pac * pbc)[nz])))

def transfer_entropy_bits(x, y, z=None, lag=lag, B=8, Bcond=24,
                          Bycond=16, Bz=10, n_surr=10, _rng=rng):
    """TE(X->Y) = I(Y_{t+lag}; X_t | Y_t), or | (Y_t, Z_t) if z is given.
    Fine conditioning bins (see module docstring); bias-corrected by circular
    time-shifts of the source X."""
    yf = _bin(y[lag:], B); xs = x[:-lag]
    if z is None:
        cond = _bin(y[:-lag], Bcond); Bc = Bcond
    else:                            # condition on (Y_t, Z_t) jointly
        cond = _bin(y[:-lag], Bycond) * Bz + _bin(z[:-lag], Bz)
        Bc = Bycond * Bz
    def te_of(xsrc):
        return _cond_mi(yf, _bin(xsrc, B), cond, B, B, Bc)
    te = te_of(xs)
    n = len(xs)
    surr = [te_of(np.roll(xs, _rng.randint(n // 10, n - n // 10)))
            for _ in range(n_surr)]
    return te - float(np.mean(surr))

def order_param(a, b):
    return float(np.mean(np.abs(0.5 * (np.exp(1j * a) + np.exp(1j * b)))))

# ---- measure everything ----
print(f"pair detuning |Dw|={Dw:.3f}  Kc(pair)={Kc_pair:.3f}  noise={noise}  "
      f"samples/scenario={n_samples}  TE lag={lag * sub * dt:.1f} time\n")
print(f"{'scenario':>24} | {'R':>5} | {'MI':>6} | {'TE 1->2':>8} | {'TE 2->1':>8}")
print("-" * 64)
MI = np.zeros(3); TE12 = np.zeros(3); TE21 = np.zeros(3); Rr = np.zeros(3)
for j in range(3):
    a, b = S1[:, j], S2[:, j]
    Rr[j] = order_param(a, b)
    mi = mutual_info_bits(a, b)
    mi_shuf = mutual_info_bits(a, rng.permutation(b))   # finite-sample floor
    MI[j] = max(mi - mi_shuf, 0.0)
    TE12[j] = transfer_entropy_bits(a, b)
    TE21[j] = transfer_entropy_bits(b, a)
    print(f"{SCEN[j]:>24} | {Rr[j]:5.3f} | {MI[j]:6.3f} | {TE12[j]:8.4f} | "
          f"{TE21[j]:8.4f}")

# conditional TE: common-drive pair given its source, and -- as the control --
# the coupled pair given the same (for it, causally irrelevant) Z series
cTE12 = transfer_entropy_bits(S1[:, 1], S2[:, 1], z=SZ)
cTE21 = transfer_entropy_bits(S2[:, 1], S1[:, 1], z=SZ)
kTE12 = transfer_entropy_bits(S1[:, 0], S2[:, 0], z=SZ)
print(f"\nconditioning on the source Z:   common-drive TE(1->2|Z)={cTE12:.4f}  "
      f"TE(2->1|Z)={cTE21:.4f}")
print(f"control (Z irrelevant):         coupled      TE(1->2|Z)={kTE12:.4f}  "
      f"(unconditioned {TE12[0]:.4f})")

# ---- checks ----
print()
print(f"Check A (MI is blind to the graph): coupled {MI[0]:.2f} / "
      f"common-drive {MI[1]:.2f} / one-way {MI[2]:.2f} bits -- all high, "
      f"same order, three different graphs")
mi_ratio = MI.min() / MI.max()
cA = MI.min() > 0.8 and mi_ratio > 0.5
print(f"   -> {'PASS' if cA else 'FAIL'}")

TEc = 0.5 * (TE12[0] + TE21[0])      # coupled, mean of directions
TEm = 0.5 * (TE12[1] + TE21[1])      # common drive
print(f"Check B (pairwise TE is fooled too): TE common-drive = {TEm:.4f} vs "
      f"coupled = {TEc:.4f} bits -- same order (ratio {TEm / TEc:.2f}); "
      f"predictive transfer over a NONEXISTENT edge")
cB = TEm > 0.02 and TEm > 0.5 * TEc
print(f"   -> {'PASS' if cB else 'FAIL'}")

print(f"Check C (conditional TE resolves it): common-drive TE|Z = "
      f"{max(cTE12, cTE21):.4f} (dead) while coupled TE|Z = {kTE12:.4f} "
      f"(vs unconditioned {TEc:.4f} -- untouched): a double dissociation")
cC = max(abs(cTE12), abs(cTE21)) < 0.01 and kTE12 > 0.7 * TEc
print(f"   -> {'PASS' if cC else 'FAIL'}")

print(f"Check D (TE is directional): one-way TE(1->2) = {TE12[2]:.4f} vs "
      f"TE(2->1) = {TE21[2]:.4f} (statistically zero); MI meanwhile reads "
      f"{MI[2]:.2f} bits -- symmetric, same as bidirectional's {MI[0]:.2f}")
cD = TE12[2] > 0.05 and abs(TE21[2]) < 0.01
print(f"   -> {'PASS' if cD else 'FAIL'}")

allok = cA and cB and cC and cD
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED")
print("\nVerdict: MI certifies a RELATIONSHIP but not an edge -- three")
print("different graphs read the same. Pairwise TE adds direction (one-way")
print("coupling: TE(2->1) is zero) but is still fooled by a hidden common")
print("cause: prediction is not causation. Only CONDITIONAL TE -- possible")
print("exactly when the confounder is observed -- certifies that a specific")
print("edge carries the information. For CPAF: 'information on an")
print("interaction' is a three-rung ladder (related < directed < connected),")
print("and the top rung costs observability of the rest of the graph.")

# ---- plot ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6))
    xpos = np.arange(3)
    labels = ["coupled\n1↔2", "common drive\nZ→1, Z→2", "one-way\n1→2"]

    ax = axes[0]
    ax.bar(xpos, MI, 0.55, color="#d62728", alpha=0.85)
    ax.set_xticks(xpos); ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("mutual information (bits)")
    ax.set_title("MI: three different graphs, one answer", fontsize=10)
    ax.grid(alpha=0.3, axis="y")

    ax = axes[1]
    w = 0.27
    ax.bar(xpos - w, TE12, w, color="#1f77b4", label="TE 1→2")
    ax.bar(xpos, TE21, w, color="#9ecae1", label="TE 2→1")
    ax.bar([0 + w, 1 + w], [kTE12, max(cTE12, cTE21)], w, color="#2a9d5c",
           alpha=0.9, label="TE 1→2 | Z (source observed)")
    ax.axhline(0, color="k", lw=0.8)
    ax.set_xticks(xpos); ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("transfer entropy (bits)")
    ax.set_title("TE: direction for free; the edge only after conditioning",
                 fontsize=10)
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    fig.suptitle("Iter 8 — interaction vs common cause: "
                 "related < directed < connected", fontsize=11)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter8_transfer_entropy.png")
    fig.tight_layout(); fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
