# K-SOM-Heb — decision log

A running record of the design and verification decisions behind K-SOM-Heb,
with rationale and status, so the *route* (not just the destination) is
legible. Newest decisions at the bottom. Statuses: **locked** (settled),
**open** (awaiting a call), **superseded** (replaced by a later entry).

| # | Decision | Rationale | Status |
|---|----------|-----------|--------|
| D1 | Take the **Hebbian** path, not signed STDP: synchrony measure `S ∈ [0,1]` | User familiarity + conservative choice. Consequence: anti-phase pairs *decay* (passive forgetting), they are not actively pushed apart | locked |
| D2 | Local synchrony `S_ij = \|cos((θ_j−θ_i)/2)\|` (pairwise order parameter) | Replaces the v1.0 bug `S=\|exp(iΔθ)\|≡1`, which carried zero information. Matches the doc's stated properties (1 at 0, 0 at π, smooth) and is wrap-immune | locked |
| D3 | Spatial (Kohonen) coupling applied **once at init**, not blended every step | The per-step blend was ~10⁴× stronger than the intrinsic dynamics and froze learning | locked |
| D4 | Connectivity entropy uses the **normalized** distribution `p_ij = K_ij/ΣK` | The unnormalized `−ΣK logK` is not a valid entropy (negative for K>1, undefined at K=0) | locked |
| D5 | Bound coupling into `[0, K_max]` | Text already recommended it; the v1.0 code enforced only the ≥0 floor | locked |
| D6 | **Verify bottom-up**: each layer checked against known theory before adding the next; every claim gets a runnable script + plot | Catch mechanism-breaking errors early; keep code matched to math | locked |
| D7 | Reference math lives in `ksomheb.py`; the browser visualiser ports it to `ksomheb.js` guarded by a Node **parity check** | One source of truth; the JS is verified identical, not assumed | locked |
| D8 | Global reward for iters 1–3 is `R = r − r_baseline`; local reward is the endogenous coupling-weighted field coherence `r_local(i)` | Uses only θ and K (no ground-truth labels), so it is a legitimate signal | locked |
| D9 | Architecture doc's **modularity claim** updated (v1.2): "refuted as specified, rescuable with per-pair reward + competition" (iter 4–5) | Simulation showed pure Hebbian coupling homogenizes; per-pair credit recovers modules. Signed off; doc edited | locked |
| D10 | Iteration 5 tests **coupling competition (synaptic normalization)** as the missing ingredient for modularity, alongside a genuinely per-pair reward | iter 4 proved per-node reward cancels from the within/cross ratio; competition is the candidate fix | locked |
| D11 | The recommended modular variant is **per-pair synchrony-gated reward** `R_ij = S_ij − thr`, optionally with **synaptic normalization** | iter 5: per-pair reward recovers modules (competition alone is inert; together they are best). This is the constructive fix for the iter-4 refutation | locked |
| D12 | The per-pair coherence threshold has a **derived** value `1/√2 ≈ 0.707` (two-oscillator locking onset), not a hand-picked one | iter 6: `Kc(pair)=\|Δω\|/2`, `R_onset=1/√2`. Grounds the `θ_S` gate and partially the `r≥0.7` line (per-pair only; global-`r` transition is continuous) | locked |
| D13 | **Mutual information** `I(θᵢ;θⱼ)` is the "information" measure; it is distinct from coherence `r` | iter 7: MI appears at the deviation point (`Kc`) and diverges from `r` (moderate `r`, ~0 MI in deep drift). Resolves seam #1. Follow-up: transfer entropy for directed interaction vs common drive | locked |
| D14 | **Interaction and deviation are distinct primitives**, detected by distinct measures: TE (interaction/edge) vs MI (deviation/locking). The **null state** = absence of *deviations* (latent sub-threshold interactions permitted), not absence of interactions | iter 11: they dissociate in the band `0<K<Kc` — TE>0 (channel) while MI≈0 (no lock) — a latent channel. Completes Ch 8's bridge; null is poised, not empty. (iters 8–10 are recorded in `verification/README.md` + `CPAF_MAPPING_NOTES.md` rather than as decision rows) | locked |
| D15 | **Latent vs active interaction is the sign of the locking discriminant** `Disc=1−(Δω/2K)²` (active=real `ψ*`, latent=complex `ψ*`); the base CPAF `int→d` construct describes *active* interactions. Framework refinements 7.1/7.2 (`nullstate.md`, `interaction.md`) **applied** with author direction | iter 12 verifies the sign framing (Ziggy's conjecture); the latent channel (iter 11) is its mechanism. Sign of the *discriminant*, not the coupling (that axis was set aside in D1). Integrated into `../Framework/` | locked |
| D16 | **Damage recovery is measured against the stored PATTERN** (gauge-invariant phase differences), with coherence only secondary; recovery requires a **protected memory** | iter 13: frozen K restores the pattern from any scramble (K=0 recovers nothing); plastic K self-heals small hits but past a threshold erodes/rewrites the memory (identity lost while coherence partly persists — ship of Theseus). Resilience = pattern recovery. First step toward the active-layer *memory* concept + graceful degradation | locked |
| D17 | The genuine ship-of-Theseus (recover *full* coherence into a *different stored* identity) requires **multistability**; modeled as an **oscillatory Hopfield** net | iter 14: with M stored memories, damage recovery lands on a different stored pattern an increasing fraction of the time (→65% at σ=3) while retrieval coherence stays ~0.85; M=1 cannot. Identity resilience = basin size (capacity). Substrate for the *memory* concept | locked |
| D18 | Adopt GPT's **canonical metalanguage** as the shared language; the iterations are **computational witnesses `[CW]`** (analytic parts `[AN]`), never universal definitions. Split the textbook into **Volume I (foundations, Ch 0–13)** and **Volume II (active layer)** | Formal-spine audit produced `Framework/CanonicalDefinitions/` (authority order in its README; `ComputationalProofs.md` = evidence layer #3). Ch 13 capstone recasts Vol I as a witness table and surfaced 4 revisions. Vol II opens with damage recovery (iters 13–14 = the canonical *identity-deviation* subtype) | locked |
| D19 | **Stigmergy** is modeled as a *mediator motif* (`a→m→b` through a persistent shared medium), the mirror of iter-8's *confounder*; its fingerprint is `Connected(a→b\|m)≈0`. The **null state is medium-relative** (no medium signal → default/search regime) | iter 15: agents coordinate through a deposit-evaporation medium; `TE` screens to 14% under `M`. Closure↔stigmergy = one axis (coordination/memory inside vs outside). Medium-relative null is a contribution to the canonical `null_state`. Direct-vs-mediated margin modest → spatial-field follow-up | locked |
| D20 | A macro-level null may be **actively maintained by micro-level interactions**. “High-frequency” metastability means high finite-horizon return probability or revisit rate; a revisit returns to the same regime or declared similarity neighbourhood, not necessarily the identical microstate | Author direction integrated into canonical `null_state.md` Draft 0.2. Maintenance requires a certificate, not mere coexistence. Horizons, similarity tolerances, and recurrence thresholds remain context-specific | locked |
| D21 | Explore **observer/clock relativity** using coupled oscillators represented on different clocks or time bases | Natural next seam after stigmergy's medium-relative null: test which synchronization, null, deviation, and interaction claims survive clock transformation. Separate coordinate or sampling disagreement from physical deviation and specify invariants before constructing a witness | locked (executed: iter 16 → D22) |
| D22 | **Two clock questions, kept separate.** *Participant* desynchronization is physical: a direct edge requires co-presence (a shared wall clock within the interaction timescale), while a persistent medium buffers desync in proportion to its persistence time — the clock-slack budget `W50 ∝ 1/γ`, so iter-15's external memory doubles as a **clock buffer** (each agent shares a clock only with the medium). Mediation carries a **memory signature**: a persistent TE-lag tail where a matched direct edge forgets. *Observer* re-clocking or resampling is representational: certificate verdicts (screened-off, regime class) and relational statistics (the Δθ distribution) are invariant under the tested transformations, while magnitudes (TE bits) and rate observables covary with the clock. Coordinate disagreement is **not** a physical deviation; the discriminator is relations-invariant vs rates-covariant | iter 16: zero-co-presence coordination (r=0.99 at overlap f=0 vs direct at drift baseline); `γ·W50` constant (5.0–7.5) over 8× γ — a few e-foldings (amplitude evaporates, stored phase persists); TE tail 81% vs 0% of peak at matched r; decimation ×2/×4 + monotone time-warp preserve verdicts while TE swings 1.4× and slip rate scales ×1.30 = warp factor; Δθ distribution L1 0.029 (warp) vs 0.739 (decoupling). Honest: N=2, one substrate; admissibility boundary unmapped (dec×4 conditional TE at estimator floor). Typed clock-transformation definitions → canonical layer (GPT) | locked |
| D23 | Canonical clock formalism separates `𝕋_phys`, participant clock/availability, observer clock, sampling, and feature maps; distinguishes bijective re-clocking from resampling; and types claims as transformation-indexed **invariant**, **covariant**, or **representation-sensitive** | Draft 0.2 `METALANGUAGE.md`, Null State Draft 0.3, and Deviation Draft 0.2 formalize the D22 handoff. Iter 16 is a bounded witness, not a universal definition; admissibility/aliasing and observer ontology remain open | open (author review) |
| D24 | **The detector (embedded observer) is the scaling motif for Volume II**: a node with no natural frequency, coupled one-way (read-only). Composition principle: feed-forward (DAG) attachments preserve upstream `[AN]` results **exactly** — verified pairs are foundation blocks. Detector bandwidth is a derived law (`K_d ≥ \|Ω\|`, no factor 2 — only one side yields; lag `arcsin(Ω/K_d)`) = iter 16's admissibility made physical. A relation-detector's *own state* registers the pair's deviation at `Kc` (bandwidth-robust) — the first awareness-shaped witness, scoped as *registration only*. Completes the 3-node motif set: confounder / mediator / detector | iter 17 (Ziggy's motif): pair trajectory bit-identical with detector attached (max dev 0.0); `ψ*` = arcsin to 4 decimals; MI 2.1 bits, TE fwd 0.118, TE back +0.003 (true null); lock onset brackets `K_d=Ω`, lag matches `[AN]` to 3 decimals; settle at K*=0.50–0.52 vs Kc=0.5 for both bandwidths. Honest revision: *following* a drifting pair is priced by the **peak** slip rate `Δω+2K` (saddle-node ghost), not the mean — original mean-slip bound refuted on the run. ε back-coupling: reader→participant is a continuous dial (TE 0.002→0.019; ψ* error 0.001→0.141 rad), and a static source reads free even at ε>0 (lag is the lever arm). Textbook: Vol II Ch 1 "Isolation and scale" | locked |

