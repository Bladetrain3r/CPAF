# CPAF ↔ Game of Life — concept mapping (substrate #2)

> ⚠️ **Planning / conjecture, pre-verification** — the same status the
> oscillator mapping notes had before their iterations. This is the
> correspondence to *test*, not results. Each row will be graded by an
> experiment under `experiments/`, exactly as the textbook graded the
> oscillator mapping. Conjecture here; prove there; then promote.

## Why a second substrate at all

Everything the textbook grounded — deviation, information, interaction, entity,
closure — was grounded *in coupled oscillators*. CPAF claims its basic-layer
vocabulary is **substrate-neutral**: a property of information dynamics, not of
any particular physics. That claim is, so far, assumed (textbook Ch 0 admits
it). The whole point of `gol/` is to **test** it in a substrate as unlike
oscillators as we can find while still being simple:

| | oscillators (textbook) | Game of Life (here) |
|---|---|---|
| state | continuous phase `θ ∈ [0, 2π)` | binary cell `∈ {0, 1}` |
| time | continuous (Euler steps) | discrete, synchronous |
| space | none (a graph of couplings) | a 2-D grid (Moore neighbourhood) |
| interaction | tunable coupling `K` | **fixed** local rule B3/S23 |
| dynamics | stochastic (noise added) | **deterministic** |
| entities | locked clusters (emergent, fuzzy) | catalogued patterns (discrete, exact) |

If the dictionary reproduces here — same operational definitions, same graded
verdicts — substrate-neutrality graduates from assumption to cross-substrate
evidence. If it *strains*, we learn precisely which parts were oscillator-
specific. **Both outcomes are the point.** A failed mapping is as valuable as a
clean one, in this project's economy.

## The honest prior-art note (read before claiming anything)

Information dynamics in cellular automata is a developed field, and we are
walking into it deliberately. **Lizier, Prokopenko & Zomaya** ("Local
information dynamics of distributed computation in cellular automata", and
related work ~2008–2014; the JIDT toolkit) already established the decomposition
that shadows our whole dictionary:

- **gliders / spaceships = coherent information *transfer*** (they carry high
  local transfer entropy across space-time) — our *interaction / information
  on a channel*;
- **blinkers, still lifes, domains = information *storage*** — our *entity /
  memory*;
- **collisions = information *modification*** — our *interaction that produces a
  change* / *deviation*.

