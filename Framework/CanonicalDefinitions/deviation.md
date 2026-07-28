# Deviation

**Status:** Draft 0.2
**Dependencies:** null state/reference regime, analysis context, difference criterion  
**Primary adjacent concepts:** information, interaction, meta-null

## Intent

Describe distinguishable change without conflating:

- amount of difference;
- transition event;
- detectability;
- actual observation;
- cause of the change.

## Abstract definition

[DEF] A **deviation magnitude** is a context-indexed measure of difference
between a current state/trajectory and a declared reference regime.

For a set-valued null:

```text
Δ_N(x_t) ≔ inf_{n ∈ N_s} δ_s(O_s(x_t), O_s(n))
```

[DEF] A **deviation event** is a declared transition where a state, trajectory,
relation, or regime crosses the relevant criterion relative to its reference.

A default threshold-crossing form is:

```text
Dev_s(t; C) ≔
    Δ_N(x_t) > ε_D
    ∧ Δ_N(x_t-) ≤ ε_D
```

where `x_t-` denotes the relevant preceding comparison interval.

A bifurcation, structural transition, identity change, or relation change may
use a criterion other than metric distance.

## Natural-language bridge

Deviation is not simply “anything changed.”

It is a change that becomes distinguishable relative to:

- what counted as normal;
- what aspect of the state is being compared;
- the scale;
- the time window;
- the criterion.

The amount of departure and the event of crossing into a new regime are
different things.

## Core distinctions

### Magnitude

“How far from the reference is the current state?”

```text
Δ_N(x_t)
```

### Event

“Did a relevant boundary, threshold, or regime transition occur?”

```text
Dev_s(t; C)
```

### Detectable

“Could the deviation be distinguished under the available method/context?”

```text
Detectable(Dev; C)
```

### Observed

“Was the deviation actually registered?”

```text
Observed(Dev; C)
```

A deviation may be detectable but not observed. A physical transition may occur
while remaining undetectable under a poor representation.

## Causes

Information processing is one possible cause or mediator of deviation, but is
not built into the universal definition.

Permitted sources include:

- external interaction;
- internal dynamics;
- stochastic fluctuation;
- structural damage;
- learning or adaptation;
- endogenous phase transition;
- reference/meta-null change.

This avoids defining deviation through information while defining information
through deviation.

## Subtypes

### State deviation

Departure in a state variable or feature.

### Trajectory deviation

Departure in path, trend, orbit, or temporal pattern.

### Regime deviation

Transition between qualitatively different dynamical regimes.

### Structural deviation

Change to organization, boundary, topology, or coupling structure.

### Relational deviation

Change in a relation between entities even where local states remain similar.

### Identity deviation

Loss or replacement of a stored or recoverable pattern despite continued
coherence or activity.

### Reference deviation

Change that establishes or alters the null regime itself; often produces a
meta-null.

## Necessary conditions

A well-formed deviation claim states:

1. the system or entity;
2. the reference regime;
3. the compared state, trajectory, structure, or relation;
4. the scale;
5. the time window;
6. the difference or transition criterion;
7. whether the claim concerns magnitude, event, detectability, or observation.

## Operationalization contract

A substrate-specific deviation criterion must provide:

- the measured variables;
- the baseline;
- the threshold or regime classifier;
- calibration/noise treatment;
- temporal resolution;
- false-positive/false-negative considerations;
- expected counterexamples;
- falsification checks.

For clock-sensitive data, it must additionally distinguish:

- a second physical trajectory from a re-expression of the same trajectory;
- participant availability/delay from observer timestamping and sampling;
- invariant verdicts from covariant rates or estimator magnitudes;
- physical deviation from loss of observational resolution.

## K-SOM-Heb witnesses

### Locking transition

For two oscillators:

```text
K_c = |Δω| / 2
```

Crossing the locking threshold gives a sharp regime-deviation witness. The
onset coherence `1/√2` is an analytic result for the pair substrate.

### Information transition

Mutual information rises around the locking transition, demonstrating that the
deviation has measurable relational consequences.

### Identity deviation

Iterations 13–14 show that coherence can return while the original stored
pattern does not. This is a deviation of identity, not necessarily a deviation
of gross coherence.

These witnesses do not imply that every deviation is a bifurcation, locking
event, or MI transition.

### Observer re-clocking control

Iteration 16 applies decimation and a smooth monotone time-warp to the same
physical oscillator trajectory. Within the tested range, regime and screening
verdicts and the simultaneous phase-difference distribution remain stable while
TE magnitudes and rate observables change. This is a computational witness that
coordinate disagreement and measurement change need not be physical deviation.

## Relationship to null state

A null regime supplies the reference. A deviation may leave it temporarily,
destroy it, or establish a new meta-null.

Because nulls can be scale-relative:

```text
Dev_s(t; λ_micro)
```

may coexist with:

```text
Null_s(t; λ_macro)
```

and vice versa.

## Relationship to interaction

An interaction channel may remain latent without a relevant deviation. An
active interaction is a channel-mediated deviation event under the selected
criterion.

The realization:

```text
latent interaction → active interaction
```

is itself a deviation in interaction state.

## Relationship to information

Information can:

- make a deviation distinguishable;
- be produced or shared at a deviation;
- encode potential future deviations;
- cause or modulate a deviation.

None of these roles should be assumed universally without an operational
criterion.

## Non-claims

This definition does not claim:

- every change is cognitively relevant;
- every deviation is observed;
- every deviation is caused by information;
- every deviation uses a symmetric metric;
- every deviation magnitude belongs in `[0,1]`;
- one threshold transfers unchanged across substrates or scales;
- a larger deviation implies a higher cognitive capability.

## Observer-relativity marker

The ontology remains **Deferred**. Operationally, compare representations only
after establishing that they refer to the same physical events. For a declared
admissible representation operation `g`:

```text
Invariant(Dev_s; g, C) ≔ Dev_s(D_o; C) ↔ Dev_s(D_o'; C')
```

When this holds, a covariant change such as
`dθ/dτ' = (dθ/dτ)/(dh/dτ)` is a coordinate effect, not a physical deviation.
If a classifier changes after coarse resampling, the first conclusion is that
the certificate is representation-sensitive or unresolved; a physical
deviation requires evidence from the underlying trajectory or an invariant
relation. Independent participant-clock changes are different: altered
co-presence, delay, or medium persistence changes the physical interaction
conditions and may produce a genuine deviation.

## Legacy crosswalk

- `Framework/deviation.md`: preserves distinguishability and recursion while
  separating detectable from observed.
- `Foundations/Definitions.md`: replaces “observable change” with a typed set of
  predicates.
- `Foundations/LogicalConstructs.md`: removes the requirement that every
  deviation be generated by information processing.
- `Framework/ComputationalProofs.md`: retains the locking transition as a
  witness rather than a universal definition.

## Open decisions

1. Whether canonical deviation requires a regime crossing or also includes any
   nonzero magnitude.
2. How to mark cognitively relevant versus merely physical deviations.
3. Whether to normalize all reported magnitudes for cross-system comparison.
4. Which deviation predicates remain invariant under which admissible clock and
   sampling transformations, including the aliasing boundary.

## Change log

- **Draft 0.2:** separates participant-clock physics from observer re-clocking;
  types invariant deviation verdicts and covariant rates; and adds iteration 16
  as a bounded computational control.
- **Draft 0.1:** introduced typed magnitude, event, detectability, and
  observation distinctions.