## Findings that drove decisions

- **iter 2 — saturation bound** `R_sat = K_max·λ/η`. Sustained reward above it
  pins coupling at K_max and erases the synchrony gradient. Keep sustained
  reward below R_sat or retune η/λ.
- **iter 3 — bistability.** Global reward closes a positive-feedback loop; the
  system runs away to saturation or collapses to zero, storing ~one bit. It
  commits rather than regulates.
- **iter 4 — modularity is not emergent.** Reward mode cancels from the
  within/cross ratio (only `S_ij` carries per-pair information); self-entrainment
  inflates cross-synchrony until the clusters merge. Needs competition or
  per-pair credit.
- **iter 5 — modularity is recoverable.** Per-pair synchrony-gated reward
  recovers the modules (contrast 1.24→2.16, Q 0.045→0.156); competition alone
  is inert but amplifies per-pair to contrast 3.32 / Q 0.262. The doc's ambition
  is reachable with ingredients it omits.
- **iter 6 — a derived threshold.** Two oscillators lock at `Kc=|Δω|/2` (a
  saddle-node bifurcation) with order parameter exactly `1/√2 ≈ 0.707` at onset.
  Gives a principled per-pair coherence threshold matching the hand-picked 0.7;
  candidate grounding for CPAF's noise→deviation boundary (per-pair only so far).
