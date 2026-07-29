# Chapter 9 — Interaction vs common cause

> *Where the information measure we just earned turns out to answer the wrong
> question — and fixing it costs exactly one thing: being able to see the rest
> of the graph.*

Chapter 8 ended with three unbuilt spans, and flagged one as urgent: mutual
information sees *correlation*, not *causation*. We had grounded "information"
as the MI born at a locking event (iteration 7), but MI cannot certify that the
**edge** is what carries it. Two oscillators driven by a shared external source
light up with MI while having no coupling between them at all. If CPAF's
"information on an interaction" is to mean anything, we need to tell those
situations apart. This chapter builds that span — and, in this book's tradition,
the honest result is more interesting than the advertised one: the standard fix
only half-works, and *where* it fails is itself the lesson.

## 9.1 Three graphs, one MI

Make the blind spot concrete. Take the two-oscillator setup from iterations 6–7
(detuned pair, noise) and prepare three *different causal graphs*:

1. **Coupled** `1 ↔ 2`: a genuine bidirectional edge, `K > Kc`, locked.
2. **Common drive** `Z → 1, Z → 2`: **zero** coupling between 1 and 2; each is
   entrained by a hidden third oscillator `Z` (a noisy source neither "knows"
   the other is listening to).
3. **One-way** `1 → 2`: oscillator 2 follows 1, but 1 never feels 2 — the
   architecture's asymmetric-coupling extension (`Kᵢⱼ ≠ Kⱼᵢ`), realized.

In all three, the pair looks synchronized (`R ≈ 0.9`), and iteration 8 measures
the MI between the two phases at **1.89 / 1.51 / 1.90 bits** respectively. Same
order, no separation: *MI cannot tell these graphs apart* (Check A). In the
common-drive case there are 1.5 bits of perfectly real shared information — and
no edge. The information sits on paths through `Z`, a vertex our pairwise
measurement doesn't even know exists.

## 9.2 Transfer entropy: asking a directed question

The standard repair is to change the question from "do these two know about
each other?" to "does one help *predict* the other?" **Transfer entropy** from
`X` to `Y` is the information `X`'s present carries about `Y`'s *future*, beyond
what `Y`'s own past already says:

```
TE(X→Y) = I( Y_{t+τ} ; X_t | Y_t )
```

Read the conditioning carefully — it does the work. `Y_t` already predicts
`Y_{t+τ}` (an oscillator mostly keeps rotating); TE only counts what `X_t` adds
*on top of that*. Two properties follow immediately:

- **It is directional.** `TE(X→Y)` and `TE(Y→X)` are different quantities —
  unlike MI, which is symmetric by construction.
- **It is dynamical.** TE lives on trajectories (a time-lagged conditional MI),
  not on the static joint distribution MI reads. It's asking whether influence
  *flows*, per unit time, along a specific direction.

Implementation-wise it's the same machinery as iteration 7 — bin the phases,
build a histogram, sum `p·log(p/…)` — just over the triple `(Y_{t+τ}, X_t, Y_t)`
instead of a pair, with a surrogate correction (circularly time-shift the
source, which destroys directed pairing but preserves each signal's own
statistics) subtracting the finite-sample floor.

## 9.3 The estimator trap: fake transfer from coarse bins

Before the results, a bug-that-wasn't-a-bug worth its own section (this book's
Appendix A instinct). Our first TE estimate used 8 bins for everything — and
found `TE(2→1) = 0.11 bits` in the **one-way** scenario, where oscillator 2 has
*no influence whatsoever* on 1. Real code, clean math, confidently wrong answer.

The leak: when the pair is locked, `θ₂` is a tight copy of `θ₁`. Binning `Y_t`
into 45° cells throws away `Y_t`'s fine position — but the correlated `X_t`
still carries it. So `X_t` "predicts `Y`'s future" merely by *re-supplying
sub-bin information about `Y`'s present* that the coarse conditioning
discarded. That's not transfer; it's quantization error wearing transfer's
clothes. The fix is to bin the **conditioning** variable finely (24 bins) while
keeping the others coarse enough to estimate: the phantom 0.11 bits collapses to
0.000, and the genuine direction survives. Moral for any information-theoretic
pipeline: *the conditioning variable is the one you can't afford to blur* —
whatever you fail to condition away gets credited to your source.

## 9.4 Iteration 8: the half-win

`verification/iter8_transfer_entropy.py` runs the three scenarios side by side
(same noise, 100k samples each) and checks four claims:

**Check A — MI is blind.** As above: 1.89 / 1.51 / 1.90 bits across three
different graphs. Confirmed, quantitatively.

**Check D — TE gets direction for free.** In the one-way scenario,
`TE(1→2) = 0.161 bits` while `TE(2→1) = −0.001` — statistically zero, the
correct null. MI meanwhile reads 1.90 bits, identical to the bidirectional
case. A *directed* interaction finally has a directed readout — the asymmetric
`Kᵢⱼ` extension now has an operational signature (this closes the
directionality tension from the mapping notes).

