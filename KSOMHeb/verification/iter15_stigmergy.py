"""
Iteration 15 -- Stigmergy: coordination through a shared, persistent medium.

Stigmergy is indirect coordination: agents do not signal each other directly;
they WRITE a shared, persistent, modifiable medium (deposit), and the medium
STEERS who acts next (sense). Ants + pheromone. The medium is external memory.

This witnesses stigmergy in the K-SOM-Heb family and, crucially, gives it an
operational fingerprint using the iter-8 certificate machinery. Where iter 8's
hidden variable Z was a *confounder* (a←Z→b, a common cause), a stigmergic medium
M is a *mediator* (a→M→b, a shared pathway). Both are third variables conditional
TE handles -- opposite causal roles.

Model. Agents are phase oscillators theta_i (heterogeneous omega_i). A persistent
complex medium M (the "pheromone") accumulates their deposit and evaporates:

    dM/dt = a * (1/N) sum_j e^{i theta_j}   -   gamma * M          (deposit - evaporation)

Agents sense ONLY the medium (no direct theta_i-theta_j coupling):

    dtheta_i/dt = omega_i + K * |M| * sin(arg(M) - theta_i) + noise

Positive feedback (aligned agents build a coherent M, which pulls harder) with
evaporation gamma as the leak. |M|_eq ~ (a/gamma) * r, so gamma controls whether
the trail persists.

Claims:
 1. Stigmergic coordination: with a persistent medium (low gamma) the agents
    synchronize THROUGH it, with no direct coupling -- r rises well above the
    medium-free drift baseline.
 2. The null state is MEDIUM-RELATIVE: raise evaporation (gamma) so the trail
    cannot persist and the agents fall back to their default drift/"search"
    regime (r ~ the uncoupled baseline). No trail -> search null.
 3. Stigmergy fingerprint (screening-off): between two agents through the medium,
    TE(1->2) > 0 but TE(1->2 | M) collapses -- conditioning on the medium removes
    the apparent direct influence, because the medium IS the pathway.
 4. Direct vs mediated (directional dissociation): add a direct theta_1-theta_2
    edge and more transfer SURVIVES conditioning on M (22% of raw vs 14% for the
    pure-mediated case) -- a real edge is not (fully) screened. The margin is
    modest and honest: in this minimal 2-oscillator substrate a strong medium's
    phase tracks the agents' closely, so conditioning on M also absorbs much of a
    direct edge. A crisp double dissociation needs a medium clearly distinct from
    the agents (e.g. a spatial pheromone FIELD) -- a follow-up.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

rng = np.random.RandomState(15)

# ---------- estimators (as in iter 8) ----------
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

def order_param(TH):                      # TH: (n_samples, N) or (N,)
    return np.abs(np.mean(np.exp(1j * TH), axis=-1))

# ---------- simulator: agents + persistent medium ----------
def simulate(N, gamma, K=2.0, a=1.5, direct=0.0, noise=0.05, omega=None,
             T=500.0, dt=0.02, sub=8, burn=4000, seed=0):
    r = np.random.RandomState(seed)
    if omega is None:                     # rotating frame: small detunings, no fast
        omega = 0.4 * np.linspace(-1, 1, N)   # common rotation (else the slow medium
        #                                        averages a fast-spinning deposit to ~0)
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
        if direct:                        # optional DIRECT coupling (control)
            d = th[None, :] - th[:, None]
            dth = dth + direct * np.sin(d).mean(axis=1)
        th = (th + dt * dth + amp * r.randn(N)) % (2 * np.pi)
        if k >= burn and (k - burn) % sub == 0:
            TH.append(th.copy()); ARGM.append(argM % (2 * np.pi)); ABSM.append(absM)
    return np.array(TH), np.array(ARGM), np.array(ABSM)

# ================= Part A: coordination & the medium-relative null =================
print("Part A -- stigmergic coordination and the medium-relative null (N=6):")
print(f"{'gamma':>6} | {'|M|':>5} | {'r_agents':>8} | regime")
print("-" * 46)
gammas = [0.2, 0.5, 1.0, 2.0, 4.0, 8.0]
rA = {}
for g in gammas:
    TH, ARGM, ABSM = simulate(6, g, seed=1)
    r_mean = float(order_param(TH).mean()); m_mean = float(ABSM.mean())
    rA[g] = r_mean
    reg = "coordinated (on trail)" if r_mean > 0.75 else \
          "search / drift (no trail)" if r_mean < 0.55 else "partial"
    print(f"{g:6.1f} | {m_mean:5.2f} | {r_mean:8.3f} | {reg}")
# medium-free baseline (K=0: agents ignore the medium -> pure drift)
TH0, _, _ = simulate(6, 1.0, K=0.0, seed=1)
r_drift = float(order_param(TH0).mean())
print(f"medium-free drift baseline (K=0): r = {r_drift:.3f}")

c1 = rA[min(gammas)] > 0.75
c2 = rA[max(gammas)] < rA[min(gammas)] - 0.2 and rA[max(gammas)] < r_drift + 0.15
print(f"\nCheck 1 (coordination through the medium): low gamma={min(gammas)} -> "
      f"r={rA[min(gammas)]:.3f} (no direct coupling)  -> {'PASS' if c1 else 'FAIL'}")
print(f"Check 2 (null is medium-relative): high gamma={max(gammas)} -> "
      f"r={rA[max(gammas)]:.3f} ~ drift baseline {r_drift:.3f} (trail can't persist "
      f"-> fall back to search)  -> {'PASS' if c2 else 'FAIL'}")

# ================= Part B: the stigmergy fingerprint (screening-off) =================
print("\nPart B -- stigmergy fingerprint: does conditioning on the medium screen "
      "off the apparent edge? (N=2)")
om2 = np.array([0.6, -0.6])          # detuned enough to stay PARTIALLY coupled
# (full lock makes the pair redundant and TE->0, iter 11; we want a live channel)
# two agents coordinating ONLY through the medium (no direct edge)
TH, ARGM, ABSM = simulate(2, 1.0, K=2.5, direct=0.0, noise=0.60, omega=om2,
                          T=4000.0, dt=0.02, sub=5, seed=2)
th1, th2 = TH[:, 0], TH[:, 1]
r_stig = float(order_param(TH).mean())
te12 = transfer_entropy_bits(th1, th2)
te12_M = transfer_entropy_bits(th1, th2, z=ARGM)
frac_stig = te12_M / te12 if te12 > 1e-6 else 0.0
print(f"  stigmergic (medium only, r_pair={r_stig:.2f}): TE(1->2)={te12:.4f}  "
      f"TE(1->2|M)={te12_M:.4f}  (M-conditioned is {frac_stig:.0%} of raw)")

# control: BOTH a medium path AND a genuine direct edge. Conditioning on M should
# remove the mediated part but leave the direct part -- so TE(1->2|M) survives,
# and clearly higher than the medium-only case. (A K=0 "direct-only" control is
# unsound: with no sensing, M is a common EFFECT/collider of the two agents, so
# conditioning on it is not neutral.)
THd, ARGMd, _ = simulate(2, 1.0, K=2.5, direct=0.6, noise=0.60, omega=om2,
                         T=4000.0, dt=0.02, sub=5, seed=2)
td1, td2 = THd[:, 0], THd[:, 1]
r_dir = float(order_param(THd).mean())
ted12 = transfer_entropy_bits(td1, td2)
ted12_M = transfer_entropy_bits(td1, td2, z=ARGMd)
frac_dir = ted12_M / ted12 if ted12 > 1e-6 else 0.0
print(f"  medium + DIRECT edge (r_pair={r_dir:.2f}):   TE(1->2)={ted12:.4f}  "
      f"TE(1->2|M)={ted12_M:.4f}  (M-conditioned is {frac_dir:.0%} of raw)")

c3 = te12 > 0.015 and frac_stig < 0.45
c4 = ted12_M > 0.008 and ted12_M > 1.5 * te12_M   # direct leaves clearly more residual
print(f"\nCheck 3 (screening-off = stigmergy): conditioning on M collapses the "
      f"apparent edge ({frac_stig:.0%} of raw remains)  -> {'PASS' if c3 else 'FAIL'}")
print(f"Check 4 (a real edge is NOT screened): with a direct edge added, "
      f"TE(1->2|M)={ted12_M:.4f} survives (vs {te12_M:.4f} for medium-only) "
      f"-> {'PASS' if c4 else 'FAIL'}")

allok = c1 and c2 and c3 and c4
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED")
print("\nVerdict: agents coordinate through a shared, persistent, agent-written")
print("medium with NO direct coupling -- stigmergy. Its fingerprint is the")
print("screening-off certificate: TE(a->b) is real but collapses once you")
print("condition on the medium (the medium is the pathway), whereas a genuine")
print("direct edge leaves more residual -- the mediator/edge dissociation (modest")
print("here: this minimal medium tracks the phase, so a spatial-field substrate")
print("would sharpen it), the mirror of iter 8's confounder case. And the null is")
print("medium-relative: strip the trail (high evaporation) and the agents decay")
print("to their default search/drift regime. Less-closed systems keep their")
print("coordination -- and their memory -- outside themselves, in the medium.")

# ---------- plot ----------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    gs = np.array(gammas)
    ax[0].plot(gs, [rA[g] for g in gammas], "o-", color="#2a9d5c",
               label="r (coordination via medium)")
    ax[0].axhline(r_drift, color="#d62728", ls="--", label="drift / search null (no medium)")
    ax[0].set_xlabel("evaporation  γ"); ax[0].set_ylabel("agent order parameter r")
    ax[0].set_title("Trail persists (low γ) → coordinate; evaporates (high γ) → search",
                    fontsize=10)
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3); ax[0].set_ylim(0, 1.05)
    labels = ["stigmergic\n(medium only)", "direct edge\n(control)"]
    xpos = np.arange(2)
    ax[1].bar(xpos - 0.2, [te12, ted12], 0.38, color="#1f77b4", label="TE(1→2)")
    ax[1].bar(xpos + 0.2, [te12_M, ted12_M], 0.38, color="#e08a1e",
              label="TE(1→2 | M)")
    ax[1].set_xticks(xpos); ax[1].set_xticklabels(labels, fontsize=9)
    ax[1].set_ylabel("transfer entropy (bits)")
    ax[1].set_title("Conditioning on M screens the mediated edge, not the direct one",
                    fontsize=10)
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3, axis="y")
    fig.suptitle("Iter 15 — stigmergy: coordination (and memory) held in a shared "
                 "medium", y=1.02, fontsize=11)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter15_stigmergy.png")
    fig.tight_layout(); fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
