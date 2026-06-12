# K-SOM-Heb verification suite

Each script checks one claim of the architecture against either known theory or
the architecture's own stated properties. Run any of them directly with
`python3 <script>.py` (needs `numpy`; plots need `matplotlib`).

| Script | What it checks | Status |
|--------|----------------|--------|
| `verify_bugs.py` | Reproduces the four v1.0 bugs (S ≡ 1, per-step spatial blend, invalid entropy, etc.) | the bugs, demonstrated |
| `verify_fixes.py` | Confirms the v1.1 corrected update: coupling adapts, stays bounded, synchrony varies, entropy well-defined | passing |
| `iter1_kuramoto_transition.py` | **Foundation.** Base (fixed-coupling) dynamics reproduce the Kuramoto synchronization transition; empirical Kc matches mean-field theory Kc = 2σ√(2/π) ≈ 1.596σ | passing (Kc_emp ≈ 1.60) |
| `iter2_hebbian_fixed_point.py` | **Hebbian rule in isolation** (phases frozen). Each pair relaxes exponentially to its own fixed point K* = ηSR/λ, matching the closed-form trajectory to ~1e-6; clamps at K_max; negative reward floors synced pairs while S=0 pairs decay passively | passing |
| `iter3_closed_loop.py` | **Closed loop** (phases + coupling + live reward R = r − r_baseline). Bistability predicted by the positive-feedback structure and confirmed: supercritical start → runaway to 100% K_max saturation (r 0.88→0.97 vs fixed control); subcritical start → coupling stripped to 0 and sync lost (r 0.14→0.10). Plasticity P spikes during the transition and → 0 at either steady state | passing |

## Findings log

- **Saturation bound (iter2):** the doc's heuristic parameters give gain
  η/λ = 10, so K* = 10·S·R. Any *sustained* reward above
  `R_sat = K_max·λ/η = 0.2` drives well-synced pairs into the K_max clamp,
  where the synchrony gradient is erased (S=0.98 and S=0.36 pairs both read
  2.0 — coupling stops being informative). Operate with sustained R below
  R_sat, or retune η/λ. Found because iteration 2's first run used R = 1 and
  saturated nearly everything.
- **Pure-Hebbian asymmetry (iter2, by design):** negative reward only punishes
  pairs that are *synchronized*; zero-synchrony pairs feel no reward signal at
  all and just decay on timescale τ = 1/λ. Forgetting is decay, not repulsion.
- **Global reward is bistable, not regulating (iter3):** R = r − r_baseline
  closes a positive feedback loop (coupling → sync → reward → coupling).
  Start above the separatrix and the system runs away until *every* pair sits
  at K_max (a fully saturated, uninformative coupling matrix — the iter2
  saturation bound realized in closed loop); start below it and coupling is
  stripped to zero and synchrony collapses. The doc's v1.1 caveat
  ("winner-take-all or collapse, not modularity") is now demonstrated, not
  just argued. Consequences: (a) the steady state of K under pure global
  reward carries ~no pairwise information — memory claims need heterogeneous
  input or local reward; (b) anything homeostatic needs a restoring term,
  e.g. reward shaped as a band/target (R rises when r is *near* a setpoint,
  falls when past it) rather than an unbounded "more sync is always better".

## Iteration plan

We verify bottom-up — each layer only after the one beneath it holds:

1. **Base synchronization** (done) — order parameter, fixed-coupling Kuramoto
   transition vs theory.
2. **Hebbian coupling, frozen phases** — does `dK/dt = ηSR − λK` move coupling
   toward the equilibrium `K* = ηSR/λ` as the math predicts, bounded by `K_max`?
3. **Full coupled system** — phases + coupling together: does reward-driven
   adaptation raise steady-state `r` relative to fixed coupling?
4. **Emergent-property claims** — the ones the doc still asserts on faith:
   functional modularity `Q`, memory traces in `K`, damage recovery.
