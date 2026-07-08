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
| `iter7_information_transition.py` | **Deviation creates information; coherence ≠ information.** Mutual information between two noisy phases climbs from ~0.05 bits (deep drift) to ~2.7 bits (locked) across `Kc` — a deviation *creates* shared information (an operational measure for CPAF's "information"). Meanwhile `r` is already 66% of its max deep in the drift regime while MI is 2% — `r` overreads relationship where none persists, so **coherence is not information** (Ch 6 seam #1, demonstrated) | passing |
| `iter8_transfer_entropy.py` | **Interaction vs common cause.** Three causal graphs (coupled 1↔2, common-driven Z→1,Z→2 with zero coupling, one-way 1→2) carry the same MI (1.89/1.51/1.90 bits) — MI is graph-blind. Transfer entropy `TE(X→Y)=I(Y_{t+τ};X_t\|Y_t)` resolves direction (one-way: TE(1→2)=0.16, TE(2→1)=−0.001 — a true null) but is *also* fooled by the hidden common drive (0.036 vs coupled 0.047 — genuine predictive transfer over a nonexistent edge; prediction ≠ causation). Conditional TE\|Z gives a double dissociation: kills the spurious transfer (−0.004), leaves the real edge untouched (0.049). Ladder: related (MI) < directed (TE) < connected (TE\|confounders) | passing |
| `iter10_grown_entities.py` | **The splice: grown modules are entities.** Grow modules with iter-5's machinery verbatim (per-pair reward + competition; reproduces contrast 3.32, Q +0.262), freeze K, and run iter-9's entity criteria unadjusted, predicting from the grown module's *measured* ω̄ and ρ: one clock per module (velocity spread 0.0002 vs natural 0.12); entrainment thresholds within 2.5% of `κc=\|Δω\|/(2ρ)`; the 1/√2 branch to 0.004. **Closure is a boundary detector:** on the same noisy trajectory, the grown boundary reads 0.005 bits of member→Θ leakage while an arbitrary boundary (15+15 across modules) leaks 0.284 bits — 50–60×. Bonus: first entity-to-entity macro channel, TE(Θ_B→Θ_A\|Θ_A)=0.013 bits through grown cross-links. (Expected in-situ leak from module B: below estimator floor — reported, not confirmed) | passing |
| `iter9_entity_as_cluster.py` | **Entity-as-cluster (the CPAF recursion).** Coarse-grain a 5-member cluster to its mean phasor (Θ, ρ). A *locked* cluster passes every entity criterion: one shared frequency (member velocity spread 0.0% of natural); entrains to an external probe exactly per iter 6 with effective coupling **K_eff = κρ** — empirical thresholds within 2.5% of `κc=\|Δω\|/(2ρ)`, and a mid-coherence cluster (ρ=0.92) sides with the ρ-corrected prediction over naive `\|Δω\|/2`; the measured locked branch matches `R=cos(½ arcsin(Δω/2ρκ))` (floor 1/√2) to 0.016; and **macro closure** holds — TE(member→Θ\|Θ)=0.002 bits vs 0.027 for an unlocked collection and 0.106 for a genuine external influence (control). An unlocked collection fails all criteria: entity-hood is *created* by the locking transition | passing |

## Findings log

- **Grown modules are entities, and closure finds the boundary (iter10):**
  iter-5's learned modules pass all four iter-9 entity criteria with nothing
  adjusted — the reduction's cancellation needs only *symmetry* of K, so the
  pair law covers heterogeneous learned coupling blocks, and it does
  (thresholds to 2.5% from measured ρ). The sharper result: closure TE
  separates the grown boundary from an arbitrary boundary through the same
  trajectory by 50–60× (0.005 vs 0.284 bits) — the entity criteria can
  *locate* boundaries, not just grade them. Also the first entity-to-entity
  macro information channel (0.013 bits). Caveats: seeded structure, one
  growth seed, K frozen during tests, detector is proof-of-concept (no blind
  search yet).
- **A cluster's coupling to the world is discounted by its internal coherence
  (iter9):** for a locked cluster, the macro-phase obeys the two-oscillator
  equation with `K_eff = κρ` (derived by averaging: internal terms cancel by
  antisymmetry; the offset spread collapses to the factor ρ), so the
  entrainment threshold is `κc = |Δω|/(2ρ)` — confirmed to 2.5%, with the ρ
  discount itself resolved against the naive law. Macro noise shrinks by √M.
  Macro closure (TE(member→Θ|Θ) ≈ 0) appears at the same locking transition
  that creates the shared frequency — entities, like deviations and
  information, are born at the bifurcation. Methods note: don't point-sample
  a steep branch — "R at onset = 1/√2" fails at any finite grid point (theory
  itself predicts ~0.80 at the first locked sample); check the whole branch
  curve instead.
- **Pairwise TE is prediction, not causation (iter8):** a hidden common driver
  produces *genuine* transfer entropy between two uncoupled oscillators (each
  is a second noisy sensor of the source, so one really does help predict the
  other) — pairwise TE cannot certify an edge, only conditional TE (given the
  confounder) can, and it does so cleanly (double dissociation: spurious
  transfer dies, real edge unaffected). Directionality, by contrast, comes
  free: the no-influence direction of a one-way coupling reads statistically
  zero. Estimator caveat caught during tuning: the **conditioning variable
  must be binned finely** — coarse `Y_t` bins let the correlated source
  re-supply the discarded sub-bin information and read as 0.11 bits of phantom
  transfer (fine bins: 0.000).
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
