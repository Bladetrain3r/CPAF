"""
Iteration 16 -- Clocks: participant desynchronization vs observer re-clocking.

Two DIFFERENT "clock" questions live in the observer-relativity seam (D21), and
this witness keeps them separate, per the canonical guardrails (GPTSol: do not
classify coordinate disagreement as physical deviation):

  PART A -- PARTICIPANT clocks (physical). Agents genuinely acting at different
  times: interleaved duty windows, so the two agents are NEVER co-present. A
  direct interaction requires co-presence (a message must be received as it is
  sent); a stigmergic medium (iter 15) buffers it. Externalizing memory also
  externalizes the simultaneity requirement.

  PART B -- OBSERVER clock (representational). The SAME physical trajectory,
  re-represented: coarser sampling, a smooth monotone time-warp. Nothing
  physical changed, so classifications must not change -- only magnitudes may.

Model (Part A). Two phase oscillators write/read a deposit-evaporation medium
M (as iter 15) but only during their own duty window of length W: agent 1 is
present on [0,W) of each period P=2W, agent 2 on [W(1-f), W(2-f)) -- overlap
fraction f (f=0: strict alternation, never co-present; f=1: fully co-present).
While present an agent deposits AND senses; while absent it free-drifts. Duty
is 50% for every f, so only co-presence varies. Trail amplitude is matched
across evaporation rates (deposit a = a0*gamma, so |M|_eq is gamma-invariant):
we vary persistence at fixed trail strength.

Claims:
 1. Coordination WITHOUT co-presence: at f=0 (agents never simultaneously
    present) the pair still locks through the medium when the trail outlives
    the window (gamma*W << 1). r >> drift baseline, with zero direct contact.
 2. The persistence time 1/gamma is a CLOCK-SLACK BUDGET: coordination dies
    when the window exceeds what the trail can carry. The tolerated window W50
    (where r falls halfway to baseline) scales as 1/gamma -- gamma*W50 is
    constant across an 8x range of gamma. The constant is a FEW e-foldings
    (~5-7), not 1, and that is itself informative: evaporation decays the
    medium's AMPLITUDE, while its PHASE (the stored direction) persists, so
    coordination survives until the returning pull K|M| ~ exp(-gamma*W) drops
    below the drift it must correct -- W50 ~ (1/gamma) * ln(pull/drift margin).
    External memory buys clock slack proportional to its persistence time,
    with a log bonus from its stored-phase structure.
 3. A DIRECT edge requires co-presence: gate a direct coupling by simultaneous
    presence and sweep overlap f. Direct coordination needs f (r rises from
    baseline at f=0 to locked at f=1); mediated coordination is f-INDEPENDENT
    (flat, high). Internal systems must share a wall clock; stigmergic ones
    need only each share a clock with the medium.
 4. Mediation has a MEMORY signature in the lag structure: comparing edges at
    MATCHED coordination level (direct strength tuned so pair r matches the
    mediated pair's; a sub-threshold direct pair drifts and its profile is a
    slip artifact), the direct edge's TE-vs-lag profile decays to the
    estimator floor within ~2 time units -- a direct channel forgets at its
    relaxation time -- while the mediated edge's transfer PERSISTS (>50% of
    peak out to 4 units): the medium retains the writer's past and keeps it
    informative about the reader's future. External memory, visible in the
    information plane; a clock-structure discriminator complementing iter
    15's modest screening margin. (The mediated peak also sits later, but on
    this substrate the persistent TAIL is the robust part of the signature.)
 5. Observer re-clocking preserves VERDICTS: under decimation (x2, x4) and a
    smooth monotone time-warp, the iter-15 screening verdict (TE|M collapses
    below 45% of raw) and the regime classification are unchanged -- while the
    raw TE magnitudes in bits are NOT invariant (they are measurements, tied
    to the observer's clock; the certificates are the portable part).
 6. Coordinate change is DISTINGUISHABLE from physical change: the warp scales
    rate observables (the phase-slip rate of an uncoupled pair reads c times
    its true value on the warped clock, c the mean warp factor) but leaves the
    RELATIONAL structure invariant (the distribution of the simultaneous phase
    difference theta_1 - theta_2 is unchanged), whereas an actual physical
    change (decoupling) reshapes the relational structure. Invariant
    relational statistics = the discriminator GPT's guardrail asks for: a
    clock change moves rates, not relations.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

rng = np.random.RandomState(16)

# ---------- estimators (as in iters 8/15) ----------
def _bin(a, B):
    return np.minimum((a / (2 * np.pi) * B).astype(np.int64), B - 1)

def _cond_mi(a, b, c, Ba, Bb, Bc):
    flat = np.bincount((a * Bb + b) * Bc + c, minlength=Ba * Bb * Bc)
    p = flat.reshape(Ba, Bb, Bc) / flat.sum()
    pc = p.sum((0, 1), keepdims=True); pac = p.sum(1, keepdims=True); pbc = p.sum(0, keepdims=True)
    nz = p > 0
    return float(np.sum(p[nz] * np.log2((p * pc)[nz] / (pac * pbc)[nz])))

def transfer_entropy_bits(x, y, z=None, lag=3, B=8, Bcond=20, Bycond=12, Bz=10,
                          n_surr=8, _rng=rng):
    """TE(X->Y)=I(Y_{t+lag}; X_t | Y_t), or |(Y_t,Z_t) if z given; surrogate-corrected."""
    yf = _bin(y[lag:], B); xs = x[:-lag]
    if z is None:
        cond = _bin(y[:-lag], Bcond); Bc = Bcond
    else:
        cond = _bin(y[:-lag], Bycond) * Bz + _bin(z[:-lag], Bz); Bc = Bycond * Bz
    def te_of(xsrc):
        return _cond_mi(yf, _bin(xsrc, B), cond, B, B, Bc)
    te = te_of(xs); n = len(xs)
    surr = [te_of(np.roll(xs, _rng.randint(n // 10, n - n // 10))) for _ in range(n_surr)]
    return te - float(np.mean(surr))

def order_param(TH):
    return np.abs(np.mean(np.exp(1j * TH), axis=-1))

# ---------- Part A simulator: duty-windowed agents + persistent medium ----------
def simulate_sched(W, gamma, f=0.0, K=2.0, D=0.0, a0=2.0, noise=0.05,
                   om=(0.1, -0.1), T=None, dt=0.02, sub=5, burn=2000, seed=0,
                   medium=True):
    """Two agents on 50%-duty windows of length W, overlap fraction f.
    Present -> deposit into M and sense K|M|sin(argM - theta); absent -> free
    drift. Optional direct coupling D gated by SIMULTANEOUS presence.
    Deposit a = a0*gamma keeps |M|_eq matched across gamma."""
    r = np.random.RandomState(seed)
    om = np.asarray(om, float)
    if T is None:
        T = max(240.0, 30.0 * W)
    a = a0 * gamma if medium else 0.0
    th = r.uniform(0, 2 * np.pi, 2)
    M = 0 + 0j
    P = 2.0 * W
    s1 = W * (1.0 - f)                      # agent-2 window start
    n_steps = burn + int(T / dt)
    amp = noise * np.sqrt(dt)
    TH = []
    for k in range(n_steps):
        t = (k * dt) % P
        pres = np.array([t < W, ((t - s1) % P) < W], dtype=float)
        dep = 0.5 * np.sum(pres * np.exp(1j * th))
        M = M + dt * (a * dep - gamma * M)
        absM, argM = np.abs(M), np.angle(M)
        dth = om + pres * K * absM * np.sin(argM - th)
        if D:
            g = D * pres[0] * pres[1]       # direct needs BOTH present
            dth = dth + g * np.sin(th[::-1] - th)
        th = (th + dt * dth + amp * r.randn(2)) % (2 * np.pi)
        if k >= burn and (k - burn) % sub == 0:
            TH.append(th.copy())
    return np.array(TH)

# ---------- continuous simulator (as iter 15): agents + medium, no schedule ----------
def simulate(N, gamma, K=2.0, a=1.5, direct=0.0, noise=0.05, omega=None,
             T=500.0, dt=0.02, sub=8, burn=4000, seed=0):
    r = np.random.RandomState(seed)
    if omega is None:
        omega = 0.4 * np.linspace(-1, 1, N)
    th = r.uniform(0, 2 * np.pi, N)
    M = 0 + 0j
    n_steps = burn + int(T / dt)
    TH = []; ARGM = []; ABSM = []
    amp = noise * np.sqrt(dt)
    for k in range(n_steps):
        dep = np.mean(np.exp(1j * th))
        M = M + dt * (a * dep - gamma * M)
        absM, argM = np.abs(M), np.angle(M)
        dth = omega + K * absM * np.sin(argM - th)
        if direct:
            d = th[None, :] - th[:, None]
            dth = dth + direct * np.sin(d).mean(axis=1)
        th = (th + dt * dth + amp * r.randn(N)) % (2 * np.pi)
        if k >= burn and (k - burn) % sub == 0:
            TH.append(th.copy()); ARGM.append(argM % (2 * np.pi)); ABSM.append(absM)
    return np.array(TH), np.array(ARGM), np.array(ABSM)

# ================= Part A1/A2: coordination without co-presence; the slack budget =================
print("Part A -- participant clocks: coordination with ZERO co-presence (f=0)")
print("(agents alternate strict duty windows of length W; trail amplitude matched across gamma)\n")

# drift baseline: same detuning/noise, no medium, no direct
TH0 = simulate_sched(1.0, 1.0, K=0.0, medium=False, seed=3)
r_base = float(order_param(TH0).mean())

gammas = [0.5, 1.0, 2.0, 4.0]
Ws = np.geomspace(0.125, 16.0, 8)
rW = {}
print(f"drift baseline (no medium): r = {r_base:.3f}")
print(f"{'gamma':>6} | " + " | ".join(f"W={w:5.2f}" for w in Ws))
for g in gammas:
    rW[g] = [float(order_param(simulate_sched(w, g, f=0.0, seed=3)).mean()) for w in Ws]
    print(f"{g:6.1f} | " + " | ".join(f"{r:7.3f}" for r in rW[g]))

def crossover_W(rs, Ws, r_top, r_base):
    """First W where r falls below the midpoint, log-interpolated."""
    mid = 0.5 * (r_top + r_base)
    for i in range(1, len(Ws)):
        if rs[i] < mid <= rs[i - 1]:
            t = (rs[i - 1] - mid) / (rs[i - 1] - rs[i])
            return float(np.exp(np.log(Ws[i - 1]) + t * (np.log(Ws[i]) - np.log(Ws[i - 1]))))
    return float(Ws[-1]) if rs[-1] >= mid else float(Ws[0])

W50 = {g: crossover_W(rW[g], Ws, max(rW[g][:2]), r_base) for g in gammas}
print("\nclock-slack budget: tolerated window W50 vs persistence time 1/gamma")
print(f"{'gamma':>6} | {'1/gamma':>7} | {'W50':>6} | {'gamma*W50':>9}")
for g in gammas:
    print(f"{g:6.1f} | {1/g:7.2f} | {W50[g]:6.2f} | {g*W50[g]:9.2f}")

c1 = rW[gammas[0]][0] > 0.85 and rW[gammas[0]][0] > r_base + 0.2
gW = [g * W50[g] for g in gammas]
c2 = (W50[0.5] / W50[4.0] > 3.0) and (max(gW) / min(gW) < 2.0)
print(f"\nCheck 1 (coordination without co-presence): f=0, gamma={gammas[0]}, "
      f"W={Ws[0]:.3f} -> r={rW[gammas[0]][0]:.3f} vs baseline {r_base:.3f} "
      f"-> {'PASS' if c1 else 'FAIL'}")
print(f"Check 2 (slack budget scales as 1/gamma): W50 ratio (gamma 0.5 vs 4) = "
      f"{W50[0.5]/W50[4.0]:.1f}x across an 8x persistence range, and gamma*W50 "
      f"constant within {max(gW)/min(gW):.2f}x ([{min(gW):.1f}, {max(gW):.1f}] ~ "
      f"a few e-foldings: amplitude decays, stored phase persists)  "
      f"-> {'PASS' if c2 else 'FAIL'}")

# ================= Part A3: a direct edge requires co-presence =================
print("\nPart A3 -- overlap sweep: direct coupling needs co-presence, the medium doesn't")
fs = [0.0, 0.25, 0.5, 1.0]
Wf, gf = 0.5, 0.5                          # gamma*W = 0.25: trail comfortably persists
r_med = [float(order_param(simulate_sched(Wf, gf, f=f, K=2.0, D=0.0, seed=4)).mean())
         for f in fs]
r_dir = [float(order_param(simulate_sched(Wf, gf, f=f, K=0.0, D=2.0, medium=False,
                                          seed=4)).mean()) for f in fs]
print(f"{'overlap f':>9} | " + " | ".join(f"{f:5.2f}" for f in fs))
print(f"{'mediated':>9} | " + " | ".join(f"{r:5.3f}" for r in r_med))
print(f"{'direct':>9} | " + " | ".join(f"{r:5.3f}" for r in r_dir))

c3 = (r_med[0] > 0.85 and r_dir[0] < r_base + 0.1 and r_dir[-1] > 0.85
      and (max(r_med) - min(r_med)) < 0.1)
print(f"\nCheck 3 (co-presence dissociation): direct r goes {r_dir[0]:.2f} -> "
      f"{r_dir[-1]:.2f} as overlap 0 -> 1 (needs a shared clock); mediated stays "
      f"{min(r_med):.2f}-{max(r_med):.2f} (clock-indifferent)  -> {'PASS' if c3 else 'FAIL'}")

# ================= Part A4: the lag signature of mediation =================
print("\nPart A4 -- TE(1->2) vs lag: a mediated edge remembers, a direct edge forgets")
om2 = np.array([0.6, -0.6])
# mediated pair (iter-15 Part B configuration; live partial-lock channel)
TH_m, ARGM_m, _ = simulate(2, 1.0, K=2.5, direct=0.0, noise=0.60, omega=om2,
                           T=4000.0, dt=0.02, sub=5, seed=2)
# direct pair: same drive/noise, genuine edge, no medium (a=0 -> M stays 0).
# direct=3.5 tuned so pair r matches the mediated pair's (~0.97): a fair
# comparator must sit at the same coordination level (a sub-threshold direct
# pair drifts, and its lag profile is a slip artifact).
TH_d, _, _ = simulate(2, 1.0, K=0.0, a=0.0, direct=3.5, noise=0.60, omega=om2,
                      T=4000.0, dt=0.02, sub=5, seed=2)
sample_dt = 0.02 * 5
lags = np.arange(1, 41, 3)
r_m, r_d = float(order_param(TH_m).mean()), float(order_param(TH_d).mean())
print(f"  (coordination matched: mediated r={r_m:.3f}, direct r={r_d:.3f})")
prof_m = np.array([transfer_entropy_bits(TH_m[:, 0], TH_m[:, 1], lag=int(l))
                   for l in lags])
prof_d = np.array([transfer_entropy_bits(TH_d[:, 0], TH_d[:, 1], lag=int(l))
                   for l in lags])
pk_m, pk_d = int(lags[int(np.argmax(prof_m))]), int(lags[int(np.argmax(prof_d))])
tail_sel = lags * sample_dt >= 2.5
tail_m = max(float(prof_m[tail_sel].mean()), 0.0) / prof_m.max()
tail_d = max(float(prof_d[tail_sel].mean()), 0.0) / prof_d.max()
print(f"  mediated: peak {prof_m.max():.4f} bits at lag {pk_m*sample_dt:.1f}u; "
      f"tail (2.5-4.0u) retains {tail_m:.0%} of peak")
print(f"  direct:   peak {prof_d.max():.4f} bits at lag {pk_d*sample_dt:.1f}u; "
      f"tail (2.5-4.0u) retains {tail_d:.0%} of peak (estimator floor)")
c4 = (tail_m > 0.5) and (tail_d < 0.15)
print(f"Check 4 (memory signature): the direct edge forgets within ~2 time units; "
      f"the mediated edge's transfer persists ({tail_m:.0%} vs {tail_d:.0%} of peak "
      f"at 2.5-4u) -- the medium holds the writer's past  -> {'PASS' if c4 else 'FAIL'}")

# ================= Part B: observer re-clocking of ONE trajectory =================
print("\nPart B -- observer clock: re-represent the SAME mediated trajectory")
th1, th2, argM = TH_m[:, 0], TH_m[:, 1], ARGM_m[:, ]

def warp_series(series_list, h, c=1.3, A=0.45, Tw=60.0):
    """Resample at observer times tau: t = g(tau), dt/dtau = c(1 + A sin(2pi tau/Tw)).
    Smooth, monotone (c(1-A) > 0). Interpolation on the unit phasor."""
    n = len(series_list[0])
    t_grid = np.arange(n) * h
    n_tau = int(n / c)
    tau = np.arange(n_tau) * h
    rate = c * (1 + A * np.sin(2 * np.pi * tau / Tw))
    t_of = np.concatenate([[0.0], np.cumsum(0.5 * (rate[1:] + rate[:-1]) * h)])
    t_of = t_of[t_of <= t_grid[-1]]
    out = []
    for s in series_list:
        z = np.exp(1j * s)
        zi = np.interp(t_of, t_grid, z.real) + 1j * np.interp(t_of, t_grid, z.imag)
        out.append(np.angle(zi) % (2 * np.pi))
    return out

versions = {"original": (th1, th2, argM)}
for d in (2, 4):
    versions[f"decimate x{d}"] = (th1[::d], th2[::d], argM[::d])
versions["time-warp"] = tuple(warp_series([th1, th2, argM], sample_dt))

print(f"{'version':>12} | {'r':>5} | {'TE(1->2)':>8} | {'TE|M':>7} | {'frac':>5} | verdicts")
res = {}
for name, (a1, a2, am) in versions.items():
    te = transfer_entropy_bits(a1, a2)
    teM = transfer_entropy_bits(a1, a2, z=am)
    frac = teM / te if te > 1e-6 else 0.0
    rv = float(order_param(np.stack([a1, a2], axis=1)).mean())
    screened = frac < 0.45
    regime = "partial" if 0.45 < rv < 0.95 else ("locked" if rv >= 0.95 else "drift")
    res[name] = dict(te=te, teM=teM, frac=frac, r=rv, screened=screened, regime=regime)
    print(f"{name:>12} | {rv:5.2f} | {te:8.4f} | {teM:7.4f} | {frac:5.0%} | "
          f"{'screened' if screened else 'NOT screened'}, {regime}")

names = list(versions)
tes = [res[n]["te"] for n in names]
swing = max(tes) / min(tes) if min(tes) > 0 else np.inf
c5 = (all(res[n]["screened"] for n in names)
      and len({res[n]["regime"] for n in names}) == 1
      and swing > 1.3)
print(f"\nCheck 5 (verdicts survive re-clocking, magnitudes don't): screening verdict "
      f"and regime class identical across all {len(names)} representations, while raw "
      f"TE swings {swing:.1f}x  -> {'PASS' if c5 else 'FAIL'}")

# --- B2: coordinate change vs physical change ---
print("\nPart B2 -- what separates a clock change from a physical change?")
def mean_freq(th, h):
    return float(np.angle(np.exp(1j * np.diff(th))).sum() / (len(th) - 1) / h)
def dphase_hist(a1, a2, bins=36):
    hgt, _ = np.histogram((a1 - a2) % (2 * np.pi), bins=bins,
                          range=(0, 2 * np.pi), density=True)
    return hgt * (2 * np.pi / bins)
# physical control: actually decouple the pair (K=0, no medium force), same drive/noise
TH_p, _, _ = simulate(2, 1.0, K=0.0, a=0.0, direct=0.0, noise=0.60, omega=om2,
                      T=4000.0, dt=0.02, sub=5, seed=2)
# rate observable: the phase-SLIP rate of the uncoupled pair (true value Δω=1.2;
# the locked pair's mean frequency is ~0 in this frame -- no rate to rescale)
psi_p = (TH_p[:, 0] - TH_p[:, 1]) % (2 * np.pi)
psi_p_w = warp_series([psi_p], sample_dt)[0]
f_orig = mean_freq(psi_p, sample_dt)
f_warp = mean_freq(psi_p_w, sample_dt)     # observer uses her own tick
ratio = f_warp / f_orig if abs(f_orig) > 1e-9 else np.inf
h_orig = dphase_hist(th1, th2)
L1_warp = 0.5 * float(np.abs(h_orig - dphase_hist(*versions["time-warp"][:2])).sum())
L1_phys = 0.5 * float(np.abs(h_orig - dphase_hist(TH_p[:, 0], TH_p[:, 1])).sum())
print(f"  rate observable:      uncoupled-pair slip rate reads {f_orig:+.3f} rad/unit "
      f"(original clock) vs {f_warp:+.3f} (warped clock) -- ratio {ratio:.2f} "
      f"(mean warp factor c = 1.30)")
print(f"  relational invariant: L1 distance of the Delta-theta distribution: "
      f"warp {L1_warp:.3f} vs physical decoupling {L1_phys:.3f}")
c6 = (abs(ratio - 1.3) < 0.15) and (L1_warp < 0.15) and (L1_phys > 3 * L1_warp)
print(f"Check 6 (coordinate vs physical): the warp rescales rates (x{ratio:.2f}) but "
      f"leaves relations invariant ({L1_warp:.3f}); decoupling reshapes relations "
      f"({L1_phys:.3f})  -> {'PASS' if c6 else 'FAIL'}")

allok = c1 and c2 and c3 and c4 and c5 and c6
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED")
print("\nVerdict: the two clock questions separate cleanly. PARTICIPANT clocks are")
print("physical: a direct edge only transmits while both parties share a wall clock")
print("(co-presence), whereas a stigmergic medium buffers desynchronization in")
print("proportion to its persistence time -- clock-slack budget W50 ~ (1/gamma) *")
print("ln(margin): the amplitude evaporates but the stored phase persists -- and it")
print("wears its mediation as a MEMORY signature in the lag structure: a")
print("coordination-matched direct edge forgets at its relaxation time, while the")
print("mediated edge's transfer persists far beyond it (the medium holds the past).")
print("External memory doubles as a clock buffer: each agent needs only to share a")
print("clock with the medium, never with each other. OBSERVER clocks are")
print("representational: re-sampling and smooth time-warps move the measured")
print("magnitudes (TE bits, frequencies) but not the certificates (screened-off,")
print("regime class) nor the relational structure (Delta-theta distribution) --")
print("coordinate disagreement is not a physical deviation, and the discriminator")
print("is invariance of relations vs covariance of rates.")

# ---------- plot ----------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(2, 2, figsize=(12.5, 9))
    for g, col in zip(gammas, ["#2a9d5c", "#1f77b4", "#e08a1e", "#d62728"]):
        ax[0, 0].plot(np.array(Ws) * g, rW[g], "o-", color=col, ms=4,
                      label=f"gamma={g}")
    ax[0, 0].axhline(r_base, color="gray", ls="--", lw=1, label="drift baseline")
    ax[0, 0].set_xscale("log")
    ax[0, 0].set_xlabel("gamma * W  (window / persistence time)")
    ax[0, 0].set_ylabel("r")
    ax[0, 0].set_title("A: zero co-presence; slack budget = persistence (curves "
                       "collapse in gamma*W)", fontsize=9.5)
    ax[0, 0].legend(fontsize=7.5); ax[0, 0].grid(alpha=0.3)
    ax[0, 1].plot(fs, r_med, "o-", color="#2a9d5c", label="mediated (via M)")
    ax[0, 1].plot(fs, r_dir, "s-", color="#d62728", label="direct (gated by co-presence)")
    ax[0, 1].axhline(r_base, color="gray", ls="--", lw=1)
    ax[0, 1].set_xlabel("co-presence overlap f"); ax[0, 1].set_ylabel("r")
    ax[0, 1].set_title("A3: a direct edge needs a shared wall clock; the medium "
                       "doesn't", fontsize=9.5)
    ax[0, 1].legend(fontsize=8); ax[0, 1].grid(alpha=0.3); ax[0, 1].set_ylim(0, 1.05)
    ax[1, 0].plot(lags * sample_dt, prof_m, "o-", color="#1f77b4", ms=4,
                  label="mediated edge")
    ax[1, 0].plot(lags * sample_dt, prof_d, "s-", color="#d62728", ms=4,
                  label="direct edge (matched r)")
    ax[1, 0].axhline(0, color="gray", lw=0.8)
    ax[1, 0].axvspan(2.5, 4.0, color="gray", alpha=0.12, label="tail window")
    ax[1, 0].set_xlabel("lag (time units)"); ax[1, 0].set_ylabel("TE(1->2) (bits)")
    ax[1, 0].set_title("A4: memory signature -- the mediated edge's transfer "
                       "persists; the direct edge forgets", fontsize=9.5)
    ax[1, 0].legend(fontsize=8); ax[1, 0].grid(alpha=0.3)
    xpos = np.arange(len(names))
    ax[1, 1].bar(xpos - 0.2, [res[n]["te"] for n in names], 0.38, color="#1f77b4",
                 label="TE(1->2)")
    ax[1, 1].bar(xpos + 0.2, [res[n]["teM"] for n in names], 0.38, color="#e08a1e",
                 label="TE(1->2 | M)")
    for i, n in enumerate(names):
        ax[1, 1].text(i, res[n]["te"] + 0.001, f"{res[n]['frac']:.0%}",
                      ha="center", fontsize=8)
    ax[1, 1].set_xticks(xpos)
    ax[1, 1].set_xticklabels([n.replace(" ", "\n") for n in names], fontsize=8)
    ax[1, 1].set_ylabel("bits")
    ax[1, 1].set_title("B: re-clocking moves magnitudes, not the screening verdict "
                       "(% = surviving fraction)", fontsize=9.5)
    ax[1, 1].legend(fontsize=8); ax[1, 1].grid(alpha=0.3, axis="y")
    fig.suptitle("Iter 16 -- clocks: the medium buffers participant desync; "
                 "observer re-clocking moves measurements, not certificates",
                 y=0.995, fontsize=11)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter16_clock_relativity.png")
    fig.tight_layout(); fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
