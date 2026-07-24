# CPAF Canonical Definitions — Cheatsheet

Use this for quick reinforcement. The detailed rules live in `METALANGUAGE.md`.

## One-sentence model

CPAF describes how systems acquire increasingly demanding forms of organized
change, information use, recursive entity structure, memory, and higher
integration without assuming those capabilities lie on one scalar axis.

## Never collapse these pairs

| Keep separate | Why |
|---|---|
| reference regime / current state | the baseline is not the thing being measured |
| deviation magnitude / deviation event | distance is not threshold crossing |
| interaction channel / interaction event | capacity may exist without realization |
| latent / active | potential is not realized effect |
| information / information certificate | a signal is not proof of a direct edge |
| entity candidate / certified entity | a declared boundary must earn support |
| coherence / identity | a system may synchronize into the wrong pattern |
| definition / proof | restating a definition does not establish universality |
| abstract concept / substrate witness | TE, MI, `K`, and `r` are not universal by fiat |

## Claim labels

`PRIM` primitive · `DEF` definition · `ASM` assumption · `PROP` derived
proposition · `CONJ` conjecture · `OP` operational criterion · `AN` analytic
result · `CW` computational witness · `EMP` empirical result · `EX` example

## Core symbols

| Symbol | Type | Meaning |
|---|---|---|
| `s ∈ 𝒮` | system candidate | object inside an analysis boundary |
| `X_s` | state space | possible states of `s` |
| `x_t ∈ X_s` | state | state at time `t` |
| `T_s` | transition rule/kernel | how states may evolve |
| `B_s` | boundary | internal/external partition |
| `λ` | scale | level of description |
| `W` | time window | interval used for assessment |
| `N_s ⊆ X_s` | reference regime | baseline set, basin, orbit, or distribution |
| `δ_s` | difference measure | compares observations or state features |
| `ε` | criterion | threshold for a declared distinction |
| `Δ_N(x_t)` | deviation magnitude | distance from the reference regime |
| `Dev_s(t)` | deviation event | declared transition/crossing |
| `𝓔_s` | entity candidates | possible internal loci/subsystems |
| `𝓒_s` | channels | capacities for influence |
| `𝓐_s` | active interactions | realized channel events |
| `𝓙_s` | information candidates | processable differences/signals |

## Null state in one line

A null state is a **reference regime**, often recurrent or metastable, within
which the system remains for the chosen criterion and scale.

It is **not necessarily**:

- static;
- empty;
- interaction-free;
- maximum entropy;
- globally unique.

Possible subtypes: reference, equilibrium, attractor, metastable, recurrent,
statistical, informational, maximum-entropy, meta-null.

## Deviation in one line

A deviation is a **distinguishable departure or regime transition relative to a
declared reference**.

```text
Δ_N(x_t) = distance from x_t to N_s
Dev_s(t) = criterion says a departure/transition occurred
```

A deviation may exist without being currently observed. “Detectable” and
“observed” are separate predicates.

## Interaction ladder

```text
channel exists
    ↓
latent interaction: influence capacity, no certified relevant deviation
    ↓ threshold/condition
active interaction: channel-mediated deviation certified
```

K-SOM-Heb witness:

```text
TE > floor, MI ≈ floor       latent channel
locking discriminant ≥ 0     active/realized locking relation
```

These are witnesses, not universal definitions.

## Information certificate ladder

Always index the claim by context, window, and available conditioning variables.

```text
RELATED   — statistical dependence
DIRECTED  — predictive direction
CONNECTED — direct edge certified relative to observed confounders
```

`connected` does not mean absolute metaphysical causation.

## Entity rule of thumb

An entity may be composite. It earns entity status at a scale when a
coarse-grained description has persistent identity, a supported boundary, and a
useful interface to the rest of the system.

## Emergence rule of thumb

Interaction plus chaos is insufficient. A macro-property is emergent only under
specified local dynamics/organization and a declared coarse-graining.

## Progression rule of thumb

CPAF progression is a **complexity/headroom bound**, not necessarily a total
order.

Concept `B` may be later than `A` because representing or implementing `B`
requires `A` plus additional relations, memory, recursion, integration, or
counterfactual depth. Systems can still have uneven capability profiles.

## Kolmogorov warning

Kolmogorov complexity is a useful analogy for irreducible description length,
but:

- it is uncomputable in general;
- it depends on the description language up to a constant;
- greater description length is not automatically greater cognition;
- CPAF also cares about organization, dependency, and function.

## Fast sanity checks

Before accepting a formula, ask:

1. Are all symbols typed and bound?
2. Is this a definition, assumption, or result?
3. Could an implication be vacuously true?
4. Is the scale and time window clear?
5. Is a measure being mistaken for the property?
6. Is a K-SOM-Heb result being generalized without support?
7. Does the construct permit counterexamples it should exclude?
8. Does it exclude dynamic, composite, or metastable systems accidentally?
