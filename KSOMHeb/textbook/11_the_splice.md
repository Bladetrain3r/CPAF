# Chapter 11 — The splice: grown modules are entities

> *Where the book's two halves — the metric that learns and the bridge that
> means — turn out to be one story, and the entity criteria turn out to be a
> detector.*

This book has been two arcs pretending to be one. Chapters 1–5 built a system
whose connections *learn*: Hebbian coupling, its failure to form modules, and
the rescue (per-pair synchrony-gated reward plus coupling competition) that
finally sculpted a coupling matrix into blocks. Chapters 7–10 built a bridge
of *meaning*: deviation, information, and entity, each grounded on structures
we assembled by hand. The obvious question sat between them, and Chapter 10's
honest-boundary section said it plainly: iteration 9's entities were
**imposed**. Does a module the system *grew from experience* pass the same
tests? If yes, the arcs fuse. If no, "module" and "entity" are different
things and the book must say so. Iteration 10 asked, and it is the cleanest
result in the suite.

## 11.1 The rules of the splice

Faithfulness on both sides, nothing adjusted in the middle:

- **Growth is iteration 5, verbatim.** Same machinery (`ksomheb.py`
  functions), same parameters, same seed, best condition (per-pair reward +
  competition). The run reproduces iteration 5's result on the nose: contrast
  3.32, `Q = +0.262`, two clean blocks in `K`.
- **The entity tests are iteration 9's, unadjusted.** Coupling is then frozen
  (the criteria are stated for fixed `K`; plasticity at the grown steady
  state is small), and every prediction is computed from **measured**
  properties of the grown module — its members' mean natural frequency `ω̄`,
  its free-running internal coherence `ρ` — with no hand-tuning anywhere.

Why it *should* work is worth a paragraph, because it sharpens what the test
means. Iteration 9's reduction — the macro-phase obeying the pair equation
with `K_eff = κρ` — rests on one cancellation: the internal coupling terms
vanish from the macro-motion. Checking the algebra, that cancellation needs
only `Kᵢⱼ = Kⱼᵢ`; sine's antisymmetry does the rest. It never required the
couplings to be *uniform*. So the theory genuinely predicts that a learned,
heterogeneous, lopsided-but-symmetric coupling block behaves as one
oscillator. That is a real, breakable prediction about structures the
learning rule built without ever being told about entities — exactly the
kind of claim this book exists to test rather than admire.

## 11.2 The grown module passes everything

**One clock (Check A).** In situ — the full grown system, both modules and
their cross-links live — each grown module's member velocities collapse to a
single value (spread 0.0002 rad/s, against a natural jitter of 0.12): module
A runs at its `ω̄_A`, module B at its `ω̄_B`, 2.76 rad/s apart. Two entities,
two clocks, made from sixty oscillators.

**The pair law with measured coherence (Check B).** Excise module A with its
learned couplings, measure `ρ = 0.995` free-running, couple a probe per
iteration 9, and sweep. Empirical thresholds: within **2.5%** of
`κc = |Δω|/(2ρ)` at both detunings — the same 2.5% the imposed clusters
achieved. The learning rule's handiwork is, dynamically, indistinguishable
from the hand-built ideal.

**The 1/√2 branch, third appearance (Check C).** The grown module's locked
branch matches `R(κ) = cos(½·arcsin(Δω/2ρκ))` to 0.004 mean error — tighter
than iteration 9 itself. Bare pairs (iter 6), imposed clusters (iter 9),
grown modules (iter 10): one law, three substrates, and the second and third
are the first one recursed.

## 11.3 Closure as a boundary *detector*

The last check got an upgrade beyond a pass/fail. Iteration 9's non-entity
control was a weak cluster — a different *system*. Iteration 10's control is
a different *boundary through the same system*: a fake "module" of 15
members from each true cluster, evaluated on the **same noisy trajectory** as
the true module. Same physics, same data; only the circle we drew differs.

| boundary | TE(member → Θ \| Θ) | verdict |
|----------|--------------------:|---------|
| true grown module, excised | **0.006 bits** | closed — an entity |
| true grown module, in situ | **0.005 bits** | closed even amid its neighbour |
| fake boundary, in situ | **0.284 bits** | leaks 50× louder — no entity here |

That 50–60× separation on identical data is the chapter's second headline:
the entity criteria don't just *grade* a proposed boundary, they can
**locate** the real one. Draw the wrong circle and the macro-phase you
compute is not closed — the members shout past it. Draw the grown circle and
they fall silent. Entity boundaries are discoverable from dynamics alone, no
labels, no knowledge of how the system was built. (This vindicates the
"internal transfer entropy" instinct that motivated the closure measure back
in Chapter 10 — it was proposed as a boundary criterion, and that is exactly
what it turns out to be good for.)

