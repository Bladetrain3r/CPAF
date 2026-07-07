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
1. **Synchrony ≠ integration** — `r=1` can be coherent but information-empty.
2. **The `r ≥ 0.7` threshold is borrowed, not derived.** ← see the hot lead below.
3. **One-bit memory vs "connectivity is memory"** — qual claim vs the elaborate machinery.
4. **Plasticity `P` is double-edged** — low `P` = "dead" or "settled"; ambiguous alone.
5. **Substrate-neutrality assumed, not shown** — only abstract oscillators run so far.

### B. Untested claims
- **Damage recovery / graceful degradation** — asserted in the doc, never simulated.

### C. HOT LEAD — a principled threshold from the phase transition (confirmed math)
Origin: the two-oscillator "entangle/disentangle" script (Opus3/GPT3-era,
re-derived here). For **two** oscillators with detuning `Δω = ω₁ − ω₂`, the pair
phase difference obeys `ψ' = Δω − 2K·sin ψ`, which has a stable locked solution
**iff**

```
K ≥ Kc = |Δω| / 2          (a saddle-node bifurcation — the "phase transition")
```

Numerically confirmed (`/tmp/twoosc.py`, to be promoted to `iter6`): for the
script's detuning `|Δω| = 0.1885`, locking switches on exactly at
`Kc = 0.0942`. **And the order parameter at the onset of locking is exactly**

```
R_onset = |cos(ψ*/2)| = 1/√2 ≈ 0.7071      (ψ* = π/2 at the bifurcation)
```

The locked branch always has `R ∈ (1/√2, 1]`; below `1/√2` a pair **cannot**
stay locked. Since our per-pair synchrony `Sᵢⱼ` **is** this `R`, this gives a
*derived* (not hand-picked) threshold: **`Sᵢⱼ > 1/√2 ≈ 0.707` is the condition
for a pair to phase-lock.** It coincides with the architecture's `r ≥ 0.7` line
— strong evidence that 0.7 is not arbitrary at the pairwise level.

**Caveats (keep honest):** this is exact for N=2. The *global* N-oscillator
transition is continuous (2nd-order) with `Kc = 2/(π g(0))` and no special 0.7 —
so `1/√2` justifies a **per-pair** threshold, not automatically a global-`r` one.
Noise smears the sharp bifurcation. Next step: make this `iter6`, then decide
whether the pairwise `1/√2` can/should ground CPAF's noise→deviation boundary and
the consciousness threshold (seam #2).

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
