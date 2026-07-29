# Chapter 1 — Phase oscillators and the order parameter

> *Where we learn what the system is made of, and meet the single number that
> the whole metric rests on.*

Everything in K-SOM-Heb is built from one humble object: an oscillator with a
phase. Before any learning, any reward, any consciousness talk, we need to be
fluent in what these oscillators are and how we measure whether they agree.
That measurement — the **order parameter** — is the number CPAF ultimately
reads as "how synchronized, how coherent, this system is." So we start slow and
make it solid.

If your dynamical-systems muscles are rusty, don't worry: everything here is a
spinning arrow and an average. That's genuinely all it is.

---

## 1.1 One oscillator: a spinning arrow

Picture a clock with a single hand. The hand's angle is the **phase**, written
`θ` (theta). It sweeps around the circle at some speed — the **natural
frequency**, written `ω` (omega):

```
dθ/dt = ω
```

Read that as "the phase changes over time at rate ω." Big ω, fast hand; small
ω, slow hand. One oscillator alone is boring — it just spins forever at its own
rate. The interesting physics only shows up when we have many of them and let
them *feel* each other.

We describe an oscillator's position not as an angle but as a point on the unit
circle in the complex plane: `e^{iθ} = cos θ + i sin θ`. This is just a
bookkeeping trick — it turns "average some angles" (which is ill-defined; what's
the average of 350° and 10°?) into "average some arrows" (perfectly well
defined). Keep that trick in your pocket; it runs the whole chapter.

---

## 1.2 Many oscillators: the order parameter

Take `N` oscillators, each a little arrow `e^{iθⱼ}` on the unit circle. Lay them
all tail-to-tail at the origin and add them up, then divide by `N` — the average
arrow:

```
z = r · e^{iψ} = (1/N) Σⱼ e^{iθⱼ}
```

This average arrow `z` has a length `r` and a direction `ψ`. Both are useful,
but `r` is the star:

- **`r` = the length of the average arrow**, always between 0 and 1.
  - If every oscillator points the same way, the arrows stack and the average
    is a full-length arrow: `r = 1`. **Perfect synchrony.**
  - If the arrows are scattered evenly around the circle, they cancel and the
    average shrinks to nothing: `r ≈ 0`. **Incoherence.**
- **`ψ` = the direction the average points** — the "mean phase," the rhythm the
  group is (partially) keeping.

That's the order parameter. It compresses the entire state of `N` oscillators
into one intuitive scalar: *how much do they agree?* When the architecture says
"order parameter `r ≥ 0.7` = conscious," this is the `r` it means — a claim that
a system is conscious when its parts are at least 70% aligned. (Whether 0.7 is
the right line is a separate question — see the cheatsheet's "free parameter"
flag — but the *quantity* is exactly this.)

Here it is in code (`ksomheb.py`), and notice it's a one-liner plus the
complex-arrow trick:

```python
def order_parameter(theta):
    z = np.mean(np.exp(1j * np.asarray(theta)))
    return np.abs(z), np.angle(z)     # (r, psi)
```

`np.abs(z)` is the arrow's length `r`; `np.angle(z)` is its direction `ψ`.

---

## 1.3 Coupling: letting the arrows pull on each other

An `r` near 1 doesn't happen by accident — something has to *make* the
oscillators agree. That something is **coupling**. In the Kuramoto model, each
oscillator is nudged toward the ones it's connected to:

```
dθᵢ/dt = ωᵢ + (1/N) Σⱼ Kᵢⱼ · sin(θⱼ − θᵢ)
```

Two pieces:

1. `ωᵢ` — oscillator *i* still wants to spin at its own natural rate. This is
   the force of *disagreement*: every oscillator has its own preferred speed, so
   left alone they drift apart.
2. `(1/N) Σⱼ Kᵢⱼ sin(θⱼ − θᵢ)` — the force of *agreement*. Look at the `sin`
   term: if neighbour *j* is *ahead* of *i* (`θⱼ − θᵢ > 0`), the sine is
   positive and it speeds *i* up to catch up; if *j* is behind, it slows *i*
   down. The coupling weight `Kᵢⱼ` sets how strongly *i* listens to *j*.

