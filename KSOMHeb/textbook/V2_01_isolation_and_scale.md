# Volume II, Chapter 1 — Isolation and scale: the detector

> *Volume II's opening problem: how do you grow past two oscillators without
> losing the mathematics that two oscillators earned? Volume I gave one answer
> — coarse-grain a locked cluster into a single macro-oscillator (Ch 10). This
> chapter gives the complementary one: compose with **one-way edges**, and the
> parts you've verified stay verified. The tool that falls out — a node that
> reads without writing — turns out to be the suite's first embedded observer,
> and its first awareness-shaped witness.*

## 1.1 The problem of scale

Add a third oscillator symmetrically and everything renormalizes: thresholds
shift, the pair law stops applying directly, and you're doing mean-field
theory (Ch 1) instead of reusing proofs. Volume I escaped this once by going
*up* — a locked cluster coarse-grains to one effective oscillator with
`K_eff = κρ`, and the pair law survives one level higher (Ch 10).

The other escape goes *sideways*. If a new node's influence flows strictly
**forward** — it listens but never speaks — then the upstream system's
equations of motion contain no trace of it. Not approximately: literally. The
pair remains a foundation block — *foundational, if not quite atomic* — and
feed-forward graphs of verified blocks inherit every `[AN]` result their
blocks own. **Isolation buys scale.**

## 1.2 The detector, defined

- **[DEF] A detector** is a node with **no natural frequency** (`ω_d = 0` in
  the analysis frame) coupled one-way to a *target*:

  ```
  dθ_d/dt = K_d · sin(target − θ_d) + noise        (read-only)
  ```

  The target may be a single phase (`θ₁` — a *phase*-detector) or a relation
  (`θ₁ − θ₂` — a *relation*-detector). `K_d` is the detector's **bandwidth**.
- In the canonical typing (`METALANGUAGE.md` §§3–4): the observer's feature
  map `O_o` and clock are *maps outside the system*. A detector is the same
  role played by a *device inside* `X_s` — an **embedded observer**. That
  makes properties of observation (bandwidth, lag, back-action) physical,
  measurable quantities rather than analysis choices.

Everything below is `iter17_detector.py`; claim classes marked as always.

## 1.3 Isolation is exact `[CW]`

Simulate the pair alone; simulate pair-plus-detector with the same noise
stream. The pair's trajectories are **bit-identical** (max deviation 0.0),
and its locked offset sits on the analytic value `ψ* = arcsin(Δω/2K)` to four
decimals. Reading is free — by construction, and now by demonstration.

The consequence deserves its own sentence: **any DAG of one-way attachments
preserves every upstream result exactly.** This is Volume II's composition
principle, and it is why the pair can anchor larger structures without its
Volume I mathematics ever being re-derived.

## 1.4 The detector's own law: bandwidth `[AN]`+`[CW]`

Point a phase-detector at a source rotating at `Ω`. The tracking error obeys
a one-way Adler equation:

```
dψ/dt = Ω − K_d · sin ψ        →  locks iff K_d ≥ |Ω|,  lag = arcsin(Ω/K_d)
```

Measured: lock onset brackets `K_d = Ω` (not `Ω/2`!), and the locked lag
matches `arcsin(Ω/K_d)` to three decimals across the sweep. Note the missing
factor of two — the pair locks at `Kc = |Δω|/2` because *both* sides yield;
a detector's source concedes nothing. That completes a small family of
locking laws distinguished by *who is free to move*:

| System | Lock condition | Who yields |
|---|---|---|
| pair (Ch 7) | `K ≥ \|Δω\|/2` | both |
| cluster vs probe (Ch 10) | `κ ≥ \|Δω\|/(2ρ)` | both, one discounted by coherence |
| detector (this chapter) | `K_d ≥ \|Ω\|` | detector only |

And the CPAF reading: **a detector can only follow a world slower than its
own bandwidth.** This is Intermission III's admissibility boundary made
physical — an embedded observer with insufficient `K_d` loses the signal the
way an external observer with insufficient sampling does. Bandwidth *is*
admissibility, worn as dynamics.

## 1.5 The certificate: the purest one-way edge `[CW]`

In a live noisy channel: `MI(src; det) = 2.1` bits — present, as it must be,
because mutual information is symmetric and cannot see direction. Transfer
entropy can: `TE(src→det) = 0.118` bits, `TE(det→src) = +0.003` — the
surrogate floor, a true statistical null. Iteration 8's one-way case was an
asymmetric coupling between peers; the detector is a node *defined* as sink,
so this is the suite's cleanest directed edge.

It also completes the three-node causal motif set, each with its distinct
fingerprint: the **confounder** (`a←Z→b`, iter 8 — conditioning *kills a
spurious* edge), the **mediator** (`a→m→b`, iter 15 — conditioning *kills a
genuine* one), and now the **detector** (`a→d` — nothing to kill: the reverse
direction is null on its own).

