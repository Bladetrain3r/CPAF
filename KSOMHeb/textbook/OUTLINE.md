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
| 0 | Orientation: why oscillators, and how this fits CPAF | CPAF context; consciousness-as-continuum; why a *dynamical* metric (r); orientation map + "returning after a break" re-entry guide | README, architecture doc | ✅ `00_orientation.md` |
| 1 | Phase oscillators and the order parameter | What θ, ω, and r are; the Kuramoto model; synchronization as a phase transition with a critical coupling Kc | `iter1` (Kc≈1.60 vs theory 1.596) | ✅ `01_phase_oscillators.md` |
| 2 | Making connections learn | Hebbian coupling as leaky integration; fixed points K*=ηSR/λ; the saturation bound R_sat | `iter2` | ✅ `02_the_learning_rule.md` |
| 3 | Closing the loop | Reward from the system's own synchrony; positive feedback; bistability (runaway vs collapse); "stores one bit" | `iter3` | ✅ `03_closing_the_loop.md` |
| 4 | Is connectivity really memory? | Modularity Q; why per-node reward cancels; self-entrainment; the homogenization failure | `iter4` | ✅ `04_is_connectivity_memory.md` |
| 5 | What actually makes modules | Coupling competition / synaptic normalization; the biological limiting mechanisms; does modularity recover? | `iter5` | ✅ `05_what_makes_modules.md` |
| 6 | Using K-SOM-Heb as a CPAF metric | Which metrics are sound (r, plasticity P), which need care (H(K)), which are refuted as-specified (Q); operating envelope (R_sat, bistability); the quant/qual seams | synthesis | ✅ `06_using_it_as_a_cpaf_metric.md` |
| 7 | Grounding the threshold | Two-oscillator reduction; saddle-node locking at Kc=\|Δω\|/2; the derived coherence onset 1/√2 ≈ 0.707; the N=2-only caveat; first handshake with CPAF's null→deviation | `iter6` | ✅ `07_grounding_the_threshold.md` |
| 8 | The first bridge: oscillators as CPAF primitives | The graph reframing (entity=vertex, interaction=edge); deviation=locking event (grounded, iter6); information=MI born at the crossing (grounded, iter7); null=absence of deviations not interactions; the still-conjectural spans | `iter6`, `iter7` | ✅ `08_bridge_to_cpaf.md` |
| 9 | Interaction vs common cause | Transfer entropy TE(X→Y)=I(Y_{t+τ};X_t\|Y_t): MI blind to the causal graph (confirmed); TE directional (one-way coupling → TE(2→1)=0, grounding asymmetric Kᵢⱼ) but *also* fooled by a hidden common drive (prediction ≠ causation); conditional TE\|Z resolves it as a double dissociation. The ladder: related < directed < connected, priced in observability | `iter8` | ✅ `09_interaction_vs_common_cause.md` |
| A | Appendix: bugs we caught | The v1.0 errors (S≡1, per-step blend, invalid entropy, STDP gaps) as cautionary tales in reading math against code | `verify_bugs.py`, doc v1.1 changelog | ✅ `A_bugs_we_caught.md` |

**Draft through Ch 9 complete.** Live threads: (1) remaining quant/qual seams
(Ch 6 §6.3: one-bit memory, plasticity's double edge, substrate-neutrality);
(2) the CPAF basic-layer mapping (`../CPAF_MAPPING_NOTES.md`) — with
information now graded (MI/TE/conditional TE, iter 7–8), the next grounded
span is the **entity-as-cluster recursion probe** (coarse-grain a locked
module, test whether it entrains as a single effective oscillator → Ch 10
candidate); a learning rule that *produces* asymmetric `Kᵢⱼ` is a further
candidate (Ch 9 gives directed interactions a readout but not an origin).

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
