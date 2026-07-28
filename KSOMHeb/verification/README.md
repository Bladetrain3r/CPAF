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
| `iter11_interaction_vs_deviation.py` | **The latent channel (interaction vs deviation).** Sweep one pair's coupling through Kc. MI (deviation detector, iter 7) stays ~0 until locking; TE (interaction detector, iter 8) is nonzero for *any* K>0. They dissociate: at K/Kc=0.34, TE=0.015 bits (interaction present) while MI=0.04 (no deviation) — a **latent channel**, a real but silent edge. TE turns on (K/Kc≈0.34) before MI (≈0.53): interaction is graded, deviation is an onset. K=0 is a true null (both at floor). Bonus: TE peaks near Kc then declines (redundancy — a locked pair is its own best predictor). Grounds Ch 8's last span; hardens null=poised-not-empty | passing |
| `iter12_interaction_sign.py` | **The sign of an interaction (latent vs active).** Latent vs active interaction is a *sign problem*: the sign of the locking discriminant `Disc=1−(Δω/2K)²`. Active (Disc>0): locked offset `ψ*` is **real** — realized, a deviation, and the simulated pair settles to `Re ψ*`. Latent (Disc<0): `ψ*=π/2−i·arccosh(Δω/2K)` is **complex** — unrealized, a channel only, and the pair never settles (drifts). Threshold `Kc`=discriminant zero: `ψ*=π/2`, `R=1/√2` (ties to iter 6). `\|Im ψ*\|` quantifies latency. Sign of the *discriminant*, not the coupling. All 4 checks pass | passing |
| `iter15_stigmergy.py` | **Stigmergy: coordination through a shared, persistent medium.** Agents couple only to a deposit-evaporation medium `M` (no direct coupling). Low evaporation → they synchronize through the trail; high evaporation → fall back to a *search/drift* null (r≈uncoupled baseline) — the null is **medium-relative**. Fingerprint (reusing iter-8 conditional TE): `M` is a *mediator*, so `TE(1→2)` collapses to ~14% conditioned on `M` (mirror of iter-8's *confounder*). Partial: a direct edge leaves more residual (22%), margin modest (minimal medium tracks the phase). Closure↔stigmergy = one axis (memory/coordination inside vs outside) | passing |
| `iter16_clock_relativity.py` | **Clocks: participant desync vs observer re-clocking (two different questions).** *Part A (physical — participant clocks):* two agents on alternating duty windows — **never co-present** — still lock through the medium (r=0.99 at zero overlap); the tolerated window scales with the trail's persistence, `W50 ∝ 1/γ` with `γ·W50` constant (5.0–7.5 over an 8× range of γ) ≈ a few e-foldings — evaporation decays the medium's *amplitude* while its stored *phase* persists, so slack ≈ `(1/γ)·ln(pull/drift margin)`. A direct edge gated by co-presence needs overlap (r 0.65→1.00 as f 0→1) while the mediated pair is flat at 0.99 — internal systems must share a wall clock; stigmergic agents each share one only with the medium. At matched coordination (r≈0.97 both), the mediated edge's TE-vs-lag **tail persists** (81% of peak at 2.5–4 time units) where the direct edge decays to the estimator floor (~0% by 2u) — external memory visible in the information plane. *Part B (representational — observer clock):* decimation ×2/×4 and a smooth monotone time-warp of the SAME trajectory leave the screening verdict and regime class unchanged while raw TE swings 1.4×; the warp rescales rate observables (slip rate ×1.30 = the mean warp factor) but leaves the Δθ distribution invariant (L1 0.029) whereas physical decoupling reshapes it (0.739). Coordinate change moves rates and magnitudes; physical change moves relations — the discriminator GPT's guardrail (D21) asked for | passing |
| `iter17_detector.py` | **The detector: an embedded, read-only observer (Ziggy's motif).** A node with no natural frequency coupled one-way to a source. *Isolation is exact:* pair trajectory **bit-identical** with the detector attached (max dev 0.0), locked offset on `arcsin(Δω/2K)` to 4 decimals — one-way (DAG) composition preserves upstream `[AN]` results exactly, Volume II's license to scale. *Its own law is derived:* one-way Adler — locks onto a rotating source iff `K_d ≥ \|Ω\|` (onset brackets Ω, **not** Ω/2: only one side yields), lag `arcsin(Ω/K_d)` matched to 3 decimals — bandwidth = iter 16's admissibility made physical. *The purest one-way certificate:* MI(src;det)=2.1 bits (symmetric, direction-blind), TE(src→det)=0.118, TE(det→src)=+0.003 (true null); completes the 3-node motif set (confounder iter 8 / mediator iter 15 / detector). *Registering a deviation:* a relation-detector **follows** a drifting pair only if its bandwidth beats the **peak** slip rate `Δω+2K` (saddle-node ghost — the mean-slip conjecture was refuted on the run, reported per house rule), but **settles** (detector-local statistic) at the pair's `Kc` for both bandwidths tested (K*=0.50, 0.52 vs 0.5) — the first awareness-shaped witness, scoped as registration. *The observer effect is a dial:* back-coupling ε → TE(det→src) 0.002→0.019 and `ψ*` error 0.001→0.141 rad, continuously from exactly zero; a static source reads free even at ε>0 (tracking lag is the lever arm of back-action) | passing |
| `iter14_associative_recovery.py` | **Associative recovery: full coherence into the WRONG memory.** An oscillatory Hopfield net stores M=3 patterns (`K_ij=(1/N)Σ_μ sᵘᵢsᵘⱼ`); each is a stable attractor. Damage pattern A and recover: small damage → 100% back to A; but past σ≈1.5 the *retrieval coherence* stays high (~0.85 — the system still locks onto **a** stored memory) while the fraction recovering the **original** collapses (→A: 100%→20%) and the fraction landing on a **different stored pattern** grows to 65% at σ=3.0. The true ship of Theseus — same coherence, a different stored self. Requires multistability: M=1 control always returns the same pattern. All 4 checks pass | passing |
| `iter13_damage_recovery.py` | **Damage recovery = recovery of the PATTERN.** Scramble a locked module's phases; measure recovery against the *stored pattern* (gauge-invariant phase differences), not coherence. Protected memory (frozen K): pattern recovers to ~1.0 from any scramble (K=0 control recovers nothing → the coupling IS what restores identity); coherence returns before the pattern (stricter, later). Unprotected memory (plastic): resilience **threshold** at σ≈1 — small hits self-heal, big hits erode the coupling and rewrite the memory (partial coherence r≈0.5 into a *shifted* pattern, F≈0.4). Ship of Theseus. All 5 checks pass | passing |

## Findings log

- **Clock relativity separates into two questions, and external memory answers
  the first (iter16):** *participant* clocks are physical — a direct edge only
  transmits while both parties are co-present (r rises with overlap f and sits
  at the drift baseline at f=0), whereas agents that are **never co-present**
  coordinate fully through a persistent medium; the desynchronization it
  tolerates is the clock-slack budget `W50 ∝ 1/γ` (`γ·W50` ≈ 5–7.5 constant
  over an 8× persistence range — a few e-foldings, because evaporation decays
  the trail's amplitude while its stored phase persists). So iter 15's
  external memory doubles as a **clock buffer**: each agent needs only to
  share a clock with the medium, never with each other. Mediation also has a
  **memory signature** in the information plane: at matched coordination, the
  direct edge's TE-lag profile decays to the estimator floor within ~2 time
  units (a channel forgets at its relaxation time) while the mediated edge
  retains 81% of peak transfer out to 4 units — the medium holds the writer's
  past. *Observer* clocks are representational — decimation and a smooth
  monotone time-warp of the same trajectory move measured magnitudes (TE
  swings 1.4×; rates scale by the warp factor) but not the certificates
  (screened-off verdict, regime class) or the relational structure (Δθ
  distribution, L1 0.029 vs 0.739 for genuine decoupling). Coordinate
  disagreement is not a physical deviation; the discriminator is invariance
  of relations vs covariance of rates. Honest scope: N=2, one substrate;
  invariance shown for re-clockings that still resolve the medium's bandwidth
  (dec×4's conditional TE already sits at the estimator floor); the
  admissibility boundary (where verdicts DO fail, e.g. aliasing) is unmapped.
- **Stigmergy = coordination through a shared medium, and the null is
  medium-relative (iter15):** agents coupled ONLY to a persistent, agent-written
  medium `M` (deposit + evaporation, no direct coupling) synchronize through it
  when the trail persists (low evaporation) and fall back to a **search/drift
  null** when it can't (high evaporation → r ≈ the uncoupled baseline) — a real
  bifurcation, and a *medium-relative* reference regime (the ant-without-pheromone
  reverts to search). Fingerprint, reusing iter-8's conditional TE: the medium is
  a *mediator* (`a→m→b`), the mirror of iter-8's *confounder* (`a←Z→b`) — so
  `TE(a→b)` collapses to ~14% once you condition on `M` (the medium is the
  pathway). Honest partial: a genuine direct edge leaves *more* residual (22% vs
  14%) but the margin is modest — this minimal medium tracks the phase, so a
  crisp mediator/direct double dissociation needs a spatial-field substrate
  (follow-up). Ties modularity (iter 4–5 = stigmergic self-org), memory (external
  vs internal), and closure (the extended-entity boundary question). Concept:
  closure and stigmergy are two ends of one axis (coordination/memory held
  inside vs outside).
- **Associative recovery lands on the wrong stored memory (iter14):** with
  multiple memories stored in one coupling (oscillatory Hopfield), damage
  recovery can restore *full* coherence into a *different* stored identity — the
  system re-locks onto **a** memory (retrieval coherence ~0.85) but increasingly
  not the original one (→original 100%→20%, →different memory 0→65% as damage
  grows). This is the genuine ship of Theseus that iter 13's monostable module
  could only approximate (there, the "different pattern" was a shifted/eroded
  version). It is a property of associative MEMORY, not of one attractor: the
  M=1 control always returns the same pattern. Identity resilience is a basin
  question — how many memories, how far apart — i.e. capacity (a follow-up).
- **Damage recovery = recovery of the PATTERN, and it needs a protected memory
  (iter13):** disrupt a locked module by scrambling its phases and measure
  recovery against the *stored pattern* (gauge-invariant pairwise phase
  differences), not mere coherence. With the memory (coupling K) **protected**
  (frozen), the pattern recovers to ~1.0 even from a total scramble — the
  coupling is a strong attractor, and it is *what* restores the identity (K=0
  recovers nothing). Coherence is the weaker bar: it returns almost immediately
  while the exact pattern takes ~1 time unit (pattern is the stricter, later
  quantity). With the memory **unprotected** (plastic, learning during the
  disruption) there is a **resilience threshold**: small hits self-heal
  (F≈1.0), but past σ≈1 the coupling erodes and the memory is rewritten —
  partial coherence persists (r≈0.5) into a *shifted, weaker pattern* while
  fidelity collapses (F≈0.4). Ship of Theseus: coherence continuation, identity
  lost. Lesson: **resilience is recovery of the pattern, and it requires
  protecting the memory during the insult.** Honest scope: monostable module, so
  the "different pattern" is a shifted/weakened version (erosion), not a distinct
  *stored* attractor — recovering coherence into a genuinely different *stored*
  pattern needs a multistable (associative-memory) system, the natural iter 14.
- **Latent vs active interaction is a sign problem (iter12):** the sign of the
  locking discriminant `Disc = 1 − (Δω/2K)²`. An *active* interaction has a real
  locked phase-offset `ψ*` (realized on the circle — a deviation; the pair
  settles to `Re ψ*`); a *latent* interaction has a **complex** offset
  `ψ* = π/2 − i·arccosh(Δω/2K)` (unrealized — a channel only; the pair drifts).
  The threshold `Kc` is the discriminant's zero, where the offset becomes real
  at exactly `ψ*=π/2` (coherence `1/√2`, tying to iter 6), and `|Im ψ*|`
  measures how latent. Crucially this is the sign of the *discriminant* (K vs
  Kc), NOT the sign of the coupling itself (the attractive/repulsive axis set
  aside in D1) — non-negative coupling, signed discriminant. This is the exact
  form of Ziggy's "latent/active as a sign problem" conjecture, and it is the
  mechanism behind iter 11's latent channel. Purely analytic backbone (extends
  iter 6) confirmed against simulated realization.
- **Interaction and deviation are separate observables — the latent channel
  (iter11):** transfer entropy (the *interaction*/edge detector) is nonzero for
  any coupling K>0, because a coupling transmits directed influence whether or
  not it has locked; mutual information (the *deviation*/locking detector) stays
  at floor until ~Kc. In the band 0<K<Kc they dissociate — TE>0 while MI≈0 — a
  real but silent edge (at K/Kc=0.34: TE=0.015 bits, MI=0.04). So interaction is
  graded (a matter of degree) and deviation is an onset (an event); the channel
  becomes visible at *lower* coupling than the event. Bonus, honest: TE peaks
  near Kc and then *declines* as locking tightens — redundancy, since a
  well-locked pair already predicts its own future, so the partner adds little
  new information. CPAF consequence: a null state (no deviations) can be dense
  with *latent* interactions — null is poised, not empty. Ch 8's last bridge
  span, grounded. Caveats: N=2; noise softens the deviation so both onsets sit
  below the noiseless Kc; "TE≈0" = surrogate floor (K=0 column calibrates it).
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
