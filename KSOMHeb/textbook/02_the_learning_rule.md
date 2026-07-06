# Chapter 2 — Making connections learn

> *Where the coupling stops being a fixed constant and starts keeping a record
> of experience.*

In Chapter 1 the coupling `K` was a dial we set by hand — one number, the same
for every pair, held fixed while the oscillators sorted themselves out. That's
base Kuramoto. The whole innovation of K-SOM-Heb is to let each connection
`Kᵢⱼ` **change over time**, growing when two oscillators cooperate and fading
when they don't. This is the "Heb" — Hebbian learning — and it's what turns a
synchronization model into something that can remember.

## 2.1 The rule

Two oscillators, `i` and `j`. We want their connection to strengthen when
they're synchronized *and* the system is being rewarded, and to weaken slowly
all the time so nothing grows without bound. Written as a rate of change:

```
dKᵢⱼ/dt = η · Sᵢⱼ · R  −  λ · Kᵢⱼ
```

Three characters:

- `Sᵢⱼ` — the **local synchrony** of the pair (Chapter 1's order-parameter idea,
  applied to just two arrows): `Sᵢⱼ = |cos((θⱼ − θᵢ)/2)|`, which is 1 when
  they point the same way and 0 when opposed. This is the "fire together" signal.
- `R` — the **reward**, a signal that says "what's happening now is good"
  (positive) or "bad" (negative). We'll spend Chapter 3 on where `R` comes from;
  for now treat it as a knob.
- The two rates: `η` (eta) sets how fast connections grow, `λ` (lambda) how fast
  they decay.

Read the equation as a bucket with a hose and a leak. The hose (`η·Sᵢⱼ·R`) pours
water in at a rate set by synchrony times reward. The leak (`−λ·Kᵢⱼ`) drains
faster the fuller the bucket. This exact shape — constant-ish inflow, drain
proportional to level — is **leaky integration**, one of the most common
patterns in all of dynamics (it's also how a capacitor charges). If it feels
familiar from an intro circuits or biology course, that's the right instinct.

## 2.2 Where the bucket settles

A leaky bucket fills until inflow equals outflow, then holds steady. Set
`dKᵢⱼ/dt = 0` and solve:

```
η · Sᵢⱼ · R = λ · Kᵢⱼ        ⟹        K*ᵢⱼ = η · Sᵢⱼ · R / λ
```

That `K*` is the **fixed point** — the equilibrium the connection glides toward.
Two things to read off it:

1. **Coupling is proportional to synchrony.** Double a pair's synchrony and you
   double its resting connection strength. This is the gradient that makes the
   metric meaningful — and it's exactly the gradient the v1.0 bug destroyed by
   making `Sᵢⱼ ≡ 1` for every pair (Appendix A). Without it, every connection
   settles to the *same* value and the coupling matrix remembers nothing.
2. **The approach is exponential**, with timescale `τ = 1/λ`. Big `λ` = short
   memory, connections snap to their target and forget fast; small `λ` = long
   memory, connections drift slowly and hold their history. `τ` *is* the memory
   horizon of the system, in so many words.

The full solution (same as a charging capacitor) is
`Kᵢⱼ(t) = K* + (Kᵢⱼ(0) − K*)·e^{−λt}` — start anywhere, decay exponentially onto
`K*`.

## 2.3 In code

The reference step (`ksomheb.py`) is a direct Euler discretization — nudge the
state by rate × timestep, then clip into the allowed range:

```python
def update_ksom_heb(theta, omega, K, reward, dt=0.01,
                    eta=0.01, lam=0.001, K_max=2.0):
    theta_new = kuramoto_step(theta, omega, K, dt)   # Chapter 1's phase update
    S = local_synchrony(theta_new)                    # the pairwise sync matrix
    dK = eta * (S * reward) - lam * K                 # hose minus leak
    K_new = np.clip(K + dK * dt, 0.0, K_max)          # bounded, non-negative
    return theta_new, K_new
```

The `np.clip(..., 0.0, K_max)` matters: it enforces `Kᵢⱼ ∈ [0, K_max]`.
Non-negative because we're in the pure-Hebbian regime (no negative connections);
capped at `K_max` because otherwise the reward loop of Chapter 3 would let
coupling grow without limit.

## 2.4 Seeing it: iteration 2

`verification/iter2_hebbian_fixed_point.py` freezes the phases (so `Sᵢⱼ` and `R`
are constants) and watches the coupling relax. With a closed-form answer to
check against, we can be strict — and the implementation matches the analytic
trajectory to about **one part in a million**. Three things it confirms:

- **Each pair glides to its own `K* = ηSᵢⱼR/λ`,** ordered by synchrony — the
  "fire together, wire together" gradient made visible.
- **A saturation bound.** The equilibrium is `K* = (η/λ)·S·R`, so with the
  doc's default gain `η/λ = 10`, any sustained reward above
  `R_sat = K_max·λ/η` (= 0.2 for those defaults) drives well-synchronized pairs
  straight into the `K_max` ceiling. Once there, a pair with `S = 0.98` and one
  with `S = 0.36` both read `K_max` — the synchrony gradient is erased and the
  coupling stops being informative. **Keep sustained reward below `R_sat`**, or
  the memory saturates. (This bound wasn't in the original doc; iteration 2
  found it.)
- **Negative reward is asymmetric, by design.** When `R < 0`, synchronized pairs
  are actively driven to the floor, but a pair with `Sᵢⱼ ≈ 0` has drive
  `η·0·R = 0` — it feels no reward at all and simply decays on the slow `τ`
  timescale. In the pure-Hebbian model, **punishment requires participation;
  indifference just fades.** This is the property we accepted when we chose the
  Hebbian path over signed STDP (see `DECISIONS.md`, D1).

## 2.5 What to carry forward

- Coupling learns by **leaky integration**: grow by `η·S·R`, decay by `λ·K`.
- It settles at `K* = η·S·R/λ` — proportional to synchrony, approached with
  memory timescale `τ = 1/λ`.
- Beyond `R_sat = K_max·λ/η`, sustained reward saturates the connection and
  destroys the synchrony gradient.
- Negative reward punishes only the synchronized; unsynchronized pairs merely
  decay.

We've been treating `R` as a knob. But in a real system nobody's turning that
knob — the system has to generate its own reward from what it can sense. The
natural choice is to reward the system for its *own* synchrony. That closes a
loop, and closed loops behave very differently from open ones. Chapter 3.

---

### Try it yourself

In `iter2_hebbian_fixed_point.py`, the fixed point is `K* = (η/λ)·S·R`. **Before
running:** if you *halve* `λ` (from 0.001 to 0.0005), what happens to (a) the
equilibrium coupling `K*`, and (b) the time `τ` it takes to get there? Now change
it and run — did both move the way you predicted? (Answer: `K*` doubles, `τ`
doubles. Slower decay means both a higher resting strength *and* a longer memory
— which is why `λ` alone controls "how much the system holds on.")

---

*Runnable: `verification/iter2_hebbian_fixed_point.py` · Reference:
`ksomheb.py` (`update_ksom_heb`) · Symbols: `CHEATSHEET.md`.*
