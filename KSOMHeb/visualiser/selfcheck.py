"""
Self-check for the interactive companion -- the successor of parity_check.js.

The suite's trust claim is that the labs run the SAME dynamics the
verification ledger verified. Where a lab calls ksomheb.py directly there is
nothing to check; this script covers every place a lab uses a faster or
reduced form, plus a qualitative regression of each lab's headline behaviour:

  1. ch01's O(N) mean-field stepper == ksomheb.kuramoto_step with uniform
     all-to-all coupling (exact algebraic identity, checked numerically).
  2. ch01 sweep reproduces iter 1: r low below Kc, high above.
  3. ch03 reproduces iter 3's bistability: supercritical start -> saturated
     coupling; subcritical start -> stripped coupling. (Direct ksomheb calls.)
  4. ch07 reduced sweep: empirical locking onset at Kc = |dw|/2 and
     coherence ~ 1/sqrt(2) at onset (iter 6's checks 2-3, coarse grid).

Run:  python3 selfcheck.py   -> PASS/FAIL per check, exit code 0 iff all pass.
"""
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from ksomheb import kuramoto_step  # noqa: E402
from labs import ch01_kuramoto_transition as ch01  # noqa: E402
from labs import ch03_closed_loop as ch03  # noqa: E402
from labs import ch07_locking_threshold as ch07  # noqa: E402

results = []


def check(name, ok, detail=""):
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


# ---- 1. mean-field stepper parity vs ksomheb.kuramoto_step ----
rng = np.random.RandomState(0)
N = 64
theta_a = rng.uniform(0, 2 * np.pi, N)
theta_b = theta_a.copy()
omega = rng.normal(0, 1.0, N)
K = 1.7
Kmat = np.full((N, N), K)
np.fill_diagonal(Kmat, 0.0)
worst = 0.0
for _ in range(200):
    theta_a = ch01._meanfield_step(theta_a, omega, K, 0.05)
    theta_b = kuramoto_step(theta_b, omega, Kmat, 0.05)
    worst = max(worst, float(np.abs(theta_a - theta_b).max()))
check("ch01 mean-field stepper == ksomheb.kuramoto_step (uniform K)",
      worst < 1e-9, f"max |Δθ| over 200 steps = {worst:.2e}")

# ---- 2. ch01 sweep shows the transition around Kc ----
out = ch01.run({"mode": "sweep", "N": 200, "sigma": 1.0, "seed": 42})
Ks = np.array(out["sweep"]["Ks"])
r = np.array(out["sweep"]["r"])
Kc = out["Kc_theory"]
r_below = r[Ks < 0.7 * Kc].max()
r_above = r[Ks > 1.5 * Kc].min()
check("ch01 sweep: incoherent below Kc, synchronized above",
      r_below < 0.3 and r_above > 0.6,
      f"max r below 0.7·Kc = {r_below:.3f}, min r above 1.5·Kc = {r_above:.3f}")

# ---- 3. ch03 bistability (iter 3, shortened) ----
base = {"N": 60, "steps": 12000, "control": False, "seed": 11}
hi = ch03.run({**base, "K0": 1.2})
lo = ch03.run({**base, "K0": 0.4})
check("ch03 supercritical start -> runaway (coupling saturates)",
      hi["fracSat"][-1] > 0.5 and hi["meanK"][-1] > 1.2,
      f"fracSat={hi['fracSat'][-1]:.2f}, meanK={hi['meanK'][-1]:.2f}")
check("ch03 subcritical start -> collapse (coupling stripped)",
      lo["meanK"][-1] < 0.1 * 0.4 and lo["r"][-1] < 0.3,
      f"meanK={lo['meanK'][-1]:.4f}, r={lo['r'][-1]:.3f}")

# ---- 4. ch07 threshold and the 1/sqrt(2) onset ----
out = ch07.run({"mode": "sweep", "dw": 0.19, "T": 400, "seed": 7})
Ks = np.array(out["sweep"]["Ks"])
R0 = np.array(out["sweep"]["curves"]["0"])
Kc = out["Kc"]
locked = Ks[R0 > 1 / np.sqrt(2) - 5e-3]
Kc_emp = locked[0] if len(locked) else np.nan
grid = Ks[1] - Ks[0]
check("ch07 noise-free onset at Kc = |Δω|/2",
      abs(Kc_emp - Kc) < 2 * grid, f"Kc_emp={Kc_emp:.4f}, Kc={Kc:.4f}")
bKs = np.array(out["branch"]["Ks"])
bR = np.array(out["branch"]["R"])
check("ch07 analytic branch starts at R(Kc) = 1/√2",
      abs(bR[0] - 1 / np.sqrt(2)) < 1e-3 and abs(bKs[0] - Kc) < 1e-6,
      f"R(Kc) = {bR[0]:.4f}")
mask = Ks > 1.2 * Kc
R_branch = np.interp(Ks[mask], bKs, bR)
worst = float(np.abs(R0[mask] - R_branch).max())
check("ch07 empirical locked-side R matches analytic branch",
      worst < 0.02, f"max |ΔR| for K > 1.2·Kc = {worst:.4f}")

# ---- 5. ch07 probe agrees with prediction on both sides ----
drift_lo = ch07.run({"mode": "probe", "dw": 0.19, "K": 0.5 * 0.095,
                     "T": 300, "seed": 7})["probe"]["drift"]
drift_hi = ch07.run({"mode": "probe", "dw": 0.19, "K": 2.0 * 0.095,
                     "T": 300, "seed": 7})["probe"]["drift"]
check("ch07 probe: drifts below Kc, locks above",
      drift_lo > 0.02 and drift_hi < 1e-3,
      f"drift(0.5·Kc)={drift_lo:.4f}, drift(2·Kc)={drift_hi:.2e}")

print()
if all(results):
    print("ALL PASS")
    sys.exit(0)
print("SOME CHECKS FAILED")
sys.exit(1)
