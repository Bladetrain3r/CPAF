# Working_List.md — suggested tasks for the CPAF team

*A menu of pickup-able tasks for agents joining the effort. Grab one, branch, and
go — but first skim `Claude_Code.md` (conventions) and `HANDOVER.md` (status).
Update this file when you claim or finish something.*

## How to read the difficulty hint

The **Difficulty** column is a *suggestion only* — a hint about what capability a
task demands, so a model can decide whether it's a good fit. It is not a barrier;
if you think you can do a 🔴, try it.

| Tier | Means | What it asks of you |
|------|-------|---------------------|
| 🟢 **Light** | Well-scoped, follows an established pattern | Low context; mechanical care. Any capable model. |
| 🟡 **Moderate** | Needs modeling judgment, tuning, or multi-file work | A clear target exists but you must design/tune it. A strong model. |
| 🔴 **Deep** | Open-ended design, heavy math/verification, broad care | High context, novel modeling, easy to get subtly wrong. Best for the strongest models. |

**Effort** is a rough wall-clock/token sense (S/M/L). **Deps/notes** flags sign-off
needs, dependencies, or collision risk on shared files.

## Claiming a task

Add your branch name in the **Claimed by** column (edit this file on your branch,
or leave a note). Check for an existing claim before starting; if two agents want
the same task, the branch-per-agent + check-first convention applies.

---

## Tasks

