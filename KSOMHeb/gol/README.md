# `gol/` — CPAF in a second substrate: Conway's Game of Life

> *Substrate #2. The textbook grounded CPAF's basic-layer dictionary
> (deviation, information, interaction, entity, closure) in coupled
> oscillators. This subfolder tests whether the same dictionary reproduces in
> something as different as we could find that's still simple: a deterministic,
> discrete, spatial cellular automaton. Part experiment, part interactive
> learning tool — with a structured paper as the eventual target.*

## Why this exists (and why it's separate from the textbook)

CPAF's central bet is **substrate-neutrality**: that null → deviation →
information → entity is a story about information dynamics, not about
oscillators. The textbook could not test that — everything in it runs on one
substrate. Game of Life is the falsification test: if the dictionary maps over
cleanly, the bet gains real evidence; if it strains, we find out exactly where
the oscillator grounding was substrate-specific. Either way it's a distinct
piece of work — its own folder, its own plan, aimed at its own writeup
("*An experimental analysis of cellular automata as low-level cognitive
systems*", or similar) rather than another textbook chapter.

See **`CONCEPT_MAPPING.md`** for the term-by-term correspondence (and the
honest prior-art note on Lizier et al.'s CA information dynamics — we are
testing a *consistency claim*, not rediscovering that gliders carry transfer
entropy).

## What's here now

```
gol/
├── README.md            this file — the plan and roadmap
├── CONCEPT_MAPPING.md   CPAF dictionary → Conway constructs, graded, with prior art
├── gol.py               ENGINE + measurement primitives (tested): B3/S23 dynamics,
│                        a pattern zoo (still lifes, oscillators p2/p3/p15,
│                        spaceships), connected-component entity detection, and
│                        classify() — period + velocity by ISOLATED evolution
│                        (isolation = closure, operationally)
├── visualiser/          interactive browser tool (draw, stamp patterns, run,
│                        and "detect entities" — outlines + classifies live)
└── experiments/         iterN scripts (the graded claims — see roadmap below)
```

`gol.py` is the counterpart to `../ksomheb.py`; `experiments/` will be the
counterpart to `../verification/`; the visualiser is the counterpart to
`../visualiser/` — but leaned harder toward *learning tool*, per the brief.

**Quick start:**
```bash
python3 gol.py                        # smoke test: detects a glider, blinker, block
# open visualiser/gol_visualiser.html in a browser to play
```

## Design stance: visual and interactive first

This substrate is spatial, so it *wants* to be watched. Unlike the oscillator
work (where the visualiser came late), here the interactive tool is a
first-class deliverable, because the concepts are things you can literally see:
an entity is a shape, a deviation is a birth, an interaction is a collision, a
moving boundary is a glider crossing the grid. The learning-tool goal: someone
who has never heard of CPAF should be able to draw a mess, hit **detect
entities**, and watch the machinery name the gliders and blinkers that emerged —
and thereby *feel* what "entity", "period", and "closure" mean before reading a
word of theory.

## Roadmap (the graded claims — each an experiment that can fail)

Sequenced bottom-up, like the verification suite. Status ☐ = planned.

| # | Iteration | Tests / grounds | Maps concept |
|---|-----------|-----------------|--------------|
| G1 | **Engine + entity zoo** ✅ (`gol.py`) | B3/S23 correct; the pattern zoo classifies to the right periods & velocities (verified: block p1, blinker/toad/beacon p2, pulsar p3, pentadecathlon p15, glider & LWSS p4 spaceships) | entity (the objects) |
| G2 | **Entity detector** ✅ (`gol.entities`) | connected components + isolated-evolution classification = an operational entity finder (kind / period / displacement) | entity, closure (isolation) |
| G3 | **Closure = isolation, incl. moving boundaries** ☐ | an isolated pattern's future is self-determined (predict from its own cells alone); test that closure *tracks a glider's translating boundary*; measure closure breaking down as two entities approach a collision | closure (the gift: spatial + moving) |
| G4 | **Deviation: birth vs settling** ☐ | resolve the tension (`CONCEPT_MAPPING.md`): is a deviation an atomic birth, or the soup→ash *settling* transition? Measure a methuselah (R-pentomino/acorn) settling; characterize the temporal "deviation" | deviation (the strained span) |
| G5 | **Collision taxonomy: asymmetric interactions** ☐ | catalogue glider+X outcomes (survive / annihilate / construct); the **eater** as the maximally asymmetric interaction; do different-period entities collide differently? | interaction (the gift: destructive/creative) |
| G6 | **Local transfer entropy: gliders as channels** ☐ | reproduce Lizier's result (gliders carry TE) with *our* estimator; test the *related < directed < connected* ladder, using a cell's 8 neighbours as the finite, complete confounder set (conditional TE) | information (the ladder, in CA) |
| G7 | **Cross-substrate synthesis** ☐ | the writeup: which dictionary rows reproduced, which strained, which GoL extended beyond oscillators. Grade substrate-neutrality on the evidence | the whole bet |

Optional tunable-threshold detour (if G4 wants a real bifurcation): a
stochastic/density-parameterized CA (Domany–Kinzel / "Larger than Life") to
recover the oscillator-style phase transition — flagged in `CONCEPT_MAPPING.md`.

## The discipline (inherited from the textbook)

Same rules that kept the oscillator work honest, restated so this folder
doesn't drift:

1. **Code matches math; checks can be wrong too.** Every claim is a runnable
   script with a check that can fail (the textbook caught itself twice —
   binning bias, point-sampling a steep branch; expect the same here).
2. **Claims are graded, not asserted.** gift / clean / strained / open, per the
   mapping. A strained or failed mapping is a result, not an embarrassment.
3. **Credit up front.** Prior art (Lizier et al. for CA information dynamics,
   and the GoL literature for the pattern zoo) is named in `CONCEPT_MAPPING.md`
   and will anchor the writeup's sources — before results, not after.
4. **Conjecture here, prove in `experiments/`, then promote.** `CONCEPT_MAPPING.md`
   is the scratchpad; a mapping row is only "grounded" once its G-iteration
   passes.

## Open questions this substrate raises (the fun ones)

Beyond the roadmap, GoL poses questions oscillators could not (see
`CONCEPT_MAPPING.md` §"what GoL adds"):

- **Quantized entity frequencies** — do period-2 and period-3 entities interact
  differently? Is there collision "resonance"?
- **Asymmetric destruction** — what is the information signature of an
  annihilation vs a glancing perturbation vs a construction?
- **Moving boundaries** — can closure track a spaceship, and what does closure
  look like in the instant before a collision?

These are the reasons substrate #2 is more than a replication — it's a chance to
grow the dictionary, not just re-confirm it.

---

*Engine verified `python3 gol.py`. Companion docs: `CONCEPT_MAPPING.md` (the
mapping), `../textbook/` (the oscillator grounding this tests against),
`../textbook/S_sources_and_inheritances.md` (the credit-ledger model this
folder's writeup will follow).*
