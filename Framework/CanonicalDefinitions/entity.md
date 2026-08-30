# Entity

**Status:** Draft 0.1  
**Dependencies:** system candidate, state space, scale, persistence or identity
criterion, boundary and interface criteria  
**Primary adjacent concepts:** system, interaction, information, memory

## Intent

Define entity-hood as a certifiable locus of organized state and processing
without requiring primitive entities to be indivisible. The definition must
permit composite, recursive, and scale-dependent entities.

## Typed abstract definition

For a candidate `e` inside system candidate `s`:

```text
e ⊆ s
φ_e : X_e → M_e
```

`φ_e` is a declared coarse-graining from the candidate's microstate or
trajectory to a macrostate. Entity certification is proposed as a bundle:

```text
Entity_s(e; λ, C) ≔
    PersistentId(e; λ, C)
    ∧ SupportedBoundary(e; λ, C)
    ∧ PredictiveAdequacy(φ_e; C)
    ∧ Interface(e; C)
```

The predicates are operational and must be defined for the application.
`PersistentId` may mean persistence, recoverability, or a declared identity
criterion; it need not mean an unchanged microstate.

## Natural-language bridge

An entity is a relatively persistent, bounded locus that can be described as one
unit at a declared scale and can participate in interactions or processing. A
cluster, organism, process, institution, or software module may qualify when its
boundary and identity earn support from its dynamics and interface.

## Necessary and sufficient conditions

A candidate entity claim requires:

1. a candidate subset or subsystem;
2. a declared scale and coarse-graining;
3. an identity or persistence test over a time window;
4. evidence supporting the proposed boundary;
5. predictive or explanatory adequacy of the macro-description;
6. an interface through which internal and external influences can be assessed.

The conjunction is a sufficient certification rule for the selected context.
No single predicate, including cohesion or a named boundary, is sufficient in
general.

## Subtypes

- **Atomic-at-scale:** treated as indivisible for the current analysis.
- **Composite:** made of certified or candidate sub-entities.
- **Recursive:** can itself function as a component at a higher scale.
- **Process entity:** identity is carried by an organized trajectory or function.
- **Structural entity:** identity depends substantially on persistent
  organization or connectivity.
- **Relational entity:** boundary or identity is defined by a stable relation.
- **Candidate entity:** proposed but not yet certified.
- **Certified entity:** satisfies the declared certification bundle.

Entity status is always indexed by scale and context. A candidate can be an
entity at one scale and merely a collection at another.

## Relation to adjacent concepts

- A **system** supplies the candidate boundary in which an entity is assessed.
- An **interaction** is a channel or event involving entities or subsystems.
- **Information** requires a processor; an entity is one possible processor.
- **Memory** can support identity and recovery but is not required for every
  short-lived entity.
- A **deviation** may change an entity's state, boundary, or identity.

## Operationalization contract

A substrate-specific entity report must state:

1. candidate members and boundary rule;
2. coarse-graining and macrostate variables;
3. persistence, recovery, or identity metric;
4. internal cohesion and external interface tests;
5. predictive comparison against an ungrouped or alternative boundary;
6. scale, window, clock, sampling, and accessible variables;
7. fragmentation and absorption counterexamples;
8. what result would revoke certification.

Closure, effective dynamics, clustering, recovery fidelity, and predictive
adequacy are candidate tests. A high coherence value alone is insufficient.

## Known computational witness

K-SOM-Heb provides a bounded witness:

- iteration 9 shows a locked oscillator cluster coarse-graining to one effective
  oscillator, while an unlocked collection fails the same criteria;
- iteration 10 grows modules through learning, and macro closure discriminates a
  true boundary from an arbitrary one;
- iterations 13–14 distinguish coherent activity from recovery of a particular
  identity;
- iteration 17 demonstrates a read-only detector as a composable subsystem
  without changing the upstream pair trajectory.

These are computational witnesses in one substrate, not universal entity tests.

## Non-claims and counterexamples

This definition does not claim:

- every subset, connected component, or cluster is an entity;
- entities must be minimal, biological, conscious, or agentic;
- persistence requires an unchanged material substrate;
- coherence proves identity or boundary;
- a useful coarse-graining is unique;
- entity-hood is invariant under arbitrary observation maps or scales;
- composite entities eliminate the need to analyze their internal structure.

## Open decisions

1. Select minimum evidence for `SupportedBoundary` when no intervention is
   available.
2. Define how much predictive loss is acceptable for a macro-description.
3. Map absorption, fragmentation, and identity under structural lesions.
4. Determine when a medium or external memory belongs inside the entity boundary.

## Legacy crosswalk

- `Framework/entity.md`: preserves recursive processing and state-transition
  roles while replacing “any processor” with a certification bundle.
- `Framework/system.md`: supplies the non-circular candidate-system boundary.
- `Framework/ComputationalProofs.md` §5: entity and grown-entity witnesses.

## Change log

- **Draft 0.1:** introduces scale-indexed candidate/certified entity types and a
  persistence-boundary-interface rule.
