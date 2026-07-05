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
| D9 | Architecture doc's **modularity caveat** should move from "open question" to "refuted as specified" (iter 4) | Simulation showed pure Hebbian coupling homogenizes rather than forming modules | open (awaiting sign-off) |
| D10 | Iteration 5 tests **coupling competition (synaptic normalization)** as the missing ingredient for modularity, alongside a genuinely per-pair reward | iter 4 proved per-node reward cancels from the within/cross ratio; competition is the candidate fix | locked |
| D11 | The recommended modular variant is **per-pair synchrony-gated reward** `R_ij = S_ij − thr`, optionally with **synaptic normalization** | iter 5: per-pair reward recovers modules (competition alone is inert; together they are best). This is the constructive fix for the iter-4 refutation | locked |

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