So we are **not** claiming to discover that gliders carry TE or that CA compute.
Our contribution — if there is one — is narrower and specific: testing whether
*CPAF's particular operational dictionary*, as we pinned it down on oscillators
(deviation as a threshold birth, entity as a **closed** macro-variable, the
*related < directed < connected* ladder, closure-as-boundary-detector), maps
onto these known CA structures **consistently and with the same graded
discipline**. The novelty on offer is the cross-substrate *consistency test*,
not the CA information dynamics. This note belongs at the top of any writeup
(cf. the textbook's Appendix S).

## The dictionary, term by term

Grading: **gift** = GoL expresses it more cleanly than oscillators did;
**clean** = maps directly; **strained** = the oscillator version doesn't
transfer without adjustment; **open** = genuinely unclear.

### Entity — **gift**
In oscillators an entity was a locked cluster we had to *detect* (fuzzy
membership, measured `ρ`). In GoL, entities are the substrate's own catalogued
objects: **still lifes** (block, loaf — period 1, static), **oscillators**
(blinker p2, pulsar p3, pentadecathlon p15 — static position, and note the
*quantized periods*: the "entity frequencies" oscillators tuned continuously
are here discrete), and **spaceships** (glider p4, LWSS — periodic *and
moving*). Operational test (implemented in `gol.classify`): a bounded pattern
is an entity if, evolved **in isolation**, it *recurs* — period `P`, displaced
by `disp` per period. This is stricter and sharper than the oscillator version.

### Closure — **gift**, and newly *spatial*
The textbook's deepest entity criterion was macro-closure: an entity's future
is determined by its own coarse state, `TE(member→Θ | Θ) ≈ 0`. In GoL this
becomes literally geometric: **an isolated pattern's future is determined
entirely by its own cells** (the rule is local, so nothing outside its
neighbourhood can touch it until something moves into range). Closure = spatial
isolation; the boundary is the pattern's cells plus a one-cell interaction
collar. Two consequences oscillators could not produce:
- **Closure as a boundary detector** (the iter-10 result) is *native* here:
  the connected component + isolation test *is* the boundary finder. Our
  `gol.entities()` already does it.
- **A MOVING closed boundary.** A glider is a closed entity whose boundary
  *translates* every period. Oscillator clusters had fixed membership; a
  spaceship's "membership" is a set of cells that changes every step while the
  *entity* persists. Testing whether the closure machinery tracks a moving
  boundary is a genuinely new question (README, iteration C).

### Deviation — **strained** (the interesting tension)
This is where the substrates genuinely differ, and naming it honestly matters.
In oscillators a deviation was crossing a *tunable* threshold `Kc` — a
bifurcation you reach by turning a knob. **Conway is deterministic and
parameter-free: there is no `K` to turn.** So the "threshold-crossing" picture
does not transfer directly. Three candidate readings, to be chosen between by
experiment:
1. **Birth as the atomic deviation.** The literal B3 birth of a cell — null
   (dead) → structure (alive). Clean but perhaps *too* atomic.
2. **Settling as a temporal deviation.** A random "soup" boils (active, no
   persistent structure = a dynamic null) and eventually *settles* into ash
   (still lifes + oscillators + escaping gliders). The transition from
   chaotic-active to settled-structured is a deviation in *time* rather than in
   a control parameter — arguably the closest analog to drift→lock.
3. **Recover a tunable threshold** by leaving pure Conway: initial density `ρ`,
   a stochastic flip-rate, or the rule-space of "Larger than Life" / Domany–
   Kinzel CA all have genuine density/activity **phase transitions** (directed-
   percolation class). This buys back the bifurcation picture at the cost of
   "it's not Conway any more."

The plan (README) leans on (1)+(2) for pure Conway and flags (3) as the
principled way to recover the oscillator-style bifurcation if we want a true
threshold. **The tension itself is a finding**: it suggests CPAF's "deviation"
has (at least) two faces — a parameter-driven bifurcation and a
self-organized settling — that the oscillator substrate conflated.

### Interaction — **gift** (richer than oscillators could be)
Two coupled oscillators interact symmetrically and non-destructively — influence
flows, nothing is created or annihilated. GoL **collisions** are vastly richer,
and this is exactly the ground the user flagged:
- **Asymmetric, destructive outcomes.** A glider hits a block: the glider may
  die and the block survive, both may die, or a new pattern may be born. An
  **eater** absorbs a glider and is *restored unchanged* — a maximally
  asymmetric interaction (one entity annihilated, one invariant) with no
  oscillator analog at all.
- **Creative interactions.** A glider **gun** *emits* entities forever;
  collisions can *construct* still lifes, other spaceships, even logic gates.
  Interaction here can increase the entity count, not just perturb phases.
So GoL lets us test the interaction concept — and the Ch 12 noun/verb split
(influence vs the event it may cause) — over a far wider range of outcomes.
Directed influence (transfer entropy between entities) should still be the
measure; the question is whether the *related < directed < connected* ladder
survives when interactions can annihilate their endpoints.

### Information — **clean** (but cite Lizier)
Mutual information between cells/regions; **transfer entropy** between them,
directed. Local (per-cell, per-step) TE is the Lizier machinery and highlights
gliders as the carriers. Our ladder maps directly: MI = *related*, TE =
*directed*, conditional TE (given the rest of the neighbourhood) = *connected*.
The GoL twist: because the rule is deterministic and local, the "confounder set"
that conditional TE needs is *exactly a cell's 8 neighbours* — finite, known,
and complete. So the iter-8 "certificates cost context" story has a clean upper
bound here: full context is 8 cells. That is a much tidier setting than the
oscillator common-cause case, and worth exploiting.

### Null state — **clean**
Two readings, mirroring the oscillator "null = absence of *deviations*, not of
*interactions*": the **empty grid** (true null) versus a **boiling random
region** — locally active (interactions everywhere) but with no persistent
structure (no deviations that stuck). A settled field of still lifes is a third,
"latent" null: structure exists but nothing is changing. Matches the textbook's
sub-threshold-latency reframe.

### System — **clean / open**
The whole grid: population, entity census, the graph of who-can-reach-whom. No
dedicated system-level claim yet (same status as the oscillator side).

## What GoL adds that oscillators could not (the new questions)

These are the user's angles, and they are the reason substrate #2 is more than
a replication — each is a question the oscillator substrate *could not even
pose*:

1. **Quantized entity frequencies.** Periods are discrete (1, 2, 3, 4, 15, 30…).
   Do entities of different periods interact differently — is there a
   "resonance" or period-dependent collision outcome? (Oscillators had a
   continuous frequency knob; here it's a spectrum of fixed species.)
2. **Asymmetrically destructive interactions.** Winners and losers, eaters and
   guns. Does "interaction" survive as a concept when an interaction can
   *destroy* an entity? What is the TE signature of an annihilation vs a
   glancing perturbation vs a construction?
3. **Moving boundaries.** A spaceship is a closed entity whose boundary
   translates. Does closure-as-a-boundary-detector track a moving entity, and
   what is the closure signature of a spaceship *about to collide* (closure
   breaking down as two boundaries approach)?

## How each row gets graded (the discipline, unchanged)

Every mapping row above becomes an experiment under `experiments/`, each with a
runnable script, a check that can **fail**, and a graded verdict — exactly the
textbook's method. The roadmap in `README.md` sequences them. Nothing here is a
claim until an experiment there has earned it.

---

*Companion to `README.md` (the plan) and `gol.py` (the engine, which already
implements the entity/closure detector this mapping leans on). Prior art and
credit will accrue in the eventual writeup's sources section, seeded above with
Lizier et al.*
