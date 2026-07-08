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
| **Entity** | An oscillator (vertex); *recursively*, a locked cluster coarse-grained to its mean phasor (Θ, ρ). iter 9: a locked cluster passes every entity criterion — one effective frequency ω̄, entrainment per the iter-6 law with `K_eff = κρ` (coupling discounted by internal coherence), the 1/√2 branch one level up, and **macro closure** (TE(member→Θ\|Θ) ≈ 0). An unlocked collection fails all of them: entity-hood is *created* by the locking transition. iter 10: modules **grown** by iter-5's machinery pass all criteria unadjusted, and closure *locates* the boundary (arbitrary boundary through the same trajectory leaks 50–60× louder) — entities are discoverable from dynamics alone. | **operationalized, incl. grown structure** (iter 9–10); blind boundary search + fragmentation envelope open |
| **Information** | Mutual information `I(θᵢ; θⱼ)` between two phases. iter 7: it climbs from ~0 to ~2.7 bits across the locking threshold — a *deviation creates information* — and, crucially, tracks differently from `r` (moderate `r` with ~0 MI in deep drift). iter 8 grades the claim into a ladder: MI = *related* (graph-blind), transfer entropy = *directed* (but prediction ≠ causation — a hidden common drive fakes it), conditional TE = *connected* (needs the confounder observed). "Information on an interaction" is a system-level certificate, not a pairwise property. | **operationalized & graded** (iter 7–8) |
| **System** | The whole graph of entities + interactions; collective `r`, modularity `Q`. | plausible; iter 3–5 |

## Tensions to resolve (the honest list)

1. ~~**Interaction vs deviation.**~~ **Grounded (iter 11).** Interaction =
   directed influence on the channel (`TE(i→j)`, nonzero as soon as `K>0`);
   deviation = the locking event (winding number `Ω→0`, MI jumps, at `Kc`).
   They *dissociate*: below `Kc`, in a provably-drifting band (Ω large, MI at
   floor), `TE(1→2)` is significant at z in the hundreds — influence without a
   deviation. Asymmetry established: every deviation rides on an interaction,
   not vice versa (the edge is the noun, the locking the verb — now evidenced).
   Two corrections the experiment forced: TE is *non-monotonic* (peaks at
   locking onset, declines when locked — self-predictable target); and the
   locked-regime null direction carries the iter-8 bias via lag structure
   (~60× below signal — effect size, not z, is the honest null lens at large
   N).
2. ~~**Information is unmeasured.**~~ **Closed (iter 7), nuance closed
   (iter 8):** mutual information `I(θᵢ; θⱼ)` is the measure — it appears at
   the deviation point and diverges from `r`. The MI-vs-common-drive nuance is
   now graded: pairwise TE adds direction but is *also* fooled by a hidden
   common cause (genuine predictive transfer, no edge); only conditional TE —
   confounder observed — certifies the edge (double dissociation, iter 8).
   Residual honest gap: on a real network the right conditioning set is a
   causal-inference problem, not a histogram; we proved the mechanism on the
   minimal 3-vertex case.
3. **Null = K→0 or K below Kc?** These differ: a system rich in sub-threshold
   couplings is "quiet" but not structureless. Suggests null state is about the
   absence of *deviations*, not the absence of *interactions*.
4. **Directionality.** CPAF interactions may be directed; our `K` is symmetric
   (Hebbian). The doc's asymmetric-coupling extension (`Kᵢⱼ ≠ Kⱼᵢ`) would map to
   directed interactions / causal influence. **Readout grounded (iter 8):** an
   imposed one-way coupling gives `TE(2→1)` statistically zero and `TE(1→2)`
   large — directed interactions are *measurable*. Still open: a learning rule
   that *produces* asymmetric `K` (readout ≠ origin).

## Candidate iterations to ground it

- **Deviation (mostly done):** formalize "a deviation = a pair crossing `Kc`";
  iter 6 already gives the threshold and the `1/√2` onset.
- ~~**Information:**~~ **done (iter 7)** — MI rises at `Kc`; coherence ≠
  information confirmed.
- ~~**Transfer entropy:**~~ **done (iter 8)** — the ladder *related < directed
  < connected*: TE resolves direction (grounding asymmetric `Kᵢⱼ` as a
  readout) but only conditional TE separates a genuine interaction from a
  common cause. *Follow-ups:* partial observability of the confounder (does
  the certificate degrade smoothly?); a rule that learns asymmetric `K`.
- ~~**Emergent entity:**~~ **done (iter 9)** — a locked cluster IS a single
  effective oscillator (ω̄, `K_eff = κρ`, 1/√2 branch, macro closure); an
  unlocked collection is not.
- ~~**Grown entity (the splice):**~~ **done (iter 10)** — iter-5's learned
  modules pass all entity criteria unadjusted; closure doubles as a boundary
  *detector* (true vs arbitrary boundary: 50–60×); first entity-to-entity
  macro TE observed. *Follow-ups:* blind boundary search (closure as an
  objective); entity-hood along the growth trajectory; entities from
  unseeded structure; absorption-vs-fragmentation envelope; what does a
  cluster with *asymmetric* internal coupling coarse-grain to (the
  reduction's cancellation needs symmetry)?

## Where this is heading

Longer term: use the verified dynamics to give CPAF's basic layer — *null state,
deviation, interaction, information, entity, system* — concrete, computable
definitions, each earned by an iteration the way the metric claims were. The
discipline stays the same: conjecture here, prove under `verification/`, then
promote to the doc/textbook.
