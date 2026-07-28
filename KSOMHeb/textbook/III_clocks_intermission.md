# Volume II Intermission — Clocks: whose time does a system run on?

> *A second hop sideways, and a paired one. The stigmergy intermission asked
> **where** a system keeps its coordination and memory — inside or outside. This
> one asks **when**: what has to be simultaneous for an interaction to happen at
> all, and what happens to our measurements when the observer's clock is not the
> system's. One witness (iter 16), two separated questions, and one contribution
> each way. No grand claims — and one standing guardrail from the formal spine,
> honored throughout: coordinate disagreement is not a physical deviation.*

## Two questions wearing one word

"Does this claim survive a clock change?" is ambiguous, and the ambiguity is the
whole problem. There are two different clocks in it:

- **Participant clocks (physical).** The agents themselves acting at different
  times. An ant lays pheromone at noon; another follows it at dusk. They never
  meet. Whatever coordination exists between them is *really* asynchronous —
  a fact about the system, not about anyone's description of it.
- **The observer's clock (representational).** The analyst's sampling rate, lag
  units, time parameterization. Re-sampling a trajectory changes nothing the
  system does; if a claim flips under it, the claim was about the
  *representation*, not the system.

The canonical layer flagged this seam and deferred the ontology (`GPTSol.md`,
D21), with an explicit guardrail: don't let a change of coordinates masquerade
as a deviation. The seed intuition on our side (Ziggy's) was that stigmergy is
where the seam becomes concrete: an edge through a medium **must** account for
different wall-clock times — the writer's "now" reaches the reader as an
integrated past — which suggests that an *internal* system is precisely one
whose parts run on closely aligned clocks. Iter 16 tests both halves and keeps
them apart.

## Participant clocks in the metalanguage

- **[DEF] Co-presence.** Two entities are *co-present* over an interval when
  both are available to the interaction — sending and receiving on the same
  wall clock, within the interaction's own timescale.
- **[CW] A direct edge requires co-presence.** Gate a genuine direct coupling
  by simultaneous presence and sweep the overlap `f` of the agents' duty
  windows: at `f = 0` (never co-present) the pair sits at the drift baseline;
  coordination rises with `f` to full lock at `f = 1`. A direct interaction is
  a conversation — it only transmits while both parties are there.
- **[CW] A medium removes the requirement.** The same two agents, coupled
  *only* through iter 15's deposit–evaporation medium and **never
  co-present**, lock anyway (`r = 0.99` at `f = 0`). Each visits the trail on
  its own schedule; the trail carries the coordination across the gap.

So externalizing memory (the stigmergy result) also **externalizes the
simultaneity requirement**. Each agent needs only to share a clock with the
medium — never with the other agent. And that gives the closure axis a temporal
reading worth stating on its own:

> **[PROP] An *internal* system is one whose coordination requires closely
> aligned participant clocks.** Direct edges buy speed and pay for it in
> simultaneity; mediated edges buy clock-freedom and pay for it in lag.

How much clock-freedom? That's a measurable budget:

- **[CW] The clock-slack budget scales with persistence.** Sweeping the window
  length `W` against the evaporation rate `γ`, the tolerated desynchronization
  scales as `W₅₀ ∝ 1/γ` — the curves collapse in `γW` — with `γ·W₅₀ ≈ 5–7.5`
  held across an 8× range of `γ`. A few e-foldings, not one, and the excess is
  itself the lesson: evaporation decays the trail's **amplitude**, but its
  stored **phase** — the direction it points — persists. Coordination survives
  until the returning pull `K|M| ~ e^(−γW)` drops below the drift it must
  correct, so the budget is `W₅₀ ≈ (1/γ)·ln(margin)`. The medium is a phase
  memory whose amplitude is the clock-facing part.

(Honesty note: the original conjecture said "budget ≈ one persistence time."
The witness says *proportional to* the persistence time, with a logarithmic
prefactor set by the coupling-to-drift margin. The scaling held; the constant
taught us something. That's the house pattern — run the thing, keep the
surprise.)

## The memory signature

Iter 15's fingerprint for mediation — conditioning on the medium screens off
the edge — was honest but modest (14% vs 22% survival). Iter 16 found a second
fingerprint in the *lag structure*, and it is not modest:

- **[CW] A direct edge forgets; a mediated edge remembers.** Compare the two
  at **matched coordination** (`r ≈ 0.97` both — an unmatched sub-threshold
  direct pair drifts, and its lag profile is a slip artifact, not a fair
  comparator). The direct edge's transfer entropy versus lag decays to the
  estimator floor within ~2 time units: a direct channel forgets at its own
  relaxation time. The mediated edge's transfer **persists** — 81% of peak
  out to 4 time units — because the medium retains the writer's past and keeps
  it informative about the reader's future.

This is external memory made *visible in the information plane*: the TE-lag
tail is the trail's retention, measured in bits. It also answers the seed
intuition directly — yes, MI and TE on a stigmergic edge must account for
wall-clock offsets, because the influence arrives as an integral over the
writer's past. Single-lag readings systematically under-describe a mediated
edge; the tail is where its nature shows.

## The observer's clock: what survives re-representation

Now hold the physics fixed. Take *one* mediated trajectory and re-represent it
three ways: decimate ×2, decimate ×4, and resample it along a smooth, monotone
time-warp (an observer whose clock runs unevenly and, on average, 1.3× slow).
Nothing physical differs between these four descriptions. What survives?

- **[CW] Verdicts survive; magnitudes don't.** The screening certificate
  ("conditioning on `M` collapses the edge") and the regime classification
  come out identical in all four representations — while the raw transfer
  entropy swings 1.4× across them. The *bit-values* of MI/TE are measurements,
  indexed to an observer's clock; the *certificate verdicts* are the portable
  content.
- **[CW] Rates covary; relations are invariant.** The warped observer reads
  every rate scaled by her warp factor (a drifting pair's phase-slip rate
  reads ×1.30 — exactly `c`). But the **relational** structure — the
  distribution of the simultaneous phase difference `θ₁ − θ₂` — is unchanged
  (L1 distance 0.029), whereas an actual physical change (decoupling the
  pair) reshapes it completely (0.739).

That last dissociation is the discriminator the guardrail asked for:

> **[PROP] A clock change moves rates; a physical change moves relations.**
> Coordinate disagreement is measurably *not* a physical deviation: it
> rescales rate observables and magnitude observables while leaving relational
> statistics and certificate verdicts invariant. A claim should be typed by
> which side of that line it lives on.

## The contribution: two handles for the formal spine

Both halves hand something to the canonical layer:

1. **Co-presence and clock-slack, for the interaction/stigmergy accounts.**
   "Direct" and "mediated" now differ *temporally*, not just causally: a
   direct interaction requires co-presence; a stigmergic one buys
   desynchronization tolerance proportional to the medium's persistence, and
   wears its mediation as a persistent transfer tail. This composes with the
   medium-relative null (iter 15): the medium defines both the agent's
   reference regime *and* the clock it must align with.
2. **An invariance criterion for the deferred observer-relativity ontology.**
   The canonical layer can now say something operational without committing
   metaphysically: under admissible re-clockings, **certificates and
   relational statistics are the observer-portable content; rates and
   magnitudes are observer-relative measurements**. Measurement claims should
   carry their clock the way canonical claims already carry their scale `λ`.
   The typed clock-transformation formalism itself belongs to the canonical
   layer — iter 16 is the evidence, not the formalism.

## Threads it ties together

| Strand | How the clock result connects |
|---|---|
| **Stigmergy** (iter 15) | gets its second characterization: the medium is not just external memory but a **clock buffer** — it removes the simultaneity requirement that defines a direct edge. Closure↔stigmergy and aligned↔buffered clocks are the same axis seen spatially and temporally. |
| **Memory** (iters 13–14) | external memory holds a *past*, and that past is now directly measurable: the TE-lag tail is retention in bits. Internal memory (`K`) stores structure; the medium stores *recency* too — its amplitude literally decays like a timestamp. |
| **Certificates** (iter 8) | the ladder gains a rung of meaning: certificates aren't just what survives confounders — they're what survives **observers**. Related/directed/connected verdicts travel between differently-clocked analysts; bit-counts don't. |
| **Entity / closure** (iters 9–10) | a locked cluster is the limiting case of clock alignment — one shared effective frequency *is* a shared clock. Entities are where participant clocks fuse; stigmergic collectives are where they never have to. |
| **Deviation** (iter 6) | the guardrail, discharged: a re-clocking that changes measured rates does **not** cross any deviation threshold — the Δθ distribution that defines the locked pattern is invariant. Deviations are relational events, and relations don't move with the observer. |

## Where it sits, and what's open

Clock relativity is **not a new primitive** — it's a typing discipline plus two
measurable facts (the slack budget; the invariance split). What's genuinely
open, in order of bite:

1. **The admissibility boundary.** The invariance results hold for
   re-clockings that still resolve the medium's bandwidth; decimating ×4
   already pushes the conditional-TE estimator to its floor. Somewhere past
   that, verdicts *do* fail (aliasing) — mapping where, and stating
   admissibility as a theorem about sampling versus system bandwidth, is the
   natural next witness.
2. **The typed formalism.** Clock transformations, observation maps, and the
   invariant/covariant split, stated in the canonical metalanguage — GPT's
   deliverable, now with a witness to check it against.
3. **The rotating-frame caveat.** Iter 15/16 work in a frame with slow common
   rotation (a fast-spinning deposit averages to zero in the medium). A fast
   common clock plus a slow medium is exactly the regime where participant
   and observer questions could re-entangle — untested.
4. **Scope honesty.** N=2 for the schedule results; one substrate; the `W₅₀`
   ratio reads 5.4× where perfect `1/γ` scaling predicts 8× (the fixed
   detuning penalizes long windows equally at every `γ` — a known confound,
   reported, not hidden).

## Try it yourself

Pick an asynchronous system you live in — an email thread, a shared codebase,
a family whiteboard. First, the **participant** side: name the medium, its
persistence time, and estimate the clock slack it buys (how long can
contributors stay out of sync before coordination decays? does that time track
how long the medium retains its signal?). Then the **observer** side: write
down two claims about the system — one that would change if you sampled it
differently ("they commit five times a day") and one that wouldn't ("these two
files always change together"). The first is a rate — yours. The second is a
relation — theirs. If you can feel the difference, you have the whole
intermission.

---

*Witness: `../verification/iter16_clock_relativity.py` (all six checks) ·
Decision log: `../DECISIONS.md` D21–D22 · Stigmergy half of the axis:
`II_stigmergy_intermission.md`, iter 15 · Canonical seam:
`../../GPTSol.md` (observer relativity), `../../Framework/CanonicalDefinitions/
METALANGUAGE.md` §12 · Evidence-layer entry:
`../../Framework/ComputationalProofs.md` §7.5.*