| # | Task | Area / files | Difficulty | Effort | Deps / notes | Claimed by |
|---|------|--------------|:---:|:---:|--------------|-----------|
| 1 | **Volume II Ch 2 — damage recovery** — write up iters 13 (pattern recovery, protected memory) + 14 (associative, wrong-memory) as the *identity-deviation / recovery-fidelity* chapter, in the canonical metalanguage. House style: intuition→math→code→result→carry-forward→exercise | `KSOMHeb/textbook/` (Vol II), `OUTLINE.md` | 🟡 | M | iter 13–14 done; Vol II Ch 1 is now "Isolation and scale" (iter 17), so this becomes Ch 2 | — |
| 1b | ~~**Apply Ch 13's four Volume I revisions**~~ **DONE** — (i) null≠max-entropy fixed in Ch 0/8 (aligned with canonical `null_state` 0.3); (ii) `Kc`/`1/√2` typed `[AN]`@pair in Ch 8; (iii) global-`r` kept `[CONJ]` in Ch 6; (iv) iter 4 labeled a classification result in Ch 4. Ch 0/6/8 also brought current through iter 16 | `KSOMHeb/textbook/00,04,06,08,13` | 🟢 | S | done on `claude/cognition-prerequisites-formalization-adymii` | ✅ Claude |
| 2 | **Book-wide revision pass** — consistency sweep across Ch 0–13 + Intermission: cross-refs, notation, numbers; decide if iter 7's MI result needs its own chapter | `KSOMHeb/textbook/**` | 🟡 | L | Breadth, not depth; collision risk on many files — coordinate | — |
| 3 | **Framework refinement 7.3** — add certificate levels (related<directed<connected) to the information concept | `Framework/information.md`, `ComputationalProofs.md` §7.3 | 🟡 | S | **Needs author sign-off** (formal construct); folds into the formal-spine audit | GPT (formal-spine audit) |
| 4 | **Framework refinement 7.4** — make emergence conditional on the right learning ingredients (iters 4–5) | `Framework/system.md`, `ComputationalProofs.md` §7.4 | 🟡 | S | **Needs author sign-off** (formal construct); folds into the formal-spine audit | GPT (formal-spine audit) |
| 5 | **"Computational proof →" footers** — add a one-line proof pointer to each remaining `Framework/` concept doc (nullstate & interaction already have theirs) | `Framework/deviation/information/entity/system.md` | 🟢 | S | Additive, low-risk; mirror the existing footers | — |
| 6 | **Structural lesion recovery** — damage the *coupling* `K` directly (not the phases) and test recovery/collapse; predict the collapse edge = the iter-3 separatrix | `KSOMHeb/verification/` (next free iter number — 15 is stigmergy, 16 is clock relativity) | 🟡 | M | Extends iter 13; ties to iter 3/6 thresholds | — |
| 7 | **Associative capacity study** — how do M (patterns), N, and pattern distance set identity resilience (basin size)? Map the capacity cliff | `KSOMHeb/verification/` (next free iter number) | 🟡 | M | Extends iter 14; classic Hopfield capacity ~0.14·N | — |
| 8 | **Global-`r` threshold** — is there a *derivable* system-level coherence threshold (the many-oscillator analogue of the per-pair `1/√2`)? Or prove there isn't | `KSOMHeb/verification/`, notes | 🔴 | L | Open theory question; the finite-N transition is continuous | — |
| 9 | **Substrate-neutrality** — run the metric (`r`, MI, entities) on *non-oscillator* data (e.g. MLSwarm agent logs or another dynamical system); does the vocabulary transfer? | new substrate adapter + `verification/` | 🔴 | L | The biggest open honesty gap; needs a real second substrate | — |
| 10 | **Active layer: awareness / reflection** — first single-case proofs for concepts above memory (see `Overview.md` math constructs: `A`, `R`, `E`) | `KSOMHeb/verification/`, `CPAF_MAPPING_NOTES.md` | 🔴 | L | The frontier; needs careful modeling, not just an iteration | — |
| 11 | **Blind boundary search** — turn the closure detector (iter 10) into an entity-*discovery* algorithm (closure as an optimization objective) | `KSOMHeb/verification/`, Ch 11 exercise | 🔴 | M | Conceptually rich; iter 10 has the pieces | — |
| 12 | **A learning rule that *produces* asymmetric `K`** — iter 8 grounded directed interactions as a *readout*; can a rule *learn* `Kᵢⱼ≠Kⱼᵢ`? | `ksomheb.py`, `KSOMHeb/verification/` | 🔴 | M | Touches shared `ksomheb.py` — coordinate | — |
| 13 | **Visualiser: damage-recovery lab** — add a Vol II tab that scrambles a locked module's phases and shows pattern fidelity recovering (or not) | `KSOMHeb/visualiser/labs/` | 🟡 | M | Now one Python module + one renderer in the revamped suite (D25 — no JS port needed); ground in iter 13 | — |
| 14 | **Ch 6 §6.3 seams** — one-bit memory vs "connectivity is memory"; plasticity `P`'s double edge (low P = dead or settled?) | `KSOMHeb/verification/`, Ch 6 | 🟡 | M | Two of the remaining quant/qual seams | — |
| 15 | **Entity operating envelope** — absorption vs fragmentation: when does a cluster absorb a newcomer vs split? (Ch 10 exercise) | `KSOMHeb/verification/` | 🟡 | M | Extends iter 9 | — |
| 16 | ~~**Detector / embedded observer (proposed iter 17)**~~ **DONE** — iter 17 ALL PASS (5 checks incl. the ε sweep) + textbook **Vol II Ch 1 "Isolation and scale"**. Honest revision: following priced by *peak* slip rate. Follow-ups spawned: detector-on-entity, detector chains (→ reflection), noise-limited detection | `KSOMHeb/verification/iter17_detector.py`, `textbook/V2_01_isolation_and_scale.md`, D24 | 🟡 | M | done on `claude/cognition-prerequisites-formalization-adymii` | ✅ Claude |

## Team status

- **In progress:** a **formal-spine audit** of the framework (GPT, own branch) —
  tightening definitions, logical constructs, and proofs across `Framework/`,
  `Foundations/`, `General/`. **Coordinate before touching the `Framework/`
  concept docs** — that's the audit's active surface. My side (Claude Code) stays
  on `KSOMHeb/` verification + textbook; workflow is semi-interleaved (GPT works,
  then hands back), not fully concurrent.
- **Heads-up for the audit:** refinements 7.1/7.2 are already **applied** to
  `nullstate.md` and `interaction.md` (latent/active interaction = the sign of the
  locking discriminant); audit against the *current* refined state, and the
  rationale + the still-open 7.3/7.4 proposals are all in `ComputationalProofs.md`
  §7 (tasks 3–4 above fold into the audit).

## Notes

- Tasks 3, 4 change formal logical constructs → **author sign-off** before landing.
- Tasks 2, 12, 13 touch **shared/parity-checked files** → check other branches first.
- Tasks 8, 9, 10 are the **honest frontier** — high value, high risk; expect
  negative or partial results, and report them (a refutation is a result).
- When you finish, update `CHEATSHEET.md`, `verification/README.md`,
  `DECISIONS.md`, the relevant `HANDOVER.md`, and this list.
