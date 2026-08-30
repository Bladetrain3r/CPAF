# System

- **Status:** Draft 0.1
- **Dependencies:** supplied analysis boundary, state space, transition rule,
  scale, entities, channels, and interfaces
- **Primary adjacent concepts:** entity, interaction, information, deviation,
  progression

## Intent

Provide a non-circular candidate-system description and a stricter
organizational qualification. A system boundary is supplied for analysis; the
presence of entities, interactions, or cognition must then be tested rather than
assumed from the word “system.”

## Typed abstract definition

At the metalanguage level, a system candidate is:

```text
s_C ≔ (B_s, X_s, T_s)
```

where `B_s` is a boundary specification, `X_s` a state space, and `T_s` a
deterministic or stochastic transition rule/kernel. A richer CPAF description
may include:

```text
s_CPAF ≔ (B_s, X_s, T_s, 𝓔_s, 𝓒_s, Interface_s)
```

where `𝓔_s` contains entity candidates, `𝓒_s` channels, and `Interface_s`
specifies internal and external pathways.

The candidate-system tuple is a modelling primitive. A **qualified organized
system** is proposed as a candidate whose declared components and transitions
support the relevant entity, channel, and interface criteria at the selected
scale.

## Natural-language bridge

A system is a bounded description of states and how they can change. It may be
physical, computational, biological, social, or abstract. “Cohesive assembly of
entities” is a possible qualification of a system, not a prerequisite for
choosing a boundary or analysing a process.

## Necessary and sufficient conditions

### Candidate-system claim

A candidate-system claim requires:

1. a declared boundary and inclusion/exclusion rule;
2. a state or trajectory representation;
3. a transition rule, kernel, or justified process model;
4. a scale and time window where relevant.

### Organized-system claim

An organized-system claim additionally requires:

1. one or more supported component or entity descriptions;
2. specified internal or external channels;
3. a declared interface;
4. evidence that the organization is explanatory or predictive at the selected
   scale.

No universal requirement says that every system has internal interaction,
embedded information, or a natural null regime.

## Subtypes

- **Candidate system:** boundary and dynamics supplied, organization unresolved.
- **Organized system:** entity, channel, and interface criteria are supported.
- **Open system:** exchanges state, energy, matter, or information across its
  boundary under the selected model.
- **Closed-for-analysis system:** external pathways are excluded by scope, not
  necessarily absent physically.
- **Composite system:** contains nested entities or subsystems.
- **Recursive system:** a system description functions as an entity at a higher
  scale.
- **Emergent system property:** a macro-property certified relative to a
  coarse-graining and mechanism, not merely surprising or hard to predict.

## Emergence

Emergence is a relation between levels of description, not a separate substance:

```text
Emergent(P; λ_micro, λ_macro, C) ≔
    MacroProperty(P; λ_macro, C)
    ∧ CoarseGraining(λ_micro → λ_macro; C)
    ∧ MechanismSupported(C)
    ∧ ¬AdequatelyPredictedByIndependentParts(P; C)
```

The final predicate must be made precise for the application. A property being
unobvious, computationally difficult, or absent from an individual component is
not by itself evidence of emergence. The mechanism, comparison model, and
coarse-graining must be named.

## Relation to adjacent concepts

- **Entities** are candidate or certified loci inside the supplied boundary.
- **Interactions** specify pathways among components and across interfaces.
- **Information** describes processable, counterfactually effective differences.
- **Deviation** compares system or component trajectories with a reference regime.
- **Progression** compares the dependency and integration burden of descriptions;
  it does not rank every system on one scalar.

## Operationalization contract

A substrate-specific system report must state:

1. boundary, exclusions, and scale;
2. state variables and transition model;
3. candidate/certified entities and their coarse-grainings;
4. channels, mediators, and external interfaces;
5. reference regimes and deviation criteria;
6. any emergence property, comparison level, and mechanism;
7. physical time, participant availability, observer clock, sampling, and
   feature map when time-series evidence is used;
8. alternative boundaries and falsification checks.

Modularity, collective coherence, effective macro-dynamics, closure, and
cross-boundary transfer are candidate operational measures. None is a universal
system criterion.

## Known computational witness

K-SOM-Heb provides bounded witnesses:

- iterations 3–5 show collective dynamics and that modularity requires specified
  learning and competition ingredients;
- iterations 9–10 show a locked cluster and grown modules acquiring effective
  macro-dynamics and recursive entity interfaces;
- iteration 15 shows a system whose coordination is mediated by an external
  persistent medium;
- iteration 16 separates participant-clock physics from observer
  re-expression;
- iteration 17 demonstrates feed-forward detector composition without upstream
  trajectory change.

These establish conditional realizations in one substrate. They do not establish
that emergence, organization, or system boundaries are universal or unique.

## Non-claims and counterexamples

This definition does not claim:

- every chosen boundary is ontically natural;
- systems require a finite number of entities;
- interaction or complexity automatically yields cognition;
- emergence means irreducibility in every formal sense;
- modularity, coherence, or entropy alone certifies organization;
- externalized memory must be inside the system boundary;
- a system-level threshold follows from the pairwise `1/√2` witness.

## Open decisions

1. Define minimum evidence for a qualified organized system across substrates.
2. Choose a canonical boundary/interface treatment for persistent media and
   external memory.
3. Formalize emergence comparison models without conflating unpredictability
   with non-reducibility.
4. Determine whether progression stages are prerequisite-closed regions,
   ordinal bands, or both.
5. Establish whether a system-level deviation threshold can be derived or must
   remain application-specific.

## Legacy crosswalk

- `Framework/system.md`: retains state, entity, interaction, and interface roles
  while removing circular and automatic-emergence claims.
- `Framework/Overview.md`: supplies historical progression context; this Draft is
  the typed migration target.
- `Framework/ComputationalProofs.md` §6 and §7.4: evidence and conditional
  emergence refinement history.

## Change log

- **Draft 0.1:** introduces candidate versus organized systems and a
  mechanism-indexed emergence criterion.