Two honest observations from the same run:

- **We predicted a leak that didn't show.** In situ, module A is genuinely
  coupled to module B through the grown cross-links, so we expected its
  closure to read slightly worse than excised. Measured: in situ 0.0045,
  excised 0.0060 — equal within estimator noise. At this cross-coupling
  strength the neighbour's leak is below the floor. The expectation was
  reasonable; the data declined to confirm it; we report the data.
- **First entity-to-entity information measurement.** At the macro level,
  `TE(Θ_B → Θ_A | Θ_A) = 0.013 bits` — small but positive. The grown
  cross-links form a real information channel *between entities*, measured
  entirely at the coarse-grained level. That's CPAF's next floor showing up
  early: entities interacting as entities.

## 11.4 The fusion

The one-sentence version the Intermission promised, now earned:

> **Learning sculpts the boundaries; locking brings them to life; the result
> obeys the same laws as its parts.**

Iteration 5's machinery (per-pair credit + competition) carves the coupling
matrix into blocks. The blocks lock internally, and at that moment — the same
bifurcation that created deviation and information — they become entities:
one clock, the pair law at their own measured coherence, closure at their own
macro-level. Nothing in the learning rule mentions entities; nothing in the
entity criteria mentions learning. The two meet in the middle and agree.

For CPAF this upgrades the recursion from "grounded on imposed structure" to
**grounded on acquired structure**: a system can *grow its own next level*.
And the boundary-detection result sketches a procedure CPAF has otherwise
lacked: given an unlabeled dynamical system, entity boundaries are the
partitions that maximize closure (and share a clock) — a falsifiable
operationalization of "carving nature at its joints."

## 11.5 The honest boundary

- **The structure was seeded.** Iteration 5's modules recover clusters
  planted in the natural frequencies. What we've shown is that
  *experience-carved* modules are entities — not that entities arise from
  nothing. A run with no seeded structure (uniform frequencies, structured
  input instead) is a different, harder experiment.
- **One growth condition, one seed.** The splice uses iteration 5's exact
  world. Robustness across growth seeds and along the growth *trajectory*
  (when during learning does entity-hood switch on — does it track the
  locking transition as Q rises?) is untested and would be a lovely follow-up.
- **`K` was frozen for the tests.** Live plasticity during entity tests
  (probe entrains the module *while* the module rewires) is unexplored — and
  is presumably where "the entity adapts" stories live.
- **The detector claim is proof-of-concept.** One fake boundary versus one
  true one. A genuine boundary-*search* (optimize closure over partitions,
  recover the modules blind) is the exercise below, not yet a result.
- **The entity-to-entity channel is one number.** 0.013 bits, undissected: not
  yet conditioned, not yet compared across coupling strengths, not yet run
  bidirectionally with controls. It's an observation, not a finding.

## 11.6 What to carry forward

- Modules grown by **per-pair reward + competition pass all four entity
  criteria unadjusted**, with predictions computed from their own measured
  `ω̄` and `ρ`: thresholds to 2.5%, the 1/√2 branch to 0.004, closure at
  ~0.005 bits.
- The reduction's cancellation needs only **symmetry** of `K` — the pair law
  covers learned, heterogeneous coupling blocks, and the data confirm it.
- **Closure is a boundary detector**: true boundary 0.005 bits vs arbitrary
  boundary 0.284 bits on the same trajectory. Entities are findable, not just
  checkable.
- First **entity-to-entity** macro information channel measured (0.013 bits
  through grown cross-links) — the recursion's next floor, glimpsed.
- The fusion: *learning sculpts the boundaries; locking brings them to life;
  the result obeys the same laws as its parts.*

---

### Try it yourself

Make the detector earn its name. Using the grown system from
`iter10_grown_entities.py` (or its saved trajectory), implement a blind
boundary search: start from random 30-member subsets, and hill-climb by
swapping members to minimize `TE(member → Θ | Θ)` (or maximize a cheaper
proxy first — the subset's internal coherence `ρ`, or minus its
member-velocity spread). **Predict first:** will the search recover the grown
modules exactly, and which objective — closure, coherence, or shared-clock —
has the fewest local optima? If a cheap proxy finds the same boundaries as
the expensive closure measure, you've built the first practical
entity-discovery algorithm for this model — and if the objectives *disagree*,
whichever boundary closure prefers is, by Chapter 10's argument, the real
one. Either outcome is worth a chapter.

---

*Runnable: `verification/iter10_grown_entities.py` (growth: iter 5 verbatim;
criteria: iter 9 unadjusted) · Closes the "grown entities" follow-up of
Ch 10 §10.6 · Symbols: `../CHEATSHEET.md`.*
