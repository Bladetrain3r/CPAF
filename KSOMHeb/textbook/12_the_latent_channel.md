# Chapter 12 — The latent channel: interaction without deviation

> *Where the last unbuilt span of the bridge gets built — and a coupling that
> hasn't done anything yet turns out to be visible anyway.*

Chapter 8 laid out the bridge from oscillators to CPAF's foundational concepts
and was honest about which spans were load-bearing and which were still rope and
hope. One of the ropes was §8.4's first tension: the claim that an **interaction**
(an edge — a coupling channel that *exists*) and a **deviation** (the locking
*event* on that edge) are genuinely different things, not two words for the same
event. We adopted the split as a working definition — *the edge is the noun, the
locking is the verb* — but never tested it. This chapter does, and it's the last
span the foundational bridge was missing.

## 12.1 Two detectors we already own

The test needs a way to see each thing separately, and we built both already:

- **The deviation detector is mutual information** (Chapter 8 §8.2 — iter 7). MI
  between two phases is ~0 while the pair drifts and jumps up only when the pair
  *locks*. It fires on the event.
- **The interaction detector is transfer entropy** (Chapter 9 — iter 8). TE asks
  how much one oscillator's present improves prediction of the other's future,
  beyond that other's own past. Here's the key physical fact: a coupling
  transmits influence *whether or not it has locked*. Even sub-threshold, oscillator
  2 tugs on oscillator 1's instantaneous frequency through the `K·sin(θ₂−θ₁)`
  term — so θ₂'s present genuinely helps predict θ₁'s future. TE should be nonzero
  for **any** `K > 0`, locked or not. It fires on the channel.

So if the noun/verb split is real, the two detectors should come apart.

## 12.2 The prediction

Sweep the coupling `K` on a single noisy pair from zero upward:

| regime | interaction? | deviation? | prediction |
|--------|:---:|:---:|---|
| `K = 0` | no | no | MI ≈ 0, TE ≈ 0 |
| `0 < K < Kc` | **yes** | no | MI ≈ 0, **TE > 0** — a *latent channel* |
| `K > Kc` | yes | yes | MI > 0, TE > 0 |

The middle row is the whole point: a band of coupling where the edge is real but
*silent* — an interaction that has not (yet) produced a deviation.

## 12.3 The result

`verification/iter11_interaction_vs_deviation.py` runs exactly this. All four
checks pass, and the numbers tell a clean story (detuning `|Δω| = 1.26`, so
`Kc = 0.628`; noise 0.30):

- **`K = 0` is a true null.** MI = 0.000, TE = 0.0002 — both at the estimator
  floor. No channel, no event.
- **The latent channel is real.** At `K/Kc = 0.34` the transfer entropy is
  0.015 bits — a clearly detected interaction — while MI is still at 0.04, i.e.
  no deviation. The edge exists and carries directed influence, but nothing has
  locked. This is the noun without the verb, measured.
- **Interaction turns on *before* deviation.** TE lifts off the floor at
  `K/Kc ≈ 0.34`; MI only starts climbing around `K/Kc ≈ 0.53`. As you raise
  coupling from zero, the *channel* becomes visible first; the *event* comes
  later. Interaction is graded — a smooth matter of degree — while deviation is
  an onset.
- **Above `Kc`, both are present.** By `K/Kc = 2.4`, MI has climbed to 2.6 bits
  (a loud deviation) and TE remains positive (the interaction is still there).

An honest bonus fell out of the sweep: TE does not rise forever. It **peaks near
`Kc` (~0.06 bits) and then declines** as locking tightens (settling ~0.03).
That's not a bug — it's *redundancy*. Once the pair is tightly locked, each
phase's own past already predicts its future almost perfectly, so the partner
adds little *new* predictive information. TE measures what one oscillator tells
you *beyond* the other's own history, and a well-locked pair is its own best
predictor. So the interaction detector is loudest precisely in the transition
zone — where the channel is active but the target isn't yet self-predicting.

## 12.4 What it grounds

Three things, in ascending order of consequence:

1. **Interaction and deviation are separate observables.** They are detected by
   different quantities that demonstrably come apart (TE without MI in the latent
   band). The noun/verb split is no longer a definition we adopted — it's a
   dissociation we measured. Chapter 8's last rope is now a beam.

2. **Interaction is graded; deviation is an event.** TE rises continuously from
   zero with coupling; MI switches on at a threshold. An interaction has a
   *strength*; a deviation has a *moment*. CPAF can treat "how connected" as a
   dial and "did a deviation occur" as a bit, and they are not redundant.

