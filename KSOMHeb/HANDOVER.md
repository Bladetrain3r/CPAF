# K-SOM-Heb — conversation handover / pickup reference

*A snapshot for picking the project back up — whether that's a new session, a
new collaborator, or you after a break. For the deep re-entry, pair this with
`textbook/00_orientation.md` and `DECISIONS.md`.*

## Status at this checkpoint

- **Merged to `master`** at commit `c929c10` (the whole verification arc +
  textbook). This document and anything after it are follow-up work on a fresh
  branch based on that merge.
- The model is **verified through iteration 5**; the textbook **first draft is
  complete** (Ch 0–6 + Appendix A); the interactive visualiser is parity-checked
  and working.

## What exists (the map)

```
KSOMHeb/
├── KSOMHeb_Architecture.md   original design doc, corrected + annotated (v1.2)
├── CHEATSHEET.md             all symbols, equations, key relationships, verdicts
├── DECISIONS.md              decision log D1–D11 (the "why did we do that" answer key)
├── HANDOVER.md               this file
├── ksomheb.py                canonical reference implementation
├── verification/             iter1–iter5, each a runnable script + plot + README
├── visualiser/               browser demo (ksomheb.js parity-checked vs the .py)
└── textbook/                 00–06 + Appendix A (full first draft), OUTLINE.md
```

**Fastest orientation:** `CHEATSHEET.md` (math) + `verification/README.md`
(what's proven) + this file (what's open).

## The story in five experiments (verdicts)

1. **Base synchronization** — reproduces Kuramoto transition (Kc 1.60 vs 1.596). ✅
2. **Hebbian rule** — matches closed form; found saturation bound `R_sat=K_max·λ/η`. ✅
3. **Closed loop** — global reward is bistable (runaway/collapse), stores ~1 bit. ⚠️
4. **Modular memory** — refuted for baseline: coupling homogenizes. ❌
5. **Rescue** — per-pair synchrony-gated reward (+ competition) recovers modules. ✅

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

### C. Derived threshold from the phase transition — DONE (iteration 6, passing)
Origin: the two-oscillator "entangle/disentangle" script (Opus3/GPT3-era,
preserved as `verification/twoosc_entangle_demo.py`). The pair reduces exactly to
`ψ' = Δω − 2K·sin ψ`, a **saddle-node bifurcation** at `Kc = |Δω|/2`, with the
order parameter at onset exactly `1/√2 ≈ 0.7071`. All verified in
`verification/iter6_locking_threshold.py` (reduction vs full sim; `Kc = |Δω|/2`
across detunings; the `1/√2` onset; drift-below/lock-above; noise smearing).

**Result:** a *derived* per-pair coherence threshold — a pair phase-locks only if
`Sᵢⱼ > 1/√2 ≈ 0.707` — matching the architecture's hand-picked `r ≥ 0.7`.
**Caveat:** exact for N=2 only; the global N-oscillator transition is continuous
(`Kc = 2/(π g(0))`, no special 0.7). So `1/√2` grounds a **per-pair** threshold
(e.g. the `θ_S` gate in iter 5), not automatically a global-`r` one.

**Still open (the conceptual follow-up):** whether the pairwise `1/√2` should
anchor CPAF's **noise→deviation** boundary (seam #2), and whether a global-`r`
threshold can be derived at all. Candidate next steps: (i) textbook **Chapter 7**
on grounding the threshold; (ii) an iteration mapping the noise→deviation
transition explicitly (coupling vs frequency-spread-plus-noise).

## How to pick up

1. `python3 verification/iter5_competition_rescue.py` — confirm the env runs.
2. Skim this file + `CHEATSHEET.md` + `DECISIONS.md`.
3. Choose from the work queue. Likely next: promote `/tmp/twoosc.py` → `iter6`
   (the phase-transition threshold), which turns seam #2 from an open question
   into evidence and gives the textbook a Chapter 7.

## Conversation context (how we got here)

Built bottom-up, verifying each claim before adding the next; chose the Hebbian
path over signed STDP (D1); found and fixed four mechanism-breaking bugs in the
original doc (Appendix A). House style for the textbook: intuition → math → real
code → the iteration result → carry-forward → a short exercise; written for a
reader rusty on dynamics. Working branch: `claude/stoic-franklin-aijn4w`
(re-based on `master` after the merge). Development is additive to CPAF; the
K-SOM-Heb work lives entirely under `KSOMHeb/`.
