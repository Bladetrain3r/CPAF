# CPAF Core Bill of Parts

**Purpose:** a working map of the repository's current parts, authority, and
provenance. Use this document to distinguish active work from historical
reference material without moving or deleting files prematurely.

## How to use this map

The repository has two connected workstreams:

1. **Formal spine:** canonical definitions and their typed metalanguage.
2. **Evidence spine:** runnable K-SOM-Heb experiments and the documents that
   explain what they do and do not establish.

The remaining material is reference, unfinished conceptual work, presentation,
or project coordination. A file's location does not by itself make it a
canonical definition.

## Authority and evidence order

Use the following order when documents disagree:

1. An **Accepted** document in `Framework/CanonicalDefinitions/`.
2. Accepted canonical `METALANGUAGE.md` and `PROGRESSION.md`.
3. `Framework/ComputationalProofs.md` for evidence and refinement history.
4. Verified substrate code, scripts, and textbook material under `KSOMHeb/`.
5. Legacy framework, foundation, and general documents.

The canonical layer is currently a proposed gold-standard layer. Its documents
are Drafts unless their status says otherwise, so a Draft does not silently
override an accepted legacy construct.

## Core parts

| Part | Location | Current role | Status |
|---|---|---|---|
| Canonical definitions | `Framework/CanonicalDefinitions/` | Typed formal proposals and the intended long-term source of truth | **Active; Draft/Review workflow** |
| Concept-to-proof bridge | `Framework/ComputationalProofs.md` | Maps abstract concepts to computational witnesses and records refinements | **Active evidence layer** |
| Computational substrate | `KSOMHeb/ksomheb.py` | Reference K-SOM-Heb implementation | **Active** |
| Verification ledger | `KSOMHeb/verification/` | Runnable iterations, checks, plots, and recorded findings | **Active evidence** |
| Textbook | `KSOMHeb/textbook/` | Pedagogical account of the verified substrate and its CPAF mapping | **Active supporting documentation** |
| Substrate coordination | `KSOMHeb/CHEATSHEET.md`, `DECISIONS.md`, `CPAF_MAPPING_NOTES.md`, `HANDOVER.md` | Symbols, decisions, mappings, and detailed pickup context | **Active project metadata** |
| Project coordination | `HANDOVER.md`, `GPTSol.md`, `Claude_Code.md`, `Working_List.md` | Repository map, formal-spine handover, agent conventions, and task queue | **Active project metadata** |

### Current canonical contents

The canonical folder currently contains:

- `README.md` — authority order, status labels, and concept-document contract;
- `METALANGUAGE.md` — typed analysis context, claim classes, scales, clocks, and
  observer-relativity guardrails;
- `PROGRESSION.md` — progression as a partial dependency/complexity relation;
- `CHEATSHEET.md` — compact notation and sanity checks;
- `null_state.md` — Draft 0.3 null-regime definition;
- `deviation.md` — Draft 0.2 deviation definition.

The canonical interaction, information, entity, and system documents described
as future structure in the handover are not yet present in this checkout.

## Reference and legacy parts

These parts remain useful, but are not the current formal authority:

| Location | Contents | Use |
|---|---|---|
| `Framework/nullstate.md`, `Framework/deviation.md`, `Framework/interaction.md`, `Framework/information.md`, `Framework/entity.md`, `Framework/system.md` | Earlier foundational concept documents | Historical cross-checks and migration targets |
| `Foundations/` | Earlier definitions, logical constructs, case analyses, and prose tests | Historical reasoning and examples |
| `General/` | Earlier framework drafts, plans, trees, summaries, and propositions | Historical context |
| `Framework/1 - Basic/`, `Framework/2 - Intermediate/` | Basic and intermediate cognitive concepts | Ungrounded frontier/reference material |
| `Framework/Goals.md`, `Framework/Overview.md` | Older framework overview and goals | Orientation only; follow canonical status and evidence instead |

Do not treat a statement in these locations as current merely because it is
more specific or older. When a canonical document disagrees with a legacy
document, preserve the disagreement in the canonical crosswalk until the
canonical document is accepted.

## Presentation and exploratory parts

| Location | Role |
|---|---|
| `Framework/Tests/` | Earlier demonstrations, case studies, and exploratory analyses |
| `Framework/Axioms/`, `Framework/Applications/` | Proposed axioms and applications; not automatically established results |
| `Framework/Templates/`, `Framework/Docs/` | Templates, glossary, assessments, and supporting documentation |
| `BigBookofCPAF/` | LaTeX presentation assets |

These parts can inform examples or future work, but they do not outrank the
canonical definitions or a runnable verification.

## Practical navigation

- Start with [`HANDOVER.md`](HANDOVER.md) for project status and open work.
- Read [`Framework/CanonicalDefinitions/README.md`](Framework/CanonicalDefinitions/README.md)
  for formal authority and migration rules.
- Read [`Framework/ComputationalProofs.md`](Framework/ComputationalProofs.md)
  for the concept-to-evidence map.
- Read [`KSOMHeb/HANDOVER.md`](KSOMHeb/HANDOVER.md) and
  [`KSOMHeb/verification/README.md`](KSOMHeb/verification/README.md) for the
  computational evidence ledger.
- Read [`KSOMHeb/textbook/00_orientation.md`](KSOMHeb/textbook/00_orientation.md)
  for a guided re-entry.

## Migration and archival rule

Keep migration additive:

1. Create or refine a canonical construct.
2. Review its implications and counterexamples.
3. Obtain explicit author acceptance.
4. Add pointers from affected legacy files.
5. Archive or trim legacy material only after references are stable.

Until then, leave legacy/reference files in place and label their role rather
than mass-editing or deleting them.
