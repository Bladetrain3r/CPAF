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

### Reference dynamics: null state → deviation

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

## Open clarification

When “high-frequency metastable phase” is used for a null state, this handover
currently interprets **high-frequency** as **frequently occupied or revisited**,
not high physical oscillation frequency.

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

1. Canonical authority and document contract.
2. Metalanguage and quick-reference cheatsheet.
3. Draft canonical null-state definition.
4. Draft canonical deviation definition.
5. Legacy and computational-witness crosswalks.

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
