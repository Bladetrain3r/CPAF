# K-SOM-Heb — conversation handover / pickup reference

*A snapshot for picking the project back up — whether that's a new session, a
new collaborator, or you after a break. For the deep re-entry, pair this with
`textbook/00_orientation.md` and `DECISIONS.md`.*

## Status at this checkpoint

- **Merged to `master`** at commit `c929c10` (the verification arc through
  iter 5 + textbook Ch 0–6). Everything after is follow-up work on branches.
- The model is **verified through iteration 11**; the textbook runs **Ch 0–12
  + Intermission + Appendix A**; the interactive visualiser is parity-checked
  and working. The Intermission (`textbook/I_intermission.md`) is the
  mid-course synthesis — read it for the fastest conceptual re-entry into the
  bridge arc.
- The **CPAF foundational bridge (Ch 7–12) is now COMPLETE.** It grounds every
  foundational concept: null (poised, not empty), deviation, interaction,
  information (graded: related < directed < connected), entity-as-cluster, and
  — via the splice (iter 10) — *grown* entities with closure as a boundary
  detector. iter 11 built the last span: interaction vs deviation (noun/verb)
  is a *measured dissociation* (TE detects the channel for any `K>0`; MI waits
  for `Kc`; a latent-channel band between).
- **Integration into the main framework has begun.**
  `../Framework/ComputationalProofs.md` is the new spine document: for each of
  CPAF's six foundational concepts it maps the abstract construct → the concrete
  single-case proof (the iteration) → verdict, and proposes **four refinements**
  to the framework (§7): (7.1) the null state permits *latent* interactions —
  relax `nullstate.md`'s `(¬∃d)∧(¬∃int)` to `(¬∃d)`; (7.2) split interaction
  *capacity* (latent channel) from interaction *event* in `interaction.md`;
  (7.3) tag informational claims with a certificate level (related<directed<
  connected) in `information.md`; (7.4) `system.md` emergence is conditional on
  the right learning ingredients (iters 4–5), not automatic. Pointers added from
  `Framework/Overview.md` and the root `README.md`. **These §7 refinements edit
  the core formal concept docs' logical constructs — proposed, pending author
  sign-off (cf. D9).**

## What exists (the map)

```
KSOMHeb/
├── KSOMHeb_Architecture.md   original design doc, corrected + annotated (v1.2)
├── CHEATSHEET.md             all symbols, equations, key relationships, verdicts
├── DECISIONS.md              decision log D1–D11 (the "why did we do that" answer key)
├── CPAF_MAPPING_NOTES.md     CPAF ↔ oscillator correspondence, tensions, next probes
├── HANDOVER.md               this file
├── ksomheb.py                canonical reference implementation
├── requirements.txt          numpy + matplotlib (the container is ephemeral — see below)
├── verification/             iter1–iter11, each a runnable script + plot + README
├── visualiser/               browser demo (ksomheb.js parity-checked vs the .py)
└── textbook/                 00–12 + Intermission + Appendix A, OUTLINE.md
```

**Environment note (ephemeral container):** a fresh session starts with no
Python packages. Before running any iteration: `pip3 install -r
KSOMHeb/requirements.txt` (or `pip3 install numpy matplotlib`).

**Fastest orientation:** `CHEATSHEET.md` (math) + `verification/README.md`
(what's proven) + this file (what's open).

## The story in ten experiments (verdicts)

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
11. **The latent channel** — interaction (TE) and deviation (MI) are separate
    observables: TE detects a coupling channel for any `K>0`, MI waits for `Kc`,
    and the band `0<K<Kc` is a latent channel (TE>0, MI≈0 — a real but silent
    edge). Interaction graded, deviation an onset; TE peaks near Kc then declines
    (redundancy). Null state = poised, not empty. Completes the Ch 7–12 bridge. ✅

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

