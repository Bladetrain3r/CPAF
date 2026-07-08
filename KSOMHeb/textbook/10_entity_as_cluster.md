# Chapter 10 — Entity as cluster

> *Where the model's biggest promissory note gets paid: a locked cluster
> doesn't just look like one thing — it obeys the one-thing laws, and its
> parts stop mattering.*

CPAF's architecture is recursive: entities interact, form systems, and those
systems become entities at the next level up, all the way from oscillators to
whatever you are. Chapter 8 flagged this recursion as the bridge's most
load-bearing conjecture and its least tested: *entity-as-cluster* sat in the
correspondence table marked "conjecture," a promissory note. This chapter
cashes it. The claim to test is precise: a **locked** cluster of oscillators,
coarse-grained to a single macro-phase, should behave as **one oscillator** —
and a collection that hasn't locked should not, so that entity-hood is
something the dynamics *create*, not a circle we draw for convenience.

There are really two criteria hiding in "behaves as one," and they're worth
separating because they answer different questions:

1. **Cohesion** — is the boundary real? Influence inside the cluster should
   dominate influence across its edge (a modularity-`Q` in *causal* terms
   rather than coupling terms).
2. **Closure** — is the coarse-graining lossless *at its own level*? Viewed
   from outside, the cluster should present one interface: its macro-state's
   future should be predictable from its macro-past alone, with the internal
   division of labor never leaking through.

Iteration 9 tests the second, stronger criterion — plus the sharpest possible
version of "acts like one oscillator": the cluster must obey the *quantitative
laws* we derived for single oscillators in iteration 6, one recursion rung up.

## 10.1 Coarse-graining: the cluster's one phase

A cluster of `M` members with phases `θᵢ` is summarized by the magnitude and
direction of its mean phasor — quantities we've had since Chapter 1, just
restricted to the cluster:

```
ρ·e^{iΘ} = (1/M) Σᵢ e^{iθᵢ}
```

