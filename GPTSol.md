# GPTSol — formal spine handover

**Current author:** GPT-5.6 Thinking  
**Branch:** `GPTSol/formal-spine-audit`  
**Focus:** canonical definitions and formal spine

## Mission

Build a gold-standard formal-definition layer for CPAF so that computational
verifications begin from clear, typed, falsifiable constructs rather than
repairing ambiguous definitions after the fact.

The work is additive. Existing documents under `Framework/`, `Foundations/`,
and `General/` remain historical context until the canonical layer is mature
enough for an explicit archive or trimming pass.

## Current focus

### Observer relativity after null state → deviation

Null state and deviation are the first paired concepts because later constructs
depend on a stable account of reference, change, threshold, recurrence, and
regime transition.

Working direction:

- a null state is not necessarily maximum entropy;
- it may be a fixed point, attractor, metastable basin, recurrent phase,
  statistical regime, or explicitly chosen reference;
- maximum entropy is an optional subtype or property;
- deviation magnitude and deviation event are different types;
- a dynamic null may contain internal interactions and state changes while
  remaining inside the reference regime;
- latent interactions are therefore permitted, and active micro-interactions
  may also be permitted when they maintain a macro-level null;
- observer and representation relativity are acknowledged but deferred as an
  ontology decision.

<<<<<<< ours
The null-state draft is now at 0.2. The next seam is separating changes in the
system from changes in the observer's representation or clock. A proposed
computational witness is a set of coupled oscillators represented on different
clocks or time bases. Before promotion, it must distinguish:
=======
The null-state draft is now at 0.3 and the metalanguage at 0.2. Iteration 16 is
the first computational witness for separating changes in the system from
changes in the observer's representation or clock. The canonical pass now
distinguishes:
>>>>>>> theirs

- coordinate or sampling differences from physical deviations;
- clock-relative phase/frequency from invariant relational structure;
- synchronization in one time parameter from synchronization preserved under
  an admissible clock transformation;
- observer-relative operational certificates from ontic claims.

<<<<<<< ours
This is an open research direction, not evidence that K-SOM-Heb has already
resolved clock relativity.
=======
Iteration 16 supports these distinctions for one oscillator substrate and a
bounded set of re-clockings. The admissibility/aliasing boundary and the ontic
status of observer-relative properties remain open.
>>>>>>> theirs

## Author decisions recorded

1. **Canonical folder:** establish a gold-standard definitions folder. Legacy
   documents may later be archived, marked historical, or removed.
2. **Null state:** maximum entropy is not necessary. Use a subtype/decomposition
   approach centred on recurrent or metastable reference regimes.
3. **Observer relativity:** postpone a final commitment. Keep the dependency
   visible rather than silently deciding it.
4. **Entity recursion:** entities may be composite. “Minimal entity” is a
   possible subtype, not the universal definition.
5. **Progression:** stages bound relative conceptual or organizational
   complexity and the mental headroom needed to model the construct. They do
   not place all cognitive capability on one linear scalar axis.
6. **Complexity:** Kolmogorov complexity is a useful analogy, not yet the metric.
   It is uncomputable in general and cannot express every relation between CPAF
   concepts.
7. **Information certificates:** adopt context-indexed levels
   `related < directed < connected`, with room for later refinement.
8. **Emergence:** emergence is conditional. Local organizational and dynamical
   criteria must be satisfied; chaos or interaction alone does not guarantee it.
9. **Active null maintenance:** a macro-level null may be maintained by active
   micro-level interactions. Nullness at one scale does not entail inactivity at
   finer scales; a maintenance claim must still be certified rather than inferred
   from coexistence.
10. **Frequent recurrence:** “high-frequency” metastability means a high return
    probability or revisit rate within a declared time horizon, unless physical
    oscillation frequency is explicitly intended. A revisit returns to the same
    regime or a declared similarity neighbourhood, not necessarily an identical
    microstate.
11. **Observer/clock witness direction:** explore coupled oscillators represented
    on different clocks as the next test of observer relativity. Coordinate
    disagreement is not a physical deviation without an invariant or explicitly
    context-relative criterion.
<<<<<<< ours
=======
12. **Clock typing:** distinguish physical time, participant clock and
    availability, observer clock, sampling schedule, and feature map. Treat
    re-clocking and resampling as different operations; type portable predicates
    as invariant, rate-like measurements as covariant under a declared law, and
    unresolved quantities as representation-sensitive.
>>>>>>> theirs

## Open clarification

Operational domains still need to choose appropriate recurrence estimators,
time horizons, similarity tolerances, and thresholds; the canonical definition
does not impose universal values.

## Canonical structure

```text
Framework/CanonicalDefinitions/
├── README.md
├── CHEATSHEET.md
├── METALANGUAGE.md
├── PROGRESSION.md
├── null_state.md
├── deviation.md
├── interaction.md
├── information.md
├── entity.md
└── system.md
```

Only the first six files are introduced in the initial package. The remaining
concept documents should be added one at a time after their dependencies are
stable.

## Working rules

- Label statements as definition, primitive, assumption, proposition,
  conjecture, operational criterion, analytic result, computational witness,
  empirical result, or example.
- Type every symbol and give functions a domain and codomain.
- Separate abstract constructs from K-SOM-Heb operational witnesses.
- Separate capacity, state, event, measurement, and certificate.
- Preserve a natural-language bridge beside formal notation.
- Treat failed derivations and counterexamples as useful results.
- Do not change an accepted logical construct without Ziggy’s sign-off.
- Keep unresolved ontology choices visible.

## Immediate deliverables

<<<<<<< ours
1. Draft the observer/representation-relativity decision space without silently
   choosing an ontology.
2. Type clock/time-base transformations and candidate invariants in the
   canonical metalanguage.
3. Specify what a different-clock oscillator witness would prove and falsify
   before implementing it in K-SOM-Heb.
4. Test null and deviation classifications against changes of observation map,
   sampling rate, and time parameter.
=======
1. Seek author review of the Draft 0.2 clock metalanguage without silently
   choosing an ontology.
2. Map the admissibility boundary where sampling or time warping loses the
   bandwidth needed for a certificate.
3. Test the formalism on non-affine clocks, irregular sampling, and observation
   maps that preserve or destroy relational structure.
4. Decide whether ontic, epistemic, and operational variants belong in each
   concept document or in one shared observer-relativity document.
>>>>>>> theirs

## Main risks

- creating a formalism so general that it says nothing;
- making K-SOM-Heb observables universal by accident;
- replacing useful conceptual ambiguity with arbitrary precision;
- treating progression as a scalar ranking rather than a complexity bound over
  partially independent capabilities;
- allowing multiple files to continue claiming canonical precedence.

## Pickup order

1. this file;
2. `Framework/CanonicalDefinitions/README.md`;
3. `Framework/CanonicalDefinitions/CHEATSHEET.md`;
4. `Framework/CanonicalDefinitions/METALANGUAGE.md`;
5. `Framework/CanonicalDefinitions/null_state.md`;
6. `Framework/CanonicalDefinitions/deviation.md`;
7. `Framework/ComputationalProofs.md`;
8. `KSOMHeb/HANDOVER.md`.
