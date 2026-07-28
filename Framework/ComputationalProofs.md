# Computational Single-Case Proofs of CPAF's Foundational Concepts

*The bridge between the abstract concept docs and the verified simulations under
`../KSOMHeb/`. For each foundational concept, CPAF gives a definition and a
logical/mathematical construct; here each construct is **realized concretely and
checked by running code**.*

> **Canonical-layer note.** The formal-spine audit has since introduced a
> gold-standard definition layer, `CanonicalDefinitions/` (its `README.md` sets
> the authority order — this document is **level 3, the evidence/refinement
> layer**). In that layer's **metalanguage** (`CanonicalDefinitions/
> METALANGUAGE.md`), each "single-case proof" below is a **computational witness
> `[CW]`** (an existence demonstration in one substrate), and the analytic parts
> (e.g. `Kc=|Δω|/2`, `1/√2`) are **analytic results `[AN]`** — never universal
> definitions. The canonical concept docs cite these as their witnesses (e.g.
> `deviation.md` → iter 6 and the identity-deviation of iters 13–14). The four
> refinements in §7 have largely been absorbed into that layer; where they touch
> a formal construct, the canonical docs are authoritative. Pedagogical
> walkthrough: `../KSOMHeb/textbook/13_capstone_metalanguage.md`.

---

## What a "single-case proof" is (and isn't)

A single-case proof is an **existence proof**. It shows that a foundational
construct is not merely a definition on paper but is *realizable and computable*
in at least one rigorous substrate — here, a population of coupled phase
oscillators whose connections learn (K-SOM-Heb). Each proof:

- instantiates the abstract construct in concrete dynamics,
- **measures** the quantity the construct names,
- and passes a runnable check (`../KSOMHeb/verification/iterN_*.py`, all
  printing `ALL PASS`).

What it does **not** do is establish CPAF's *universality* claim — that the
concept holds across all substrates. Universality is argued separately in the
concept docs. A single-case proof does two humbler but essential things: it
proves the concept is **coherent and mechanizable** (you can build a thing that
provably has the property), and it **exposes refinements** — places where the
concrete mechanism is sharper than, or gently contradicts, the abstract
construct. Those refinements (collected in §7) are the main way this exercise
*strengthens* the framework rather than merely illustrating it.

The substrate in one line: **coupled phase oscillators `θᵢ` with detunings
`ωᵢ` and learning couplings `Kᵢⱼ`**; coherence is the order parameter
`r ∈ [0,1]`. See `../KSOMHeb/CHEATSHEET.md` for the math and
`../KSOMHeb/textbook/` for the derivations.

---

## Summary

| CPAF concept | Construct (from the concept doc) | Single-case realization | Proof | Verdict |
|---|---|---|---|---|
| **Null state** | maximum entropy; `f(s₀)=0`; `(¬∃d)∧(¬∃int)` at `s=ns` | incoherent population, `r≈0`, all pairs below their locking threshold | iter 1, **iter 11** | ✅ realized; `¬∃int`→`¬∃int_act` (applied) |
| **Deviation** | distinguishable change from `s₀`; `f:S→[0,1]` | a pair crossing its locking threshold `Kc=\|Δω\|/2` | **iter 6**, iter 7 | ✅ realized with a *derived* onset |
| **Information** | processable thing that induces a deviation; `Impact=d(s,I(d,s))` | mutual information born at the locking transition | **iter 7**, iter 8 | ✅ realized & graded |
| **Interaction** | event where info is transmitted → deviation; `int → d` | the coupling `Kᵢⱼ` (channel) vs the locking (event); latent/active = sign of `Disc=1−(Δω/2K)²` | iter 8, iter 11, **iter 12** | ✅ realized; latent/active split (applied) |
| **Entity** | locus of information processing; recursive | a locked cluster coarse-grained to one macro-oscillator `(Θ,ρ)` | **iter 9**, iter 10 | ✅ realized, incl. *grown* & recursive |
| **System** | assembly of interacting entities; emergence `Em:S×I→S'` | the coupled graph; entity-hood emerges at locking | iter 3–5, **iter 9–10** | ✅ realized; emergence concrete |

---

## 1. Null state

**CPAF construct.** "A representation of maximum entropy"; a function `f(s₀)=0`
with `f(s)∈(0,1]` for deviations; logically `(¬∃d ∈ D) ∧ (¬∃int ∈ Int)` when the
system sits at its null state. Axiom: *change is the most fundamental descriptor.*

**Single-case realization.** An incoherent oscillator population: random phases,
order parameter `r ≈ 0`, every pair below its locking threshold. This is a
maximum-entropy configuration in exactly CPAF's sense — no phase relationship
carries information (iter 7 shows `r≈0` ⇒ ~0 mutual information). The coherence
`r` is a concrete instance of the deviation function `f`: `r=0` at the incoherent
null, rising toward 1 as structure appears.