## 1.6 Registering a deviation — the awareness-shaped step `[CW]`

Point a *relation*-detector at the pair's phase difference and sweep the pair
through its locking threshold. Two capacities come apart:

- **Following is priced by the peak rate.** A drifting pair's difference
  slips *nonuniformly* (the saddle-node ghost: slow near the bottleneck,
  peak rate `Δω + 2K` on the sweep). A wideband detector (`K_d = 3.0`,
  above the peak) tracks the drifting pair everywhere (`R_follow ≥ 0.99`);
  a narrowband one (`K_d = 0.8 < Δω`) never does. Honesty note, house
  rule: the original conjecture priced following at the *mean* slip rate —
  the run refuted it, and the peak-rate bound is the revision. Report the
  miss.
- **Settling registers the event, bandwidth-robustly.** The detector's *own*
  phase freezes — `R_settle`, a statistic local to the detector, no access
  to the pair required — at `K* = 0.52` and `0.50` for the two bandwidths,
  against the pair's true `Kc = 0.5`.

So the detector's own state answers "has the deviation happened?" without
touching either oscillator. **Measurement of a deviation is a deviation in
the measurer** — CPAF's "distinguishable through effects or measurement"
clause, realized as dynamics.

Scope, said plainly: this is *registration* — a subsystem carrying
information about another subsystem without disturbing it. It is
awareness-**shaped**, and it is the right first ingredient; it is not the
canonical awareness concept (no self-model, no access to its own state, no
use made of what's registered). The claim is `[CW]` for the ingredient, not
for the concept.

## 1.7 The price of touching `[CW]`

Add back-coupling `ε` (the detector now tugs its source) and both isolation
guarantees fail *continuously*: `TE(det→src)` climbs off the floor (0.002 →
0.019 bits) and the pair's locked offset departs from `arcsin(Δω/2K)`
(error 0.001 → 0.141 rad) as `ε` goes 0 → 1. Reader becomes participant on
a dial, with `ε = 0` exactly free.

One subtlety worth keeping: against a **static** source, even `ε > 0` is
inert — the detector sits exactly on target and `sin(0) = 0`. It is a
*moving* world that makes reading costly, because the tracking lag is the
lever arm of back-action (drag `≈ ε·sin(lag) ≈ ε·Ω/K_d`). Observation of
change is what disturbs; observation of stasis is free even for a clumsy
reader.

## 1.8 What to carry forward

- **The composition principle:** one-way edges preserve upstream `[AN]`
  results *exactly* — verified blocks compose feed-forward into structures
  that need no re-derivation. This is Volume II's license to scale.
- **The detector** (`ω_d = 0`, read-only) is an *embedded observer*; its
  bandwidth law `K_d ≥ |Ω|` (no factor 2) and lag `arcsin(Ω/K_d)` are
  derived; bandwidth is Intermission III's admissibility, made physical.
- **The one-way certificate**: MI present, TE forward, reverse a true null —
  and the causal motif set is complete (confounder, mediator, detector).
- **Following ≠ settling**: tracking a changing world is priced by its peak
  rate; *noticing it stopped changing* is bandwidth-robust and detector-local
  — the first awareness-shaped witness, scoped as registration only.
- **Observation costs only when the world moves**, and the cost is
  continuous in `ε` — the observer effect as a threshold-free dial.

Open, in rough order of appetite: a detector pointed at an *entity* (see the
exercise); chains of detectors (a detector of a detector — the first shape
that could carry *reflection*); the `ε` dial refined into a proper
reader→participant boundary (when does the pair's classification, not just
its offset, change?); and detection under noise (bandwidth vs noise floor —
the detector's ROC curve).

---

### Try it yourself

Point detectors at an *entity*. Grow or build a locked cluster (Ch 10), then
attach two phase-detectors: one reading the macro-phase `Θ`, one reading a
single member `θᵢ`. **Predict first**, using macro closure
(`TE(member→Θ|Θ) ≈ 0`, Ch 10): once you know what the `Θ`-detector knows,
how much *extra* does the member-detector's state tell you about the
cluster's future — and what should happen to that number if the cluster is
*unlocked*? Then run it: compute `TE(det_i → cluster | det_Θ)` both ways.
If closure holds, the entity's interface is exactly what a well-placed
detector reads — and a detector aimed *inside* a healthy entity is
redundant. (If you find otherwise for a locked cluster, that's a finding
about closure, and worth more than the exercise.)

---

*Witness: `../verification/iter17_detector.py` (all five checks) · Decision
log: `../DECISIONS.md` D24 · Composition context: Ch 10 (the other route to
scale), Intermission III (bandwidth as admissibility) · Motif set: iter 8
(confounder), iter 15 (mediator) · Spec that predicted this chapter:
`../CPAF_MAPPING_NOTES.md` (detector entry).*
