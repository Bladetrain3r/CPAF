# Chapter 7 — Grounding the threshold

> *Where a number we'd been picking by hand turns out to fall out of the
> mathematics on its own — and where the model first touches CPAF's most
> fundamental concept.*

Every chapter so far has taken the architecture's `r ≥ 0.7 = conscious` line at
face value while quietly flagging it (Chapter 6, seam #2) as *borrowed* — a
plausible-looking threshold with nothing underneath it. This chapter asks whether
we can do better: is there a value of coherence that the dynamics single out on
their own, rather than one we impose? For a pair of oscillators, the answer is
yes, and it's a clean one.

## 7.1 Two oscillators collapse to one equation

The trick that makes this exactly solvable: with only two oscillators, we don't
need to track both phases — only their *difference*. Write `ψ = θ₁ − θ₂` and
`Δω = ω₁ − ω₂` (the detuning — how mismatched their natural frequencies are).
Subtract the two Kuramoto equations and everything collapses:

```
dψ/dt = Δω − 2K·sin ψ
```

One variable, one equation. Read it as a tug-of-war we've seen before, now in
miniature: `Δω` drives the phase difference to grow (the oscillators want to run
at different rates), and `−2K·sin ψ` fights to hold it fixed (coupling wants them
together). Whether they lock depends on which wins.

## 7.2 The threshold, and the number that falls out

The pair is **locked** when the phase difference stops changing — a fixed point,
`dψ/dt = 0`:

```
2K·sin ψ* = Δω        ⟹        sin ψ* = Δω / (2K)
```

A sine can't exceed 1, so this has a solution *only* when `|Δω/(2K)| ≤ 1`, i.e.

```
K ≥ Kc = |Δω| / 2
```

Below `Kc`, no fixed point exists — the phase difference slides forever and the
pair drifts. At exactly `Kc`, a stable and an unstable fixed point are born
together (a **saddle-node bifurcation**), and above it the pair locks. This is a
genuine, sharp threshold — the finite-system cousin of a phase transition.

Now the payoff. At the moment of onset (`K = Kc`), the fixed point sits at
`ψ* = π/2`, so the pair's coherence there is

```
R_onset = |cos(ψ*/2)| = cos(π/4) = 1/√2 ≈ 0.7071
```

and the locked branch never drops below it: a locked pair always has
`R ∈ (1/√2, 1]`. Below `1/√2`, two oscillators *cannot* hold together. That
number wasn't put in by hand — it came out of `cos(π/4)`. And because our
per-pair synchrony `Sᵢⱼ` **is** exactly this `R`, we've derived a threshold:

> A pair of oscillators can phase-lock only if `Sᵢⱼ > 1/√2 ≈ 0.707`.

The architecture's hand-picked `r ≥ 0.7` is, at the pairwise level, this locking
floor rounded to one decimal. The borrowed threshold has a home after all.

## 7.3 Iteration 6 confirms it

`verification/iter6_locking_threshold.py` checks every link in that chain:

- The 1-D reduction reproduces the full two-oscillator order parameter (three
  decimals) — the collapse to one equation is exact, not an approximation.
- Empirical `Kc` matches `|Δω|/2` across three detunings.
- The locked-branch `R` matches `|cos(ψ*/2)|`, with onset at `1/√2` to four
  decimals.
- Below `Kc` the phase drifts; above it, it locks.
- Add noise and the sharp knee smears into a gradual rise (§7.5).

## 7.4 The honest boundary: this is a pairwise result

Resist the temptation to declare `r ≥ 0.7` vindicated in general. It isn't. The
`1/√2` result is exact for **two** oscillators. The *global*, many-oscillator
order parameter behaves completely differently: its transition is **continuous**
(second-order), turning on at `Kc = 2/(π·g(0))` (Chapter 1) with `r` rising
smoothly from zero — there is no special value 0.7 anywhere on that curve. So
what we've grounded is a **per-pair** threshold, not a global one. Concretely,
`1/√2` is the principled value for iteration 5's synchrony gate `θ_S` (we'd been
using 0.6 as a guess); whether a *global* `r`-threshold can be derived at all
remains open. Saying more than that would be exactly the kind of overclaim this
book exists to catch.

## 7.5 Noise, and the first handshake with CPAF

Turn on noise and the bifurcation softens: locking becomes probabilistic near
`Kc`, and the `R`-vs-`K` curve bends from a knife-edge into a ramp. That's not a
nuisance — it's the *realistic* picture, and it's where this chapter reaches
toward CPAF.

CPAF's most fundamental concept is the step from the **null state** (maximal
entropy — undifferentiated noise) to a **deviation** (the first real change). The
locking transition is a candidate for exactly that step, made measurable: below
`Kc` a pair is drifting noise; crossing `Kc` it snaps into a sustained
relationship — order where there was none. With noise in play, that boundary is
smeared rather than sharp, which is precisely how a "noise → deviation" line
*should* look: not a wall, but a threshold where coupling reliably overcomes both
the frequency mismatch and the noise. We'll pick this thread up as its own piece
of work — mapping the oscillator primitives (a pair, a coupling, a locking event)
onto CPAF's foundational vocabulary (entity, interaction, deviation). Chapter 7
is where the metric stops being self-contained and starts trying to *mean*
something in the framework it was built to serve.

## 7.6 What to carry forward

- Two oscillators reduce **exactly** to `dψ/dt = Δω − 2K·sin ψ`.
- They lock above `Kc = |Δω|/2` (a saddle-node bifurcation); the coherence at
  onset is **exactly `1/√2 ≈ 0.707`**, so a pair locks only if `Sᵢⱼ > 1/√2`.
- This is a **derived** per-pair threshold — grounding the `θ_S` gate and
  matching the hand-picked `r ≥ 0.7` *pairwise only*. The global transition is
  continuous with no special 0.7.
- With noise the transition smears — the candidate operational picture of CPAF's
  **null → deviation** step.
- *Since recurred and typed:* the same law returns one level up — a locked
  cluster obeys this exact equation with `K_eff = κρ`, `1/√2` floor included
  (Ch 10) — and the canonical layer types the pair (`Kc`, `1/√2`) as `[AN]`
  **at the pair scale**, never universal constants (Ch 13).

---

### Try it yourself

The onset coherence `1/√2` came from `ψ* = π/2` at the bifurcation. **Question:**
does that value depend on the detuning `Δω`? Reason it out from
`R_onset = |cos(ψ*/2)|` with `ψ*` fixed at `π/2`, then change `Δω` in
`iter6_locking_threshold.py` and check. (Answer: no — `Δω` sets *where* the
threshold is in coupling, `Kc = |Δω|/2`, but the coherence *at* the threshold is
always `1/√2`. The "how coupled" and the "how coherent at onset" are separate
facts — a distinction worth holding onto when we map this to CPAF.)

---

*Runnable: `verification/iter6_locking_threshold.py` (seed:
`twoosc_entangle_demo.py`) · Reference: `ksomheb.py`, `CHEATSHEET.md`.*