- **iter 7 — information at the deviation.** Mutual information between two
  noisy phases climbs ~0 → ~2.7 bits across `Kc`: a deviation *creates* shared
  information. And `r` overreads (66% of max in deep drift while MI is 2%), so
  coherence ≠ information — seam #1 resolved. MI is the "information" primitive.
- *(iters 8–10 recorded in `verification/README.md` and `CPAF_MAPPING_NOTES.md`:
  the related<directed<connected TE ladder; entity-as-cluster; the splice.)*
- **iter 11 — the latent channel.** TE (interaction) is nonzero for any `K>0`
  while MI (deviation) waits for `Kc`; the band `0<K<Kc` is a real-but-silent
  edge. Interaction is graded, deviation is an onset; null is poised, not empty.
  Completes the foundational bridge (Ch 7–12).
- **iter 12 — the sign of an interaction.** Latent vs active = sign of the
  locking discriminant `Disc=1−(Δω/2K)²`. Active: `ψ*` real (realized, a
  deviation). Latent: `ψ*` complex (unrealized, a channel). Threshold = zero of
  the discriminant. Grounds the interaction refinement now integrated into the
  main framework (`nullstate.md`, `interaction.md`, `ComputationalProofs.md`).
- **iter 13 — damage recovery is pattern recovery.** A locked module's identity
  is its stored pattern; protected memory (frozen K) restores it from any
  scramble (K=0 recovers nothing), coherence returning before the pattern.
  Unprotected memory (plastic) self-heals small hits but past σ≈1 erodes and
  rewrites → identity lost while r partly persists (ship of Theseus). Opens the
  active-layer *memory* / graceful-degradation thread.
