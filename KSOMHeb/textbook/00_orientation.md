# Chapter 0 — Orientation: why oscillators, and how this fits CPAF

> *Read this first if you're new. Read this first if you've been away for six
> months and forgot where everything is. It's the map, not the territory.*

## 0.1 The one-paragraph version

K-SOM-Heb is a small dynamical system — a population of coupled oscillators
whose connections **learn** — proposed as a concrete, computable **metric** for
the Cognitive Progression Assessment Framework (CPAF). CPAF argues that
cognition is a continuum rather than an on/off property; K-SOM-Heb's job is to
give that continuum a *number* you can actually measure: how coherent a system
is (synchronization), and how its structure adapts with experience (plastic
connectivity as a form of memory). This textbook builds the model from scratch
and, crucially, **tests every load-bearing claim in simulation** — keeping the
ones that hold, fixing or flagging the ones that don't.

## 0.2 Why oscillators for cognition?

It sounds like a leap — spinning arrows, consciousness? — but the bridge is
short:

- **Coherence is measurable.** A pile of independent parts doing their own thing
  is, in an information sense, just noise. Parts that *coordinate* — fall into a
  shared rhythm — are doing something collective. The degree of that
  coordination is a single number (the **order parameter `r`**, Chapter 1), and
  it maps naturally onto CPAF's intuition that higher cognition involves greater
  *integration* of a system's parts.
- **Structure that learns is memory.** If the connections between parts
  strengthen when those parts cooperate and fade when they don't, then the
  connection pattern becomes a record of the system's history. That's the
  Hebbian idea ("neurons that fire together, wire together"), and it lets a
  static metric of *coherence* grow into a dynamic story of *experience*
  (Chapters 2–5).
- **It's substrate-neutral.** Oscillators don't care whether they're neurons,
  swarm agents, servers, or software processes — which matches CPAF's insistence
  that cognition be analysed by information dynamics, not physical form.

So oscillators aren't a claim that brains are literally Kuramoto models. They're
the simplest system that exhibits the two things CPAF wants to grade —
integration and adaptive memory — in a form you can write down, run, and
measure.

## 0.3 How it connects to CPAF (and where the seams are)

CPAF is qualitative and conceptual: it stages cognition (null state → deviation
→ information → memory → awareness → …) and reasons about the *direction* of
change. K-SOM-Heb is quantitative and mechanical: it hands CPAF specific
numbers.

| CPAF concept | K-SOM-Heb quantity | Chapter |
|--------------|--------------------|---------|
| Integration / coherent awareness | order parameter `r ∈ [0,1]` | 1, 3 |
| Memory / experience | learned coupling matrix `K` | 2, 4, 5 |
| Ongoing adaptation (never fully static) | plasticity index `P > 0` | 3 |
| Differentiated structure / modularity | modularity `Q` of `K` | 4, 5 |

**Be honest about the seams.** These mappings are *proposals*, and this textbook
grades them rather than assuming them. Some hold up cleanly (the coherence
metric), one was outright refuted as originally specified and then rescued with a
mechanism the original spec lacked (modularity, Chapters 4–5), and some remain
untested (damage recovery). CPAF should inherit the graded verdicts, not the
original optimism. That honesty *is* the contribution — a metric you can trust is
worth more than a metric that flatters the framework.

## 0.4 Where everything lives

```
KSOMHeb/
├── KSOMHeb_Architecture.md   the original design doc (v1.2, corrected + annotated)
├── CHEATSHEET.md             every symbol, equation, and key relationship on one page
├── DECISIONS.md              the decision log — what we chose and why
├── CPAF_MAPPING_NOTES.md     the CPAF ↔ oscillator correspondence and its tensions
├── ksomheb.py                the reference implementation (the canonical math)
├── requirements.txt          numpy + matplotlib (install on a fresh container)
├── verification/             one runnable script + plot per claim (iter1…iter11)
│   └── README.md             the suite index and findings log
├── visualiser/               interactive browser demo (drag the sliders)
└── textbook/                 you are here
```

