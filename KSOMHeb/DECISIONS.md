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
