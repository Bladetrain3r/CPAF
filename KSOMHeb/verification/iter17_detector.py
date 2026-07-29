"""
Iteration 17 -- The detector: an embedded, read-only observer.

A DETECTOR is a node with no natural frequency (omega_d = 0 in the analysis
frame) that couples ONE-WAY to a source and never feeds back:

    dtheta_d/dt = K_d * sin(target - theta_d) + noise            (read-only)

It reads without writing (Ziggy's motif). Because the edge is strictly
unidirectional, the source's dynamics are unchanged BY CONSTRUCTION -- which is
what lets verified pairs act as composable foundation blocks: feed-forward
attachments never invalidate upstream [AN] results. This iteration witnesses
that isolation exactly, derives the detector's own laws, and takes the first
awareness-shaped step: a subsystem that registers another subsystem's
deviation without disturbing it.

Claims:
 1. PAIR INVARIANCE (exact, not approximate). With the detector attached at
    eps=0 (no back-coupling), the pair's trajectory is bit-identical to the
    pair alone (same noise stream), and its locked offset matches the [AN]
    prediction psi* = arcsin(dw/2K). Zero back-action by construction.
 2. THE ONE-WAY CERTIFICATE. Source theta_1, detector theta_d in a live noisy
    channel: MI(src; det) > 0 (MI is symmetric and blind to direction),
    TE(src->det) >> 0, TE(det->src) ~ 0 (true statistical null). The purest
    one-way case in the suite: iter 8's one-way was an asymmetric coupling
    between peers; the detector is a node DEFINED as sink.
 3. DETECTOR BANDWIDTH IS A DERIVED LAW -- and it differs from the pair's.
    Against a source rotating at Omega, the detector's error obeys the
    one-way Adler equation dpsi/dt = Omega - K_d sin(psi): it locks iff
    K_d >= |Omega| (onset at K_d = Omega, NOT Omega/2 -- no factor of two,
    because only one side is free to move; compare Kc = |dw|/2 for the pair
    where both yield), with tracking lag arcsin(Omega/K_d) [AN]. A detector
    can only follow a world slower than its own bandwidth -- iter 16's
    admissibility boundary realized as physics (an embedded observer with
    insufficient bandwidth loses the signal) rather than as a sampling
    schedule.
 4. DETECTING A DEVIATION (the awareness-shaped step). A RELATION-detector
    reads the pair's phase difference (target = theta_1 - theta_2). Two
    capacities dissociate, and an honest revision sharpened the first:
      - FOLLOWING a drifting pair is priced by the PEAK rate, not the mean:
        an unlocked pair's difference slips nonuniformly (saddle-node ghost
        -- slow near the bottleneck, max rate dw + 2K on the sweep), so a
        detector follows it only when K_d exceeds ~the peak rate [AN]. The
        naive mean-slip bound sqrt(dw^2-K_d^2)/2 was the original
        conjecture; the run refuted it (kept here as the house rule: report
        the miss). Witness: K_d = 3.0 > dw + 2K follows the drifting pair
        everywhere; K_d = 0.8 < dw can never follow it.
      - SETTLING (the detector's own phase freezes -- an intrinsic,
        detector-local statistic) happens at the pair's Kc for BOTH
        bandwidths [CW]: a bandwidth-robust registration of the deviation.
    Following a changing world and noticing it stopped changing are
    different capacities; the detector's own state distinguishes a locked
    pair from a drifting one WITHOUT touching either. Measurement of a
    deviation = a deviation in the measurer.
 5. READER -> PARTICIPANT IS A CONTINUOUS DIAL (the observer effect). Add
    back-coupling eps: TE(det->src) climbs off the floor and the pair's
    locked offset departs from its [AN] value. At eps=0 both are exact.
    Subtlety worth stating: against a STATIC source the back-term is inert
    even at eps>0 (the detector sits exactly on target, sin(0)=0); it is a
    MOVING source that makes reading costly, because the tracking lag is the
    lever arm of back-action (drag ~ eps*sin(lag) ~ eps*Omega/K_d).

Scope honesty: one substrate, N=2+1; "awareness-shaped" means a minimal
registration witness, not the canonical awareness concept; the deviation
verdict's sharpness near Kc is limited by the observation window (critical
slowing smears any finite-time readout).
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

rng = np.random.RandomState(17)

# ---------- estimators (as iters 8/15/16) ----------
def _bin(a, B):
    return np.minimum((a / (2 * np.pi) * B).astype(np.int64), B - 1)

def _cond_mi(a, b, c, Ba, Bb, Bc):
    flat = np.bincount((a * Bb + b) * Bc + c, minlength=Ba * Bb * Bc)
    p = flat.reshape(Ba, Bb, Bc) / flat.sum()
    pc = p.sum((0, 1), keepdims=True); pac = p.sum(1, keepdims=True); pbc = p.sum(0, keepdims=True)
    nz = p > 0
    return float(np.sum(p[nz] * np.log2((p * pc)[nz] / (pac * pbc)[nz])))

def transfer_entropy_bits(x, y, lag=3, B=8, Bcond=20, n_surr=8, _rng=rng):
    yf = _bin(y[lag:], B); xs = x[:-lag]; cond = _bin(y[:-lag], Bcond)
    def te_of(xsrc):
        return _cond_mi(yf, _bin(xsrc, B), cond, B, B, Bcond)
    te = te_of(xs); n = len(xs)
    surr = [te_of(np.roll(xs, _rng.randint(n // 10, n - n // 10))) for _ in range(n_surr)]
    return te - float(np.mean(surr))

def mutual_info_bits(a, b, B=16, n_shuff=8, _rng=rng):
    ab, bb = _bin(a, B), _bin(b, B)
    def mi_of(x):
        p = np.bincount(x * B + bb, minlength=B * B).reshape(B, B) / len(x)
        pa = p.sum(1, keepdims=True); pb = p.sum(0, keepdims=True)
        nz = p > 0
        return float(np.sum(p[nz] * np.log2(p[nz] / (pa @ pb)[nz])))
    mi = mi_of(ab)
    sh = [mi_of(np.roll(ab, _rng.randint(len(ab) // 10, len(ab) - len(ab) // 10)))
          for _ in range(n_shuff)]
    return mi - float(np.mean(sh))

def mean_freq(th, h):
    return float(np.angle(np.exp(1j * np.diff(th))).sum() / (len(th) - 1) / h)

# ---------- simulator: pair + one detector ----------
def simulate(K, om=(0.6, -0.6), Om0=0.0, Kd=2.0, eps=0.0, relation=False,
             noise=0.05, dnoise=None, T=400.0, dt=0.02, sub=5, burn=4000,
             seed=0, detector=True):
    """Pair (bidirectional K) + optional detector (one-way Kd; eps = optional
    back-coupling onto member 1, member-mode only). Separate RNGs for pair and
    detector noise, so the pair's stream is identical with or without the
    detector -- the exactness of claim 1 is testable, not assumed."""
    rp = np.random.RandomState(seed)          # pair noise
    rd = np.random.RandomState(seed + 1000)   # detector noise + init
    om = np.asarray(om, float)
    if dnoise is None:
        dnoise = noise
    th = rp.uniform(0, 2 * np.pi, 2)
    thd = rd.uniform(0, 2 * np.pi)
    n_steps = burn + int(T / dt)
    ap, ad = noise * np.sqrt(dt), dnoise * np.sqrt(dt)
    TH = []; THD = []
    for k in range(n_steps):
        d12 = th[1] - th[0]
        dth = Om0 + om + K * np.array([np.sin(d12), -np.sin(d12)])
        if detector:
            target = (th[0] - th[1]) if relation else th[0]
            dthd = Kd * np.sin(target - thd)
            if eps and not relation:
                dth[0] = dth[0] + eps * np.sin(thd - th[0])
            thd = (thd + dt * dthd + ad * rd.randn()) % (2 * np.pi)
        th = (th + dt * dth + ap * rp.randn(2)) % (2 * np.pi)
        if k >= burn and (k - burn) % sub == 0:
            TH.append(th.copy()); THD.append(thd)
    return np.array(TH), np.array(THD)

def circ_R(a):
    return float(np.abs(np.mean(np.exp(1j * a))))

# ================= Check 1: pair invariance, exact =================
print("Check 1 -- pair invariance: reading is free (at eps=0), by construction")
Kq, omq = 1.5, (0.6, -0.6)                    # quiet locked pair, dw=1.2
TH_alone, _ = simulate(Kq, om=omq, detector=False, seed=3)
TH_with, THD_w = simulate(Kq, om=omq, Kd=2.0, eps=0.0, seed=3)
max_dev = float(np.max(np.abs(np.angle(np.exp(1j * (TH_alone - TH_with))))))
psi = (TH_with[:, 0] - TH_with[:, 1]) % (2 * np.pi)
psi_meas = float(np.angle(np.mean(np.exp(1j * psi))))
psi_an = float(np.arcsin(1.2 / (2 * Kq)))
c1 = (max_dev < 1e-9) and (abs(psi_meas - psi_an) < 0.03)
print(f"  pair trajectory with vs without detector: max |dtheta| = {max_dev:.2e}")
print(f"  locked offset psi* measured {psi_meas:.4f} vs [AN] arcsin(dw/2K) = "
      f"{psi_an:.4f}")
print(f"  -> {'PASS' if c1 else 'FAIL'}")

# ================= Check 2: the one-way certificate =================
print("\nCheck 2 -- one-way certificate: MI blind to direction, TE not")
TH2, THD2 = simulate(2.5, om=(0.6, -0.6), Kd=2.0, noise=0.60, dnoise=0.30,
                     T=4000.0, seed=2)
src, det = TH2[:, 0], THD2
mi = mutual_info_bits(src, det)
te_fwd = transfer_entropy_bits(src, det)
te_back = transfer_entropy_bits(det, src)
c2 = (mi > 0.5) and (te_fwd > 0.02) and (abs(te_back) < 0.006) \
     and (abs(te_back) < 0.15 * te_fwd)
print(f"  MI(src;det) = {mi:.3f} bits (symmetric -- present, as it must be)")
print(f"  TE(src->det) = {te_fwd:.4f} bits   TE(det->src) = {te_back:+.4f} bits "
      f"(floor: a true null)")
print(f"  -> {'PASS' if c2 else 'FAIL'}")

# ================= Check 3: bandwidth law (one-way Adler) =================
print("\nCheck 3 -- detector bandwidth: locks iff K_d >= Omega (no factor 2), "
      "lag arcsin(Omega/K_d)")
Om0 = 1.0
Kds = np.geomspace(0.3, 4.0, 10)
slips, offs = [], []
for kd in Kds:
    THb, THDb = simulate(2.0, om=(0.1, -0.1), Om0=Om0, Kd=kd, noise=0.03,
                         T=300.0, seed=5)
    delta = (THb[:, 0] - THDb) % (2 * np.pi)
    slips.append(abs(mean_freq(np.unwrap(delta), 0.02 * 5)))
    offs.append(float(np.angle(np.mean(np.exp(1j * delta)))))
slips = np.array(slips); offs = np.array(offs)
locked = slips < 0.05 * Om0
onset = float(Kds[np.argmax(locked)]) if locked.any() else np.inf
i2, i4 = int(np.argmin(np.abs(Kds - 2.0))), int(np.argmin(np.abs(Kds - 4.0)))
lag_an2, lag_an4 = np.arcsin(Om0 / Kds[i2]), np.arcsin(Om0 / Kds[i4])
print(f"  {'K_d':>5} | {'slip':>6} | {'offset':>7} | arcsin(Om/Kd)")
for kd, s, o in zip(Kds, slips, offs):
    an = f"{np.arcsin(Om0/kd):7.3f}" if kd >= Om0 else "   --  "
    print(f"  {kd:5.2f} | {s:6.3f} | {o:7.3f} | {an}")
c3 = (0.8 <= onset <= 1.35) and abs(offs[i2] - lag_an2) < 0.06 \
     and abs(offs[i4] - lag_an4) < 0.06
print(f"  lock onset at K_d ~ {onset:.2f} (predicted {Om0}; the pair's law "
      f"would say {Om0/2} -- one-way means no factor 2)")
print(f"  -> {'PASS' if c3 else 'FAIL'}")

# ================= Check 4: registering the deviation =================
print("\nCheck 4 -- relation-detector: FOLLOWING is bandwidth-priced (by the "
      "PEAK rate), SETTLING registers the deviation")
dw = 1.0                                      # pair Kc = 0.5
Ks = np.linspace(0.05, 0.95, 10)
res4 = {}
for kd4 in (0.8, 3.0):                        # below dw / above dw + 2K
    Rf, Rs = [], []
    for kk in Ks:
        TH4, THD4 = simulate(kk, om=(0.5, -0.5), Kd=kd4, relation=True,
                             noise=0.03, T=400.0, seed=7)
        target = (TH4[:, 0] - TH4[:, 1]) % (2 * np.pi)
        Rf.append(circ_R(target - THD4))      # tracks its target?
        Rs.append(circ_R(THD4))               # detector-local: has it frozen?
    res4[kd4] = (np.array(Rf), np.array(Rs))
def flip_at(Ks, R, thr):
    for i in range(1, len(Ks)):
        if R[i] >= thr > R[i - 1]:
            t = (thr - R[i - 1]) / (R[i] - R[i - 1])
            return float(Ks[i - 1] + t * (Ks[i] - Ks[i - 1]))
    return np.inf
print(f"  {'K':>5} | {'Rf(0.8)':>8} {'Rs(0.8)':>8} | {'Rf(3.0)':>8} {'Rs(3.0)':>8}")
for i, kk in enumerate(Ks):
    print(f"  {kk:5.2f} | {res4[0.8][0][i]:8.3f} {res4[0.8][1][i]:8.3f} | "
          f"{res4[3.0][0][i]:8.3f} {res4[3.0][1][i]:8.3f}")
drift = Ks <= 0.45
K_settle_lo = flip_at(Ks, res4[0.8][1], 0.80)
K_settle_hi = flip_at(Ks, res4[3.0][1], 0.80)
c4 = (res4[3.0][0].min() > 0.9                       # wideband follows ALWAYS
      and res4[0.8][0][drift].max() < 0.7            # narrowband can't (peak rate > K_d)
      and abs(K_settle_lo - 0.5) < 0.1 and abs(K_settle_hi - 0.5) < 0.1)
print(f"  wideband (K_d=3.0 > dw+2K): follows everywhere (min R_follow = "
      f"{res4[3.0][0].min():.3f}); narrowband (K_d=0.8 < dw): never follows the "
      f"drifting pair (max R_follow = {res4[0.8][0][drift].max():.3f} in drift)")
print(f"  BOTH settle at the deviation: K* = {K_settle_lo:.2f} and "
      f"{K_settle_hi:.2f} (predicted Kc = {dw/2}) -- a bandwidth-robust, "
      f"detector-local registration of the pair's locking event")
print(f"  -> {'PASS' if c4 else 'FAIL'}")

# ================= Check 5: reader -> participant (eps sweep) =================
print("\nCheck 5 -- the observer effect as a dial: back-coupling eps")
eps_list = [0.0, 0.3, 1.0]
te_back_eps, psi_err_eps = [], []
psi_an15 = float(np.arcsin(1.2 / (2 * 1.5)))
for e in eps_list:
    # TE emergence: live noisy channel
    THe, THDe = simulate(2.5, om=(0.6, -0.6), Kd=2.0, eps=e, noise=0.60,
                         dnoise=0.30, T=4000.0, seed=2)
    te_back_eps.append(transfer_entropy_bits(THDe, THe[:, 0]))
    # [AN] distortion: quiet locked pair, ROTATING source (lag = lever arm)
    THq, _ = simulate(1.5, om=(0.6, -0.6), Om0=1.0, Kd=2.0, eps=e,
                      noise=0.03, T=300.0, seed=9)
    psi_q = (THq[:, 0] - THq[:, 1]) % (2 * np.pi)
    psi_err_eps.append(abs(float(np.angle(np.mean(np.exp(1j * psi_q)))) - psi_an15))
print(f"  {'eps':>5} | {'TE(det->src)':>12} | {'|psi* error|':>12}")
for e, tb, pe in zip(eps_list, te_back_eps, psi_err_eps):
    print(f"  {e:5.2f} | {tb:12.4f} | {pe:12.4f}")
c5 = (abs(te_back_eps[0]) < 0.006 and psi_err_eps[0] < 0.02
      and te_back_eps[-1] > 0.015 and psi_err_eps[-1] > 0.05
      and psi_err_eps[-1] > psi_err_eps[0])
print(f"  eps=0: TE at floor, psi* exact. eps=1: TE(det->src)="
      f"{te_back_eps[-1]:.4f} (the reader is now a participant), psi* shifted "
      f"by {psi_err_eps[-1]:.3f} rad (the lag is the lever arm)")
print(f"  -> {'PASS' if c5 else 'FAIL'}")

allok = c1 and c2 and c3 and c4 and c5
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED")
print("\nVerdict: a read-only node leaves its source EXACTLY unchanged -- so")
print("verified pairs compose feed-forward into larger structures with all")
print("their [AN] math intact (isolation buys scale). The detector's own laws")
print("are derived: it locks onto a rotating source iff K_d >= Omega (one-way:")
print("no factor 2) with lag arcsin(Omega/K_d) -- bandwidth is admissibility")
print("made physical. Its certificate is the pure one-way case: MI present,")
print("TE one-directional, reverse TE a true null. A relation-detector's own")
print("state registers the pair's locking event -- following a changing world")
print("and noticing it stopped changing are different, separately-derived")
print("boundaries -- the first awareness-shaped witness. And reading becomes")
print("participation continuously with back-coupling: at eps=0 observation is")
print("free; a moving world makes it costly, because tracking lag is the lever")
print("arm of back-action.")

# ---------- plot ----------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(2, 2, figsize=(12.5, 9))
    ax[0, 0].plot(Kds, slips, "o-", color="#1f77b4", label="slip rate |<dpsi/dt>|")
    kk = np.linspace(Om0, Kds.max(), 100)
    ax[0, 0].plot(kk, np.arcsin(Om0 / kk), "--", color="#2a9d5c",
                  label="lag arcsin(Omega/K_d)  [AN]")
    ax[0, 0].plot(Kds, offs, "s", color="#2a9d5c", ms=4)
    ax[0, 0].axvline(Om0, color="gray", ls=":", label="onset K_d = Omega")
    ax[0, 0].axvline(Om0 / 2, color="#d62728", ls=":", alpha=0.6,
                     label="pair law Omega/2 (wrong here)")
    ax[0, 0].set_xscale("log"); ax[0, 0].set_xlabel("detector bandwidth K_d")
    ax[0, 0].set_title("3: one-way Adler -- lock at K_d = Omega, no factor 2",
                       fontsize=9.5)
    ax[0, 0].legend(fontsize=7.5); ax[0, 0].grid(alpha=0.3)
    ax[0, 1].plot(Ks, res4[3.0][0], "o-", color="#1f77b4",
                  label="R_follow, K_d=3.0 (wideband)")
    ax[0, 1].plot(Ks, res4[0.8][0], "o--", color="#1f77b4", alpha=0.5,
                  label="R_follow, K_d=0.8 (narrowband)")
    ax[0, 1].plot(Ks, res4[3.0][1], "s-", color="#e08a1e",
                  label="R_settle, K_d=3.0")
    ax[0, 1].plot(Ks, res4[0.8][1], "s--", color="#e08a1e", alpha=0.5,
                  label="R_settle, K_d=0.8")
    ax[0, 1].axvline(0.5, color="gray", ls=":", label="pair Kc = 0.5")
    ax[0, 1].set_xlabel("pair coupling K")
    ax[0, 1].set_title("4: following is bandwidth-priced; settling registers "
                       "the deviation at Kc", fontsize=9.5)
    ax[0, 1].legend(fontsize=7); ax[0, 1].grid(alpha=0.3)
    labels = ["MI(src;det)", "TE(src->det)", "TE(det->src)"]
    vals = [mi, te_fwd, te_back]
    cols = ["#2a9d5c", "#1f77b4", "#d62728"]
    ax[1, 0].bar(labels, vals, color=cols)
    ax[1, 0].axhline(0, color="gray", lw=0.8)
    ax[1, 0].set_yscale("symlog", linthresh=0.01)
    ax[1, 0].set_ylabel("bits (symlog)")
    ax[1, 0].set_title("2: the one-way certificate -- related, directed, and a "
                       "true null back", fontsize=9.5)
    ax[1, 0].grid(alpha=0.3, axis="y")
    ax2 = ax[1, 1]
    ax2.plot(eps_list, te_back_eps, "o-", color="#d62728", label="TE(det->src)")
    ax2.set_xlabel("back-coupling eps"); ax2.set_ylabel("TE (bits)", color="#d62728")
    ax2b = ax2.twinx()
    ax2b.plot(eps_list, psi_err_eps, "s--", color="#1f77b4", label="|psi* error|")
    ax2b.set_ylabel("pair offset error (rad)", color="#1f77b4")
    ax2.set_title("5: reader -> participant -- observation cost grows from "
                  "exactly zero", fontsize=9.5)
    ax2.grid(alpha=0.3)
    fig.suptitle("Iter 17 -- the detector: exact isolation, derived bandwidth, "
                 "a registered deviation, and the price of touching",
                 y=0.995, fontsize=11)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter17_detector.png")
    fig.tight_layout(); fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
