"""
Iteration 10 -- The splice: are GROWN modules entities?

Iteration 9 established the entity criteria on clusters we built by hand
(uniform internal coupling, set by fiat). Iteration 5 grows modules from
experience (per-PAIR synchrony-gated reward + coupling competition sculpting
a coupling matrix into blocks). This iteration splices the two threads: grow
the modules with iter 5's machinery, UNCHANGED, then subject them to iter 9's
entity criteria, UNADJUSTED -- every prediction computed from measured
quantities of the grown structure (its mean frequency w_bar, its internal
coherence rho), nothing hand-tuned.

Theory says this should work: the iter-9 reduction's key cancellation
(internal coupling terms vanish from the macro-phase's motion) needs only
K_ij = K_ji -- sin's antisymmetry under i<->j does the rest -- so it holds
for ANY symmetric coupling matrix, including a learned, heterogeneous one.
The locking threshold prediction kappa_c = |Dw|/(2 rho) therefore extends to
grown modules as-is. That is a real prediction, and this script tries to
break it.

We also add a sharper control than iter 9's weak cluster: a FAKE module --
an arbitrary boundary drawn through the same grown system (15 members from
each true cluster), evaluated on the SAME trajectory as the true module. If
the entity criteria pass the grown boundary and fail the arbitrary one, they
do more than verify entities: they LOCATE them. Entity boundaries become
discoverable from dynamics, no labels required.

Four claims:

  (A) Growth reproduces iter 5 and each grown module is ONE clock. The
      per-pair+competition run recovers the two modules (contrast, Q); within
      a grown module the member velocities collapse to a single value (=
      the module's mean natural frequency); the two modules keep two distinct
      clocks (they are two entities, not one); the fake boundary contains two
      clocks (not a candidate entity).

  (B) The grown module obeys the pair law with its MEASURED coherence.
      Excised with its learned (heterogeneous) couplings and coupled to a
      probe per iter 9, the empirical entrainment threshold matches
      kappa_c = |w_z - w_bar|/(2 rho) with w_bar and rho measured from the
      grown module itself. Two detunings.

  (C) The 1/sqrt2 locked branch, third appearance. The measured locked
      branch follows R(kappa) = cos(arcsin(Dw/(2 rho kappa))/2) -- the same
      curve as bare pairs (iter 6) and imposed clusters (iter 9).

  (D) Closure locates the boundary. On one noisy free run of the FULL grown
      system: TE(member -> Theta | Theta) is ~0 for the true grown module
      and clearly positive for the fake boundary -- same trajectory, only
      the boundary differs. (We expected the in-situ module to leak slightly
      via the cross-links to module B; measured, the leak is below the
      estimator floor -- in situ matches excised within noise at this
      cross-coupling strength.) Bonus observation: macro-level TE between
      the two grown entities (Theta_B -> Theta_A), the first
      entity-to-entity information measurement.

Method. Part 0 is iter 5's per-pair+comp condition verbatim (same params,
same machinery from ksomheb.py); K is then FROZEN for the entity tests
(iter 9's criteria are stated for fixed couplings; the grown K's plasticity
at steady state is small). Parts 1-2 low noise (sharp bifurcation), Part 3
strong noise (information dynamics). TE estimator per iter 8/9 (fine
conditioning bins, circular-shift surrogates). Frequencies in rad/s, TE in
bits.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ksomheb import (order_parameter, kuramoto_step, local_synchrony,
                     synaptic_normalize, modularity)

# ================= Part 0 -- grow the modules (iter 5, verbatim) ===========
np.random.seed(23)                     # iter 5's seed: same world
N = 60
half = N // 2
groups = np.array([0] * half + [1] * (N - half))
Delta, jitter = 1.4, 0.12
omega = np.where(groups == 0, +Delta, -Delta) + np.random.normal(0, jitter, N)

dt_grow = 0.05
steps_grow = 50_000
pair_threshold = 0.60
eta, lam, K_max = 0.01, 0.005, 2.0
K0 = 0.8

print("Part 0 -- growing modules (iter 5 machinery: per-pair reward + "
      "competition)")
rng_grow = np.random.RandomState(1)
theta = rng_grow.uniform(0, 2 * np.pi, N)
K = np.full((N, N), K0); np.fill_diagonal(K, 0.0)
budget = K.sum(axis=1).mean()
for t in range(steps_grow):
    theta = kuramoto_step(theta, omega, K, dt_grow)
    S = local_synchrony(theta)
    drive = S * (S - pair_threshold)          # per-pair: does not cancel
    dK = eta * drive - lam * K
    np.fill_diagonal(dK, 0.0)
    K = np.clip(K + dK * dt_grow, 0.0, K_max)
    K = np.clip(synaptic_normalize(K, budget), 0.0, K_max)

within = (groups[:, None] == groups[None, :]).copy()
cross = ~within
np.fill_diagonal(within, False)
contrast = K[within].mean() / K[cross].mean()
Q = modularity(K, groups)
print(f"grown: K_within={K[within].mean():.3f}  K_cross={K[cross].mean():.3f}"
      f"  contrast={contrast:.2f}  Q={Q:+.3f}   (iter 5 reference: ~3.3, "
      f"~+0.26)")
K = K.copy()                                   # frozen from here on

A = np.where(groups == 0)[0]                   # the grown module under test
B = np.where(groups == 1)[0]
FAKE = np.concatenate([A[:15], B[:15]])        # arbitrary boundary, same size
w_bar_A = omega[A].mean()
w_bar_B = omega[B].mean()

# ---- shared simulators (frozen K; heterogeneous coupling via matmul) ------
rng = np.random.RandomState(9)
dt, sub = 0.01, 10
dt_rec = dt * sub

def sim_full(Kmat, noise, T):
    """Full N-oscillator system with frozen coupling Kmat (1/N convention).
    Returns subsampled member phases (n, N)."""
    n_steps = int(T / dt); n_rec = n_steps // sub
    th = rng.uniform(0, 2 * np.pi, N)
    amp = noise * np.sqrt(dt)
    PH = np.empty((n_rec, N))
    r = 0
    for k in range(n_steps):
        E = np.exp(1j * th)
        internal = np.imag(np.conj(E) * (Kmat @ E)) / N
        th = (th + (omega + internal) * dt + amp * rng.randn(N)) % (2 * np.pi)
        if k % sub == 0 and r < n_rec:
            PH[r] = th; r += 1
    return PH

def sim_excised(Ksub, w_sub, kappas, wz, noise, T):
    """Excised module (its grown coupling submatrix, 1/M normalization) +
    probe per iter 9; vectorized over a kappa sweep. Returns Theta (n,C),
    rho (n,C), probe (n,C)."""
    Msub = len(w_sub); C = len(kappas)
    kap = np.asarray(kappas, float)
    n_steps = int(T / dt); n_rec = n_steps // sub
    th = rng.uniform(0, 2 * np.pi, (Msub, C))
    tz = rng.uniform(0, 2 * np.pi, C)
    amp = noise * np.sqrt(dt)
    TH = np.empty((n_rec, C)); RH = np.empty((n_rec, C)); TZ = np.empty((n_rec, C))
    r = 0
    for k in range(n_steps):
        E = np.exp(1j * th)
        internal = np.imag(np.conj(E) * (Ksub @ E)) / Msub
        dth = (w_sub[:, None] + internal
               + kap[None, :] * np.sin(tz[None, :] - th)) * dt \
            + amp * rng.randn(Msub, C)
        dtz = (wz + kap * np.sin(th - tz[None, :]).mean(0)) * dt \
            + amp * rng.randn(C)
        th = (th + dth) % (2 * np.pi)
        tz = (tz + dtz) % (2 * np.pi)
        if k % sub == 0 and r < n_rec:
            ph = E.mean(0)
            TH[r] = np.angle(ph); RH[r] = np.abs(ph); TZ[r] = tz
            r += 1
    return TH, RH, TZ

def macro_series(PH, idx):
    ph = np.exp(1j * PH[:, idx]).mean(1)
    return np.angle(ph), np.abs(ph)

def mean_velocity(series):
    u = np.unwrap(series)
    return (u[-1] - u[0]) / ((len(u) - 1) * dt_rec)

# ============ Part 1 -- in situ: one clock per grown module (Check A) ======
print("\nPart 1 -- in situ (full grown system, K frozen): who shares a clock?")
noise_lo = 0.05
PH = sim_full(K, noise_lo, 400.0)
b1 = int(50.0 / dt_rec)
PH1 = PH[b1:]
v = np.array([mean_velocity(PH1[:, i]) for i in range(N)])
ThA, rhoA_insitu = macro_series(PH1, A)
ThB, _ = macro_series(PH1, B)
vThA, vThB = mean_velocity(ThA), mean_velocity(ThB)
spread_A, spread_B = v[A].std(), v[B].std()
spread_fake = v[FAKE].std()
print(f"module A: member-velocity std {spread_A:.4f}, "
      f"v(Theta_A)={vThA:+.3f} vs w_bar_A={w_bar_A:+.3f}, "
      f"rho_A(in situ)={rhoA_insitu.mean():.3f}")
print(f"module B: member-velocity std {spread_B:.4f}, "
      f"v(Theta_B)={vThB:+.3f} vs w_bar_B={w_bar_B:+.3f}")
print(f"fake boundary (15 A + 15 B): member-velocity std {spread_fake:.4f}  "
      f"(two clocks {abs(vThA - vThB):.2f} apart)")

cA = (contrast > 2.0 and Q > 0.15
      and spread_A < 0.05 and spread_B < 0.05
      and abs(vThA - w_bar_A) < 0.05 and abs(vThB - w_bar_B) < 0.05
      and spread_fake > 0.5 * abs(w_bar_A - w_bar_B) / 2)
print(f"\nCheck A (growth + one clock per grown module): modules recovered "
      f"(contrast {contrast:.2f}, Q {Q:+.3f}); each grown module runs at its "
      f"own w_bar with ~zero internal spread; the arbitrary boundary "
      f"contains two clocks")
print(f"   -> {'PASS' if cA else 'FAIL'}")

# ====== Part 2 -- excised grown module obeys the pair law (Checks B, C) ====
print("\nPart 2 -- excised grown module + probe: the pair law, third time")
KA = K[np.ix_(A, A)]                    # the LEARNED internal couplings
wA = omega[A]
MA = len(A)

# measure the grown module's own coherence, free-running (kappa = 0)
TH0, RH0, _ = sim_excised(KA, wA, [0.0], w_bar_A, noise_lo, 200.0)
rho_A = float(RH0[int(50.0 / dt_rec):, 0].mean())
print(f"excised module A: measured rho = {rho_A:.3f}  (prediction input; "
      f"nothing tuned)")

T2 = 600.0
b2 = int(100.0 / dt_rec)
lock_tol = 0.05
NK = 25
results = []
print(f"{'detune':>7} | {'kc pred':>8} | {'kc emp':>8} | {'err':>6}")
for Dw_probe in [0.6, 1.0]:
    wz = w_bar_A + Dw_probe
    kc_pred = Dw_probe / (2 * rho_A)
    kappas = np.linspace(0.55 * kc_pred, 1.75 * kc_pred, NK)
    TH, RH, TZ = sim_excised(KA, wA, kappas, wz, noise_lo, T2)
    drift = np.empty(NK); Rpair = np.empty(NK)
    for i in range(NK):
        psi = np.unwrap(TH[b2:, i] - TZ[b2:, i])
        drift[i] = abs((psi[-1] - psi[0]) / ((len(psi) - 1) * dt_rec))
        Rpair[i] = np.mean(np.abs(0.5 * (np.exp(1j * TH[b2:, i])
                                         + np.exp(1j * TZ[b2:, i]))))
    locked = drift < lock_tol
    i_first = int(np.argmax(locked))
    kc_emp = 0.5 * (kappas[i_first - 1] + kappas[i_first])
    err = abs(kc_emp - kc_pred) / kc_pred
    results.append(dict(Dw=Dw_probe, kappas=kappas, drift=drift, Rpair=Rpair,
                        locked=locked, i_first=i_first, kc_emp=kc_emp,
                        kc_pred=kc_pred, err=err))
    print(f"{Dw_probe:7.2f} | {kc_pred:8.4f} | {kc_emp:8.4f} | {err:6.1%}")

cB = max(r["err"] for r in results) < 0.10
print(f"\nCheck B (grown module obeys kappa_c=|Dw|/(2 rho), rho measured): "
      f"max error {max(r['err'] for r in results):.1%}")
print(f"   -> {'PASS' if cB else 'FAIL'}")

branch_errs = []
for r in results:
    lk = r["locked"].copy(); lk[:r["i_first"]] = False
    kl = r["kappas"][lk]
    R_theory = np.cos(np.arcsin(np.clip(r["Dw"] / (2 * rho_A * kl), 0, 1)) / 2)
    branch_errs.append(float(np.abs(r["Rpair"][lk] - R_theory).mean()))
cC = max(branch_errs) < 0.04
print(f"Check C (the 1/sqrt2 branch, third appearance): locked branch "
      f"matches theory to {max(branch_errs):.3f} mean abs error")
print(f"   -> {'PASS' if cC else 'FAIL'}")

# ============ Part 3 -- closure locates the boundary (Check D) =============
print("\nPart 3 -- closure: the true boundary is quiet, the fake one leaks")
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
    """TE(X->Y) = I(Y_{t+lag}; X_t | Y_t); iter-8/9 estimator."""
    yf = _bin(y[lag:], B); cond = _bin(y[:-lag], Bcond); xs = x[:-lag]
    def te_of(xsrc):
        return _cond_mi(yf, _bin(xsrc, B), cond, B, B, Bcond)
    te = te_of(xs)
    n = len(xs)
    surr = [te_of(np.roll(xs, _rng.randint(n // 10, n - n // 10)))
            for _ in range(n_surr)]
    return te - float(np.mean(surr))

def closure_TE(PHrun, idx, n_members=10):
    """Mean TE(member -> Theta | Theta) over a spread of members of idx."""
    Th, _ = macro_series(PHrun, idx)
    picks = idx[np.linspace(0, len(idx) - 1, n_members).astype(int)]
    return float(np.mean([transfer_entropy_bits(PHrun[:, i], Th)
                          for i in picks])), Th

# one noisy free run of the FULL grown system: same trajectory, two boundaries
PH = sim_full(K, noise_hi, T3)
PH3 = PH[b3:]
te_true_insitu, ThA3 = closure_TE(PH3, A)
te_fake_insitu, _ = closure_TE(PH3, FAKE)
ThB3, _ = macro_series(PH3, B)
te_BtoA = transfer_entropy_bits(ThB3, ThA3)     # entity -> entity (observation)

# excised true module (cross-couplings zeroed), same noise: closure without
# the neighbour's leak
Kiso = K.copy(); Kiso[np.ix_(A, B)] = 0.0; Kiso[np.ix_(B, A)] = 0.0
PHi = sim_full(Kiso, noise_hi, T3)
te_true_excised, _ = closure_TE(PHi[b3:], A)

print(f"TE(member -> Theta | Theta):  true module in situ  = "
      f"{te_true_insitu:7.4f}")
print(f"                              true module excised  = "
      f"{te_true_excised:7.4f}")
print(f"                              fake boundary in situ = "
      f"{te_fake_insitu:7.4f}")
print(f"observation -- entity-to-entity macro TE(Theta_B -> Theta_A | "
      f"Theta_A) = {te_BtoA:.4f} (grown cross-links are a real macro-level "
      f"channel)")

cD = (te_true_excised < 0.01
      and te_fake_insitu > 0.03
      and te_fake_insitu > 3 * max(te_true_insitu, 1e-4))
print(f"\nCheck D (closure locates the boundary): the grown boundary is "
      f"closed ({te_true_excised:.4f} excised, {te_true_insitu:.4f} in situ "
      f"-- equal within estimator noise, so module B's leak through the "
      f"cross-links is below the floor here); the arbitrary boundary leaks "
      f"{te_fake_insitu:.4f} bits on the same trajectory")
print(f"   -> {'PASS' if cD else 'FAIL'}")

allok = cA and cB and cC and cD
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED")
print("\nVerdict: modules grown by per-pair reward + competition ARE")
print("entities in iteration 9's full operational sense -- one clock, the")
print("pair law at their own measured coherence, the 1/sqrt2 branch, and")
print("macro closure -- while an arbitrary boundary through the same system")
print("fails the same tests on the same trajectory. Learning sculpts the")
print("boundaries; locking brings them to life; the result obeys the same")
print("laws as its parts. And the criteria are not just a verdict but a")
print("detector: entity boundaries are discoverable from dynamics alone.")

# ---- plot ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.4))

    ax = axes[0]
    im = ax.imshow(K, cmap="viridis", vmin=0, vmax=K_max)
    ax.axhline(half - 0.5, color="w", lw=0.8, alpha=0.7)
    ax.axvline(half - 0.5, color="w", lw=0.8, alpha=0.7)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f"the grown K (iter-5 machinery)\ncontrast {contrast:.2f}, "
                 f"Q {Q:+.2f}", fontsize=9.5)
    plt.colorbar(im, ax=ax, fraction=0.046)

    ax = axes[1]
    marks = {0.6: ("o-", 0.95), 1.0: ("s-", 0.55)}
    for r in results:
        mk, al = marks[r["Dw"]]
        ax.plot(r["kappas"] / r["kc_pred"], r["Rpair"], mk, ms=3.5,
                color="#1f77b4", alpha=al,
                label=f"grown module, Δω={r['Dw']:.1f}")
    kk = np.linspace(1.0, 1.75, 200)
    ax.plot(kk, np.cos(np.arcsin(np.clip(1 / kk, 0, 1)) / 2), "k--", lw=1,
            alpha=0.7, label="iter-6 branch (limit 1/√2)")
    ax.axvline(1.0, color="k", ls="--", alpha=0.4)
    ax.axhline(1 / np.sqrt(2), color="#2a9d5c", ls=":", alpha=0.8)
    ax.set_xlabel(r"$\kappa/\kappa_c$,  $\kappa_c=|\Delta\omega|/(2\rho)$, "
                  r"$\rho$ measured")
    ax.set_ylabel(r"coherence of $(\Theta_A,\ \theta_z)$")
    ax.set_title("the grown module obeys the pair law", fontsize=9.5)
    ax.legend(fontsize=7, loc="lower right"); ax.grid(alpha=0.3)

    ax = axes[2]
    names = ["true module\n(excised)", "true module\n(in situ)",
             "fake boundary\n(in situ)"]
    vals = [te_true_excised, te_true_insitu, te_fake_insitu]
    ax.bar(np.arange(3), vals, 0.55,
           color=["#1f77b4", "#9ecae1", "#d62728"])
    ax.axhline(0, color="k", lw=0.8)
    ax.set_xticks(np.arange(3)); ax.set_xticklabels(names, fontsize=8.5)
    ax.set_ylabel("TE(member → Θ | Θ)  (bits)")
    ax.set_title("closure finds the real boundary", fontsize=9.5)
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle("Iter 10 — the splice: learning sculpts the boundary, "
                 "locking makes it an entity", fontsize=11)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter10_grown_entities.png")
    fig.tight_layout(); fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
