# Chapter 5 — What actually makes modules

> *Where the refuted claim gets rescued, using an ingredient the original spec
> never mentioned — and the rescue turns out to be biology's answer too.*

Chapter 4 left us with a precise diagnosis: the model can't build modular memory
because (a) per-node reward cancels, leaving only synchrony to distinguish
connections, and (b) self-entrainment washes even that out. The exercise at the
end asked what reward *wouldn't* cancel. This chapter answers it, and then finds
the second ingredient that makes the answer sing.

## 5.1 The fix hiding in the algebra: per-pair reward

The cancellation in §4.2 happened because a per-*node* reward gives every
connection touching a node the same `R`. The escape is almost embarrassingly
direct: reward each **connection** by its *own* synchrony rather than by a
node-level scalar.

```
Rᵢⱼ = Sᵢⱼ − θ_S          (θ_S a synchrony threshold, e.g. 0.6)
```

Now the reward is genuinely per-pair, and it does *not* cancel:

- A **within-group** pair has high synchrony (`S ≈ 0.98`), sits well above the
  threshold, gets positive reward, and strengthens.
- A **cross-group** pair has low synchrony, falls *below* the threshold, gets
  **negative** reward, and decays.

The threshold acts as a gate: a connection only survives if its two oscillators
genuinely move together. Note this cannot be derived from a single global number
— it needs each pair's own `Sᵢⱼ`, which (Chapter 4) is the sole per-pair signal
the model has. We're finally using it directly.

Run it (iteration 5): contrast rises from the baseline's **1.24 to 2.16**, and
modularity `Q` from **0.045 to 0.156**. The modules the baseline destroyed come
back. Your hypothesis from the Chapter 4 exercise — heterogeneous, synchrony-based
reward — was the fix.

## 5.2 The second ingredient: competition

There's a complementary idea from neuroscience. Real neurons can't grow synapses
without limit — they have a finite metabolic budget, so their connections
*compete*: strengthen one and others must weaken to stay within budget. We can
add the same constraint. After each learning step, rescale every node's incoming
coupling so it sums to a fixed budget:

```
Kᵢⱼ  ←  budget · Kᵢⱼ / Σⱼ Kᵢⱼ        (then symmetrize)
```

This is **synaptic normalization**, and `ksomheb.py` implements it as
`synaptic_normalize`. It forces the connections of each node into a zero-sum
fight: the winners (high-synchrony within-links) crowd out the losers
(cross-links).

## 5.3 The surprise: competition alone does nothing

Here's the result that makes the chapter honest. If you add competition to the
*baseline* (global reward, no per-pair signal), modularity does **not** improve —
contrast stays at 1.24, `Q` at 0.044, unchanged. Competition on its own is inert.

Why? Competition only redistributes a fixed budget; it needs something to
redistribute *toward*. If every connection is rewarded equally (global reward),
there's no reason to prefer one over another, so normalization just scales them
all down uniformly and the blob stays a blob. **Competition is a sharpener, not
a source.** It has no opinion of its own — it only amplifies an opinion already
present in the signal.

Give it the per-pair signal to sharpen, though, and the two together are the best
of all four conditions:

| Condition | contrast | `Q` |
|-----------|----------|-----|
| baseline (global reward, no competition) | 1.24 | 0.045 |
| competition only | 1.24 | 0.044 |
| **per-pair reward** | **2.16** | **0.156** |
| **per-pair reward + competition** | **3.32** | **0.262** |

The picture is now complete and, pleasingly, biologically apt: **synchrony-based
per-pair reward *chooses* which connections matter; a finite-resource budget
*enforces* the choice.** Either alone is insufficient — reward without
competition leaves cross-links limping along, competition without reward has
nothing to act on. Together they build and hold modules.

## 5.4 What this costs, and what it means for CPAF

Be clear-eyed about the price. Neither ingredient is in the original K-SOM-Heb
spec. The per-pair reward `Rᵢⱼ = Sᵢⱼ − θ_S` replaces the doc's global/local/hybrid
reward menu entirely, and it introduces a new free parameter (the threshold
`θ_S`). Synaptic normalization adds a second mechanism and a budget parameter.
The architecture's modular-memory ambition is *reachable* — but only by a model
meaningfully more elaborate than the one originally written down.

For CPAF, that's the honest headline: the modularity metric `Q` is meaningful
**only for the per-pair (plus competition) variant**, not the baseline. When CPAF
reads modularity off a K-SOM-Heb system, it must be *this* system. The doc
(v1.2) and `DECISIONS.md` (D11) now record that.

## 5.5 What to carry forward

- **Per-pair synchrony-gated reward** `Rᵢⱼ = Sᵢⱼ − θ_S` breaks the §4.2
  cancellation and recovers modules (contrast 1.24 → 2.16, `Q` 0.045 → 0.156).
- **Competition alone is inert** — it sharpens an existing per-pair signal but
  cannot create one (baseline + competition: unchanged).
- **Together they're best** (contrast 3.32, `Q` 0.262): reward chooses, competition
  enforces.
- The rescue requires mechanisms **beyond the original spec**, with new
  parameters — an honest cost, now documented.
- *Since built on (Ch 11, iter 10):* the modules this machinery grows later
  pass **every entity criterion unadjusted** — this chapter's recipe became
  the suite's standard way of growing structure that earns its boundaries.

We've reached the end of the model-building arc: from a single spinning arrow
(Ch 1) to a self-organizing, modular, adaptive memory (Ch 5), verifying or
correcting each claim on the way. Chapter 6 steps back and asks the question CPAF
actually cares about: of everything we built, *which numbers can CPAF trust as a
measure of cognition* — and which come with an asterisk?

---

### Try it yourself

Competition is inert without a per-pair signal but powerful with one. **Predict
the ordering:** rank the four conditions in the table by `Q` from memory, then
open `iter5_competition_rescue.py` and confirm. Then a harder one: the threshold
`θ_S = 0.6` is a new free parameter — what do you expect to happen to the modules
if you set it *too high* (say 0.95), so that even within-group pairs struggle to
clear it? Run it and see. (This is the kind of parameter-sensitivity a future
iteration should map properly.)

---

*Runnable: `verification/iter5_competition_rescue.py` · Reference: `ksomheb.py`
(`synaptic_normalize`, `modularity`) · Symbols: `CHEATSHEET.md`.*
