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
| `iter4_reward_modes.py` | **Modular "memory" claim.** Two hidden frequency clusters; do global / local / hybrid reward recover them in K? Reward mode is ~irrelevant (contrast spread 0.016 — it cancels from the within/cross ratio); S==1 ablation flattens contrast to 1.0; and the dynamics **fail to recover the modules** — self-entrainment inflates cross-synchrony (isolated 0.16 → coupled 0.34–0.85) until the clusters merge into one module (learned Q ≤ 0.05 vs Q = 0.50 for the true partition) | passing (claim refuted) |
| `iter5_competition_rescue.py` | **The rescue.** Per-PAIR synchrony-gated reward (R_ij = S_ij − thr) recovers the modules where per-node reward could not (contrast 1.24 → 2.16, Q 0.045 → 0.156) — per-pair credit does not cancel. Coupling competition (synaptic normalization) is inert alone (1.24) but amplifies the per-pair signal to the best result (contrast 3.32, Q 0.262). Modularity IS achievable, with ingredients the doc omits | passing (claim rescued) |
| `iter6_locking_threshold.py` | **A derived coherence threshold.** Two oscillators reduce exactly to `dψ/dt = Δω − 2K sin ψ`, a saddle-node bifurcation at `Kc = \|Δω\|/2` (confirmed across detunings). Order parameter at onset is exactly `1/√2 ≈ 0.707`, so a pair locks only if `S_ij > 1/√2` — a *derived* per-pair threshold matching the hand-picked `r ≥ 0.7`. Noise smears the bifurcation. (`twoosc_entangle_demo.py` is the original seed script) | passing |

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
- **Modularity is not emergent under pure Hebbian coupling (iter4):** the doc's
  "functional networks emerge from experience" / modularity-Q metric does not
  hold as specified. Two causes, both demonstrated:
  (a) *Reward mode cancels.* A per-node reward R_i multiplies all of node i's
  links equally, so it drops out of K*_within/K*_cross = S_within/S_cross —
  global, local, and hybrid reward give the same modular contrast (~1.25). The
  only per-pair signal is S_ij (which the v1.0 S==1 bug destroyed; the ablation
  here flattens contrast to exactly 1.0).
  (b) *Self-entrainment homogenizes.* All-to-all Hebbian coupling with positive
  reward is self-reinforcing: surviving cross-links entrain the two clusters,
  raising cross-synchrony (0.16 isolated → 0.34–0.85 coupled), which keeps the
  cross-links alive. The system merges toward ONE module (or collapses, per the
  decay-rate bistability seen in the sweep) instead of splitting into two.
  Implication for CPAF: do not treat modularity Q as an emergent given.
  Recovering pre-existing modules needs an ingredient the doc omits — coupling
  competition/normalization, a distance or anti-Hebbian term, or genuinely
  per-pair reward. (Architecture doc modularity caveat should be upgraded from
  "open question" to "refuted as specified, rescuable"; pending sign-off.)
- **Modularity IS recoverable with per-pair credit (iter5):** replacing the
  per-node reward with a per-PAIR synchrony-gated reward R_ij = S_ij − thr
  breaks the cancellation (low-synchrony cross links fall below threshold and
  decay), lifting contrast 1.24 → 2.16 and Q 0.045 → 0.156. Coupling
  competition (synaptic normalization) does nothing on its own (it needs a
  per-pair signal to sharpen) but amplifies the per-pair reward to the best
  result (contrast 3.32, Q 0.262). So the doc's modular-memory ambition is
  reachable — but only with per-pair credit assignment and, ideally,
  competition; neither is in the v1.0 spec.
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
