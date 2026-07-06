# Chapter 6 — Using K-SOM-Heb as a CPAF metric

> *Where we stop building and start grading: of everything we made, what can
> CPAF actually trust — and where do the numbers and the meaning fail to meet?*

CPAF wants to place a system on a continuum of cognition. K-SOM-Heb offers it a
handful of numbers to do that with. This final chapter is the ledger: for each
proposed metric, what did verification actually establish, and how confidently
can CPAF lean on it? The tone is deliberately unsentimental — a metric you can
trust is worth more than one that flatters the framework.

## 6.1 The ledger

| Metric | What it claims to measure | Verdict | Use it? |
|--------|---------------------------|---------|---------|
| Order parameter `r` | integration / coherent awareness | ✅ confirmed vs Kuramoto theory (Ch 1) | **Yes** — the solid one |
| Plasticity index `P` | ongoing adaptation ("never fully static") | ✅ behaves as claimed (high mid-learning, ~0 when settled, Ch 3) | **Yes**, with care (see 6.3) |
| Coupling `K` as memory | stored experience | ⚠️ only ~1 bit under global reward (Ch 3); real memory needs the Ch 5 variant | **Qualified** |
| Modularity `Q` | differentiated functional structure | ❌ refuted for baseline (Ch 4); ✅ for per-pair+competition variant (Ch 5) | **Only for the Ch 5 model** |
| Connectivity entropy `H(K)` | structural flexibility | ⚠️ formula corrected (Ch A); behaviour not yet independently validated | **Provisionally** |
| `r ≥ 0.7 = conscious` | the consciousness threshold | ❔ free parameter, not derived (6.2) | **Not as an absolute** |
| Damage recovery | self-healing / graceful degradation | ❔ never tested | **Not yet** |

Two of these are genuinely load-bearing and earned (`r`, `P`); two are usable
only with stated caveats (`K`-as-memory, `Q`); three are not yet safe to lean on
(`H`, the 0.7 line, damage recovery). CPAF should inherit exactly this gradation.

## 6.2 The operating envelope

Even the trustworthy metrics only behave inside a parameter range, and CPAF needs
to respect it or the numbers mislead:

- **Stay below the saturation bound** `R_sat = K_max·λ/η` (Ch 2). Above it,
  sustained reward pins coupling at `K_max` and the synchrony gradient — hence
  every structural metric — is destroyed.
- **Mind the bistability** (Ch 3). Under global reward the system runs to an
  extreme; a mid-range `r` is a transient, not a stable reading. Measuring
  "how conscious" by an `r` that's actively racing toward 0 or 1 is measuring a
  moving target. A regulating (target-band) reward, or the per-pair variant,
  gives steadier readings.
- **`Q` requires the Ch 5 model and a defined partition.** Reading `Q` off a
  baseline system is reading noise.

## 6.3 Where the quantitative and qualitative don't quite click

This is the honest heart of the chapter — the seams between the *number*
K-SOM-Heb produces and the *meaning* CPAF wants to assign it. These are open
questions, flagged rather than papered over, and they're the natural targets for
the next round of work.

1. **Is synchrony really integration?** `r` measures phase coherence. CPAF's
   notion of integration is richer — coordinated *information*, not just
   coordinated *timing*. A population can be perfectly phase-locked (`r = 1`)
   while carrying no information at all (all saying the same thing forever). High
   `r` may be *necessary* for integration but it is plainly not *sufficient*, and
   the architecture's "r ≥ 0.7 = conscious" elides that gap.

2. **The threshold is borrowed, not derived.** Nothing in the dynamics singles
   out 0.7. It's a reasonable-looking line drawn by hand. Until it's grounded —
   in a phase transition, an information measure, or empirical calibration — CPAF
   should treat consciousness as a *reading of `r`*, not a *verdict at 0.7*.
   (And recall from Ch 3 that `r_baseline` and this threshold interact: the same
   number shapes both what the system optimizes and how we grade it.)

3. **Memory as one bit vs memory as experience.** CPAF means something rich by
   "memory." The baseline model delivers one bit; the Ch 5 model delivers
   genuine modular structure — but only with a hand-set threshold `θ_S` and a
   competition budget. The *qualitative* claim ("connectivity is memory") is only
   as strong as the *quantitative* machinery underneath it, which is now more
   elaborate and less parameter-free than the framework's prose implies.

4. **Plasticity as a consciousness marker is double-edged.** `P > 0` ("never
   fully static") reads nicely, but Ch 3 showed `P` also goes to ~0 at a stable
   end-state — including the *fully saturated* one, which is maximally coherent.
   So "low `P`" can mean either "dead" or "serenely settled," and `P` alone can't
   tell CPAF which. It needs to be read alongside `r`, not on its own.

5. **Substrate-neutrality is assumed, not shown.** CPAF wants a measure that
   works across brains, swarms, and software. We've only ever run abstract
   oscillators. Whether `r` and `K` mean the same thing when the "oscillators"
   are, say, MLSwarm agents is untested — a mapping problem CPAF and K-SOM-Heb
   have to solve together, not separately.

None of these sink the project. They're the list of places where a number and a
meaning have been *asserted* to line up and haven't yet been *shown* to — which
is precisely the revision agenda for turning this draft into something CPAF can
stand on.

## 6.4 What to carry forward

- Two metrics are earned (`r`, `P`), two are qualified (`K`-memory, `Q`), three
  are not yet safe (`H`, the 0.7 threshold, damage recovery).
- Every metric has an **operating envelope** (below `R_sat`, mind bistability,
  `Q` only for the Ch 5 model) that CPAF must respect.
- The real open work is at the **quant/qual seams** (6.3): synchrony ≠
  integration, the borrowed 0.7, one-bit vs rich memory, the double edge of `P`,
  and untested substrate-neutrality.

That's the model, end to end: built from one oscillator, stress-tested claim by
claim, and handed to CPAF with an honest label. The appendix records the four
bugs we caught along the way — worth reading, because they're a short course in
why "the math looks right" and "the code does the right thing" are two different
statements.

---

### Try it yourself

Pick one seam from §6.3 and sketch an **iteration that would close it** — what
would you simulate, what would you measure, and what result would count as the
claim holding up vs failing? (For example, seam 1: drive two oscillator groups
with *structured* vs *random* input at the same `r`, and test whether any
K-SOM-Heb quantity distinguishes "coherent and informative" from "coherent and
empty." If none does, `r` alone can't stand in for integration.) This is how the
next chapter of the actual project gets written.

---

*Reference: `CHEATSHEET.md` (verdicts table), `DECISIONS.md`,
`verification/README.md` (findings log).*