3. **The null state is *poised*, not empty.** Chapter 8 reframed CPAF's null
   state as the absence of *deviations*, not of *interactions*. This chapter
   hardens that: a system sitting at `r ≈ 0` with no locked pairs can still be
   *dense with latent channels* — sub-threshold couplings that carry real
   directed influence (TE > 0) while producing no deviations (MI ≈ 0). Null is
   not structurelessness. It is a field of interactions waiting below threshold,
   any of which a small nudge — more coupling, less noise, a narrower frequency
   gap — could tip into a deviation. The null state has latent structure, and
   that structure is measurable.

## 12.5 The honest edges

- **Noise softens the deviation.** Both onsets sit somewhat below the noiseless
  `Kc` (MI begins near `0.53·Kc`), because noise smears the locking transition —
  as we already saw in Chapters 7–8 (iters 6–7). The result is about the *order*
  of the two onsets and the *existence* of a latent band, not their exact
  locations.
- **It's still a pair.** Like every result in this arc's foundation, this is
  N = 2. The claim is about a single edge; whether "latent channels" compose
  the way locked ones do (Chapters 10–11) is a separate question.
- **The TE floor is set by an estimator.** "TE ≈ 0" means "at the
  surrogate-corrected floor," not literally zero; the K = 0 column is what
  calibrates it. This is the same discipline iteration 8 insisted on.

## 12.6 What to carry forward

- Interaction (edge) and deviation (locking) are **separate, separately
  measurable** things: **TE detects the channel, MI detects the event.**
- There is a **latent-channel band** `0 < K < Kc`: TE > 0 (interaction present)
  while MI ≈ 0 (no deviation) — the noun without the verb.
- **Interaction is graded, deviation is an onset**; the channel becomes visible
  at lower coupling than the event.
- The **null state is poised**: it can hold dense latent interactions with no
  deviations — latency below threshold, not emptiness. *The foundational bridge
  (Chapters 7–12) is now complete.*
- **Latent vs active is a *sign*** (§12.7): the sign of the locking discriminant
  — a latent interaction's locked relationship is *complex* (unrealized), an
  active one's is *real*.

## 12.7 Postscript — the sign of an interaction

There's a sharper way to say "latent vs active," and it falls out of the same
two-oscillator algebra. A locked pair solves `sin ψ* = Δω/(2K)`, which has a real
solution only when the **locking discriminant** is non-negative:

```
Disc(K) = 1 − (Δω/2K)²
  Disc > 0  → ψ* real     → active   (the relationship is realized: a deviation)
  Disc = 0  → ψ* = π/2    → threshold Kc (onset coherence 1/√2)
  Disc < 0  → ψ* complex  → latent   (the relationship is unrealized: a channel)
```

Below threshold the locked offset is literally **complex**,
`ψ* = π/2 − i·arccosh(Δω/2K)`: the phase relationship exists in analytic
continuation but is *not realized on the real circle*, and the size of the
imaginary part says how far below threshold — how latent — the interaction is.
So the latent/active distinction is a **sign problem**: the sign of the
discriminant, equivalently the *realness* of `ψ*`. One caution worth holding: this
is the sign of the *discriminant* (coupling versus threshold), **not** the sign of
the coupling itself — a coupling being attractive vs repulsive is a different axis
we set aside long ago (Appendix A / the Hebbian choice). `iter12_interaction_sign.py`
confirms all of it: the simulated pair settles onto `Re ψ*` above threshold and
never settles below it, and the discriminant's zero lands exactly at `Kc` with
`ψ* = π/2`, `R = 1/√2`. This is the form your framework's *latent interaction*
takes once it's grounded in dynamics.

---

### Try it yourself

The latent band is bounded below by where TE clears the floor and above by where
MI switches on. **Question:** what happens to the *width* of that band as you
shrink the detuning `|Δω|`? Reason it out — `Kc = |Δω|/2` moves the deviation
onset, but does the interaction onset (where TE clears the floor) move the same
way? — then narrow `|Δω|` in `iter11_interaction_vs_deviation.py` and watch the
band. (Hint: a smaller frequency gap means a weaker coupling suffices to *lock*,
so the verb arrives sooner — but even a whisper of coupling still transmits, so
the noun barely moves. The band should narrow from the top. If it does, "how
poised is the null state" becomes a question with a knob.)

---

*Grounded by: `verification/iter11_interaction_vs_deviation.py` · Detectors from
`iter7_information_transition.py` (MI) and `iter8_transfer_entropy.py` (TE) ·
Working notes: `../CPAF_MAPPING_NOTES.md` (tensions #1, #3).*
