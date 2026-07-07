# K-SOM-Heb — conversation handover / pickup reference

*A snapshot for picking the project back up — whether that's a new session, a
new collaborator, or you after a break. For the deep re-entry, pair this with
`textbook/00_orientation.md` and `DECISIONS.md`.*

## Status at this checkpoint

- **Merged to `master`** at commit `c929c10` (the verification arc through
  iter 5 + textbook Ch 0–6). Everything after is follow-up work on branches.
- The model is **verified through iteration 8**; the textbook runs **Ch 0–9 +
  Appendix A**; the interactive visualiser is parity-checked and working.
- The current arc is the **CPAF basic-layer bridge** (Ch 8–9): deviation,
  information, and now the information *ladder* (related < directed <
  connected) are grounded; entity-as-cluster recursion is the next span.

## What exists (the map)

```
KSOMHeb/
├── KSOMHeb_Architecture.md   original design doc, corrected + annotated (v1.2)
├── CHEATSHEET.md             all symbols, equations, key relationships, verdicts
├── DECISIONS.md              decision log D1–D11 (the "why did we do that" answer key)
├── CPAF_MAPPING_NOTES.md     CPAF ↔ oscillator correspondence, tensions, next probes
├── HANDOVER.md               this file
├── ksomheb.py                canonical reference implementation
├── verification/             iter1–iter8, each a runnable script + plot + README
├── visualiser/               browser demo (ksomheb.js parity-checked vs the .py)
└── textbook/                 00–09 + Appendix A, OUTLINE.md
```

**Fastest orientation:** `CHEATSHEET.md` (math) + `verification/README.md`
(what's proven) + this file (what's open).

## The story in eight experiments (verdicts)

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

### C. The CPAF bridge (Ch 8–9) — grounded spans and the next one
Grounded so far: **deviation** = an edge crossing `Kc = |Δω|/2` (iter 6, onset
coherence `1/√2`); **information** = MI born at that crossing (iter 7);
**information graded** = the ladder *related (MI) < directed (TE) < connected
(conditional TE)* with the honest finding that pairwise TE is fooled by a
hidden common cause — prediction ≠ causation — and only conditioning on the
observed confounder certifies an edge (iter 8, double dissociation). Direction
itself comes free: a one-way coupling reads `TE(2→1) ≈ 0` exactly, giving the
asymmetric-`Kᵢⱼ` extension an operational readout.

**Next span (likely iter 9 / Ch 10): entity-as-cluster.** Coarse-grain a locked
module (iter 5's) into one effective phase/frequency and test whether it
entrains like a single oscillator — the recursion CPAF leans on, still a
promissory note (Ch 8 §8.4). Smaller follow-ups: partial observability of the
confounder (noisy `Z̃` — does the edge-certificate degrade smoothly?); a
learning rule that *produces* asymmetric `K`; the global-`r` threshold.

## How to pick up

1. `python3 verification/iter8_transfer_entropy.py` — confirm the env runs
   (needs numpy + matplotlib; ~20 s, should print ALL PASS).
2. Skim this file + `CHEATSHEET.md` + `CPAF_MAPPING_NOTES.md` + `DECISIONS.md`.
3. Choose from the work queue. Likely next: the entity-as-cluster probe
   (iter 9), which would turn Ch 8's central conjecture into evidence and give
   the textbook a Chapter 10.

## Conversation context (how we got here)

Built bottom-up, verifying each claim before adding the next; chose the Hebbian
path over signed STDP (D1); found and fixed four mechanism-breaking bugs in the
original doc (Appendix A). House style for the textbook: intuition → math → real
code → the iteration result → carry-forward → a short exercise; written for a
reader rusty on dynamics. Iterations 6–8 (and Ch 7–9) were developed on
follow-up branches (`claude/stoic-franklin-aijn4w`, then
`claude/transfer-entropy-mutual-info-8csyw7`). Development is additive to CPAF;
the K-SOM-Heb work lives entirely under `KSOMHeb/`.