**Check B — but TE is fooled by the common cause too.** Here's the honest
headline. In the common-drive scenario, pairwise TE reads **0.036 bits against
the coupled pair's 0.047** — same order, no separation. And this is *not* an
estimator artifact to be tuned away. Each driven oscillator is a noisy sensor
of the hidden `Z`; oscillator 1's present genuinely improves prediction of
oscillator 2's future, because it carries an independent reading of the source
that is driving 2. The predictive transfer is real. The **edge** it implies is
not. *Prediction is not causation*, and TE is a prediction measure.

**Check C — conditioning resolves it, both ways.** Hand the estimator the
source and compute `TE(1→2 | Z)`: the common-drive pair's transfer drops to
**−0.004 bits** — dead. Run the same conditioning on the genuinely coupled pair
(for which `Z` is irrelevant): TE is **untouched** (0.047 → 0.049). A double
dissociation: conditioning on the confounder kills exactly the spurious
transfer and none of the real one. The edge is certified — but only because we
could *observe* `Z`.

## 9.5 The ladder: related < directed < connected

Putting iterations 7 and 8 together, "information on an interaction" resolves
into three rungs, each strictly stronger and strictly more expensive:

| Rung | Measure | Certifies | Costs |
|------|---------|-----------|-------|
| **Related** | mutual information `I(θᵢ;θⱼ)` | a relationship exists *somewhere* | observing the pair |
| **Directed** | transfer entropy `TE(i→j)` | who predicts whom, per direction | observing the pair's *dynamics* |
| **Connected** | conditional TE `TE(i→j \| rest)` | this edge carries the influence | observing the *rest of the graph* |

The progression has a clean epistemic reading that CPAF should inherit: **what
you can claim about an edge depends on how much of the graph you can see.** A
pairwise observer — however sophisticated — cannot distinguish a genuine
interaction from a hidden common cause; that distinction only exists relative
to an observed context. "Information on an interaction" is not a property a
pair carries around; it's a certificate issued by a wider measurement. In CPAF
terms: an *interaction* is only fully distinguishable from a *coincidence of
deviations* at the **system** level, where confounders are inside the
measurement rather than outside it.

## 9.6 The honest boundary

What iteration 8 does **not** establish:

- **Full causal discovery.** Conditioning on `Z` worked because we knew `Z` and
  could measure it. In a real network the "rest of the graph" is large; the
  right conditioning set is a research field (causal inference), not a
  histogram. We've shown the *mechanism* of the fix, on the minimal case —
  three vertices — not a general procedure.
- **Learned asymmetric coupling.** The one-way scenario *imposes* `Kᵢⱼ ≠ Kⱼᵢ`;
  the Hebbian rule as specified still learns symmetric `K`. TE gives directed
  interactions a readout, not yet a learning rule that produces them.
- **Anything about clusters.** All of this is two (plus one hidden) oscillators.
  The entity-as-cluster span from Chapter 8 remains open, and TE across
  coarse-grained clusters is untested.

## 9.7 What to carry forward

- MI certifies **related**, not **connected**: three different causal graphs
  (coupled, common-driven, one-way) carry the same MI (iter 8, Check A).
- **Transfer entropy** `TE(X→Y) = I(Y_{t+τ}; X_t | Y_t)` adds direction: a
  one-way coupling reads `TE(2→1) ≈ 0`, `TE(1→2) ≫ 0` — the asymmetric-`Kᵢⱼ`
  extension has an operational signature (Check D).
- **Pairwise TE is still fooled by a hidden common cause** — the predictive
  transfer is genuine even though the edge is absent; prediction ≠ causation
  (Check B).
- **Conditional TE** `TE(X→Y|Z)` resolves it as a double dissociation: kills
  the spurious transfer, spares the real edge (Check C) — at the price of
  observing the confounder.
- Estimator lesson: **bin the conditioning variable finely** — coarse
  conditioning leaks sub-bin correlation into fake transfer (0.11 phantom bits
  in our first run).
- For CPAF: information claims are graded by observability — *related <
  directed < connected* — and the top rung is a system-level certificate, not a
  pairwise property.
- *Since adopted and mirrored:* the ladder is now canonical — context-indexed
  certificate levels in the gold-standard `information.md` — and iter 15 found
  the confounder's mirror image: conditioning that kills a **genuine** edge,
  because the third variable is the *pathway* (a stigmergic mediator), not a
  common cause. Same tool, opposite causal role (Intermission II).

---

### Try it yourself

In the common-drive scenario, make the confounder *partially* hidden: condition
the TE not on `Z` itself but on a noisy proxy `Z̃ = Z + ξ` with increasing noise
on `ξ`. **Predict first:** should the spurious `TE(1→2 | Z̃)` return gradually or
all at once, and what does that imply for a CPAF observer whose view of the
"rest of the graph" is merely *imperfect* rather than absent? Then modify
`iter8_transfer_entropy.py` (the `z=` argument of `transfer_entropy_bits`) and
check. (You should find the certificate degrades smoothly — partial
observability buys partial confidence in the edge, which is a very CPAF-shaped
conclusion.)

---

*Runnable: `verification/iter8_transfer_entropy.py` · Grounds the third
unbuilt span of Ch 8 §8.4 and the directionality tension in
`../CPAF_MAPPING_NOTES.md` · Symbols: `../CHEATSHEET.md`.*
