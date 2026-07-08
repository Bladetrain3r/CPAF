# K-SOM-Heb — conversation handover / pickup reference

*A snapshot for picking the project back up — whether that's a new session, a
new collaborator, or you after a break. For the deep re-entry, pair this with
`textbook/00_orientation.md` and `DECISIONS.md`.*

## Status at this checkpoint

- **Merged to `master`** at commit `c929c10` (the verification arc through
  iter 5 + textbook Ch 0–6). Everything after is follow-up work on branches.
- The model is **verified through iteration 9**; the textbook runs **Ch 0–10 +
  Intermission + Appendix A**; the interactive visualiser is parity-checked
  and working. The Intermission (`textbook/I_intermission.md`) is the
  mid-course synthesis — read it for the fastest conceptual re-entry into the
  bridge arc.
- The current arc is the **CPAF basic-layer bridge** (Ch 8–10): deviation,
  information (graded: related < directed < connected), and the
  entity-as-cluster recursion are all grounded. The bridge's remaining
  conjecture is interaction-vs-deviation (noun/verb); the entity result has
  grown-module and fragmentation-envelope follow-ups.

## What exists (the map)

```
KSOMHeb/
├── KSOMHeb_Architecture.md   original design doc, corrected + annotated (v1.2)
├── CHEATSHEET.md             all symbols, equations, key relationships, verdicts
├── DECISIONS.md              decision log D1–D11 (the "why did we do that" answer key)
├── CPAF_MAPPING_NOTES.md     CPAF ↔ oscillator correspondence, tensions, next probes
├── HANDOVER.md               this file
├── ksomheb.py                canonical reference implementation
├── verification/             iter1–iter9, each a runnable script + plot + README
├── visualiser/               browser demo (ksomheb.js parity-checked vs the .py)
└── textbook/                 00–10 + Appendix A, OUTLINE.md
```

**Fastest orientation:** `CHEATSHEET.md` (math) + `verification/README.md`
(what's proven) + this file (what's open).

## The story in nine experiments (verdicts)

1. **Base synchronization** — reproduces Kuramoto transition (Kc 1.60 vs 1.596). ✅
2. **Hebbian rule** — matches closed form; found saturation bound `R_sat=K_max·λ/η`. ✅
3. **Closed loop** — global reward is bistable (runaway/collapse), stores ~1 bit. ⚠️
4. **Modular memory** — refuted for baseline: coupling homogenizes. ❌
5. **Rescue** — per-pair synchrony-gated reward (+ competition) recovers modules. ✅
6. **Derived threshold** — pair locks at `Kc=|Δω|/2`, onset coherence exactly `1/√2≈0.707`. ✅
7. **Information at the deviation** — MI climbs ~0→2.7 bits across `Kc`; coherence ≠ information. ✅
8. **Interaction vs common cause** — MI graph-blind; TE directional but fooled by hidden
   common drive (prediction ≠ causation); conditional TE certifies the edge (double
   dissociation). Ladder: related < directed < connected. ✅⚠️ (the ⚠️ is the honest
   pairwise-TE limitation, itself a finding)
9. **Entity-as-cluster** — a locked cluster IS one oscillator: shared frequency,
   iter-6 law with `K_eff = κρ` (2.5%), the 1/√2 branch one level up, and macro
   closure (members add ~nothing beyond Θ); an unlocked collection fails everything.
   Entity-hood is created by the locking transition. ✅

## Open work queue

### A. Quant/qual seams (from textbook Ch 6 §6.3) — the revision agenda
1. ~~**Synchrony ≠ integration**~~ **addressed (iter 7):** mutual information
   diverges from `r`; `r` overreads. (Full "integration" still richer than MI.)
2. ~~**The `r ≥ 0.7` threshold is borrowed**~~ **grounded per-pair (iter 6):**
   `1/√2` locking floor. Global-`r` threshold still open.
3. **One-bit memory vs "connectivity is memory"** — qual claim vs the elaborate machinery.
4. **Plasticity `P` is double-edged** — low `P` = "dead" or "settled"; ambiguous alone.
5. **Substrate-neutrality assumed, not shown** — only abstract oscillators run so far.

### B. Untested claims
- **Damage recovery / graceful degradation** — asserted in the doc, never simulated.

### C. The CPAF bridge (Ch 8–10) — grounded spans and what's left
Grounded: **deviation** = an edge crossing `Kc = |Δω|/2` (iter 6, onset
coherence `1/√2`); **information** = MI born at that crossing (iter 7),
graded by iter 8 into the ladder *related (MI) < directed (TE) < connected
(conditional TE)* — pairwise TE is fooled by a hidden common cause
(prediction ≠ causation); only conditioning on the observed confounder
certifies an edge, while direction comes free (`TE(2→1) ≈ 0` for a one-way
coupling — the asymmetric-`Kᵢⱼ` readout); and **entity** = a locked cluster
coarse-grained to (Θ, ρ), which obeys the pair law with `K_eff = κρ` and is
informationally closed at the macro level (iter 9) — entity-hood is created
by the locking transition.

**Remaining spans / follow-ups:** interaction-vs-deviation (noun/verb — the
last unbuilt Ch 8 span); re-run the iter-9 entity checks on a *grown* iter-5
module (splices the two threads); the entity operating envelope (absorption
vs fragmentation under strong drive — Ch 10's exercise); partial
observability of the confounder (noisy `Z̃`); a learning rule that *produces*
asymmetric `K`; the global-`r` threshold.

## How to pick up

1. `python3 verification/iter9_entity_as_cluster.py` — confirm the env runs
   (needs numpy + matplotlib; ~1 min, should print ALL PASS).
2. Skim this file + `CHEATSHEET.md` + `CPAF_MAPPING_NOTES.md` + `DECISIONS.md`.
3. Choose from the work queue. Committed next: **the splice** — grow modules
   with iter-5's machinery, run iter-9's entity criteria on them unadjusted
   (predict each grown module's `κc` from its measured ρ). See the
   Intermission §I.5 for the framing.

## Conversation context (how we got here)

Built bottom-up, verifying each claim before adding the next; chose the Hebbian
path over signed STDP (D1); found and fixed four mechanism-breaking bugs in the
original doc (Appendix A). House style for the textbook: intuition → math → real
code → the iteration result → carry-forward → a short exercise; written for a
reader rusty on dynamics. Iterations 6–8 (and Ch 7–9) were developed on
follow-up branches (`claude/stoic-franklin-aijn4w`, then
`claude/transfer-entropy-mutual-info-8csyw7`). Development is additive to CPAF;
the K-SOM-Heb work lives entirely under `KSOMHeb/`.