- **iter 17 — reading is free; touching costs; noticing is a state.** A
  read-only, no-natural-frequency node leaves its source *bit-identical* —
  one-way composition preserves verified math exactly, which is Volume II's
  license to scale without re-derivation. The detector's own physics is
  derived: lock iff `K_d ≥ |Ω|` (one-way: no factor 2), lag `arcsin(Ω/K_d)`
  — bandwidth as physical admissibility. Following a drifting pair needs
  bandwidth above the **peak** slip rate (nonuniform saddle-node slipping;
  the mean-slip conjecture was refuted on the run), but *settling* — a
  detector-local statistic — registers the pair's deviation at `Kc` for any
  bandwidth: measurement of a deviation is a deviation in the measurer. With
  back-coupling ε, reading becomes participation continuously; against a
  static source even ε>0 is inert (`sin(0)=0`) — a moving world is what makes
  observation costly.
- **iter 16 — external memory is a clock buffer; observers move magnitudes,
  not verdicts.** Agents that are never simultaneously present coordinate
  fully through the medium; the tolerated window scales as `W50 ∝ 1/γ` with a
  log-margin prefactor (`γ·W50` ≈ 5–7.5: the trail's amplitude decays but its
  stored phase persists). A co-presence-gated direct edge needs overlap; the
  medium doesn't — "internal system" operationally = coordination that
  requires closely aligned participant clocks. Mediated edges also wear a
  memory signature: TE-lag transfer persists far beyond a matched direct
  edge's forgetting time. Meanwhile re-representing the *same* trajectory
  (decimation, smooth time-warp) moves TE magnitudes (1.4×) and rates (×warp
  factor) but leaves screening verdicts, regime class, and the Δθ
  distribution invariant — certificates and relations are the portable
  content; rates and bit-counts are clock-relative measurements.
- **iter 14 — associative recovery / wrong memory.** An oscillatory Hopfield net
  (M stored patterns) recovers *full* coherence into a *different stored* memory
  as damage grows (→different: 0→65%), while a single-pattern net cannot. The
  genuine ship of Theseus; identity resilience = basin/capacity. Follow-ups:
  capacity study; structural K-lesions; combine 13+14 into textbook Ch 13.
