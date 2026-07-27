# Volume II Intermission — Stigmergy: how less-closed systems work

> *A hop sideways. Volume I's entities were defined by **closure** — a locked
> cluster whose members reach the world only through the macro-phase (iter 9–10).
> Stigmergy is the complement: systems whose coordination, and whose memory, live
> **outside** the agents, in a shared medium. This intermission locates that idea
> in the canonical metalanguage and witnesses it once. No grand claims — a
> definition, a witness, and one genuine contribution to the null-state account.*

## What stigmergy is

Ants don't tell each other where the food is. An ant lays pheromone (it **writes**
a shared medium); later ants sense the pheromone and follow it (they **read** the
medium); their own trail-laying reinforces it. Coordination with no direct
agent-to-agent message — the environment carries the signal, and the environment
*remembers*. Grassé named it *stigmergy* in 1959. Two feedbacks make it work:
trails reinforce trails (**positive**), and pheromone evaporates (**negative**),
so structure forms without running away.

The reason it belongs in CPAF: it is the clean case of a system whose *memory is
external*. Volume I's memory (the coupling `K`, iters 2–5, 13–14) lives *inside*
the system's connectivity. Stigmergic memory lives in a medium the agents merely
visit. Same framework should cover both.

## Stigmergy in the metalanguage

Stigmergy is **not a new primitive** — it's a named *composite motif*: interaction
+ a persistent shared medium + feedback. In the canonical vocabulary
(`../../Framework/CanonicalDefinitions/METALANGUAGE.md`):

- **[DEF] A medium** `m` is a part of the state `X_s` that is (i) *writable* —
  entities' transitions modify it; (ii) *persistent* — it has its own slower
  dynamics, i.e. it **retains** (it is memory); (iii) *readable* — it enters the
  entities' transition rules.
- **[DEF] A stigmergic interaction** `a → b` is one whose influence is **mediated
  by `m`**: the causal path is `a → m → b`, with no direct `a → b` channel.

And it has an **[OP] operational fingerprint**, using the very certificate ladder
Volume I built for iter 8:

> `a → b` is stigmergic via `m` iff there is apparent influence
> (`Directed(a → b)`) that is **screened off by the medium**:
> `Connected(a → b | m) ≈ 0`, while `m` is persistent and agent-written.

This is the mirror of iter 8. There, a hidden `Z` was a **confounder**
(`a ← Z → b`, a common *cause*): conditioning on `Z` killed a *spurious* transfer.
Here `m` is a **mediator** (`a → m → b`, a shared *pathway*): conditioning on `m`
kills a *genuine* transfer, because the medium *is* the road the influence travels.
Same tool (conditional transfer entropy), opposite causal role. That symmetry is
the sign the concept is native to CPAF, not imported.

## The witness (iter 15), honestly

`verification/iter15_stigmergy.py` builds the minimal case: phase-oscillator agents
that couple **only** to a persistent complex medium `M` (deposit + evaporation),
with no direct coupling. Two results hold cleanly and one is partial:

- **[CW] Coordination through the medium.** With a persistent trail (low
  evaporation) the agents synchronize — `r → 1` — through `M` alone. Raise
  evaporation and the trail can't hold; coordination collapses. A genuine
  bifurcation between "on trail" and "off trail."
- **[CW] The screening fingerprint.** Between two agents, `TE(1→2)` is real, but
  conditioning on the medium collapses it to ~14% of its value — the medium is the
  pathway, exactly as the definition predicts.
- **[CW, partial] Direct vs mediated.** Add a genuine direct edge and *more*
  transfer survives conditioning (22% vs 14%). The direction is right, but the
  margin is modest — and the reason is worth stating: in this minimal
  two-oscillator medium, a strong trail's phase tracks the agents' phase so
  closely that conditioning on `M` absorbs much of a direct edge too. A crisp
  mediator/direct **double** dissociation wants a medium clearly distinct from the
  agents — a **spatial pheromone field** — which is the natural follow-up. (A
  partial result, reported as one; that's the house rule.)

## The contribution: a medium-relative null state

Here is the piece worth handing to the formal-spine audit. Strip the pheromone and
an ant does not freeze — it reverts to **search**: a default behaviour it falls
back to when the medium is silent. iter 15 shows exactly this: at high evaporation
the agents decay to their free-drift regime (`r ≈` the uncoupled baseline). So:

> **[PROP] For a stigmergic agent, the null state is medium-relative.** The
> reference regime `N_s` it returns to is *what it does when the medium carries no
> signal* — a default/search regime — and the presence of a trail is a **deviation**
> away from that null, sustained by the medium.

This sharpens the canonical direction that a null state is a *reference regime*,
not maximum entropy (`null_state.md`, GPTSol §2): here the reference regime is
**defined by the absence of the medium's signal**, and it is *dynamic* — a
different, richer null than "no couplings." It also composes with the scale rule:
`Null(agent; λ_micro)` (a single searching ant) sits inside `Dev(colony; λ_macro)`
(a colony actively building a trail).

## Threads it ties together

Stigmergy isn't a detour; it braids four Volume I strands:

| Strand | How stigmergy connects |
|---|---|
| **Modularity** (iter 4–5) | is *stigmergic self-organization*: Hebbian reinforcement = trail-laying (positive feedback); competition/normalization = evaporation (negative feedback). The iter-4 homogenization runaway is a trail with no evaporation. |
| **Certificates** (iter 8) | supply the fingerprint: mediator (`m`) vs confounder (`Z`), separated by conditional TE. |
| **Memory** (iter 13–14) | gets a second *kind*: **external/distributed** memory (the medium) alongside **internal** memory (the coupling `K`). |
| **Entity / closure** (iter 9–10) | poses the boundary question: is the entity the agents, or the agents **plus the medium they maintain** (an extended whole)? Closure is the tool to decide — measure whether *agents+medium* is macro-closed. |

## Where it sits, and what's open

Stigmergy is a **compound construct** in the progression (`PROGRESSION.md`) —
interaction + persistent medium + feedback + externalized memory — not a new
foundational primitive. Two clean follow-ups: (1) a **spatial-field** substrate to
turn the partial mediator/direct result into a crisp double dissociation; (2) the
**extended-entity** closure test — does `agents+medium` pass iter 9's criteria as a
single entity one level up? Both are witnesses waiting to be written.

The takeaway for CPAF: **closure and stigmergy are two ends of one axis.** A closed
entity holds its coordination and memory *inside*; a stigmergic collective holds
them *outside*, in a medium. Most real systems sit between — and the same
metalanguage (mediation certificates, medium-relative nulls, the closure test)
measures where on that axis a system lives.

---

### Try it yourself

Pick a "less-closed" system you know — a market with a price signal, a codebase
with an issue tracker, a city with worn desire-paths. Name its **medium** `m`
(what's written, how it persists, how it's read), and predict the **screening
test**: if you conditioned on `m`, would the apparent agent-to-agent influence
collapse (stigmergic) or survive (direct)? Then name its **medium-relative null** —
what do the agents do when the medium goes silent? If you can fill all three slots,
you've located the system on the closure↔stigmergy axis.

---

*Witness: `../verification/iter15_stigmergy.py` · Metalanguage & certificates:
`../../Framework/CanonicalDefinitions/METALANGUAGE.md`, `13_capstone_metalanguage.md`,
iter 8 · Null-state direction: `../../Framework/CanonicalDefinitions/null_state.md`.*
