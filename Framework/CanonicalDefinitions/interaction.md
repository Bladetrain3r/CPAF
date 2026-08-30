# Interaction

**Status:** Draft 0.1  
**Dependencies:** analysis context, entities or subsystem candidates, channels,
information candidates, deviation criteria  
**Primary adjacent concepts:** information, deviation, system, entity

## Intent

Separate the capacity for influence from a realized interaction event. A channel
may exist and transmit influence without producing a certified deviation under
the selected scale, window, and criterion.

## Typed abstract definition

For candidates `a` and `b` in an analysis context `C`:

```text
Ch_s(a → b; C)       channel or capacity for influence
Int_lat(a → b; C)    latent interaction capacity
Int_act(a → b,t; C)  active interaction event
```

`Ch_s` is a relation in the model, not by itself evidence that influence was
realized. A latent interaction has an available channel but no certified
channel-mediated relevant deviation in `b` during the declared assessment.
An active interaction is a channel-mediated event for which that deviation is
certified.

```text
Int_lat(a → b; C) ≔ Ch_s(a → b; C) ∧ ¬ActiveCert(a → b; C)

Int_act(a → b,t; C) ≔
    Ch_s(a → b; C)
    ∧ ActiveCert(a → b,t; C)
```

`ActiveCert` is intentionally operational and scale-indexed. It must identify
the information candidate, deviation predicate, comparison interval, and
conditioning or intervention used to support the claim.

## Natural-language bridge

An interaction is an influence relation between system components. The relation
can be dormant, weak, mediated, directed, or realized as an event. “The
components are connected” and “the connection changed the target” are separate
claims.

## Necessary and sufficient conditions

### Channel claim

A channel claim requires:

1. source and target candidates;
2. a declared analysis boundary, scale, and time window;
3. a modelled or measured pathway by which source variation could affect target;
4. an admissible certificate for that pathway.

### Active-event claim

An active interaction claim requires all channel conditions plus:

1. a time or event interval;
2. a target deviation criterion;
3. evidence that the deviation is attributable to the channel relative to the
   available alternatives.

The last condition may be intervention-based, model-based, or observational.
The evidence level must be stated; observational prediction is not automatically
causal attribution.

## Subtypes

- **Direct:** influence is transmitted without a separately modelled mediator.
- **Mediated:** influence passes through a persistent or transient medium.
- **Internal:** source and target are inside one declared system boundary.
- **External:** the pathway crosses a declared system boundary.
- **Directed:** the evidence distinguishes `a → b` from `b → a`.
- **Bidirectional:** both directed pathways are separately supported.
- **Latent:** a channel is available without a certified relevant deviation.
- **Active:** a channel-mediated deviation is certified.

These labels may co-occur. A mediated channel can be latent or active, and an
active interaction need not be cognitively relevant.

## Relation to adjacent concepts

- A **deviation** supplies the target-side change criterion for an active event.
- **Information** identifies a processable difference or signal that may travel
  through a channel; information and interaction are not synonyms.
- An **entity** or subsystem supplies a possible source or target.
- A **system** supplies the boundary, scale, and available context.
- A latent-to-active transition is itself a possible deviation in interaction
  state.

## Operationalization contract

A substrate-specific interaction report must state:

1. source, target, and any mediator;
2. the physical or modelled channel;
3. the measure and null/floor used for channel evidence;
4. the active-event deviation criterion;
5. conditioning variables, interventions, or confounder limitations;
6. directionality and time-lag assumptions;
7. scale, window, clock, sampling, and feature map;
8. what result would falsify the claim.

Transfer entropy, conditional transfer entropy, mutual information, coupling
weights, and locking tests are candidate measures or certificates, not universal
definitions.

## Known computational witness

K-SOM-Heb provides a bounded witness:

- iteration 8 distinguishes directed transfer and hidden common-cause effects;
- iteration 11 shows a latent channel with transfer entropy above floor while
  mutual information remains near floor;
- iteration 12 separates latent and active regimes with the sign of the
  substrate's locking discriminant;
- iteration 15 supplies a mediated/stigmergic channel;
- iteration 16 separates participant desynchronization from observer
  re-expression;
- iteration 17 demonstrates a one-way detector channel.

These runs establish realizability in one substrate only.

## Non-claims and counterexamples

This definition does not claim:

- every coupling is an interaction in every analysis context;
- every interaction produces a deviation;
- statistical dependence proves a channel or causation;
- a symmetric model rules out directed interactions;
- a channel measure is invariant under arbitrary clocks or sampling;
- latent interaction is equivalent to zero influence;
- interaction alone implies cognition, agency, or awareness.

## Open decisions

1. Select certificate requirements for channel existence when interventions are
   unavailable.
2. Define how partial observability weakens the related/directed/connected
   certificate ladder.
3. Determine whether active interaction requires target deviation, source
   deviation, or either under a given application.
4. Map the admissibility boundary for clocks, resampling, and medium bandwidth.

## Legacy crosswalk

- `Framework/interaction.md`: preserves the active interaction construct while
  making channel/event separation canonical.
- `Framework/information.md`: retains embedded information as unrealized
  deviation potential, now related to latent channels without equating them.
- `Framework/ComputationalProofs.md` §4 and §7.2: evidence and refinement history.

## Change log

- **Draft 0.1:** introduces typed channel, latent-capacity, and active-event
  definitions; records the existing computational witnesses.
