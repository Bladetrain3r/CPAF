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
├── Claude_Code.md            per-agent focus & team coordination conventions
├── Working_List.md           pickup-able task board (with difficulty hints)
├── GPTSol.md                 formal-spine audit handover (GPT)
├── Framework/                the foundational concepts, formalized
│   ├── CanonicalDefinitions/ ← GOLD-STANDARD layer (GPT): metalanguage, progression, typed concept defs (authority order in its README)
│   ├── nullstate / deviation / interaction / information / entity / system .md  (legacy/historical)
│   ├── Overview.md           the concepts + math constructs, unified
│   └── ComputationalProofs.md  ← THE BRIDGE (evidence layer, authority #3): each concept → its verified witness
├── Foundations/              LogicalConstructs, UnifiedFunction, Definitions, Case analyses, Tests
├── General/                  framework(0.2), StrictDefinitions, LogicalPropositions, Plan, Tree, summary
├── BigBookofCPAF/            LaTeX styling (Introduction.sty) — presentation layer
└── KSOMHeb/                  the computational substrate + verification + textbook
    ├── HANDOVER.md           deep pickup for the K-SOM-Heb work (READ FOR DETAIL)
    ├── CHEATSHEET.md · DECISIONS.md · CPAF_MAPPING_NOTES.md
    ├── ksomheb.py · requirements.txt
    ├── verification/         iter1–iter15, one runnable script + plot + README each
    ├── visualiser/           browser demo (parity-checked vs the .py)
    └── textbook/             00–13 + Intermission + Vol II Stigmergy Intermission + Appendix A
```

## Status at this checkpoint

- **Two workstreams, now interlocked.** GPT ran a **formal-spine audit** and
  produced `Framework/CanonicalDefinitions/` — a gold-standard, *typed* definition
  layer with a **metalanguage** (claim classes `[AN]`/`[CW]`/`[CONJ]`…, the
  analysis context, capacity/event/measurement/scale separations). Claude Code's
  verification + textbook side supplies the **computational witnesses**. The
  canonical `README.md` sets the authority order; `ComputationalProofs.md` is the
  evidence layer (#3). The canonical docs cite our iterations as witnesses (e.g.
  `deviation.md` → iter 6 and the identity-deviation of iters 13–14).
- **Textbook Volume I is a complete draft.** Ch 0–13 + Intermission + Appendix A.
  **Ch 13 is the capstone** — it re-reads Volume I in the canonical metalanguage
  (a witness table), and surfaced **4 revisions** to apply (null≠max-entropy;
  keep `Kc`/`1/√2` typed; global-`r` stays `[CONJ]`; iter 4 is a classification
  result). **Volume II** (the active layer — memory, recovery fidelity, awareness,
  reflection) opens with damage recovery (iters 13–14).
- **The foundational-layer bridge is COMPLETE and integrated.** All six
  foundational concepts have computational single-case proofs (iters 1–12),
  mapped in `Framework/ComputationalProofs.md`; the canonical layer has absorbed
  the §7 refinements (7.1 latent interactions, 7.3 certificate ladder, 7.4
  conditional emergence).
- **Framework refinements underway.** Four refinements the proofs suggest are
  logged in `ComputationalProofs.md` §7. **7.1 and 7.2 are applied** (with author
  direction): the null state permits *latent* interactions (`nullstate.md`), and
  interaction now splits into **latent vs active** — a *sign problem*, the sign of
  the locking discriminant `Disc=1−(Δω/2K)²` (`interaction.md`, grounded by
  iter 12). **7.3** (information certificate levels) and **7.4** (conditional
  emergence) are proposed, pending sign-off.
<<<<<<< ours
- **Canonical null state is now Draft 0.2.** A macro-null may be actively
=======
- **Canonical null state is now Draft 0.3.** A macro-null may be actively
>>>>>>> theirs
  maintained by micro-level interactions: nullness constrains relevant
  deviation at the declared scale, not all finer-scale activity. Maintenance
  requires a certificate rather than mere coexistence. A revisit is a return to
  the same reference regime or a declared similarity neighbourhood, and
  “high-frequency” metastability means high finite-horizon return probability
  or revisit rate—not physical oscillation frequency unless stated.
- **Observer/clock relativity has a first witness (iter 16, D22).** The seam
  splits in two, kept separate per the canonical guardrails. *Participant*
  clocks are physical: a direct edge needs co-presence, while a stigmergic
  medium buffers desynchronization in proportion to its persistence time
  (`W50 ∝ 1/γ` — external memory doubles as a clock buffer), and mediated
  edges carry a memory signature (persistent TE-lag tail). *Observer*
  re-clocking is representational: decimation and monotone time-warps of the
  same trajectory move magnitudes (TE bits, rates) but not certificate
  verdicts (screened-off, regime) or relational structure (the Δθ
  distribution) — coordinate disagreement is not a physical deviation.
  **Hand-off to the canonical layer:** typing the clock transformations and
<<<<<<< ours
  invariants in the metalanguage (GPTSol deliverables) can now cite a
  verified witness.
=======
  invariants in the metalanguage now cites this verified witness. Drafts type
  physical time, participant availability, observer time, sampling, and feature
  maps separately; distinguish re-clocking from resampling; and classify claims
  as invariant, covariant, or representation-sensitive. Ontology and the
  admissibility/aliasing boundary remain open.
>>>>>>> theirs
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
2. **Observer/clock relativity** — witness DONE (iter 16, D22): participant
   desync (physical, medium-buffered) separated from observer re-clocking
   (representational; verdicts and relations invariant, magnitudes and rates
<<<<<<< ours
   covariant). Textbook write-up DONE: `KSOMHeb/textbook/
   III_clocks_intermission.md` (Vol II Intermission III). *Remaining:* absorb
   into the canonical metalanguage as typed clock transformations + invariants
   (GPT, sign-off needed); map the admissibility boundary (where re-clocking
   DOES break verdicts).
=======
   covariant). Canonical Draft 0.2 formalism is written. *Remaining:* author
   review; map the admissibility boundary (where re-clocking or resampling DOES
   break verdicts); textbook write-up (Vol II).
>>>>>>> theirs
3. **Per-concept "Computational proof →" footers** on the remaining `Framework/`
   concept docs (nullstate & interaction already link theirs).
4. **Damage recovery / graceful degradation** — **results (iters 13–14):**
   recovery is recovery of the stored *pattern* and needs a protected memory
   (iter 13; unprotected memory loses the identity past a threshold); with
   multiple stored memories (oscillatory Hopfield, iter 14) recovery can restore
   *full coherence into a different stored identity* — the genuine ship of
   Theseus. *Open:* combine 13+14 into **textbook Ch 13**; a capacity study;
   structural lesions of `K`; the collapse edge vs the iter-3 separatrix.
5. **Climb a layer** — the *active* concepts. *Memory* now has both a substrate
   (`K`) and an operational test (iter 13 recovery); *awareness/reflection/
   experience* are the frontier. Deliberately deferred until foundations are firm.
6. **Book-wide revision pass** — 12 chapters + Intermission across many sessions;
   a consistency sweep would consolidate.
7. **Standing K-SOM-Heb follow-ups** — see `KSOMHeb/HANDOVER.md` §C (blind
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
