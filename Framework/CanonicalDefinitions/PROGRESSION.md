# CPAF Progression as Complexity and Headroom

**Status:** Draft 0.1

## Intent

CPAF uses progression to organize concepts that demand increasing amounts of
structure, relation, retained state, recursion, integration, or future-directed
modeling.

This progression is not necessarily a single linear scale of “more cognitive.”
It is primarily a **bound on relative conceptual and organizational complexity**
and on the mental or computational headroom needed to track the construct.

## Partial order, not total order

Let `A ≺ B` mean:

> Under the canonical dependency model, a sufficient account of `B` normally
> requires an account of `A` plus at least one additional relation, operation,
> retained structure, or level of integration.

This defines a dependency/complexity relation. It does not imply:

- every system with `B` exhibits more of every capability than every system
  with `A`;
- concepts at the same stage are equivalent;
- all systems develop the concepts in one temporal order;
- there is one universal scalar cognitive score.

Two concepts may be:

- ordered by dependency;
- comparable only under one complexity dimension;
- orthogonal;
- mutually enabling;
- incomparable with current definitions.

## Capability profile

A system should eventually be representable by a profile such as:

```text
C(s) = (
    deviation discrimination,
    interaction certification,
    information use,
    entity closure,
    memory retention,
    recovery fidelity,
    reflection depth,
    preference integration,
    counterfactual projection,
    ...
)
```

A stage may then summarize the highest **prerequisite-closed region** of the
profile, while the profile preserves uneven capabilities.

## Candidate complexity dimensions

These are not yet metrics:

1. **Dependency depth** — number and structure of prerequisite concepts.
2. **Relational arity** — how many entities, states, times, or models must be
   related simultaneously.
3. **Temporal depth** — present response vs retained history vs projected future.
4. **Recursive depth** — entities/systems represented as components at multiple
   scales.
5. **Integration burden** — number of partially independent signals or models
   coordinated into one operation.
6. **Counterfactual depth** — ability to compare unrealized alternatives.
7. **Identity burden** — persistence and recovery of a particular pattern,
   rather than generic activity.
8. **Certificate burden** — context required to justify a claim.

## Kolmogorov complexity

Kolmogorov complexity may provide a useful analogy:

> later constructs may require longer irreducible descriptions because they
> encode more relations and operations.

It is not adopted as CPAF's sole complexity metric because:

- exact Kolmogorov complexity is uncomputable;
- values are relative to a description language up to an additive constant;
- random noise has high description complexity but low organization;
- cognition depends on structured function, dependency, and integration, not
  description length alone.

Useful future alternatives may include logical depth, effective complexity,
minimum description length, computational depth, causal-state complexity, or a
custom dependency-weighted construct measure.

## Working interpretation

The original progression remains useful as a teaching and reasoning scaffold:

- early concepts require little headroom and few simultaneous relations;
- later concepts require maintaining increasingly nested dependencies;
- the ordering bounds the complexity of a sufficient explanation;
- capability remains multidimensional.

## Open work

- formalize prerequisite closure;
- decide whether stages are named regions, ordinal bands, or both;
- test the ordering against counterexample systems;
- distinguish construct complexity from implementation complexity;
- avoid ranking noise, bloat, or inefficient representation as higher cognition.
