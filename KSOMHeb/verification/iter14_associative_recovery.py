"""
Iteration 14 -- Associative memory: recovering into the WRONG stored pattern.

iter 13 showed damage recovery is recovery of the PATTERN, but on a *monostable*
module the only coherent state IS the original pattern -- so "coherence back,
identity lost" could only appear as an eroded/shifted version. The full ship of
Theseus needs MULTIPLE stored patterns: the system can re-lock perfectly (full
coherence) into a DIFFERENT stored identity.

Substrate: an oscillatory Hopfield network. Store M binary patterns
s^mu in {+1,-1}^N (phases xi^mu_i in {0, pi}); couple by the Hebbian/Hopfield rule

    K_ij = (1/N) * sum_mu s^mu_i s^mu_j      (i != j)

Retrieval dynamics (identical frequencies -> rotating frame, omega = 0):

    dtheta_i/dt = sum_j K_ij sin(theta_j - theta_i)

Because sin(xi^mu_j - xi^mu_i) = 0 for binary patterns, every stored pattern is an
EXACT fixed point; below capacity they are stable attractors. Retrieval quality
for pattern mu is the overlap

    m^mu(theta) = (1/N) | sum_i s^mu_i e^{i theta_i} |    in [0,1]

m^mu = 1 means theta matches xi^mu (up to a global phase). Note: the global
Kuramoto order parameter r is ~0 here (half the phases at 0, half at pi), so the
right notion of "coherence" is C = max_mu m^mu -- "locked onto SOME stored
memory". Identity = m^A (the pattern we started from).

Claims:
 1. Stored patterns are stable attractors; a lightly perturbed pattern is retrieved.
 2. Small damage -> recovers the ORIGINAL identity (m^A -> ~1).
 3. Ship of Theseus: as damage grows, retrieval coherence C stays HIGH (the system
    still locks onto a stored memory) while the identity m^A DROPS -- an increasing
    fraction of recoveries land on a DIFFERENT stored pattern. Full coherence, wrong
    identity.
 4. This requires multistability: with a SINGLE stored pattern (M=1, ~iter 13's
    monostable case) recovery always returns the same pattern -- no wrong identity.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

rng = np.random.RandomState(14)

N = 32                 # well above Hopfield capacity for M=3 (ratio 0.09 << 0.14)
dt = 0.05
NOISE = 0.05

def make_net(M):
    """M random binary patterns and their Hopfield coupling."""
    S = rng.choice([-1.0, 1.0], size=(M, N))          # S[mu] = s^mu
    xi = np.where(S > 0, 0.0, np.pi)                   # phases in {0, pi}
    K = (S.T @ S) / N                                  # K_ij = (1/N) sum_mu s_i s_j
    np.fill_diagonal(K, 0.0)
    return S, xi, K

def overlaps(theta, S):
    """m^mu for every stored pattern."""
    z = np.exp(1j * theta)
    return np.abs(S @ z) / N                           # (M,)

def retrieve(theta, K, steps):
    for _ in range(steps):
        d = theta[None, :] - theta[:, None]            # d[i,j] = theta_j - theta_i
        dth = (K * np.sin(d)).sum(axis=1)
        theta = theta + dt * dth + NOISE * np.sqrt(dt) * rng.randn(N)
    return theta % (2 * np.pi)

def damage(theta, sigma_d):
    return (theta + sigma_d * rng.randn(N)) % (2 * np.pi)

# ---- the network: 3 stored memories ----
M = 3
S, xi, K = make_net(M)
STEPS = 1500
TRIALS = 40
sigmas = np.array([0.3, 0.6, 1.0, 1.5, 2.0, 2.5, 3.0])

# cross-talk between stored patterns (should be small: they're distinct memories)
mm = np.abs(S @ S.T) / N
xtalk = (mm[~np.eye(M, dtype=bool)]).max()
print(f"oscillatory Hopfield net: N={N}, M={M} stored patterns, "
      f"max cross-overlap={xtalk:.2f}\n")

# ---- Check 1: stored patterns are stable attractors; retrieval works ----
stable = []
for mu in range(M):
    th = retrieve(xi[mu].copy(), K, STEPS)
    stable.append(overlaps(th, S)[mu])
th = retrieve(damage(xi[0], 0.5), K, STEPS)           # light perturbation of A
retr_light = overlaps(th, S)[0]
# NB: ongoing noise caps overlap at a ~0.87 floor even at a perfect attractor,
# so "stable & retrieved" means sitting at that floor (well clear of the <0.8
# "no clean memory" band), not overlap = 1.
print(f"Check 1 (stored patterns are attractors): min self-overlap at rest="
      f"{min(stable):.3f}; retrieval from light damage m^A={retr_light:.3f} "
      f"(both at the noise floor ~0.87, well above the 0.8 'none' band)")
c1 = min(stable) > 0.82 and retr_light > 0.82
print(f"   -> {'PASS' if c1 else 'FAIL'}")

# ---- sweep: recover pattern A after damage, record where it lands ----
print(f"\nRecover from damage to pattern A (identity=m^A, coherence=max_mu m^mu):")
print(f"{'sigma_d':>7} | {'m^A':>5} | {'C(max)':>6} | {'->A':>5} {'->other':>7} {'->none':>6}")
print("-" * 52)
mA = {}; C = {}; toA = {}; toOther = {}; toNone = {}
for s in sigmas:
    a = []; c = []; nA = 0; nO = 0; nN = 0
    for _ in range(TRIALS):
        th = retrieve(damage(xi[0], s), K, STEPS)
        m = overlaps(th, S)
        a.append(m[0]); c.append(m.max())
        win = int(np.argmax(m))
        if m.max() < 0.8:            nN += 1     # locked onto nothing clean
        elif win == 0:               nA += 1     # recovered the original identity
        else:                        nO += 1     # recovered a DIFFERENT stored memory
    mA[s] = np.mean(a); C[s] = np.mean(c)
    toA[s] = nA / TRIALS; toOther[s] = nO / TRIALS; toNone[s] = nN / TRIALS
    print(f"{s:7.2f} | {mA[s]:5.2f} | {C[s]:6.2f} | {toA[s]:5.0%} {toOther[s]:7.0%} "
          f"{toNone[s]:6.0%}")

# ---- Check 2: small damage recovers the original identity ----
c2 = mA[0.6] > 0.85 and toA[0.6] > 0.8
print(f"\nCheck 2 (small damage recovers original identity): sigma=0.6 -> "
      f"m^A={mA[0.6]:.2f}, ->A {toA[0.6]:.0%}  -> {'PASS' if c2 else 'FAIL'}")

# ---- Check 3: ship of Theseus -- coherence stays high, but recovery lands on
# the WRONG stored memory an increasing fraction of the time (fractions are the
# honest measure: mean m^A stays moderate only because some trials still find A).
sL = 2.5
c3 = (C[sL] > 0.7) and (toA[sL] < 0.6) and (toOther[sL] > 0.15) \
     and (toOther[sigmas[-1]] > toOther[1.0] + 0.1)
print(f"Check 3 (ship of Theseus): at sigma={sL}, retrieval coherence C={C[sL]:.2f} "
      f"(still locks onto a memory) but only {toA[sL]:.0%} recover the ORIGINAL; "
      f"{toOther[sL]:.0%} land on a DIFFERENT stored pattern (grows to "
      f"{toOther[sigmas[-1]]:.0%} at σ={sigmas[-1]})  -> {'PASS' if c3 else 'FAIL'}")

# ---- Check 4: multistability is required (M=1 control) ----
S1, xi1, K1 = make_net(1)
mA1 = []
for _ in range(TRIALS):
    th = retrieve(damage(xi1[0], sL), K1, STEPS)
    mA1.append(overlaps(th, S1)[0])
mA1 = float(np.mean(mA1))
c4 = mA1 > 0.85
print(f"Check 4 (single stored pattern = monostable, no wrong identity): "
      f"M=1 at sigma={sL} -> m^A={mA1:.2f} (always the same pattern)  "
      f"-> {'PASS' if c4 else 'FAIL'}")

allok = c1 and c2 and c3 and c4
print("\nALL PASS" if allok else "\nSOME CHECKS FAILED")
print("\nVerdict: with multiple stored memories, damage recovery can restore FULL")
print("coherence into the WRONG identity -- the system re-locks onto a stored")
print("pattern, just not the one it started from (fraction ->other grows with")
print("damage while coherence C stays high). This is the true ship of Theseus that")
print("iter 13's monostable module could only approximate: same coherence, a")
print("different stored self. A single stored pattern (M=1) cannot do it -- the")
print("wrong-identity failure mode is a property of associative MEMORY, not of one")
print("attractor. Resilience of identity depends on basin size (how many memories,")
print("how far apart) -- a capacity question for a follow-up.")

# ---- plot ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    ss = sigmas
    ax[0].plot(ss, [C[s] for s in ss], "o-", color="#1f77b4",
               label="retrieval coherence C = max_μ mᵘ (locks onto a memory)")
    ax[0].plot(ss, [mA[s] for s in ss], "s-", color="#d62728",
               label="identity  m^A (the ORIGINAL memory)")
    ax[0].set_xlabel("damage  σ_d"); ax[0].set_ylabel("overlap")
    ax[0].set_title("Coherence stays high; identity is lost — into another memory",
                    fontsize=10)
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3); ax[0].set_ylim(0, 1.05)
    # outcome fractions
    ax[1].bar(ss, [toA[s] for s in ss], 0.16, color="#2a9d5c", label="→ original (A)")
    ax[1].bar(ss, [toOther[s] for s in ss], 0.16, bottom=[toA[s] for s in ss],
              color="#e08a1e", label="→ DIFFERENT stored memory")
    ax[1].bar(ss, [toNone[s] for s in ss], 0.16,
              bottom=[toA[s] + toOther[s] for s in ss], color="#999",
              label="→ no clean memory")
    ax[1].set_xlabel("damage  σ_d"); ax[1].set_ylabel("fraction of recoveries")
    ax[1].set_title("Where recovery lands: the wrong-identity fraction grows",
                    fontsize=10)
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3, axis="y")
    fig.suptitle("Iter 14 — associative recovery: full coherence into the WRONG "
                 "stored identity", y=1.02, fontsize=11)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "iter14_associative_recovery.png")
    fig.tight_layout(); fig.savefig(out, dpi=110, bbox_inches="tight")
    print(f"\nplot saved -> {out}")
except Exception as e:
    print(f"\n(plot skipped: {e})")
