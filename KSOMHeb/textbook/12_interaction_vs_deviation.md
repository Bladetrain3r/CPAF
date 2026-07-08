# Chapter 12 — Interaction vs deviation: the noun and the verb

> *Where the last conjectural span of the bridge gets its experiment — and the
> experiment corrects us twice on the way to confirming the claim.*

Chapter 8 laid out the CPAF bridge and marked three spans as unbuilt. Two are
now load-bearing: the information ladder (Chapter 9) and entity-as-cluster,
grown and imposed (Chapters 10–11). One remained a *definition dressed as a
mapping*: we had asserted that an **interaction** (a coupling — the channel)
and a **deviation** (the locking event on it) are different kinds of thing —
the edge is the noun, the locking is the verb — but we had never given that
split its own falsifiable test. This chapter does, and because the split was
the softest claim in the bridge, the test was built to be hard: designed so
that if interaction and deviation are secretly the same event, the checks fail.

They don't fail. But two of our predictions about *how* they'd pass turned out
wrong, and — in this book's tradition — the corrections are the most
interesting part.

## 12.1 Turning a definition into two curves

The dichotomy only becomes testable once each half has its own measurable
signature:

- **Interaction = directed influence on the channel.** Measured by transfer
  entropy `TE(1→2)` (Chapter 9). The physics guarantees this is nonzero the
  instant `K > 0`: the coupling term `K·sin(θ₁ − θ₂)` perturbs oscillator 2's
  velocity in a way that depends on oscillator 1, *whether or not they lock*.
  Influence is a property of the channel being open.

- **Deviation = the locking event.** The saddle-node bifurcation at `Kc`
  (Chapter 7), measured two independent ways: the **winding number**
  `Ω = |⟨d(θ₁−θ₂)/dt⟩|` — a pure dynamics quantity, large when the pair drifts
  (no deviation), zero when locked (deviation present) — and the **mutual
  information** MI, which jumps at `Kc` (Chapter 7). Deviation is a property of
  a sustained relationship existing.

The falsifiable claim: **these decouple.** There should be a band of coupling
*below* `Kc` where the pair is provably still drifting (Ω large, MI at floor —
no deviation) yet `TE(1→2)` is already significant (influence flowing).
Influence without a deviation. If instead TE only switched on at `Kc`, in
lockstep with the deviation, the noun and the verb would be one event and the
split would collapse.

## 12.2 The rig, and why it carries its own controls

Because this was the weakest span, iteration 11 is the most heavily
controlled in the book. The key design choice is a **one-way coupling**
(1 → 2 only): oscillator 1 runs free, oscillator 2 is driven. This buys three
controls for free:

1. **A null direction.** No channel exists from 2 to 1, so `TE(2→1)` must read
   ~0 at *every* `K` — including deep in the locked regime, where `θ₁` and
   `θ₂` are tightly correlated. A null that survives strong correlation is a
   live test that the estimator reports *transfer*, not correlation (the
   Chapter 9 conditioning lesson, on trial again).
2. **An absolute null.** At `K = 0` there is no channel at all; `TE(1→2)` there
   must sit within surrogate noise. If it does, the sub-threshold ramp we're
   about to claim can't be an estimator bias floor.
3. **A surrogate null distribution** on every TE estimate (circular
   time-shifts of the source), so significance is a `z`-score, and we only
   claim the dissociation from a *band* of consecutive significant points, not
   one lucky `K`.

## 12.3 The result: influence leads, deviation follows

The core claim holds, cleanly and at two detunings. Below `Kc`, in a band
where the winding number says the pair is unambiguously drifting
(`Ω_norm > 0.8`) and MI is at its floor (~0.06 bits — no shared relationship),
`TE(1→2)` is significant at `z` in the *hundreds*. At `K/Kc = 0.58` — the last
point before the pair even begins to bend toward locking — the interaction is
already at **63% of its peak strength** while the deviation has barely begun
(MI 6% of its maximum, the locking order parameter 19%). Interaction is most
of the way on; deviation is off. The noun exists, and carries influence,
before the verb happens.

And the controls hold where the claim lives: `TE(1→2)` at `K = 0` sits at
`z ≈ −1` (no bias floor), and across the entire drift regime the null
direction `TE(2→1)` stays below `z ≈ 3`. The sub-threshold influence is real.

> **The noun/verb split is now a finding:** an interaction is a channel that
> carries directed influence whether or not it has yet produced a deviation.
> Chapter 8's definition has become evidence.

## 12.4 Two corrections the experiment forced on us

Here is where the iteration earned its "test it harder" mandate — by refusing
two things we expected.

**Correction 1: interaction is not a simple ramp.** We predicted `TE(1→2)`
would rise monotonically — a ramp against the deviation's cliff. It doesn't.
It **peaks right at the locking onset** (`K/Kc ≈ 0.85`) and then *declines* as
the pair locks tightly. The reason is sound and, in hindsight, obvious: once
oscillator 2 is locked, its future is almost entirely predictable from its
*own* past (it just rotates in lockstep), so oscillator 1's present adds little
*new* information. Transfer entropy measures newly-supplied prediction, and a
locked target supplies its own. So the honest picture is not ramp-versus-cliff
but: **influence rises through the drift regime, peaks as locking begins, and
eases once the relationship is established and self-sustaining.** That is a
richer and more faithful statement than the one we set out to confirm — and it
is itself a small result about what "an interaction" looks like across a
deviation. (This non-monotonic-TE-across-synchronization is known in the
information-dynamics literature; we rediscovered it by being wrong first. See
Appendix S.)