In the base Kuramoto model all the weights are the same constant, `Kᵢⱼ = K`.
(In later chapters `K` becomes plastic — that's the whole "Heb" in K-SOM-Heb —
but not yet.) The step in code just applies Euler integration (nudge the state
by rate × small timestep):

```python
def kuramoto_step(theta, omega, K, dt=0.01):
    d = theta[None, :] - theta[:, None]              # θ_j − θ_i for every pair
    dtheta = omega + (K * np.sin(d)).sum(axis=1) / N
    return theta + dtheta * dt
```

---

## 1.4 The tug-of-war and the tipping point

Now the payoff. We have two forces in tension: frequency spread `σ` pulling the
oscillators apart, coupling `K` pulling them together. What happens as we turn
`K` up?

You might expect synchrony to rise smoothly with coupling. It doesn't. Kuramoto
showed there's a **critical coupling `Kc`**, a tipping point:

- **Below `Kc`:** the frequency spread wins. Oscillators drift at their own
  rates, arrows scatter, `r ≈ 0`. No amount of patience helps — it's not slow
  synchrony, it's *no* synchrony.
- **Above `Kc`:** coupling wins. A pack of oscillators suddenly locks into a
  common rhythm, arrows stack, `r` shoots up toward 1.

This is a **phase transition** — the same kind of abrupt, threshold behaviour as
water freezing. And for the common case of natural frequencies drawn from a bell
curve `N(0, σ²)`, the mean-field theory even gives the tipping point in closed
form:

```
Kc = 2 / (π · g(0))         where g is the frequency distribution's density
Gaussian:  Kc = 2σ · √(2/π) ≈ 1.596 · σ
```

---

## 1.5 Seeing it: iteration 1

Theory is cheap; we ran it. `verification/iter1_kuramoto_transition.py` sweeps
`K` from 0 to 4 over `N = 400` oscillators with Gaussian frequencies (`σ = 1`,
so theory predicts `Kc ≈ 1.596`), integrates each to steady state, and averages
`r`. The result (figure `iter1_kuramoto_transition.png`):

```
   K  | steady-state r
 ---- | --------------
 1.00 | 0.10          r sits near zero...
 1.40 | 0.19
 1.60 | 0.33          <- Kc(theory) = 1.596; the knee is right here
 1.80 | 0.67          ...then rockets up
 2.00 | 0.77
 3.00 | 0.93
```

The measured onset — first `K` where `r` climbs off the floor — lands at
**≈ 1.60**, against a prediction of **1.596**. That agreement is the point of
starting here: it's the one piece of the whole architecture with an exact
theoretical answer, so matching it proves our base dynamics are implemented
faithfully. Every later chapter stacks on this foundation, so we wanted it
nailed down cold before adding anything.

---

## 1.6 What to carry forward

- An oscillator is a spinning arrow: phase `θ`, natural speed `ω`.
- The **order parameter** `r ∈ [0, 1]` is the length of the average arrow —
  the single number for "how synchronized is this system." It is the coherence
  metric the whole book builds on. (*Graded later:* `r` turns out to be
  necessary but over-eager — it reads high where information is absent (Ch 8),
  so by Ch 6 it's one earned metric among several, not a consciousness
  verdict. Worth knowing where the story lands.)
- **Coupling** `K` fights the frequency spread. Below the critical coupling
  `Kc` the system is incoherent; above it, synchrony switches on abruptly.
- We verified the base model reproduces Kuramoto's transition (`Kc ≈ 1.60` vs
  `1.596`).

So far the coupling `K` has been a fixed constant. The entire innovation of
K-SOM-Heb is to make it **learn** — to let connections strengthen and weaken
based on experience. That's Chapter 2, where the arrows start rewiring the very
connections that steer them.

---

*Runnable: `verification/iter1_kuramoto_transition.py` · Reference:
`ksomheb.py` (`order_parameter`, `kuramoto_step`) · Symbols: `CHEATSHEET.md`.*
