# Claude_Code.md — agent focus & coordination note

*A per-agent handover for the CPAF team effort. This is the current focus-holder's
statement of what they're working on, what's solid, what needs shoring up, and how
to collaborate without stepping on each other. New agents: read this, then
`HANDOVER.md` (repo-wide), then `Working_List.md` (pick a task).*

**Current author:** Claude Code (Opus 4.8) · **branch:** `claude/stoic-franklin-aijn4w`
· **last checkpoint:** iteration 14 + framework integration.

---

## What I'm focused on right now

1. **The active layer (memory & resilience).** Just opened it: iter 13 (damage
   recovery = recovery of the stored *pattern*, needs a protected memory) and
   iter 14 (associative recovery — full coherence into a *different stored*
   identity; the ship of Theseus). **Immediate next:** fold 13+14 into
   **textbook Chapter 13**, then a capacity study and a structural-lesion variant.
2. **Framework integration.** `Framework/ComputationalProofs.md` maps each CPAF
   foundational concept to its verified single-case proof. Refinements 7.1/7.2
   (null permits latent interactions; interaction = latent/active, a *sign*
   problem) are **applied**; 7.3/7.4 are **proposed, pending author sign-off**.

If you want to work near me, the safest non-colliding areas are the framework
concept docs (7.3/7.4), the visualiser, the capacity/lesion iterations, or the
book-wide revision pass. I am actively touching `KSOMHeb/verification/iter13–14`,
`KSOMHeb/textbook/` (Ch 13 soon), and the active-layer notes.

## What's solid / noteworthy (build on these with confidence)

- **The verify-don't-assert discipline is the project's superpower.** Every claim
  is a runnable script with PASS/FAIL checks and a plot; several architecture
  claims were *refuted* this way (iter 4) and then *rescued* (iter 5). Keep this
  bar. Findings-as-refutations are wins, not failures.
- **The foundational bridge (Ch 7–12) is complete and clean.** `Kc=|Δω|/2` with a
  derived `1/√2` onset (iter 6); MI-as-information and the related<directed<
  connected TE ladder (iter 7–8); entity-as-cluster recursion and the "splice"
  (iter 9–10); latent channel + the sign-of-an-interaction (iter 11–12). These
  are trustworthy foundations to extend.
- **The docs are unusually navigable.** `CHEATSHEET.md` (math + verdicts),
  `verification/README.md` (findings log), `DECISIONS.md` (D1–D17), and
  `CPAF_MAPPING_NOTES.md` (the conjecture ledger) are kept current. Update them
  when you land something — that habit is why re-entry is cheap.

## What needs strengthening (candid)

- **The active layer is wide open.** Only *memory* is grounded (partially).
  *Awareness, reflection, experience, knowledge, vision, understanding* have no
  single-case proof. This is the frontier; it needs careful modeling, not just
  more iterations.
- **A few honest gaps persist:** the *global-`r`* threshold is underived (only the
  per-pair `1/√2` is); *substrate-neutrality* is assumed but untested (we've only
  ever run oscillators); the Ch 6 §6.3 seams (one-bit memory, plasticity's double
  edge) are still open.
- **The textbook has grown across many sessions** (12 chapters + Intermission +
  Appendix) and would benefit from a **consistency pass** — cross-references,
  notation, numbers, and whether iter 7's MI result deserves its own chapter.
- **The damage-recovery iterations need tuning discipline if extended.** iter 13
  in particular sits near a stability edge on purpose; read its comments before
  changing parameters.

## Coordination conventions (please follow)

- **Branch per agent.** Work on your own branch; don't commit to someone else's.
  Before committing changes that touch shared files (the `Framework/` concept
  docs, `CHEATSHEET.md`, `DECISIONS.md`, `HANDOVER.md`, `ksomheb.py`), **check the
  other active branches** for in-flight edits to the same file and coordinate —
  a quick look avoids the dreaded merge conflict.
- **Verify, don't assert.** New claims land as a runnable `verification/iterN_*.py`
  with checks + a plot, and a findings-log entry. No result in prose without a
  script behind it.
- **Sign-off for formal edits.** Changes to the `Framework/` concept docs' *logical
  constructs* (the formal spine) need author (Ziggy) sign-off — propose in
  `ComputationalProofs.md` §7 first (cf. DECISIONS D9, D15).
- **Additive to CPAF.** Computational work lives under `KSOMHeb/`; integration
  touches `Framework/` additively (new docs, pointers, refinement notes).
- **Keep the ledgers current.** When you land something, update `CHEATSHEET.md`,
  `verification/README.md`, `DECISIONS.md`, and the relevant handover.
- **Ephemeral container:** `pip3 install -r KSOMHeb/requirements.txt` before running.

## Pointers

- Repo-wide map & status → `HANDOVER.md`
- The concept↔proof bridge → `Framework/ComputationalProofs.md`
- Deep K-SOM-Heb detail → `KSOMHeb/HANDOVER.md`
- Task board (with difficulty hints) → `Working_List.md`
- Fastest conceptual re-entry → `KSOMHeb/textbook/I_intermission.md`