`Θ` is the **macro-phase** (the candidate entity's "one phase") and `ρ` is the
internal coherence (how much the members agree). The question is whether `Θ`
deserves to be treated as a first-class oscillator.

## 10.2 The reduction: K_eff = κ·ρ

Here's the small piece of algebra that makes the whole chapter falsifiable.
Suppose the cluster is tightly locked: `θᵢ = Θ + δᵢ` with the offsets `δᵢ`
roughly constant. Couple an external probe oscillator `z` to *every member*
with per-edge strength `κ`, and average the member equations. Two things
happen:

- **The internal coupling terms vanish.** Every internal pair contributes
  `sin(δⱼ−δᵢ)` and `sin(δᵢ−δⱼ)` — antisymmetric, summing to zero. The cluster's
  internal machinery is invisible in its own mean motion.
- **The probe terms collapse via ρ.** Averaging `κ·sin(θ_z − Θ − δᵢ)` over
  members turns the spread of offsets into a single factor:
  `(1/M)Σᵢ sin(θ_z − Θ − δᵢ) = ρ·sin(θ_z − Θ)` (using the definition of `Θ`,
  which makes the mean phasor of the `δᵢ` purely real with magnitude `ρ`).

The macro dynamics that fall out are *exactly* iteration 6's two-oscillator
system:

```
dΘ/dt   = ω̄  + κρ·sin(θ_z − Θ)        (+ noise/√M)
dθ_z/dt = ω_z + κρ·sin(Θ − θ_z)        (+ noise)
```

with `ω̄` the mean member frequency and an effective coupling

```
K_eff = κ·ρ
```

Read that twice, because it's the chapter's headline: **a cluster's grip on
the world is its raw coupling discounted by its internal coherence.** A
distracted committee (low `ρ`) needs more per-edge coupling to entrain than a
unanimous one. And the noise on the macro-phase shrinks by `√M` — an entity
built from many parts is *steadier* than its parts. Both are predictions, not
metaphors, because iteration 6 now tells us exactly when the cluster should
lock to the probe:

```
κc = |ω_z − ω̄| / (2ρ)
```

and exactly what the locked-branch coherence should be, floor `1/√2` included.

## 10.3 Iteration 9: the one-thing laws, one level up

`verification/iter9_entity_as_cluster.py` builds three clusters of five
members with a fixed symmetric frequency fan — **tight** (`ρ ≈ 0.996`),
**mid** (`ρ ≈ 0.92`), and **weak** (below internal locking, `ρ ≈ 0.4`, the
designated non-entity) — and puts the claims to work:

**Check A — one effective frequency.** In the locked clusters, every member's
long-run velocity collapses onto `ω̄` (spread: 0.0% of natural), and `Θ`
rotates at `ω̄`. In the weak collection the members keep 93% of their natural
velocity spread: five clocks, no candidate entity. The shared clock is
*created* by locking.

**Check B — the pair law holds, ρ-discount included.** Sweeping the probe
coupling, the empirical entrainment threshold of `Θ` matches
`κc = |Δω|/(2ρ)` to within **2.5%** across two detunings and both cluster
tightnesses. The discount itself is resolved: the mid cluster (`ρ = 0.92`)
needs measurably more per-edge coupling than the tight one, and the data side
with the ρ-corrected prediction over the naive `|Δω|/2`. The committee really
does have to agree before it can negotiate.

**Check C — iteration 6's locked branch, one level up.** The measured
`(Θ, θ_z)` coherence along the locked branch follows
`R(κ) = cos(½·arcsin(Δω/2ρκ))` to 0.016 mean error — the same curve, with the
same `1/√2` floor at threshold, that governed two bare oscillators. Plotted
against `κ/κc`, tight and mid clusters collapse onto one universal branch.

A methods confession that earned its keep: our first version of this check
sampled "R at onset ≈ 0.707" at the first locked sweep point and **failed** —
reading ≈ 0.80. That wasn't the model failing; it was the check being wrong.
The locked branch is steep at onset (its slope diverges at `κc`), so any point
a finite grid can land on already sits well above the floor — and theory
predicts 0.80 at that exact point, which is what we measured. Test the
*branch*, not a point-sample of it. (File under Appendix A's moral: read your
check against the math as carefully as you read the code.)

## 10.4 Macro closure: the internal transfer entropy

The last check is the one this book cares about most, because it's the
information-theoretic meaning of "the parts stop mattering." If the cluster is
a complete entity at its own level, then knowing an individual member's phase
should add **nothing** to predicting the macro-phase's future beyond what the
macro-phase's own past already says:

```
TE(θᵢ → Θ | Θ)  ≈  0        (macro closure)
```

This is iteration 8's estimator pointed at the *levels* instead of the
neighbors (and iteration 8's trap applies in force — a locked member is an
extreme case of a source correlated with the target, so fine conditioning bins
are mandatory). Three measurements, one contrast, one control:

| system | TE(member → Θ \| Θ) | reading |
|--------|--------------------:|---------|
| tight cluster | **0.002 bits** | closed: members add nothing — the entity is its macro-state |
| weak collection | **0.027 bits** | leaky: micro detail still carries the macro future |
| probe → Θ (control) | **0.106 bits** | a real external influence reads loud and clear |

The locked cluster is informationally closed at the macro level; the unlocked
one is not; and the near-zero isn't the estimator being polite, because a
genuine influence on the same data reads 50× larger. Closure — like the shared
clock, like the pair law — *appears at the locking transition*.

In stack terms (the analogy that motivated this chapter): a healthy
web/app/DB stack presents one interface to the load balancer — aggregate
history predicts aggregate future, and which tier did what never leaks
through. A stack whose tiers aren't actually coordinating doesn't get to be
summarized that way, and the closure TE is the number that says so.

## 10.5 What this buys CPAF

The recursion now has a grounded rung, and it's sharper than "clusters can be
treated as units":

- **Entity-hood is created, not declared.** The same saddle-node transition
  that created *deviation* (iter 6) and *information* (iter 7) creates
  *entities*: below internal locking, none of the entity criteria hold; above
  it, all of them do. CPAF's ladder of emergence gets its mechanism — one
  transition, three gifts.
- **The recursion is quantitative.** The composed entity doesn't merely exist;
  it obeys the *same laws* as its constituents (`Kc`, the locked branch, the
  `1/√2` floor) with calculable effective parameters (`ω̄`, `κρ`, noise/√M).
  That's what "recursive" has to mean for a framework that wants to stack
  levels without hand-waving.
- **Closure is the entity's interface.** "Members add nothing beyond Θ" is the
  information-theoretic form of *having a boundary*: outside observers lose
  nothing by seeing only the macro-state. Note the resonance with iteration
  8's lesson — there, what you could claim about an edge depended on what you
  could observe; here, a closed macro-level is precisely what makes
  coarse-grained observation *sufficient*. Entities are where observability
  gets cheap.

## 10.6 The honest boundary

- **The cluster was imposed, not grown.** We set `K_in` by hand to isolate the
  recursion question. Iteration 5 grows modules with per-pair reward and
  competition; re-running these checks on a *grown* module is the natural
  splice of the two threads, and until then "iter-5 modules are entities" is
  inferred, not shown.
- **Symmetric coupling is load-bearing.** The internal-terms cancellation in
  §10.2 uses `sin`'s antisymmetry under `i↔j` — symmetric `K`. Asymmetric
  coupling (Chapter 9's directed edges) breaks the exact reduction; what a
  directed cluster coarse-grains to is open.
- **One probe, modest scale.** `M = 5`, a single external oscillator, no
  cluster-cluster interactions, no strong-drive regime. Whether the entity
  *fragments* under coupling comparable to its internal binding (the operating
  envelope of entity-hood) is deliberately left as the exercise below.
- **Closure is approximate.** 0.002 bits is not zero; offsets `δᵢ` fluctuate,
  and the reduction is exact only in the rigid limit. The right refinement is
  a *gradient* — closure as a function of `ρ` — of which we measured two
  points.

## 10.7 What to carry forward

- Coarse-graining: `ρ·e^{iΘ} = (1/M)Σe^{iθᵢ}`; the locked cluster's macro
  dynamics reduce to iteration 6's pair equation with `ω_eff = ω̄`,
  **`K_eff = κ·ρ`**, noise reduced by `√M`.
- The **entity criteria**, all verified for a locked cluster and all failed by
  an unlocked one: one shared frequency; entrainment at `κc = |Δω|/(2ρ)`
  (ρ-discount confirmed); iteration 6's locked branch with its `1/√2` floor;
  and **macro closure** `TE(member → Θ | Θ) ≈ 0`.
- Entity-hood is **created by the locking transition** — the same bifurcation
  that creates deviation and information.
- Methods: test the *branch*, not a point-sample of a steep curve; and
  closure-TE on tightly correlated variables demands iteration 8's
  fine-conditioning discipline.

---

### Try it yourself

Find the entity's breaking point. In `iter9_entity_as_cluster.py`, push the
probe coupling far past `κc` (say `κ` up to several times `K_in/M`'s worth of
per-member pull) and watch the internal coherence `ρ` during entrainment.
**Predict first:** does a locked cluster get *absorbed as a unit* (entrains
with `ρ` intact — entity survives the interaction) or does it *fragment*
(members peel toward the probe individually, `ρ` collapses — entity destroyed
by too strong an interaction)? Does the answer depend on `K_in`? Whatever you
find is the beginning of an *operating envelope for entity-hood* — the
coupling range within which it's valid to treat a cluster as one thing. CPAF
will eventually need that envelope stated, not assumed.

---

*Runnable: `verification/iter9_entity_as_cluster.py` · Pays the promissory
note of Ch 8 §8.4 #2 (entity-as-cluster) · Uses the iter-8 estimator from
Ch 9 · Symbols: `../CHEATSHEET.md`.*
