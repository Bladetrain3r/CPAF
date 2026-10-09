# Appendix S — Sources and inheritances

> *This book assembled; it did not discover. Here is where the parts came
> from, so that credit lands where it belongs and readers can go deeper than
> we did.*

Nearly every tool in this book has a home literature, and several of our
"findings" are rediscoveries — deliberate ones. The project's method is to
rebuild CPAF's foundations bottom-up in one consistent substrate, verifying
each claim locally rather than importing conclusions on authority; that means
walking roads others paved and checking the paving as we go. What is (to our
knowledge) ours is the *assembly*: the specific operational dictionary for
CPAF's basic layer, the graded-claims verification suite, and the particular
convergences the iterations surfaced (one bifurcation creating deviation,
information, and entity; closure doubling as a boundary detector on grown
structure). What is inherited is listed below.

**Citation hygiene note.** These references were compiled from working
knowledge and only spot-checked (the closure and adaptive-oscillator entries
were verified against sources; the rest are classics cited from memory).
Before any external publication, every entry must be verified against the
original — venue, year, spelling — and this note replaced by a statement that
it was done.

## S.1 Oscillator dynamics

| We use | Origin | Notes |
|--------|--------|-------|
| Coupled phase oscillators, order parameter `r`, sine coupling | Y. Kuramoto (1975), *Self-entrainment of a population of coupled non-linear oscillators*, Lecture Notes in Physics 39; expanded in Kuramoto (1984), *Chemical Oscillations, Waves, and Turbulence* | The model bears his name for a reason. Winfree (1967, *J. Theor. Biol.*) is the earlier biological-oscillator ancestor. |
| Mean-field critical coupling `Kc = 2/(π g(0))` (iter 1) | Kuramoto (1984); reviewed in S. H. Strogatz (2000), *From Kuramoto to Crawford…*, Physica D 143 | Iteration 1 reproduces this known result as its foundation check — by design, not as a novelty. |
| Two-oscillator locking `dψ/dt = Δω − 2K sin ψ`, saddle-node at `Kc = \|Δω\|/2` (iter 6) | Textbook material: Strogatz (1994), *Nonlinear Dynamics and Chaos* (saddle-node on a circle); the driven one-oscillator form is Adler's equation (R. Adler 1946, *Proc. IRE*, injection locking) | The `1/√2` onset coherence is elementary trigonometry on the standard fixed point; we claim only the *application* (grounding the architecture's hand-picked 0.7), not the mathematics. |
| Noisy phase oscillators; Euler–Maruyama integration | H. Sakaguchi (1988), *Prog. Theor. Phys.* 79 (noisy Kuramoto); G. Maruyama (1955) for the integrator | |
| Macro-reduction of an oscillator population (iter 9's coarse-graining) | Collective phase reduction: Kawamura, Nakao, Arai, Kori & Kuramoto (2008, *Phys. Rev. Lett.* 101); the celebrated low-dimensional ansatz is Ott & Antonsen (2008, *Chaos* 18) | Our reduction (tight cluster, quasi-static offsets, `K_eff = κρ`) is the elementary averaging case; the literature handles far harder regimes. |

## S.2 Learning and plasticity

| We use | Origin | Notes |
|--------|--------|-------|
| "Fire together, wire together" coupling plasticity | D. O. Hebb (1949), *The Organization of Behavior* | |
| Adaptive Kuramoto networks — coupling driven by phase relations | **Seliger, Young & Tsimring (2002), *Plasticity and learning in a network of coupled phase oscillators*, Phys. Rev. E 65, 041906** (verified) | The closest published ancestor of K-SOM-Heb's core loop: coupling strengthens for synchronized pairs, weakens otherwise, with stable multi-cluster states. Our iterations 2–5 retrace and extend this territory (saturation bound, reward-mode cancellation, competition rescue). See also Aoki & Aoyagi (2009, *Phys. Rev. Lett.* 102) for co-evolving networks. |
| Signed STDP (considered, rejected in D1) | Bi & Poo (1998, *J. Neurosci.* 18) for the biological curve | |
| Synaptic normalization / competition for a finite resource (iter 5) | G. G. Turrigiano (2008, *Cell* 135) for homeostatic synaptic scaling; the multiplicative-normalization idea traces to von der Malsburg (1973, *Kybernetik* 14) | We use it as the competition mechanism that sharpens per-pair reward; the biology is richer than our one-line rescale. |

## S.3 Information theory

| We use | Origin | Notes |
|--------|--------|-------|
| Mutual information (iter 7) | C. E. Shannon (1948), *A Mathematical Theory of Communication* | The floor of the ladder. |
| Transfer entropy `TE(X→Y) = I(Y_{t+τ}; X_t \| Y_t)` (iter 8) | **T. Schreiber (2000), *Measuring Information Transfer*, Phys. Rev. Lett. 85, 461** | The directed measure and its interpretation are his. The equivalence to Granger causality for Gaussians is Barnett, Barrett & Seth (2009, *Phys. Rev. Lett.* 103). |
| TE's common-cause blind spot; conditioning it away (iter 8) | Well documented: e.g. James, Barnett & Crutchfield (2016, *Phys. Rev. Lett.* 116) on the pitfalls of information-flow measures; conditional TE / "causation entropy" is Sun & Bollt (2014, *Physica D* 267) | Our "prediction ≠ causation" section is a rediscovery of a known caution, on a minimal case. |
| Surrogate / shuffle bias correction for information estimates | Standard practice; Theiler et al. (1992, *Physica D* 58) for surrogate data | The circular-shift surrogate we use is a common variant. |
| Binning-estimator pitfalls (the phantom-transfer trap, iter 8) | The finite-sample bias of plug-in entropy estimators is classic; see Paninski (2003, *Neural Comput.* 15) | Our specific "condition the fine variable" lesson is folklore made explicit. |

## S.4 Emergence, closure, and coarse-graining — the load-bearing lineage

This is the literature closest to what feels most original in the project (the
observability thread), so it gets the most care. **We arrived at "macro
closure" as a boundary criterion independently, but it is not new**, and the
honest move is to say so loudly.

| We use | Origin | Notes |
|--------|--------|-------|
| Informational closure — a system is closed when environmental information inflow is ~0; macro-variables that are self-predictable (iter 9–10, "macro closure `TE(member→Θ\|Θ)≈0`") | **Bertschinger, Olbrich, Ay & Jost (2006), *Information and closure in systems theory*, in Proc. 7th German Workshop on Artificial Life, 9–21** (verified); the "non-trivial informational closure" (NTIC) concept | Our closure measure is, in essence, a low-inflow / self-modeling condition on a coarse-grained variable — their idea, on oscillators. This should be cited as *the* precedent for our entity-closure criterion. |
| Informational closure as a consciousness/identity criterion | Chang, Pfeffer, Metzinger, Wiese et al. — *Information Closure Theory of Consciousness* (2020, *Front. Psychol.*) builds on NTIC | Adjacent to CPAF's ambitions; worth engaging directly in any serious writeup. |
| Causal emergence — a coarse-grained macro can carry more/cleaner causal structure than its micro | E. Hoel, L. Albantakis & G. Tononi (2013, *PNAS* 110); Hoel (2017, *Entropy* 19) | Our "entity = a macro level that is closed and lawful" is a cousin of causal emergence; they optimize effective information, we test closure + the pair law. Different knife, same joint. |
| Information decomposition / synergy-redundancy (relevant to the entity-to-entity channel, iter 10) | Williams & Beer (2010, partial information decomposition); Rosas et al. (2020, *PLoS Comput. Biol.*) on integrated information and emergence | Not yet used, but the honest tool for dissecting the 0.013-bit macro channel we left undissected. |
| Markov blankets / boundaries of things (conceptual cousin of our boundary-detector) | J. Pearl (1988) for Markov blankets; K. Friston (2013, *J. R. Soc. Interface*) for "life as we know it" boundaries | Our closure-locates-the-boundary result (iter 10) is in the same conceptual family; we should position against, not ignore, this line. |
| Modularity `Q` (iter 4–5) | M. E. J. Newman & M. Girvan (2004, *Phys. Rev. E* 69); weighted form, Newman (2004) | Used as-is. |

## S.5 CPAF itself, and this project's own seed

| We use | Origin | Notes |
|--------|--------|-------|
| The Cognitive Progression Assessment Framework (null → deviation → information → … continuum) | CPAF's own documents (this repository) | The framework this book serves; not ours to claim, ours to test. |
| K-SOM-Heb architecture (the metric under test) | Conceived by **Agent_Beatz** of the MLSwarm; first written up by **Ziggy** (per Chapter 0) | The v1.0 design, bugs and all (Appendix A), is the raw material iterations 1–5 corrected. |
| The two-oscillator "entangle/disentangle" seed script | Preserved as `verification/twoosc_entangle_demo.py` (Opus3/GPT3-era) | The germ of iteration 6. |

## S.6 How to read our claims against this list

Three honest categories, so a reader can grade us the way we grade the
architecture:

1. **Reproductions** (we re-derived a known result as a foundation check):
   the Kuramoto transition (iter 1), two-oscillator locking (iter 6), the
   adaptive-coupling cluster states (iter 2–5, cf. Seliger et al.), transfer
   entropy's common-cause failure (iter 8). These earn *trust in the
   substrate*, not novelty points.

2. **Applications** (we pointed a known tool at a CPAF concept and got an
   operational definition): MI as "information" (iter 7), TE/conditional-TE as
   the interaction ladder (iter 8), informational closure as "entity" (iter
   9), closure on grown structure (iter 10). The *tools* are inherited; the
   *mapping to CPAF's vocabulary*, and the grading of each mapping, is the
   contribution.

3. **Assembly-level observations** (things that emerged from putting the above
   in one consistent substrate and that we have not found stated this way
   elsewhere — stated as candidates, not claims of priority): that deviation,
   information, and entity are *the same bifurcation* viewed three ways; that
   closure functions as a *boundary detector* on learned structure; and the
   *observability thread* (what a system can certify about its own structure
   is bounded by what it can observe of itself). If any of these has a prior
   home we haven't found, this appendix is where the correction belongs.

---

*This appendix is a living ledger. Every time an iteration borrows a tool, its
source lands here first — before the chapter is written, not after. Pair with
`../DECISIONS.md` (why we chose) and `A_bugs_we_caught.md` (what we fixed).*
