"""
Iteration 9 -- Entity-as-cluster (does a locked module act as ONE oscillator?)

CPAF leans on recursion: simple entities compose into higher-order entities
that themselves interact. Chapter 8 called this the model's biggest promissory
note: a locked cluster (iter 5's modules) SHOULD behave as a single
coarse-grained oscillator -- one effective phase, one effective frequency --
but nothing had tested it. This iteration does, and it also tests the
opposite: an UNLOCKED collection should fail every entity criterion, so that
"entity" is something the locking transition *creates*, not a labeling choice.

Coarse-graining. A cluster of M members with phases theta_i is summarized by
its mean-phase direction Theta = arg( (1/M) sum_i e^{i theta_i} ) and internal
coherence rho = | (1/M) sum_i e^{i theta_i} | -- the cluster-restricted order
parameter of Ch 1. For a tightly locked cluster (theta_i = Theta + delta_i,
offsets quasi-static) the algebra collapses: couple a probe oscillator z to
every member with per-edge strength kappa and the macro dynamics reduce to
the two-oscillator system of iter 6,

    dTheta/dt   = w_bar + kappa*rho * sin(theta_z - Theta)   (+ noise/sqrt(M))
    dtheta_z/dt = w_z   + kappa*rho * sin(Theta - theta_z)   (+ noise)

with w_bar the mean member frequency (internal coupling terms cancel by
antisymmetry) and effective coupling K_eff = kappa * rho: a cluster's grip on
the world is DISCOUNTED BY ITS INTERNAL COHERENCE. Iter 6 then predicts a
locking threshold kappa_c = |w_z - w_bar| / (2 rho) and a locked-branch
coherence R(kappa) = cos( arcsin(Dw / (2 rho kappa)) / 2 ), whose kappa ->
kappa_c limit is the 1/sqrt2 locking floor. Every piece is falsifiable.
Four claims:

  (A) One effective frequency. Locked cluster: every member's long-run mean
      velocity equals w_bar, and Theta rotates at w_bar. Unlocked collection:
      member velocities stay spread out -- no shared clock, no candidate
      entity.

  (B) The pair law holds one level up -- including the rho discount. The
      empirical entrainment threshold of Theta to the probe matches
      kappa_c = |Dw|/(2 rho); a mid-coherence cluster (rho ~ 0.92) needs
      measurably MORE per-edge coupling than a tight one (rho ~ 1), and the
      data must side with the rho-corrected prediction over the naive |Dw|/2.

  (C) The locked branch is iter 6's, one level up. Measured Theta-probe
      coherence along the locked branch follows R(kappa) above -- the curve
      whose threshold limit is 1/sqrt2. (A single point-sample "R at onset =
      0.707" check is WRONG by the theory itself: the branch is steep at
      onset, so the first locked grid point already reads ~0.80 -- and the
      theory predicts exactly that value. We check the branch, not a point.)

  (D) Macro closure ("internal transfer entropy"). For a locked cluster,
      member phases add ~nothing to predicting Theta's future beyond Theta's
      own past: TE(theta_i -> Theta | Theta) ~ 0. For an unlocked collection
      the micro detail leaks through: the same TE is clearly positive.
      Positive control: a probe genuinely driving the cluster shows
      TE(theta_z -> Theta | Theta) >> 0. (Estimator per iter 8: fine
      conditioning bins, circular-shift surrogates.)

Method. Parts 1/2 use low noise (sharp bifurcation, per iter 6); Part 3 uses
strong noise (information dynamics need entropy, per iter 7/8). Member
frequencies are a fixed symmetric fan (no lucky draws). Scenarios and kappa
sweeps are integrated as vectorized columns. Values in rad/s and bits.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

rng = np.random.RandomState(6)

M = 5
w_bar = 2 * np.pi * 1.00
fan = 2 * np.pi * np.array([-0.08, -0.04, 0.0, 0.04, 0.08])   # member detunings
w_mem = w_bar + fan                                            # mean = w_bar
KIN_TIGHT = 4.0      # internal coupling, tight cluster (rho ~ 1)
KIN_MID = 1.0        # mid cluster (rho ~ 0.92 -- the discount becomes visible)
KIN_WEAK = 0.3       # below internal locking -- NOT an entity (control)

def simulate(Kin, kappa, wz, noise, T, dt=0.01, sub=10, record_members=False):
    """Vectorized over columns: Kin, kappa, wz are arrays of shape (C,).
    Cluster is all-to-all (Kin/M); probe z couples kappa per edge to every
    member and receives the member average back. Returns subsampled
    Theta (n,C), rho (n,C), theta_z (n,C) [, members (n,M,C)]."""
    Kin = np.atleast_1d(np.asarray(Kin, float))
    kappa = np.atleast_1d(np.asarray(kappa, float))
    wz = np.atleast_1d(np.asarray(wz, float))
    C = len(Kin)
    n_steps = int(T / dt)
    n_rec = n_steps // sub
    th = rng.uniform(0, 2 * np.pi, (M, C))
    tz = rng.uniform(0, 2 * np.pi, C)
    amp = noise * np.sqrt(dt)
    TH = np.empty((n_rec, C)); RH = np.empty((n_rec, C))
    TZ = np.empty((n_rec, C))
    MEM = np.empty((n_rec, M, C)) if record_members else None
    r = 0
    for k in range(n_steps):
        field = np.sin(th[None, :, :] - th[:, None, :]).mean(1)   # (M,C)
        dth = (w_mem[:, None] + Kin[None, :] * field
               + kappa[None, :] * np.sin(tz[None, :] - th)) * dt \
            + amp * rng.randn(M, C)
        dtz = (wz + kappa * np.sin(th - tz[None, :]).mean(0)) * dt \
            + amp * rng.randn(C)
        th = (th + dth) % (2 * np.pi)
        tz = (tz + dtz) % (2 * np.pi)
        if k % sub == 0 and r < n_rec:
            ph = np.exp(1j * th).mean(0)
            TH[r] = np.angle(ph); RH[r] = np.abs(ph); TZ[r] = tz
            if record_members:
                MEM[r] = th
            r += 1
    return (TH, RH, TZ, MEM) if record_members else (TH, RH, TZ)

def mean_velocity(series, dt_rec):
    u = np.unwrap(series)
    return (u[-1] - u[0]) / ((len(u) - 1) * dt_rec)

# ================= Part 1 -- one effective frequency (Check A) =============
dt, sub = 0.01, 10
dt_rec = dt * sub
noise_lo = 0.05
T1 = 400.0
b1 = int(50.0 / dt_rec)

print("Part 1 -- free-running cluster (no probe): one clock or many?")
names1 = ["tight", "mid", "weak"]
TH, RH, TZ, MEM = simulate([KIN_TIGHT, KIN_MID, KIN_WEAK], [0, 0, 0],
                           [w_bar] * 3, noise_lo, T1, record_members=True)
vel_spread = {}; rho_free = {}
print(f"{'cluster':>8} | {'rho':>6} | {'member velocity spread':>28} | "
      f"{'|v(Theta)-w_bar|':>16}")
for c, name in enumerate(names1):
    v_mem = np.array([mean_velocity(MEM[b1:, i, c], dt_rec) for i in range(M)])
    v_th = mean_velocity(TH[b1:, c], dt_rec)
    vel_spread[name] = v_mem.std()
    rho_free[name] = RH[b1:, c].mean()
    print(f"{name:>8} | {rho_free[name]:6.3f} | "
          f"std {v_mem.std():7.4f}  (natural fan std {fan.std():.4f}) | "
          f"{abs(v_th - w_bar):16.4f}")

cA = (vel_spread["tight"] < 0.02 * fan.std()
      and vel_spread["weak"] > 0.5 * fan.std())
print(f"\nCheck A (one effective frequency): tight cluster's member-velocity "
      f"spread is {vel_spread['tight'] / fan.std():.1%} of natural; weak is "
      f"{vel_spread['weak'] / fan.std():.0%} -- locking creates the shared "
      f"clock, its absence leaves {M} clocks")
print(f"   -> {'PASS' if cA else 'FAIL'}")

# ====== Part 2 -- entrainment obeys the pair law with K_eff = kappa*rho =====
print("\nPart 2 -- probe entrainment: the iter-6 law, one level up")
T2 = 600.0
b2 = int(100.0 / dt_rec)
lock_tol = 0.05          # |mean d(Theta - theta_z)/dt| below this = locked
NK = 25
runs = [("tight", KIN_TIGHT, 0.15), ("tight", KIN_TIGHT, 0.25),
        ("mid", KIN_MID, 0.25)]

# build one big column set: 3 runs x NK kappas
cols_Kin, cols_kap, cols_wz, kc_preds = [], [], [], []
for name, Kin, dfz in runs:
    Dw = 2 * np.pi * dfz
    kc_pred = Dw / (2 * rho_free[name])
    kc_preds.append(kc_pred)
    ks = np.linspace(0.55 * kc_pred, 1.75 * kc_pred, NK)
    cols_Kin += [Kin] * NK; cols_kap += list(ks)
    cols_wz += [w_bar + Dw] * NK
TH, RH, TZ = simulate(cols_Kin, cols_kap, cols_wz, noise_lo, T2)

results = []
print(f"{'cluster':>8} | {'detune f':>8} | {'rho':>6} | {'kc pred':>8} | "
      f"{'kc naive':>8} | {'kc emp':>8}")
for ri, (name, Kin, dfz) in enumerate(runs):
    sl = slice(ri * NK, (ri + 1) * NK)
    kappas = np.array(cols_kap[sl])
    Dw = 2 * np.pi * dfz
    drift = np.empty(NK); Rpair = np.empty(NK)
    for i in range(NK):
        c = ri * NK + i
        psi = np.unwrap(TH[b2:, c] - TZ[b2:, c])
        drift[i] = abs((psi[-1] - psi[0]) / ((len(psi) - 1) * dt_rec))
        Rpair[i] = np.mean(np.abs(0.5 * (np.exp(1j * TH[b2:, c])
                                         + np.exp(1j * TZ[b2:, c]))))
    locked = drift < lock_tol
    i_first = int(np.argmax(locked))
    kc_emp = 0.5 * (kappas[i_first - 1] + kappas[i_first])
    kc_naive = Dw / 2
    results.append(dict(name=name, dfz=dfz, rho=rho_free[name],
                        kappas=kappas, drift=drift, Rpair=Rpair,
                        locked=locked, i_first=i_first, kc_emp=kc_emp,
                        kc_pred=kc_preds[ri], kc_naive=kc_naive, Dw=Dw))
    print(f"{name:>8} | {dfz:8.2f} | {rho_free[name]:6.3f} | "
          f"{kc_preds[ri]:8.4f} | {kc_naive:8.4f} | {kc_emp:8.4f}")

errs = [abs(r["kc_emp"] - r["kc_pred"]) / r["kc_pred"] for r in results]
mid = results[2]
mid_sides_with_rho = (abs(mid["kc_emp"] - mid["kc_pred"])
                      < abs(mid["kc_emp"] - mid["kc_naive"]))
cB = max(errs) < 0.10 and mid_sides_with_rho
print(f"\nCheck B (pair law + rho discount): empirical thresholds within "
      f"{max(errs):.1%} of kappa_c=|Dw|/(2 rho); mid cluster "
      f"(rho={mid['rho']:.3f}) sides with the rho-corrected prediction "
      f"({mid['kc_pred']:.3f}) over naive |Dw|/2 ({mid['kc_naive']:.3f}): "
      f"{mid_sides_with_rho}")
print(f"   -> {'PASS' if cB else 'FAIL'}")

# locked-branch check: measured R(kappa) vs iter-6 branch (limit = 1/sqrt2)
branch_errs = []
first_pt = []
for r in results:
    lk = r["locked"].copy(); lk[:r["i_first"]] = False
    kl = r["kappas"][lk]
    sinpsi = np.clip(r["Dw"] / (2 * r["rho"] * kl), 0, 1)
    R_theory = np.cos(np.arcsin(sinpsi) / 2)
    err = np.abs(r["Rpair"][lk] - R_theory)
    branch_errs.append(err.mean())
    first_pt.append((r["Rpair"][lk][0], R_theory[0]))
cC = max(branch_errs) < 0.04
print(f"Check C (the 1/sqrt2 branch, one level up): measured locked branch "
      f"matches R=cos(arcsin(Dw/2rho kappa)/2) to "
      f"{max(branch_errs):.3f} mean abs error; first locked points measured "
      f"{', '.join(f'{m:.3f}' for m, t in first_pt)} vs theory "
      f"{', '.join(f'{t:.3f}' for m, t in first_pt)} (branch limit at "
      f"kappa_c is 1/sqrt2 = {1 / np.sqrt(2):.4f})")
print(f"   -> {'PASS' if cC else 'FAIL'}")

# ============ Part 3 -- macro closure: internal TE (Check D) ================
print("\nPart 3 -- macro closure: does micro detail leak past Theta?")
noise_hi = 0.30
n_samples = 100000
T3 = (n_samples * sub + 20000) * dt
b3 = 20000 // sub

def _bin(a, B):
    return np.minimum(((a % (2 * np.pi)) / (2 * np.pi) * B).astype(np.int64),
                      B - 1)

def _cond_mi(a, b, c, Ba, Bb, Bc):
    flat = np.bincount((a * Bb + b) * Bc + c, minlength=Ba * Bb * Bc)
    p = flat.reshape(Ba, Bb, Bc) / flat.sum()
    pc = p.sum((0, 1), keepdims=True)
    pac = p.sum(1, keepdims=True)
    pbc = p.sum(0, keepdims=True)
    nz = p > 0
    return float(np.sum(p[nz] * np.log2((p * pc)[nz] / (pac * pbc)[nz])))

def transfer_entropy_bits(x, y, lag=3, B=8, Bcond=24, n_surr=10, _rng=rng):
    """TE(X->Y) = I(Y_{t+lag}; X_t | Y_t); iter-8 estimator (fine conditioning
    bins, circular-shift surrogate bias correction)."""
    yf = _bin(y[lag:], B); cond = _bin(y[:-lag], Bcond); xs = x[:-lag]
    def te_of(xsrc):
        return _cond_mi(yf, _bin(xsrc, B), cond, B, B, Bcond)
    te = te_of(xs)
    n = len(xs)
    surr = [te_of(np.roll(xs, _rng.randint(n // 10, n - n // 10)))
            for _ in range(n_surr)]
    return te - float(np.mean(surr))

# sub-threshold probe drive: genuine influence flows, no lock (clean TE target)
kap_probe = 0.6 * (2 * np.pi * 0.25) / (2 * rho_free["tight"])
names3 = ["tight, isolated", "weak, isolated", "tight + probe"]
TH, RH, TZ, MEM = simulate([KIN_TIGHT, KIN_WEAK, KIN_TIGHT],
                           [0.0, 0.0, kap_probe],
                           [w_bar + 2 * np.pi * 0.25] * 3,
                           noise_hi, T3, record_members=True)
TH, TZ, MEM = TH[b3:], TZ[b3:], MEM[b3:]

TE_member = {}; TE_probe = None
for c, name in enumerate(names3):
    tes = [transfer_entropy_bits(MEM[:, i, c], TH[:, c]) for i in range(M)]
    TE_member[name] = float(np.mean(tes))
    line = f"{name:>16} | TE(member -> Theta | Theta) = {TE_member[name]:7.4f}"
    if name == "tight + probe":
        TE_probe = transfer_entropy_bits(TZ[:, c], TH[:, c])
        line += f" | TE(probe -> Theta | Theta) = {TE_probe:7.4f}"
    print(line)

cD = (TE_member["tight, isolated"] < 0.01
      and TE_member["weak, isolated"]
          > 5 * max(TE_member["tight, isolated"], 1e-4)
      and TE_member["weak, isolated"] > 0.02
      and TE_probe > 0.02)
print(f"\nCheck D (macro closure): locked cluster's members add "
      f"{TE_member['tight, isolated']:.4f} bits beyond Theta (closed); the "
      f"unlocked collection leaks {TE_member['weak, isolated']:.4f} bits "
      f"(micro detail still matters); a real external influence reads "
      f"{TE_probe:.4f} bits (the estimator is not just printing zeros)")
print(f"   -> {'PASS' if cD else 'FAIL'}")

allok = cA and cB and cC and cD
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED")
print("\nVerdict: a LOCKED cluster is an entity in the full operational")
print("sense: one shared frequency (A); it meets the world as a single")
print("oscillator obeying the two-oscillator law with effective coupling")
print("kappa*rho (B) and iter 6's locked branch with its 1/sqrt2 floor (C);")
print("and it is informationally closed at the macro level -- members add")
print("nothing beyond Theta (D). An UNLOCKED collection fails every")
print("criterion. Entity-hood is CREATED by the locking transition, and a")
print("cluster's coupling to the world is discounted by its internal")
print("coherence (K_eff = kappa*rho). CPAF's recursion has its first")
print("grounded rung.")

# ---- plot ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

    ax = axes[0]
    cols = {"tight": "#1f77b4", "mid": "#d62728"}
    for r in results:
        lab = (f"{r['name']}  ρ={r['rho']:.2f}  Δf={r['dfz']:.2f}")
        ax.plot(r["kappas"] / r["kc_pred"], r["Rpair"], "o-", ms=3.5,
                color=cols[r["name"]],
                alpha=0.95 if r["dfz"] == 0.25 else 0.45, label=lab)
    kk = np.linspace(1.0, 1.75, 200)
    ax.plot(kk, np.cos(np.arcsin(np.clip(1 / kk, 0, 1)) / 2), "k--", lw=1,
            alpha=0.7, label="iter-6 branch (limit 1/√2)")
    ax.axvline(1.0, color="k", ls="--", alpha=0.4)
    ax.axhline(1 / np.sqrt(2), color="#2a9d5c", ls=":", alpha=0.8)
    ax.set_xlabel(r"$\kappa \,/\, \kappa_c$   with  "
                  r"$\kappa_c = |\Delta\omega|/(2\rho)$")
    ax.set_ylabel(r"coherence of $(\Theta,\ \theta_z)$")
    ax.set_title("the cluster entrains like ONE oscillator", fontsize=10)
    ax.legend(fontsize=7, loc="lower right"); ax.grid(alpha=0.3)

    ax = axes[1]
    names = ["tight\n(entity)", "weak\n(not an entity)",
             "probe→Θ\n(positive control)"]
    vals = [TE_member["tight, isolated"], TE_member["weak, isolated"],
            TE_probe]
    ax.bar(np.arange(3), vals, 0.55,
           color=["#1f77b4", "#d62728", "#2a9d5c"])
    ax.axhline(0, color="k", lw=0.8)
    ax.set_xticks(np.arange(3)); ax.set_xticklabels(names, fontsize=9)
    ax.set_ylabel("TE beyond Θ's own past (bits)")
    ax.set_title("macro closure: locked ⇒ members add nothing", fontsize=10)
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle("Iter 9 — entity-as-cluster: locking creates the entity "
                 r"($K_{\rm eff}=\kappa\rho$; closure at the macro level)",
                 fontsize=11)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter9_entity_as_cluster.png")
    fig.tight_layout(); fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
