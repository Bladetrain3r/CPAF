# Chapter 3 — Closing the loop

> *Where the system starts generating its own reward, and we learn that feedback
> commits rather than corrects.*

Chapter 2 left `R`, the reward, as a knob we turned by hand. That's fine for
testing the learning rule in isolation, but a real cognitive system has no
external hand on the dial — it has to judge for itself whether things are going
well. The most natural self-generated signal is the one we already have: the
system's own coherence. Reward the population for being synchronized.

## 3.1 The loop

Set the reward to the global order parameter, measured against a baseline:

```
R(t) = r(t) − r_baseline
```

When the system is more synchronized than baseline, `R > 0` and connections
strengthen; when it's less, `R < 0` and they weaken. Simple, sensible — and it
quietly changes everything, because now the thing that drives the coupling (`R`)
depends on the thing the coupling drives (synchrony). We've closed a loop:

```
coupling  →  synchrony  →  reward  →  coupling  →  …
```

## 3.2 Positive feedback doesn't regulate — it commits

There are two kinds of feedback, and the difference is the whole chapter.

**Negative feedback** corrects. Your home thermostat is the classic case: too
hot → turn the heat down → temperature falls back toward the setpoint. It has a
target and it defends it. This is what most people imagine when they hear
"feedback."

**Positive feedback** amplifies. Our loop is this kind: more synchrony → more
reward → *more* coupling → *even more* synchrony. There's no target and no
brake. Whatever direction the system is already leaning, the loop leans it
harder. A microphone near its own speaker is the everyday example — a tiny hum
becomes a shriek in seconds.

A positive-feedback system doesn't settle in the sensible middle. It runs to an
extreme and stays there. *Which* extreme depends entirely on where it starts.

## 3.3 Bistability: two fates, one rule

"Where it starts" means: is the initial coupling strong enough to get synchrony
above `r_baseline` or not? That threshold — the tipping point between the two
outcomes — is called the **separatrix**.

- **Start above it** (coupling already past the critical `Kc` from Chapter 1, so
  the system is somewhat synchronized): `r > r_baseline`, reward is positive,
  coupling grows, synchrony tightens, reward grows further. **Runaway** — the
  system climbs until every connection slams into the `K_max` ceiling.
- **Start below it** (subcritical, incoherent): `r < r_baseline`, reward is
  negative, coupling is stripped away, synchrony falls further, reward goes more
  negative. **Collapse** — coupling drains to zero and the oscillators scatter.

Same equation, same parameters, opposite destinies — decided only by the initial
condition. A system with two stable end-states like this is called **bistable**.

## 3.4 Seeing it: iteration 3

`verification/iter3_closed_loop.py` runs the full coupled system (phases *and*
coupling evolving together, reward computed live) from two starting points that
straddle the separatrix. `N = 80` oscillators, `σ = 0.5` (so `Kc ≈ 0.8`),
`r_baseline = 0.3`:

| Start | Fate | `r` | mean `K` |
|-------|------|-----|----------|
| `K₀ = 1.2` (supercritical) | **runaway** | 0.88 → **0.97** | → `K_max`, 100% of pairs saturated |
| `K₀ = 0.4` (subcritical) | **collapse** | 0.14 → **0.10** | → 0 |

Two more things the run shows:

- **The adaptive runs bracket their fixed-coupling controls** — adaptation pushes
  the supercritical case *higher* than a fixed `K` would, and the subcritical
  case *lower*. The loop exaggerates whatever it's given.
- **The plasticity index `P(t) = ‖K(t+Δt) − K(t)‖/Δt`** spikes during the
  transition and falls to near-zero at either end-state. This is the doc's
  "conscious systems show `P > 0` during learning" claim, now a measured curve:
  the system is *plastic while deciding* and *still once committed*.

## 3.5 The uncomfortable consequence: it stores one bit

Here's what iteration 3 means for the memory story. The architecture's headline
is *"connectivity IS memory"* — the coupling matrix `K` is supposed to hold a
rich record of the system's history. But look at where a global-reward loop
lands: **everything at `K_max`, or everything at 0.** The final coupling matrix
is all-or-nothing. It encodes exactly one bit — *did the swarm synchronize or
not?* — and nothing about *which* parts worked with which.

Why? Because a global reward is a single scalar shared by every pair. It can say
"everyone, more" or "everyone, less," but it can't say "this connection mattered
and that one didn't." That per-pair discrimination is precisely what memory
needs, and global reward structurally cannot provide it.

This isn't a bug to fix — it's an honest property of the design, and it sets up
the two chapters that follow. Chapter 4 asks the question directly: can this
system actually form the differentiated, modular memory the architecture
promises? (Spoiler: not as specified.) Chapter 5 finds what it takes to fix it.

## 3.6 What to carry forward

- Self-generated reward `R = r − r_baseline` closes a **positive-feedback loop**.
- Positive feedback **commits rather than regulates**: the system is **bistable**,
  running away to full coupling or collapsing to none depending on where it
  starts (the separatrix).
- The plasticity index `P` is high mid-transition, ~0 at either end-state.
- A global reward stores essentially **one bit** — it can't assign credit to
  individual connections, so it can't build a structured memory.

---

### Try it yourself

The fate is decided by whether the initial coupling puts `r` above or below
`r_baseline`. **Predict:** if you *raise* `r_baseline` from 0.3 to 0.7, does the
supercritical start (`K₀ = 1.2`) still run away, or does it now collapse? Reason
it through, then test it. (Hint: with a higher bar to clear, a synchrony that
used to count as "good" may now register as "below baseline" — and the loop
punishes what it reads as failure. This is also why the `r ≥ 0.7` consciousness
threshold isn't a free lunch: it's the same number, doing double duty.)

---

*Runnable: `verification/iter3_closed_loop.py` · Reference: `ksomheb.py` ·
Symbols: `CHEATSHEET.md`.*