**Proof.** iter 1 (the incoherent phase below the Kuramoto critical coupling);
iter 11 (the `K=0` column is a true null — both the deviation detector and the
interaction detector sit at floor).

**What it refines (see §7.1).** The logical construct says the null state has
**no interactions** (`¬∃int`). iter 11 shows this is too strong: a null state
(`r≈0`, no deviations) can be *dense with latent interactions* — sub-threshold
couplings carrying real directed influence. The null state is **poised, not
empty**. This aligns with the framework's own *meta-null* and *embedded
information* notions.

---

## 2. Deviation

**CPAF construct.** "A distinguishable change from a system's baseline,"
`f:S→[0,1]`, continuous and bounded; deviations may be *latent* ("potential to be
detected"). Axiom-adjacent: the most fundamental change.

**Single-case realization.** A pair of oscillators crossing its **locking
threshold** `Kc = |Δω|/2` (iter 6): below it they drift (baseline/noise), above
it they lock (a distinguishable, sustained change). This is a saddle-node
bifurcation — the finite-system analogue of a phase transition — so the "most
fundamental change" gets a *sharp, mechanistic* definition, not a vague one.

**Proof.** iter 6 grounds the threshold `Kc=|Δω|/2` and, remarkably, a **derived**
onset: the coherence at the moment of locking is exactly `1/√2 ≈ 0.707`. iter 7
then shows the deviation is *distinguishable by its effects*: it **creates
information** (mutual information climbs ~0 → ~2.7 bits across the crossing),
satisfying CPAF's "distinguishable through effects or measurement" clause.

**Strengthens.** CPAF's deviation function `f∈[0,1]` is instantiated by
`r∈[0,1]`; the abstract "distinguishable change" becomes a bifurcation with a
computed location and a computed onset value.

---

## 3. Information

**CPAF construct.** "Anything processable by an entity that, when processed, has
the potential to induce a deviation"; impact `= d(s, I(d,s))`. Subset **embedded
information**: "unrealized deviations… the system's potential to deviate."

**Single-case realization.** The **mutual information** `I(θᵢ;θⱼ)` that appears at
the locking transition (iter 7). It is born *with* the deviation, directly
realizing "information ⇄ deviation." Critically, it is **not** the same as
coherence: deep in the drift regime `r` reads 66 % of its max while information is
~2 % — so `r` (coherence) overreads relationship, and information is the
discriminating quantity. **Embedded information** — the framework's "unrealized
deviation potential" — is realized twice over: as the learned coupling matrix `K`
(stored history, iters 2–5) and as the **latent channel** of iter 11 (a
sub-threshold coupling that *can* produce a deviation but hasn't yet).

**Proof.** iter 7 (MI born at the deviation; coherence ≠ information). iter 8
grades "information on an interaction" into a ladder — **related** (mutual
information, but blind to the causal graph) < **directed** (transfer entropy,
which adds direction but is fooled by a hidden common cause: prediction ≠
causation) < **connected** (conditional transfer entropy, which certifies the
edge only when the confounder is observed).

**Strengthens (see §7.3).** CPAF treats "information passing along an interaction"
as primitive; the proof shows *certifying* that information rode a specific edge
is a graded, context-dependent claim, not a local one.

---

## 4. Interaction

**CPAF construct.** "An event within a system where information is… transmitted,
leading to a deviation in one or more entities"; logically `int causes i → d in
e`. External interactions may be "one-way or bidirectional."

**Single-case realization.** The coupling `Kᵢⱼ` — the channel of influence
between two oscillators. Two facts from the sims:

- **Directionality is measurable.** An imposed one-way coupling `1→2` gives
  `TE(2→1) ≈ 0` (a true statistical null) and `TE(1→2) ≫ 0` (iter 8). CPAF's
  "one-way vs bidirectional external interaction" is thus a *measurable*
  distinction, grounding the doc's asymmetric-`Kᵢⱼ` extension as a readout.
- **Channel and event are distinct** (iter 11). Transfer entropy detects the
  channel for *any* `K>0` (a coupling transmits influence whether or not it has
  locked), while the deviation (mutual information) appears only at `Kc`. Between
  them lies a **latent-channel band** `0<K<Kc`: TE > 0 (interaction present) but
  MI ≈ 0 (no deviation). Interaction is graded (a matter of degree); deviation is
  an onset (an event).

**Proof.** iter 8 (directionality; interaction vs common cause); iter 12 (latent
vs active = the sign of the locking discriminant; a latent interaction's locked
offset is complex/unrealized); iter 11 (the
latent channel — interaction ≠ deviation).

**What it refines (see §7.2).** CPAF's construct binds interaction to deviation
(`int → d`: an interaction *is* an event that produces a deviation). The proof
distinguishes the **interaction capacity** (a channel, possibly latent) from the
**interaction event** (the framework's current definition). This is not a
contradiction so much as a resolution: the latent channel is exactly the
framework's **embedded information** — a pre-encoded *potential* to deviate —
now given a concrete, measurable form (`TE > 0` with `MI ≈ 0`).

---

## 5. Entity

**CPAF construct.** "A locus of information processing, capable of initiating or
responding to deviations"; explicitly **recursive** — "entities can be composed
of sub-entities, forming nested systems."

**Single-case realization.** A **locked cluster**, coarse-grained to its mean
phasor `(Θ, ρ)` (iter 9). A locked cluster passes every criterion for being a
single entity one level up:

- **one effective clock** — member velocity spread ~0 % of the natural spread;
- **it obeys the pair law** — the macro-phase entrains exactly per iter 6 with
  effective coupling `K_eff = κρ` (coupling discounted by internal coherence),
  thresholds matching to 2.5 %;
- **it has an interface** — *macro closure*: `TE(member → Θ | Θ) ≈ 0` for a
  locked cluster (members add ~nothing beyond the macro-phase) vs clearly nonzero
  for an unlocked collection. Entity-hood is **created by the locking transition**.

**Proof.** iter 9 (a locked cluster IS one oscillator; an unlocked collection is
not). iter 10 — **the splice**: modules *grown* by the learning rule (not
hand-built) pass all entity criteria unadjusted, and *closure locates the
boundary* (the true boundary leaks 0.005 bits vs 0.284 for an arbitrary boundary
on the same trajectory — a 50–60× separation). The recursion is real and
*discoverable from dynamics alone*.

**Strengthens.** CPAF's recursion ("nested systems") is instantiated: a system of
oscillators becomes a single entity for the next level, obeying the *same laws* as
its parts.

---

## 6. System

**CPAF construct.** "A cohesive assembly of entities that interact internally,"
with embedded information defining external-interaction potential; and
**emergence** `Em: S×I → S'` producing states "not reducible to or predictable
from" the parts.

**Single-case realization.** The coupled oscillator graph as a whole: collective
coherence `r`, learned structure `K`, modularity `Q`. Its **emergence** is
concrete and measured — a locked cluster has *one* effective frequency that no
individual member possesses in isolation (iter 9), a higher-level property that
appears only through interaction. Entity-hood *is* an emergent state `S'` born at
the locking transition; the first **entity-to-entity** macro channel
(`TE(Θ_B→Θ_A|Θ_A)=0.013 bits`, iter 10) shows emergent entities then interacting
as units — the recursion closing.

**Proof.** iters 3–5 (the system's collective dynamics, and the honest refutation
+ rescue of emergent modularity — see §7.4); iters 9–10 (emergence of entities and
their macro-level interaction).

**Strengthens.** CPAF's emergence function `Em` gets a worked instance: the
macro-oscillator is a state not predictable from the members' phases alone, yet
fully lawful once formed.

---

## 7. Refinements the proofs suggest to the framework

These are the contributions — places where running the mechanism sharpened or
corrected the abstract construct. Each is a candidate edit to the concept docs.

**7.1 The null state permits latent interactions. [APPLIED]** `nullstate.md`'s
logical construct `(¬∃d)∧(¬∃int)` is refined to `(¬∃d)∧(¬∃int_act)` — no
*active* interactions, but latent ones permitted. iter 11 shows a null state can
hold latent (sub-threshold) interactions — the null state is **poised, not
empty**. This unifies the framework's *embedded information* and *meta-null*
notions: a latent channel is embedded interaction-potential. *(Applied to
`nullstate.md` as an additive refinement note.)*

**7.2 Distinguish interaction *capacity* from interaction *event* — the sign of
an interaction. [APPLIED]** `interaction.md`'s `int → d` conflated the channel
with the event. The proof separates them: a channel (measurable by `TE > 0`,
iter 11) may exist without producing a deviation (`MI ≈ 0`). A **latent
interaction** (capacity) realizes into an **active interaction** (event) by
crossing a threshold — which is itself a **deviation**. iter 12 makes this a
**sign problem**: the latent/active distinction is the sign of the *locking
discriminant* `Disc = 1 − (Δω/2K)²` — active interactions have a **real** locked
phase-offset (realized: a deviation), latent interactions have a **complex** one
(unrealized: a channel only), with `|Im ψ*| = arccosh(Δω/2K)` measuring how
latent. (Sign of the *discriminant*, not of the coupling — a separate axis.)
*(Applied to `interaction.md` as a "Latent vs Active" refinement section.)*

**7.3 "Information on an interaction" is a graded certificate, not a local fact.**
`information.md` treats transmitted information as primitive. iter 8's ladder
(*related < directed < connected*) shows that certifying information rode a
*specific* edge requires observing the rest of the graph (conditional TE);
pairwise measures confuse common causes with genuine edges. Suggested refinement:
tag informational claims with their certificate level.

**7.4 Emergent structure is not automatic — it needs a mechanism.** iters 4–5
showed the doc's "functional modularity emerges from experience" is *false as
specified* (naive Hebbian coupling homogenizes) but *rescuable* with per-pair
credit + competition. `system.md`'s emergence should inherit this: emergence is
real (iters 9–10) but conditional on the right learning ingredients, not a given.

**7.5 Clock relativity: certificates and relations are the portable content.
[PROPOSED — the canonical observer-relativity seam, D21/D22]** The canonical
layer explicitly defers the observer-relativity ontology; iter 16 supplies its
first witness and a working discriminator. Under tested representations of the
*same* trajectory (decimation/resampling and a smooth monotone re-clocking),
classification certificates (screened-off, regime class) and relational
statistics (the distribution of simultaneous phase differences) are
**invariant**, while
magnitudes (TE in bits) and rate observables **covary** with the clock — so
coordinate disagreement is measurably *not* a physical deviation, and a
measurement claim should be typed by whether it survives re-clocking.
Participant-clock desynchronization is meanwhile a *physical* axis, distinct
from representation: a direct edge transmits only under co-presence, whereas a
persistent medium (iter 15) buffers desync in proportion to its persistence
time (`W50 ∝ 1/γ`) and wears its mediation as a persistent TE-lag tail —
external memory visible in the information plane. Suggested refinement: tag
rate/magnitude claims as observer-relative measurements and reserve ontic
status for transformation-invariant certificates. *(Typed transformations now
live in the canonical metalanguage; this entry remains evidence, not the
formalism.)*

---

## 8. What is NOT yet proven (the honest ledger)

- **The active/basic layer.** *Memory* is realized (the learned coupling `K`,
  iters 2–5) and now has an **operational test** — iter 13 shows a locked
  module recovers its stored *pattern* after a disruption *if the memory is
  protected* (resilience = pattern recovery, with a threshold past which an
  unprotected memory is rewritten and the identity is lost). But *awareness*,
  *reflection*, *experience*, *knowledge*, *vision*, *understanding* (Overview
  §Math Constructs) still have **no single-case proof**. The active layer is the
  next frontier.
- **Damage recovery / graceful degradation** — **first result (iter 13):** a
  protected memory restores the pattern from even a total phase scramble; an
  unprotected one has a resilience threshold then loses the identity.
  *Open:* multistable (associative-memory) recovery into a genuinely different
  *stored* pattern; structural lesions of `K`; the collapse edge vs the iter-3
  separatrix.
- **Clock relativity: scope.** iter 16's invariance results hold for
  re-clockings that still resolve the medium's bandwidth; the **admissibility
  boundary** — how coarse or distorted an observation clock can get before the
  verdicts themselves fail (aliasing) — is unmapped, and the participant-clock
  results are N=2 in one substrate. Canonical Draft 0.2 now types clock
  transformations and resampling, but the formalism awaits author review.
- **Universality.** Every proof here is in *one* substrate (coupled oscillators).
  CPAF's cross-substrate universality is argued, not computationally proven; a
  second substrate would raise confidence.
- **A global (system-level) threshold.** The `1/√2` onset is exact per *pair*;
  the many-oscillator transition is continuous with no special value. A
  system-level deviation threshold remains open.

---

## 9. Reproducing the proofs

```
pip3 install -r ../KSOMHeb/requirements.txt      # numpy + matplotlib
python3 ../KSOMHeb/verification/iter6_locking_threshold.py       # deviation
python3 ../KSOMHeb/verification/iter7_information_transition.py  # information
python3 ../KSOMHeb/verification/iter8_transfer_entropy.py        # interaction (directed)
python3 ../KSOMHeb/verification/iter9_entity_as_cluster.py       # entity
python3 ../KSOMHeb/verification/iter10_grown_entities.py         # system / emergence
python3 ../KSOMHeb/verification/iter11_interaction_vs_deviation.py  # interaction vs deviation
python3 ../KSOMHeb/verification/iter12_interaction_sign.py          # latent vs active (the sign)
```

Each prints `ALL PASS` and writes its figure. Full index:
`../KSOMHeb/verification/README.md`. Conceptual walkthrough:
`../KSOMHeb/textbook/` (Chapters 7–12 are the bridge arc; the Intermission is the
mid-bridge synthesis).
