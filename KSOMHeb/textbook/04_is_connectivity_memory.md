# Chapter 4 — Is connectivity really memory?

> *Where we test the architecture's boldest claim and watch it fail — which is
> exactly what verification is for.*

The architecture makes a strong promise: *"connectivity IS memory."* The idea is
that after a system has lived through experiences, its coupling matrix `K` should
hold a differentiated record — clusters of nodes that worked together become
tightly linked *modules*, distinct from other clusters. A visual-processing
group here, a language group there, cross-links only where the two genuinely
cooperate. This chapter asks whether the model actually does that. The answer is
no — not as specified — and understanding *why* is more valuable than a yes would
have been.

## 4.1 What "modular memory" would look like

Set up a system with a *hidden* structure and see if the coupling discovers it.
Take `N` oscillators split into two groups with different natural frequencies —
group A spins fast, group B spins slow, with a little jitter. Within a group,
oscillators are near each other in frequency (they *can* synchronize); across
groups they're far apart (they resist synchronizing). If "connectivity is
memory," the learned `K` should end up with strong **within-group** coupling and
weak **cross-group** coupling — it should rediscover the two groups.

We measure this two ways:

- **Contrast** = mean within-group coupling ÷ mean cross-group coupling. Above 1
  means modules are forming; near 1 means the matrix is a uniform blob.
- **Modularity `Q`** = the standard (Newman) graph measure of how block-structured
  a weighted network is against chance. For our two ideal isolated blocks,
  `Q = 0.50`. A structureless matrix gives `Q ≈ 0`.

## 4.2 The reward mode doesn't matter (and here's the algebra)

The architecture offers three reward flavours — global, local (per-node), and
hybrid — and you might hope the richer ones create modules. They don't, and we
can see why on paper before running anything.

From Chapter 2, each connection settles at `K*ᵢⱼ = η·Sᵢⱼ·Rᵢⱼ/λ`. Take the ratio
that defines contrast:

```
K*_within     η·S_within·R_within/λ     S_within   R_within
─────────  =  ─────────────────────  =  ──────── · ────────
K*_cross      η·S_cross ·R_cross /λ      S_cross    R_cross
```

For any **per-node** reward, a within-pair and a cross-pair attached to the same
node see the *same* `R` — so `R_within/R_cross ≈ 1` and the reward **cancels
out**. The contrast is set by the synchrony ratio `S_within/S_cross` alone. That
means global, local, and hybrid reward all produce essentially the *same*
modular contrast. The knob you were hoping would help isn't connected to
anything. (Confirmed in simulation: the contrast spread across all three modes
was 0.016 — statistical noise.)

Only `Sᵢⱼ` carries per-pair information. Hold that thought; it's the key to
Chapter 5.

## 4.3 Why it fails anyway: self-entrainment

Fine — so synchrony sets the contrast. Within-pairs have high `S`, cross-pairs
low `S`, so shouldn't we still get *some* modularity? Here's the trap. Coupling
doesn't just *read* synchrony — it *creates* it. A cross-group connection, once
it exists, pulls its two oscillators toward each other, raising their
synchrony... which under the learning rule keeps that very connection alive. The
system entrains itself.

The numbers tell the story starkly. In isolation the two groups have cross-group
synchrony around 0.16 (they barely align). But turn on all-to-all Hebbian
coupling and cross-synchrony climbs to **0.34–0.85** — the connections
manufacture the agreement that justifies them. The result: the clusters melt
together into a single module. Measured learned modularity is `Q ≤ 0.05`,
against `Q = 0.50` for the true partition. The memory doesn't differentiate; it
homogenizes.

## 4.4 The ablation that proves S is the protagonist

One more check, and it ties the whole book together. Iteration 4 re-runs the
experiment with the v1.0 bug deliberately restored — `Sᵢⱼ ≡ 1` for every pair
(Appendix A). With synchrony flattened to a constant, the contrast collapses to
**exactly 1.0**: no modular structure whatsoever, not even the weak amount the
correct `S` produced. This is the cleanest possible demonstration that `Sᵢⱼ` is
the *only* thing carrying per-pair credit in the model. Break it and there is no
memory at all; fix it and there's at least a fighting chance. Everything hinges
on that one term.

## 4.5 What to carry forward

- The "connectivity is memory / modular networks emerge" claim is **false for the
  baseline model** — verified, not asserted.
- **Reward mode cancels** from the contrast ratio (only `Sᵢⱼ` is per-pair), so
  global/local/hybrid are interchangeable and none creates modules.
- **Self-entrainment homogenizes:** coupling manufactures the cross-synchrony
  that keeps cross-links alive, merging clusters into one blob (`Q ≤ 0.05` vs a
  true `0.50`).
- The `S ≡ 1` ablation flattens contrast to exactly 1.0, proving `Sᵢⱼ` is the
  sole carrier of per-pair credit.

A refuted claim isn't the end of the road — it's a precise statement of what's
missing. We now know the exact problem: the model has no way to assign credit to
individual connections, and its own dynamics wash out the little structure
synchrony provides. Chapter 5 asks what minimal ingredient fixes that — and finds
that the answer was hiding in §4.2 all along.

**Typing note (per Chapter 13's revision pass).** In the canonical metalanguage
this iteration is a **classification result**, not a universal "❌": a
computational witness `[CW]` that the baseline model *as specified* — per-node
reward, all-to-all Hebbian coupling, no competition — falls in the
non-modularizing class. It says nothing about Hebbian systems in general, and
Chapter 5 immediately exhibits members of the *modularizing* class (per-pair
credit, competition). Refutation-as-classification is the precise reading; the
verdict tables elsewhere keep the shorthand ❌ with this footnote understood.

---

### Try it yourself

§4.2 argues the reward mode cancels because a per-node reward hits within- and
cross-pairs equally. **Question:** what kind of reward would *not* cancel — i.e.,
what would `Rᵢⱼ` have to depend on so that within- and cross-pairs get genuinely
different values? Write down the simplest thing you can think of, then read
Chapter 5 and see if you beat us to it. (You have everything you need: §4.2 says
only `Sᵢⱼ` distinguishes the pairs.)

---

*Runnable: `verification/iter4_reward_modes.py` · Reference: `ksomheb.py`
(`local_synchrony`, `modularity`) · Symbols: `CHEATSHEET.md`.*