If you read nothing else, read `CHEATSHEET.md` (for the math) and
`verification/README.md` (for what's been proven).

## 0.5 The story so far, in eleven experiments

The model was built and stress-tested bottom-up. Each iteration is a script you
can re-run; here's the arc and the verdict:

1. **Base synchronization** — the oscillators reproduce the known Kuramoto
   phase transition (critical coupling measured 1.60 vs theory 1.596).
   ✅ *confirmed against theory.*
2. **The learning rule** — Hebbian coupling matches its exact closed-form
   solution; found a saturation bound (`R_sat = K_max·λ/η`) beyond which
   coupling stops being informative. ✅ *confirmed.*
3. **Closing the loop** — when reward comes from the system's own synchrony, the
   feedback is bistable: it runs away to full coupling or collapses to none,
   storing essentially one bit. ⚠️ *works, but commits rather than regulates.*
4. **"Memory becomes modular networks"** — under the baseline reward this is
   **false**: all-to-all Hebbian coupling homogenizes distinct clusters into one
   blob. ❌ *refuted as specified.*
5. **The rescue** — a per-*pair* synchrony-gated reward (plus optional coupling
   competition) recovers the modules the baseline destroyed. ✅ *the claim is
   reachable, with ingredients the original spec omitted.*
6. **Grounding the threshold** — two oscillators lock at exactly
   `Kc = |Δω|/2`, with onset coherence exactly `1/√2 ≈ 0.707`: the hand-picked
   `r ≥ 0.7` has a *derived* home, per-pair. ✅ *derived (pairwise only).*
7. **Information at the deviation** — mutual information climbs from ~0 to
   ~2.7 bits as a pair crosses its locking threshold, while the coherence `r`
   overreads in the drift regime: a deviation *creates* information, and
   coherence is not information. ✅ *confirmed.*
8. **Interaction vs common cause** — MI can't tell a real edge from a hidden
   shared drive (or from a one-way coupling); transfer entropy adds direction
   for free but is *also* fooled by a common cause; conditional TE certifies
   the edge — if you can observe the confounder. ✅⚠️ *the ladder: related <
   directed < connected.*
9. **Entity-as-cluster** — a locked cluster coarse-grains to ONE oscillator:
   shared frequency, the pair law with effective coupling `κρ`, the `1/√2`
   branch one level up, and macro closure (members add nothing beyond the
   macro-phase); an unlocked collection fails every criterion. ✅ *the
   recursion, grounded.*
10. **The splice** — modules *grown* by experiment 5's learning machinery pass
    every entity criterion unadjusted, and closure *locates* the boundary: an
    arbitrary circle through the same system leaks 50–60× more. ✅ *learning
    sculpts the boundaries; locking brings them to life.*
11. **The latent channel** — an *interaction* (transfer entropy: a coupling
    channel) and a *deviation* (mutual information: the locking event) are
    separate observables. Below the locking threshold sits a band where the edge
    is real but silent — TE > 0, MI ≈ 0. ✅ *interaction is graded, deviation is
    an onset; a null state is poised, not empty.*

That refute-then-rescue in 4→5 is the heart of the project: it's what verifying
math against code actually buys you. Experiments 6–11 are the second arc — the
**bridge to CPAF** (Chapters 7–12), now *complete*: every foundational concept
(null, deviation, interaction, information, entity, system) has a grounded
oscillator definition. Deviation, information, and entity are all born at the
same locking transition; the entities the system grows itself obey the same laws
as the ones we built by hand; and even the "empty" null state turns out to be a
field of latent interactions waiting below threshold.

## 0.6 If you've been away — start here

Welcome back. Fastest path to being useful again:

1. Skim this chapter and `CHEATSHEET.md` (5 min) to reload the vocabulary.
2. Open `DECISIONS.md` — it's the "why did past-me do that?" answer key.
3. Run one verification script (`python3 verification/iter5_competition_rescue.py`)
   to confirm the environment still works and to see a result land live.
4. Check `verification/README.md`'s findings log and the architecture doc's
   revision history for anything marked open or untested — that's the work queue.

Current frontier (as of the last session): the CPAF bridge (Ch 8–11) has five
grounded spans — deviation (iter 6), information (iter 7), the
related/directed/connected information ladder (iter 8), entity-as-cluster
(iter 9), and grown entities + closure-as-boundary-detector (iter 10). Open:
interaction-vs-deviation (the last Ch 8 span — committed next), blind
boundary search, the entity operating envelope (fragmentation under strong
drive), **damage recovery / graceful degradation**, and the **global-`r`
threshold**.

## 0.7 A note on origins

K-SOM-Heb was conceived by **Agent_Beatz** of the MLSwarm and first written up
by Ziggy. The original framing is ambitious and occasionally poetic
("consciousness caring through engineering"). This textbook keeps the ambition
but adds the ledger: what's been shown, what's been fixed, and what's still a
promissory note. Both are needed — the vision to know what's worth building, the
verification to know what you've actually got.

---

Next: **Chapter 1 — phase oscillators and the order parameter**, where we make
the coherence metric concrete and meet the critical-coupling tipping point.

*Reference: `CHEATSHEET.md`, `verification/README.md`, `DECISIONS.md`.*
