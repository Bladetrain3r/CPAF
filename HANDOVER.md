# CPAF — project handover / pickup reference (repo-wide)

*The top-level map for the whole repository. For deep re-entry into the
computational work, pair this with `KSOMHeb/HANDOVER.md` (iteration-by-iteration
detail) and `Framework/ComputationalProofs.md` (the concept↔proof bridge).*

---

## What CPAF is, in one paragraph

The **Cognitive Progression Assessment Framework** treats cognition as a
*continuum* and stages it from a **null state** upward through **deviation,
interaction, information, entity, system**, and (higher) awareness, memory, and
beyond. The framework proper (`Framework/`, `Foundations/`, `General/`) defines
each concept abstractly — definition, logical construct, math. The newer half of
the project (`KSOMHeb/`) builds a **running, verified computational substrate**
(coupled learning oscillators) that gives those abstract concepts concrete,
testable **single-case proofs**. The two halves meet in
`Framework/ComputationalProofs.md`.

## Repository map

```
CPAF/
├── README.md                 project front door
├── HANDOVER.md               this file (repo-wide pickup)
├── Framework/                the foundational concepts, formalized
│   ├── nullstate / deviation / interaction / information / entity / system .md
│   ├── Overview.md           the concepts + math constructs, unified
│   └── ComputationalProofs.md  ← THE BRIDGE: each concept → its verified proof
├── Foundations/              LogicalConstructs, UnifiedFunction, Definitions, Case analyses, Tests
├── General/                  framework(0.2), StrictDefinitions, LogicalPropositions, Plan, Tree, summary
├── BigBookofCPAF/            LaTeX styling (Introduction.sty) — presentation layer
└── KSOMHeb/                  the computational substrate + verification + textbook
    ├── HANDOVER.md           deep pickup for the K-SOM-Heb work (READ FOR DETAIL)
    ├── CHEATSHEET.md · DECISIONS.md · CPAF_MAPPING_NOTES.md
    ├── ksomheb.py · requirements.txt
    ├── verification/         iter1–iter12, one runnable script + plot + README each
    ├── visualiser/           browser demo (parity-checked vs the .py)
    └── textbook/             00–12 + Intermission + Appendix A (the mini-textbook)
```

## Status at this checkpoint

- **The foundational-layer bridge is COMPLETE and integrated.** All six
  foundational concepts now have computational single-case proofs (K-SOM-Heb
  iters 1–12), mapped in `Framework/ComputationalProofs.md`, with discoverability
  pointers from `Framework/Overview.md` and the root `README.md`.
- **Framework refinements underway.** Four refinements the proofs suggest are
  logged in `ComputationalProofs.md` §7. **7.1 and 7.2 are applied** (with author
  direction): the null state permits *latent* interactions (`nullstate.md`), and
  interaction now splits into **latent vs active** — a *sign problem*, the sign of
  the locking discriminant `Disc=1−(Δω/2K)²` (`interaction.md`, grounded by
  iter 12). **7.3** (information certificate levels) and **7.4** (conditional
  emergence) are proposed, pending sign-off.
- **Damage recovery has a first result (iter 13).** Recovery is recovery of the
  stored *pattern* (not mere coherence), and it requires a *protected* memory —
  the first step into the active layer (memory + graceful degradation).
- **What's NOT yet grounded** (honest ledger, `ComputationalProofs.md` §8): the
  *active/higher* layer beyond memory (awareness, reflection, experience,
  knowledge, vision, understanding); *universality* (one substrate only); a
  *system-level* deviation threshold; multistable "recover into a different
  stored pattern".

## Open work queue (project level)

1. **Finish the interaction-cluster refinement** — 7.3 (`information.md`:
   related<directed<connected certificate levels) and 7.4 (`system.md`:
   emergence conditional on the right learning ingredients). *Sign-off needed.*
2. **Per-concept "Computational proof →" footers** on the remaining `Framework/`
   concept docs (nullstate & interaction already link theirs).
3. **Damage recovery / graceful degradation** — **first result done (iter 13):**
   recovery is recovery of the stored *pattern*, and it needs a protected memory
   (unprotected memory has a resilience threshold then loses the identity —
   "ship of Theseus"). *Open follow-ups:* multistable/associative-memory recovery
   into a genuinely *different stored* pattern (iter 14 candidate); structural
   lesions of `K`; the collapse edge vs the iter-3 separatrix.
4. **Climb a layer** — the *active* concepts. *Memory* now has both a substrate
   (`K`) and an operational test (iter 13 recovery); *awareness/reflection/
   experience* are the frontier. Deliberately deferred until foundations are firm.
5. **Book-wide revision pass** — 12 chapters + Intermission across many sessions;
   a consistency sweep would consolidate.
6. **Standing K-SOM-Heb follow-ups** — see `KSOMHeb/HANDOVER.md` §C (blind
   boundary search, asymmetric-`K` learning rule, global-`r` threshold, …).

## How to pick up

1. **Environment (ephemeral container):** `pip3 install -r KSOMHeb/requirements.txt`.
2. **Confirm it runs:** `python3 KSOMHeb/verification/iter12_interaction_sign.py`
   (should print `ALL PASS`).
3. **Orient:** this file → `Framework/ComputationalProofs.md` (the bridge) →
   `KSOMHeb/HANDOVER.md` (iteration detail) → `KSOMHeb/textbook/I_intermission.md`
   (fastest conceptual re-entry).
4. **Pick from the work queue.** The current thread is the framework-integration
   refinement (item 1).

## Conventions

- Development is **additive to CPAF**; the computational work lives under
  `KSOMHeb/`, and integration touches `Framework/` only additively.
- Discipline: **conjecture in notes → prove under `KSOMHeb/verification/` →
  promote to the framework docs.** Nothing asserted that isn't run.
- Refinements that edit the concept docs' **formal logical constructs** get
  author sign-off before landing (cf. `KSOMHeb/DECISIONS.md` D9, D15).
