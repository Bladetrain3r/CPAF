# Chapter 8 — The first bridge: oscillators as CPAF primitives

> *Where the metric stops being self-contained and starts trying to speak
> CPAF's language — carefully, marking what's earned and what's still a
> conjecture.*

Everything up to here built and stress-tested a *measure*. But K-SOM-Heb was
never meant to be an island; its whole reason for existing is to give CPAF —
the framework that stages cognition from a null state upward — something
concrete and computable to stand on. This chapter is the first attempt to
connect the two: to show that the oscillator primitives we've been simulating
line up with CPAF's *foundational* concepts (null state, deviation, interaction,
information, entity, system). It is a **bridge, not a proof**. Some spans are now
load-bearing (verified by an iteration); others are rope and hope (plausible,
untested). We label which is which, because pretending a conjecture is a result
is exactly the failure mode this book was written to avoid.

## 8.1 The reframing: the model is already a graph

The key that opens the door is small and structural. A coupling connects exactly
two oscillators — it is *the vertex pair of a connection*. Once you see that, the
whole model re-reads as a graph, and CPAF's vocabulary is itself graph-shaped:

- an **oscillator** is a vertex,
- a **coupling `Kᵢⱼ`** is an edge,
- the **whole population** is the graph.

CPAF's foundational concepts drop onto that structure with surprisingly little
forcing. Here is the correspondence, each row graded by how well it's supported:

| CPAF concept | Oscillator primitive | Status |
|--------------|----------------------|--------|
| **Entity** | an oscillator (vertex); recursively, a locked cluster acting as one | edge: clean · cluster: **conjecture** |
| **Interaction** | the coupling `Kᵢⱼ` — the channel between two entities | clean fit |
| **Deviation** | an edge crossing its locking threshold `Kc = \|Δω\|/2` | **grounded (iter 6)** |
| **Information** | the mutual information `I(θᵢ; θⱼ)` that appears at that crossing | **grounded (iter 7)** |
| **Null state** | incoherent population — couplings may exist but none has locked | reframed (see 8.3) |
| **System** | the whole graph: collective `r`, modularity `Q` | plausible |

## 8.2 The two grounded spans

Two of these are not analogies — they're backed by passing iterations, and they
are the reason this bridge is worth building at all.

**Deviation = a locking event.** CPAF's most fundamental change is the step from
undifferentiated null to a first *deviation*. Iteration 6 gave that step a sharp,
derived location: two oscillators drift (undifferentiated) below `Kc = |Δω|/2`
and lock (differentiated, structured) above it — a saddle-node bifurcation, with
the coherence at onset pinned to exactly `1/√2`. A deviation, in oscillator
terms, is an edge crossing that threshold. It is not a vague "something changed";
it is a specific, measurable bifurcation.

**Information = what appears at the deviation.** Iteration 7 then showed that the
crossing is precisely where *information* is born: mutual information between the
two phases climbs from ~0 (drifting, independent) to ~2.7 bits (locked, related)
as `K` passes `Kc`. So the deviation doesn't merely change a state — it *creates
shared information on the edge*. Better still, iteration 7 proved this information
is a genuinely new quantity, not a relabelling of coherence: deep in the drift
regime the order parameter `r` already reads ~66% of its maximum while
information sits near zero. `r` overreads; information discriminates. CPAF gets an
information primitive that its coherence metric could not have supplied.

Put together: **a deviation is the birth of information on an interaction.** That
sentence is now anchored to two experiments, not to hope.

## 8.3 The subtle reframe: what "null" really means

The bridge also sharpens a CPAF concept. Naively, the null state — maximal
entropy, no structure — sounds like "no connections." But the dynamics say
otherwise. A population can be dense with couplings and still sit in the null
state, provided every edge is *below* its locking threshold: lots of latent
channels, no actual locking, no deviations, `r ≈ 0`. So:

> The null state is the absence of **deviations**, not the absence of
> **interactions**.

That's a meaningful distinction CPAF can use. A "quiet" system full of
sub-threshold couplings is poised — a small increase in coupling (or decrease in
noise, or in frequency spread) tips edges over `Kc` and deviations bloom. Null is
not emptiness; it's latency below threshold.

## 8.4 The unbuilt spans (marked, not hidden)

Three parts of the bridge are conjecture, and the book's honesty depends on
saying so plainly:

1. **Interaction vs deviation — a noun and a verb.** We treat the edge existing
   (interaction) and the edge locking (deviation) as distinct: the channel versus
   the event on it. This is a clean conceptual split, but "an interaction is a
   channel that *may* produce a deviation" hasn't been given its own test; it's a
   definition we've adopted, not a result.

2. **Entity-as-cluster — the recursion.** CPAF leans hard on recursion: simple
   parts compose into higher-order units that themselves interact. The natural
   claim is that a *locked cluster* (iteration 5's modules) behaves as a single
   coarse-grained entity — one effective phase, one effective frequency. Plausible,
   and central to the whole framework — but **untested**. Until we coarse-grain a
   module and show it acts like one oscillator, entity-as-cluster is a promissory
   note.

3. **Information's blind spot.** Mutual information sees correlation, not
   causation: two oscillators driven by a *common* external signal would share
   high MI with no coupling between them at all. So MI grounds "information" but
   cannot yet distinguish a genuine **interaction** from a shared cause. Doing so
   needs a *directed* measure — transfer entropy — which is exactly the next
   iteration (Chapter 9). Until then, our "information on an edge" can't fully
   certify that the edge is what carries it.

## 8.5 What we can and can't claim

We **can** say: CPAF's deviation and information have concrete, verified
oscillator definitions, and its null state has a sharper reading (sub-threshold
latency). That is a real bridge — the first place the metric earns its keep as a
*model of the framework*, not just a number.

We **cannot** say: that K-SOM-Heb *is* CPAF's basic layer. The recursion
(entity-as-cluster) is untested, the interaction/deviation split is a definition
rather than a finding, and information can't yet be pinned to a specific edge.
Those are the next spans to build — and each is a falsifiable experiment, which
is the only kind of bridge this project trusts.

## 8.6 What to carry forward

- The model is a **graph**: oscillators = entities, couplings = interactions.
- **Grounded:** *deviation* = an edge crossing `Kc` (iter 6); *information* =
  the mutual information born at that crossing (iter 7). A deviation is the birth
  of information on an interaction.
- **Reframed:** the *null state* is the absence of deviations, not of
  interactions — latency below threshold.
- **Still conjecture:** interaction-vs-deviation as noun/verb; entity-as-cluster
  (recursion); and separating true interaction from common drive (needs transfer
  entropy — Chapter 9).

---

### Try it yourself

Pick the correspondence you trust *least* from §8.1's table and write the
one-paragraph experiment that would confirm or break it — what you'd simulate,
what you'd measure, and which outcome would falsify the mapping. (Worked example
for entity-as-cluster: drive a synchronized cluster with an external oscillator
and measure whether the *cluster's* mean phase entrains as if it were a single
oscillator with an effective frequency; if it fragments instead of entraining,
the "cluster = entity" span fails.) This is how a conjecture row becomes a
grounded one — and how the bridge gets built, span by span.

---

*Grounded by: `verification/iter6_locking_threshold.py`,
`iter7_information_transition.py` · Working notes: `../CPAF_MAPPING_NOTES.md` ·
Symbols: `../CHEATSHEET.md`.*
