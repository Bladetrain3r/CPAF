# Null State

**Status:** Draft 0.1  
**Dependencies:** canonical metalanguage, analysis context, state, time, scale  
**Primary adjacent concept:** deviation

## Intent

Provide the reference condition from which CPAF can describe change without
requiring the reference to be static, empty, globally unique, or maximum
entropy.

## Abstract definition

[DEF] For a system candidate `s` under analysis context `C`, a **null regime**
`N_s` is a declared baseline subset, trajectory class, basin, attractor, or
state distribution against which relevant deviations are measured.

[DEF] A current state or trajectory segment is **null-relative-to `N_s`** when
it remains within the tolerance or membership criterion of that reference
regime for the declared scale and time window.

For a set-valued baseline:

```text
Δ_N(x_t) ≔ inf_{n ∈ N_s} δ_s(O_s(x_t), O_s(n))

Null_s(x_t; C) ≔ Δ_N(x_t) ≤ ε_N
```

For a dynamic or statistical null, membership may instead be determined by an
orbit, basin, recurrence, residence-time, classifier, or distributional
criterion.

## Natural-language bridge

A null state is the “normal enough for this analysis” regime.

It may be:

- a resting point;
- a stable operating range;
- a repeating cycle;
- a metastable basin;
- a frequently revisited phase;
- a learned or historically established pattern;
- a statistical distribution;
- an externally selected baseline.

The system does not have to stop changing inside the null regime. What matters
is whether it leaves or transforms the reference regime in a way that satisfies
the selected deviation criterion.

## Necessary conditions

A usable null regime requires:

1. a system boundary or candidate;
2. a state or trajectory description;
3. a declared scale;
4. a comparison/reference regime;
5. a membership, distance, recurrence, or divergence criterion;
6. a time window where applicable.

## Not universally necessary

The following are not required of every null state:

- zero motion;
- zero internal interaction;
- zero information;
- maximal entropy;
- permanent stability;
- global uniqueness;
- a single point in state space.

## Subtypes

### Reference null

Any explicitly selected baseline used for comparison.

### Equilibrium null

A fixed point or equilibrium region under the system dynamics.

### Attractor null

A reference regime defined by attraction from a basin of states.

### Metastable null

A reference regime with finite but meaningful residence time before escape.

### Recurrent null

A regime revisited sufficiently often under a declared recurrence criterion.

### Statistical null

A baseline distribution or stochastic process rather than a fixed state.

### Informational null

A regime in which a selected informational relation or certificate remains
below its criterion.

### Maximum-entropy null

A special subtype or property where the reference maximizes a declared entropy
measure under stated constraints.

Maximum entropy is not part of the general null-state definition.

### Meta-null

A new reference regime established after a transition, adaptation, or
interaction. A meta-null changes the baseline from which later deviations are
measured.

## Interaction inside a null regime

[CONJ / decision point] A macro-level null may be maintained by active
micro-level interactions. Therefore:

```text
null at scale λ_macro
```

does not automatically imply:

```text
no active interaction at every λ_micro.
```

The existing “poised, not empty” refinement safely permits latent channels.
The canonical version may need to go further and permit active internal
maintenance while no relevant macro-deviation occurs.

This requires author sign-off because it changes the strongest reading of the
current `¬∃int_act` null-state construct.

## Metastability and frequency

The phrase “high-frequency metastable phase” is provisionally read as a regime
that is **frequently occupied or revisited**, despite finite residence or
occasional departure.

A future operational criterion might use:

- occupancy fraction;
- return frequency;
- mean residence time;
- basin size;
- transition probability;
- recurrence rate.

No universal threshold is proposed yet.

## Relationship to deviation

Null and deviation are relational:

```text
no reference regime → no reference-relative deviation
```

A deviation may:

- leave a null regime;
- alter its structure;
- establish a new meta-null;
- occur at one scale while another scale remains null.

## Operationalization contract

A substrate-specific null-state claim must state:

1. what `N_s` is;
2. how membership or distance is measured;
3. the scale and time window;
4. the tolerance/threshold;
5. whether the regime is fixed, dynamic, metastable, recurrent, or statistical;
6. which internal dynamics are permitted;
7. what would falsify the classification.

## K-SOM-Heb witness

The incoherent oscillator regime provides one witness:

- phases are dispersed;
- coherence is near its floor;
- pairwise locking deviations are absent;
- latent sub-threshold channels may remain.

This is a computational witness for a loaded/informational null, not a universal
definition of null states.

## Non-claims

This definition does not claim:

- every system has one natural null;
- the assessor always chooses the correct baseline;
- all null states are maximum entropy;
- all scales share the same null classification;
- nullness is representation-invariant;
- metastability alone makes a regime cognitively meaningful.

## Observer-relativity marker

**Deferred.** The operational criterion necessarily uses a state
representation. CPAF has not yet decided whether nullness is fundamentally
observer-relative, merely measurement-relative, or invariant under an
appropriate class of representations.

## Legacy crosswalk

- `Framework/nullstate.md`: preserves baseline/reference and meta-null intent;
  relaxes universal maximum-entropy language.
- `Foundations/Definitions.md`: generalizes equilibrium to dynamic regimes.
- `General/StrictDefinitions.md`: rejects a single compact definition as
  sufficient without reference criteria.
- `Framework/ComputationalProofs.md`: preserves the loaded-null result while
  separating substrate witness from abstract definition.

## Open decisions

1. Confirm “high-frequency” means frequently occupied/revisited.
2. Decide whether active micro-interactions may maintain a macro-null.
3. Decide whether a system must possess a natural null or may use only
   assessor-selected references.
4. Revisit observer relativity later.
