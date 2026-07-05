# K-SOM-Heb: a mini-textbook — plan / outline

**Goal.** A short, self-contained deep-dive that teaches the K-SOM-Heb metric
by *retracing the verification route* that built and stress-tested it. The
spine is pedagogical: each chapter introduces one concept, then earns it with
the runnable experiment (and plot) that proved — or disproved — it. A reader
finishes able to (a) reason about the dynamics, (b) run the sims, and (c) know
which claims are load-bearing versus aspirational.

**Audience.** Someone comfortable with basic calculus and Python but rusty on
dynamical systems — refreshers inline, no assumed fluency. (This is the same
posture we've used all along.)

**Form.** Markdown chapters under `KSOMHeb/textbook/`, each referencing the
matching `verification/iterN_*.py` script and its `.png`. Prose explains the
math; the scripts are the worked examples; the plots are the figures.

**Status.** Plan only. Chapters get written *after* the iteration they cover is
verified, so the textbook never runs ahead of the evidence.

---

## Chapter map

| Ch | Title | Concept taught | Anchored by | Written? |
|----|-------|----------------|-------------|----------|
| 0 | Why measure cognition with oscillators | CPAF context; consciousness-as-continuum; why a *dynamical* metric (r) instead of a checklist | README, architecture doc | ☐ |
| 1 | Phase oscillators and the order parameter | What θ, ω, and r are; the Kuramoto model; synchronization as a phase transition with a critical coupling Kc | `iter1` (Kc≈1.60 vs theory 1.596) | ☐ |
| 2 | Making connections learn | Hebbian coupling as leaky integration; fixed points K*=ηSR/λ; the saturation bound R_sat | `iter2` | ☐ |
| 3 | Closing the loop | Reward from the system's own synchrony; positive feedback; bistability (runaway vs collapse); "stores one bit" | `iter3` | ☐ |
| 4 | Is connectivity really memory? | Modularity Q; why per-node reward cancels; self-entrainment; the homogenization failure | `iter4` | ☐ |
| 5 | What actually makes modules | Coupling competition / synaptic normalization; the biological limiting mechanisms; does modularity recover? | `iter5` (in progress) | ☐ |
| 6 | Using K-SOM-Heb as a CPAF metric | Which metrics are sound (r, plasticity P), which need care (H(K)), which are refuted as-specified (Q); operating envelope (R_sat, bistability) | synthesis | ☐ |
| A | Appendix: bugs we caught | The v1.0 errors (S≡1, per-step blend, invalid entropy) as cautionary tales in reading math against code | `verify_bugs.py`, doc v1.1 changelog | ☐ |

## Cross-cutting threads to keep visible

1. **Code must match math.** Every chapter shows the equation *and* the lines
   that implement it, and how we checked they agree (closed form, known theory,
   or ablation).
2. **The synchrony term `S_ij` is the protagonist.** It is the credit-assignment
   mechanism; the v1.0 bug that flattened it (Ch A) and the modularity it
   drives (Ch 4–5) are the same thread.
3. **Claims are graded, not asserted.** Confirmed (Ch 1–3), refuted-as-specified
   (Ch 4), rescued-with-an-added-ingredient (Ch 5). CPAF inherits the graded
   verdicts, not the doc's optimism.

## Open questions to resolve before/while writing

- How much CPAF framing belongs in Ch 0 vs the main CPAF docs (avoid
  duplication)?
- Ch 6 depends on how many metrics survive iterations 5–6; write it last.
- Decide whether damage-recovery / graceful-degradation (another unverified doc
  claim) gets its own iteration+chapter or a short section in Ch 6.
