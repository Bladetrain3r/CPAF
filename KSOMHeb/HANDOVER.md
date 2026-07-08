# K-SOM-Heb — conversation handover / pickup reference

*A snapshot for picking the project back up — whether that's a new session, a
new collaborator, or you after a break. For the deep re-entry, pair this with
`textbook/00_orientation.md` and `DECISIONS.md`.*

## Status at this checkpoint

- **Merged to `master`** at commit `c929c10` (the verification arc through
  iter 5 + textbook Ch 0–6). Everything after is follow-up work on branches.
- The model is **verified through iteration 11**; the textbook runs **Ch 0–12
  + Intermission + Appendices A & S**; the interactive visualiser is
  parity-checked and working. The Intermission (`textbook/I_intermission.md`)
  is the mid-course synthesis — read it for the fastest conceptual re-entry
  into the bridge arc; Appendix S (`textbook/S_sources_and_inheritances.md`)
  is the credit ledger (what we inherited vs assembled).
- The **CPAF basic-layer bridge** (Ch 8–12) now grounds all of it: deviation,
  information (graded: related < directed < connected), entity-as-cluster,
  *grown* entities (splice, iter 10, closure as boundary detector), and
  interaction-vs-deviation (iter 11 — the noun/verb split, the last unbuilt
  Ch 8 span). **The next big move is substrate #2** (CA / Game of Life) — the
  substrate-neutrality bet, targeted at a structured paper.

## What exists (the map)

```
KSOMHeb/
├── KSOMHeb_Architecture.md   original design doc, corrected + annotated (v1.2)
├── CHEATSHEET.md             all symbols, equations, key relationships, verdicts
├── DECISIONS.md              decision log D1–D11 (the "why did we do that" answer key)
├── CPAF_MAPPING_NOTES.md     CPAF ↔ oscillator correspondence, tensions, next probes
├── HANDOVER.md               this file
├── ksomheb.py                canonical reference implementation
├── verification/             iter1–iter11, each a runnable script + plot + README
├── visualiser/               browser demo (ksomheb.js parity-checked vs the .py)
└── textbook/                 00–12 + Intermission + Appendices A, S, OUTLINE.md
```

**Fastest orientation:** `CHEATSHEET.md` (math) + `verification/README.md`
(what's proven) + this file (what's open).

## The story in eleven experiments (verdicts)

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
10. **The splice** — modules *grown* by iter-5's machinery pass all entity criteria
    unadjusted (thresholds to 2.5% from measured ρ); closure *locates* the boundary
    (true 0.005 vs arbitrary 0.284 bits, same trajectory); first entity-to-entity
    macro TE observed. Learning sculpts the boundaries; locking brings them to
    life; the result obeys the same laws as its parts. ✅
11. **Interaction vs deviation** — directed influence (TE) is significant on a
    channel below Kc where the pair provably drifts and shares no MI: influence
    without a deviation, the noun/verb split evidenced. Two corrections: TE is
    non-monotonic (peaks at onset, declines when locked); the locked-regime null
    carries the iter-8 bias via lag structure (~60× below signal — effect size,
    not z, at large N). ✅ (self-controlled: one-way coupling gives its own nulls)

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

### C. The CPAF bridge (Ch 8–12) — grounded spans and what's left
Grounded: **deviation** = an edge crossing `Kc = |Δω|/2` (iter 6, onset
coherence `1/√2`); **information** = MI born at that crossing (iter 7),
graded by iter 8 into the ladder *related (MI) < directed (TE) < connected
(conditional TE)* — pairwise TE is fooled by a hidden common cause
(prediction ≠ causation); only conditioning on the observed confounder
certifies an edge, while direction comes free (`TE(2→1) ≈ 0` for a one-way
coupling — the asymmetric-`Kᵢⱼ` readout); **entity** = a locked cluster
coarse-grained to (Θ, ρ), which obeys the pair law with `K_eff = κρ` and is
informationally closed at the macro level (iter 9) — entity-hood is created
by the locking transition; the **splice** (iter 10): *grown* iter-5 modules
pass all entity criteria unadjusted, and closure doubles as a boundary
*detector* (0.005 vs 0.284 bits); and **interaction vs deviation** (iter 11):
directed influence flows on a channel below `Kc` where the pair still drifts
— influence without a deviation, the noun/verb split evidenced (with TE's
non-monotonicity and the locked-regime null floor as honest riders). **All
three Ch 8 unbuilt spans are now built.**

**The next big move — substrate #2.** Everything so far is grounded *in
oscillators*; substrate-neutrality is CPAF's central bet and still untested.
The plan: reproduce the basic-layer dictionary (deviation, information,
entity, closure) in **cellular automata / Conway's Game of Life** — discrete
deviations (births), visible entities (gliders, still lifes), closure testable
on patterns — aimed at a structured paper (abstract + conclusion). This is the
program's real falsification test; walk toward it, not around it.

**Smaller follow-ups:** blind boundary search (closure as objective — Ch 11's
exercise); mutual (two-way) interaction vs deviation (Ch 12's exercise);
entity-hood along the growth trajectory; entities from unseeded structure; the
entity operating envelope (Ch 10's exercise); dissect the entity-to-entity
channel; a learning rule that *produces* asymmetric `K`; the global-`r`
threshold; the Ch 6 §6.3 seams (the substrate-neutrality one folds into
substrate #2).

## How to pick up

1. `python3 verification/iter11_interaction_vs_deviation.py` — confirm the env
   runs (needs numpy + matplotlib; ~30 s, should print ALL PASS).
2. Skim this file + `CHEATSHEET.md` + `CPAF_MAPPING_NOTES.md` + `DECISIONS.md`;
   Appendix S for what's inherited vs assembled.
3. Choose from the work queue. The big one: **substrate #2 (CA / Game of
   Life)** — the substrate-neutrality test, targeted at a paper.

## Conversation context (how we got here)

Built bottom-up, verifying each claim before adding the next; chose the Hebbian
path over signed STDP (D1); found and fixed four mechanism-breaking bugs in the
original doc (Appendix A). House style for the textbook: intuition → math → real
code → the iteration result → carry-forward → a short exercise; written for a
reader rusty on dynamics. Iterations 6–8 (and Ch 7–9) were developed on
follow-up branches (`claude/stoic-franklin-aijn4w`, then
`claude/transfer-entropy-mutual-info-8csyw7`). Development is additive to CPAF;
the K-SOM-Heb work lives entirely under `KSOMHeb/`.