### C. The CPAF bridge (Ch 8–11) — grounded spans and what's left
Grounded: **deviation** = an edge crossing `Kc = |Δω|/2` (iter 6, onset
coherence `1/√2`); **information** = MI born at that crossing (iter 7),
graded by iter 8 into the ladder *related (MI) < directed (TE) < connected
(conditional TE)* — pairwise TE is fooled by a hidden common cause
(prediction ≠ causation); only conditioning on the observed confounder
certifies an edge, while direction comes free (`TE(2→1) ≈ 0` for a one-way
coupling — the asymmetric-`Kᵢⱼ` readout); **entity** = a locked cluster
coarse-grained to (Θ, ρ), which obeys the pair law with `K_eff = κρ` and is
informationally closed at the macro level (iter 9) — entity-hood is created
by the locking transition; and the **splice** (iter 10): *grown* iter-5
modules pass all entity criteria unadjusted, and closure doubles as a
boundary *detector* (true vs arbitrary boundary on the same trajectory:
0.005 vs 0.284 bits).

**interaction-vs-deviation is now GROUNDED (iter 11)** — the last Ch 8 span is
built; the foundational bridge is complete. **Remaining follow-ups (none
committed):** blind boundary search (closure as an optimization objective —
Ch 11's exercise); entity-hood along the growth trajectory; entities from
unseeded structure; the entity operating envelope (absorption vs fragmentation
— Ch 10's exercise); dissect the entity-to-entity channel; partial
observability of the confounder (noisy `Z̃`); a learning rule that *produces*
asymmetric `K`; the global-`r` threshold; latent-channel *composition* (do
sub-threshold channels compose like locked ones? — Ch 12's exercise narrows
the band via detuning).

### C2. Framework integration (in progress — the current thread)
- **APPLIED (7.1, 7.2):** `nullstate.md` `¬∃int`→`¬∃int_act`; `interaction.md`
  Latent-vs-Active section, grounded by **iter 12** (latent/active = sign of the
  locking discriminant `Disc=1−(Δω/2K)²`; complex vs real `ψ*`). Ziggy's "sign
  problem" conjecture, verified.
- **Still to apply (proposed):** 7.3 certificate levels to `information.md`;
  7.4 conditional emergence to `system.md`. *Sign-off pending — formal constructs.*
- **Add per-concept "Computational proof" footers** to the remaining
  `Framework/*.md` docs (nullstate & interaction already link their proofs).
- **Then** the active layer becomes the next grounding target (see below).

### D. The bigger forks (choose by appetite)
- **Climb a layer.** The foundational bridge is done; CPAF's *basic/active*
  layer (experience, memory, awareness, reflection) is next. Memory is partly
  in hand (K, iters 2–5); the rest are open, higher-risk, and would need fresh
  entity criteria. The natural but ambitious continuation.
- **Book-wide revision pass.** 12 chapters + Intermission across many sessions
  — a consistency sweep (numbers, cross-references between chapters, notation,
  and how iter 7's MI result is split across Ch 8 rather than given its own
  chapter) would consolidate before pushing further. Lower-risk, high-legibility.
- **Untested doc claim: damage recovery / graceful degradation** — never
  simulated; a self-contained iteration.

## How to pick up

1. `pip3 install -r KSOMHeb/requirements.txt` (ephemeral container — packages
   are gone on a fresh session), then `python3
   verification/iter11_interaction_vs_deviation.py` to confirm the env runs
   (~1.5 min, should print ALL PASS).
2. Skim this file + `CHEATSHEET.md` + `CPAF_MAPPING_NOTES.md` + `DECISIONS.md`;
   `textbook/I_intermission.md` for the fastest conceptual re-entry.
3. Choose from the work queue. The foundational bridge is complete, so this is a
   genuine fork — the two cleanest options are **climb a layer** (CPAF's active
   layer: experience/memory/awareness/reflection) or a **book-wide revision
   pass** to consolidate 12 chapters before pushing on. See "Open work queue → D".

## Conversation context (how we got here)

Built bottom-up, verifying each claim before adding the next; chose the Hebbian
path over signed STDP (D1); found and fixed four mechanism-breaking bugs in the
original doc (Appendix A). House style for the textbook: intuition → math → real
code → the iteration result → carry-forward → a short exercise; written for a
reader rusty on dynamics. Iterations 6–8 (and Ch 7–9) were developed on
follow-up branches (`claude/stoic-franklin-aijn4w`, then
`claude/transfer-entropy-mutual-info-8csyw7`). Development is additive to CPAF;
the K-SOM-Heb work lives entirely under `KSOMHeb/`.
