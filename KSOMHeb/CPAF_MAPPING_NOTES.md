# CPAF ↔ oscillator mapping — working notes

> ⚠️ **SPECULATIVE / thinking scaffold, not verified.** Unlike everything under
> `verification/`, nothing here has been simulated or proven. This is a place to
> accumulate the correspondence between the K-SOM-Heb dynamics and CPAF's
> foundational ("basic layer") concepts, and to turn each correspondence into a
> testable iteration. Treat entries as conjectures with a status, not results.

## The core intuition (Ziggy)

A pairwise coupling is naturally **the vertex pair of a connection** — an edge
with two endpoints. That reframes the whole model in CPAF's own graph-shaped
vocabulary: oscillators are *entities* (vertices), couplings are *interactions*
(edges), and the locking event on an edge is a *deviation*. The oscillator model
may be a concrete substrate for CPAF's basic layer.

## Candidate correspondences

| CPAF foundational concept | Oscillator-model candidate | Status / anchor |
|---------------------------|----------------------------|-----------------|
| **Null state** (maximal entropy) | Incoherent population: random phases, `r ≈ 0`, all pairs below their locking threshold. Note: null ≠ "no couplings" — it's "no *deviations*" (couplings may exist but sit below `Kc`). | plausible; ties to iter 1/6 |
| **Deviation** (most fundamental change) | A pair crossing its locking threshold `Kc = \|Δω\|/2`: drift → locked, noise → structure. The saddle-node bifurcation. | **operationalized** (iter 6) |
| **Interaction** | The coupling `Kᵢⱼ` itself — the channel of influence between two entities (the edge). | clean; the "vertex pair" |
| **Entity** | An oscillator (vertex); *recursively*, a locked cluster/module acting as one coherent unit (iter 5) — an emergent higher-order entity. | partial; recursion untested |
| **Information** | Mutual information `I(θᵢ; θⱼ)` between two phases. iter 7: it climbs from ~0 to ~2.7 bits across the locking threshold — a *deviation creates information* — and, crucially, tracks differently from `r` (moderate `r` with ~0 MI in deep drift). | **operationalized** (iter 7); resolves seam #1 |
| **System** | The whole graph of entities + interactions; collective `r`, modularity `Q`. | plausible; iter 3–5 |

## Tensions to resolve (the honest list)

1. **Interaction vs deviation.** Is a deviation a *property of* an interaction or
   its own object? Working split: interaction = the channel exists (a coupling);
   deviation = that channel produces a *sustained state change* (locking). The
   edge is the noun; the locking event is the verb.
2. ~~**Information is unmeasured.**~~ **Closed (iter 7):** mutual information
   `I(θᵢ; θⱼ)` is the measure — it appears at the deviation point and diverges
   from `r`. Remaining nuance: MI cannot tell a genuine *interaction* from a
   *common drive* (both raise MI); distinguishing them needs a *directed*
   measure (transfer entropy). That is the next refinement, and it connects to
   tension #4 (directionality).
3. **Null = K→0 or K below Kc?** These differ: a system rich in sub-threshold
   couplings is "quiet" but not structureless. Suggests null state is about the
   absence of *deviations*, not the absence of *interactions*.
4. **Directionality.** CPAF interactions may be directed; our `K` is symmetric
   (Hebbian). The doc's asymmetric-coupling extension (`Kᵢⱼ ≠ Kⱼᵢ`) would map to
   directed interactions / causal influence.

## Candidate iterations to ground it

- **Deviation (mostly done):** formalize "a deviation = a pair crossing `Kc`";
  iter 6 already gives the threshold and the `1/√2` onset.
- ~~**Information:**~~ **done (iter 7)** — MI rises at `Kc`; coherence ≠
  information confirmed. *Follow-up:* transfer entropy to separate genuine
  interaction from common drive (directed information).
- **Emergent entity (new):** coarse-grain a locked cluster and test whether it
  behaves as a single effective oscillator (effective phase/frequency) — the
  recursion CPAF leans on.

## Where this is heading

Longer term: use the verified dynamics to give CPAF's basic layer — *null state,
deviation, interaction, information, entity, system* — concrete, computable
definitions, each earned by an iteration the way the metric claims were. The
discipline stays the same: conjecture here, prove under `verification/`, then
promote to the doc/textbook.
