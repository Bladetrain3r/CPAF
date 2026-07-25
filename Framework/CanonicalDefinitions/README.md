# CPAF Canonical Definitions

**Status:** proposed gold-standard layer  
**Authority:** canonical only after explicit author acceptance  
**Migration policy:** additive first; archive or remove legacy definitions later

## Purpose

This folder is the intended long-term source of truth for CPAF definitions,
formal constructs, dependency relations, and scope conditions.

The older files under `Framework/`, `Foundations/`, and `General/` remain useful
historical and explanatory material. During migration they may disagree with
this folder. Such disagreement must be recorded rather than silently resolved.

## Authority order

Once a concept document in this folder is marked **Accepted**, use this order:

1. accepted canonical concept document;
2. accepted canonical metalanguage and progression documents;
3. `Framework/ComputationalProofs.md` for evidence and refinement history;
4. substrate-specific verification and textbook documents;
5. legacy framework, foundation, and general documents.

A **Draft** canonical document proposes a replacement but does not yet override
an accepted legacy construct.

## Status labels

Every canonical document begins with one of:

- **Draft** — active proposal; no authority over accepted definitions.
- **Review** — coherent enough for author decision and adversarial checking.
- **Accepted** — current canonical definition.
- **Superseded** — retained for history but no longer authoritative.
- **Deferred** — intentionally unresolved.

## Claim classes

Every substantial statement should be identifiable as one of:

| Class | Role |
|---|---|
| **Primitive** | supplied term in the metalanguage |
| **Definition** | stipulated meaning or membership condition |
| **Assumption** | condition adopted for a scope, model, or derivation |
| **Derived proposition** | follows from definitions and assumptions |
| **Conjecture** | proposed claim awaiting proof or test |
| **Operational criterion** | measurable substrate-specific test |
| **Analytic result** | mathematically derived under stated assumptions |
| **Computational witness** | runnable existence demonstration |
| **Empirical result** | measured result from a run or data set |
| **Example** | illustration; not evidence by itself |

A contradiction with a definition usually proves only a classification result:

> If `x` lacks a defining property, `x` is not a member of the defined class.

It does not prove universal existence or necessity.

## Canonical concept contract

Each concept document should contain:

1. **Status and version**
2. **Intent**
3. **Dependencies**
4. **Typed abstract definition**
5. **Natural-language bridge**
6. **Necessary and sufficient conditions**
7. **Subtypes**
8. **Relations to adjacent concepts**
9. **Operationalization contract**
10. **Known analytic/computational witnesses**
11. **Non-claims and counterexamples**
12. **Open decisions**
13. **Legacy crosswalk**
14. **Change log**

## Separation rules

Canonical documents must distinguish:

- abstract concept from substrate-specific witness;
- capacity from event;
- state from transition;
- magnitude from threshold crossing;
- measurement from the measured property;
- evidence level from ontological certainty;
- component scale from system scale.

## Current accepted directions

These are author-guided directions, not yet complete concept definitions:

- null state does not require maximum entropy;
- null states may be recurrent or metastable regimes;
- entities may be composite and recursive;
- context-indexed information certificates are allowed;
- emergence requires local criteria and is not automatic;
- progression bounds relative complexity/headroom rather than imposing a total
  ordering over every capability;
- observer relativity remains deferred.

## Migration rule

Do not delete or mass-edit legacy documents while a canonical replacement is
still Draft. First:

1. create the canonical construct;
2. review implications and counterexamples;
3. obtain author acceptance;
4. add pointers from legacy files;
5. archive or trim only after references are stable.
