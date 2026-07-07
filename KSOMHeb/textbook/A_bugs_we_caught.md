# Appendix A — The bugs we caught

> *A short course in why "the math looks right" and "the code does the right
> thing" are two different statements.*

Before any of the iterations in this book ran, the K-SOM-Heb design document was
a page of clean-looking equations and plausible Python. It had never been
executed. When we sat down to verify it, four errors surfaced — each one
mechanism-breaking, and each one invisible to a casual read. They're collected
here because catching them is the whole reason this project exists, and because
the *kinds* of mistake they represent recur everywhere theory meets code. The
corrected model is in `ksomheb.py`; the demonstrations are in
`verification/verify_bugs.py`.

## A.1 The synchrony measure that was always 1

**The claim.** Local synchrony was defined as `Sᵢⱼ = |exp(i(θⱼ − θᵢ))|`, said to
be 1 when in phase, 0 when anti-phase, smooth between.

**The bug.** `exp(ix)` for a real angle `x` is a point on the unit circle, so its
magnitude is *always exactly 1*, for every phase difference. The definition even
spelled it out — `|cos Δθ + i·sin Δθ|` — which is `√(cos² + sin²) = 1`. The
measure the whole learning rule depends on was a constant.

**The damage.** With `Sᵢⱼ ≡ 1`, the coupling update `dK = η·S·R − λK` becomes
identical for every pair. No connection can distinguish itself from any other;
the "fire together, wire together" gradient — the thing that makes the coupling a
*memory* — is gone. The entire Hebbian premise silently fails. (Chapter 4's
ablation shows exactly this: contrast collapses to 1.0.)

**The fix.** The magnitude of the *average of two phasors*:
`Sᵢⱼ = |½(e^{iθᵢ} + e^{iθⱼ})| = |cos((θⱼ − θᵢ)/2)|`. Now it's genuinely 1 in
phase, 0 anti-phase, smooth between — and, being built from complex
exponentials, immune to phase-wrapping glitches.

**The lesson.** *A formula that type-checks can still compute a constant.* The
expression was dimensionally and notationally fine; only by asking "what value
does this actually take?" — or better, printing it for a few inputs — does the
problem appear.

## A.2 The spatial blend that froze learning

**The claim.** To keep some of the original spatial (Kohonen) structure, the
update blended it back in: `K ← 0.8·K + 0.2·K_spatial`, run every timestep.

**The bug.** That blend was applied *every step* and *not scaled by `dt`*. At 0.2
per step it's a pull toward the spatial baseline roughly `10⁴×` stronger than the
learning dynamics it was sitting next to (`λ·dt ≈ 10⁻⁵` per step). The coupling
was effectively nailed to `K_spatial`; whatever the Hebbian rule tried to learn
was erased before the next step.

**The fix.** Apply spatial structure **once, at initialization**, and let the
coupling adapt away from it. A baseline is a starting point, not a leash.

**The lesson.** *In a discrete-time simulation, "how often" and "scaled by `dt`?"
are correctness questions, not style.* A term that's perfectly reasonable as a
one-time nudge becomes a straitjacket when it runs every step at full strength.

## A.3 The entropy that wasn't an entropy

**The claim.** Structural flexibility via `H(K) = −Σ Kᵢⱼ log Kᵢⱼ`.

**The bug.** That's the *form* of Shannon entropy, but `Kᵢⱼ` are coupling weights,
not probabilities. They don't sum to 1; they exceed 1 (up to `K_max = 2`), which
makes terms *negative*; and they hit 0 — exactly the floor the model clamps to —
where `log 0` is undefined. The quantity could go negative and could return
`NaN`, neither of which an entropy can do.

**The fix.** Normalize first: `pᵢⱼ = Kᵢⱼ / Σ Kᵢⱼ`, then `H = −Σ pᵢⱼ log pᵢⱼ`,
with the convention `0·log 0 = 0`. Now it's a real entropy of a real distribution.

**The lesson.** *Borrowing a formula means borrowing its preconditions.* Shannon
entropy assumes a probability distribution; hand it raw weights and it returns a
number-shaped object that isn't the thing you named.

## A.4 The step function with holes

**The claim.** An STDP-style plasticity kernel defined piecewise: `+1` if
`|Δφ| < π/4`, `0` if `|Δφ| ≈ π/2`, `−1` if `|Δφ| > 3π/4`.

**The bug.** Look at the gaps: what happens for `π/4 < |Δφ| < π/2`, or
`π/2 < |Δφ| < 3π/4`? Undefined. The kernel had holes, and where it was defined it
was discontinuous — contradicting the "smooth gradient" the text promised.

**The fix.** A smooth signed kernel, `g(Δφ) = cos(Δφ)`, defined everywhere: `+1`
in phase, `0` at quadrature, `−1` anti-phase. And because this signed version
belongs to a *different* design (it actively pushes anti-phase pairs apart), we
marked it as an optional non-Hebbian variant, not part of the chosen model
(`DECISIONS.md`, D1).

**The lesson.** *Piecewise definitions have to cover the whole domain.* "It's
obviously +1 near 0 and −1 near π" hides the question of what happens in between —
which is where the actual behaviour lives.

## A.5 The meta-lesson

None of these four is exotic. A constant masquerading as a function, a term that's
fine once but toxic every step, a borrowed formula stripped of its preconditions,
a piecewise map with gaps — these are the ordinary ways careful-looking math goes
wrong in code. The defence isn't cleverness; it's *running it*. Every bug here
died the moment someone printed the value, checked the units of `dt`, or fed the
formula a number outside the happy path. That habit — treat the design as a
hypothesis and make the machine try to falsify it — is what the whole
`verification/` suite institutionalizes, and it's the single most transferable
thing in this book.

---

*Runnable: `verification/verify_bugs.py` (the bugs), `verify_fixes.py` (the
corrections) · Doc: `KSOMHeb_Architecture.md` revision history (v1.1) ·
Reference: `ksomheb.py`.*