The claim survives the correction intact, because the claim was never "TE is a
ramp" — it was "TE is significant where there is no deviation," and the drift
regime is exactly where TE is *climbing to* its peak. We just had to measure
the dissociation by comparing *values at a drift reference point* rather than
by the transition-width metric we'd naively reached for. When your check
assumes the wrong shape, fix the check, not the data.

**Correction 2: the null direction is not exactly zero — and finding out why
matters.** In the *locked* regime, the no-influence direction `TE(2→1)` creeps
up to `z ≈ 16`. Taken at face value that's "significant reverse transfer" on a
channel that does not exist — alarming, until you see the effect size: it's
~0.0014 bits against a forward signal ~60× larger. This is the **Chapter 9
conditioning bias, resurfaced through the lock's lag structure**: a locked
`θ₂` is essentially a *delayed copy* of `θ₁`, so coarsely binning `θ₁` (the
conditioning variable) leaves sub-bin position that the delayed `θ₂` can
"predict" — phantom transfer, exactly the mechanism from Chapter 9's §9.3,
now triggered by the tight correlation of a locked pair rather than a shared
drive.

Two lessons ride on it, both worth more than a clean pass would have been.
First, **with 100,000 samples, `z`-scores over-report.** A bias of a thousandth
of a bit becomes "16 sigma" when the sample is large enough; statistical
significance stops being the right lens and *effect size* takes over. The
honest null statement is not "`TE(2→1) = 0`" but "`TE(2→1)` is 60× below the
signal and consistent with the known estimator floor." Second, **our own rigor
apparatus caught our own estimator's limit** — the null direction was included
precisely so that if the method manufactured transfer, we'd see it, and we did.
A control that never trips teaches you nothing about whether it *could*.

## 12.5 What this settles, and what it doesn't

**Settled.** The interaction/deviation distinction is not bookkeeping. A
channel carries measurable, directed, significant influence in a regime where
no deviation has occurred and none is imminent. The noun precedes and
underlies the verb. All three of Chapter 8's unbuilt spans are now built —
the bridge from oscillators to CPAF's basic-layer vocabulary (null, deviation,
interaction, information, entity) has an evidenced span for each.

**Not settled.** (i) The experiment is one-way and two-body; a *mutual*
interaction (both directions live) and the interplay of many overlapping
channels is untested — and the entity-to-entity channel glimpsed in Chapter 11
is exactly where that gets interesting. (ii) The locked-regime null floor is
bounded and explained, not eliminated; a bias-free estimator (k-nearest-
neighbour TE, say) would sharpen the locked-regime numbers, though not the
conclusion. (iii) We have shown influence *without* deviation; we have not
shown a deviation *without* influence — and by construction we can't, since a
deviation requires a channel. That asymmetry ("every deviation rides on an
interaction, but not every interaction produces a deviation") is the precise
shape of the noun/verb relationship, and it is worth stating as such.

## 12.6 What to carry forward

- **Interaction** (directed influence, `TE`) and **deviation** (the locking
  event, winding number and MI) are **distinct and dissociable**: below `Kc`,
  in a provably-drifting band, `TE(1→2)` is significant at `z` in the hundreds
  while MI sits at its floor. Influence without a deviation.
- The relationship is **asymmetric**: every deviation rides on an interaction,
  but an interaction carries influence whether or not it has produced a
  deviation. The noun underlies the verb.
- **Interaction is not a monotonic ramp** — `TE` peaks at the locking onset and
  declines under strong locking (the locked target becomes self-predictable).
  The richer, truer picture.
- **Rigor notes:** with very large samples, use *effect size*, not `z`-scores,
  to read a null; and the locked-regime reverse-`TE` floor is the Chapter 9
  conditioning bias resurfacing through the lock's lag structure — named and
  bounded (~60× below signal), not reverse causation.
- Fix the check, not the data: our transition-width metric assumed a shape the
  physics didn't have; the finding survived once the check matched the theory.

---

### Try it yourself

We showed influence *without* deviation. Now probe the boundary from the other
side: in `iter11_interaction_vs_deviation.py`, replace the one-way coupling
with a **mutual** coupling and re-run. **Predict first:** does the
"influence-before-locking" band survive when *both* oscillators push on each
other, or does mutual influence hasten locking enough to erase the gap? And
what happens to the two-null control structure — you lose the clean null
direction, so how would you now prove the sub-threshold TE is real? (Hint: the
`K = 0` absolute null still works, and a phase-scrambled surrogate still gives
you a floor.) Designing the controls for the harder, symmetric case is most of
the exercise — and most of what rigor actually is.

---

*Runnable: `verification/iter11_interaction_vs_deviation.py` · Closes the last
unbuilt span of Ch 8 §8.4 (#1, interaction vs deviation) · Estimator and its
known bias: Ch 9 · Sources: `S_sources_and_inheritances.md`.*
