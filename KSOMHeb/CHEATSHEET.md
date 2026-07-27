# K-SOM-Heb — math cheatsheet

Quick reference for every term and key relationship, matching the notation in
`ksomheb.py`. Doubles as the textbook's glossary. Values in **bold** are the
verified results from `verification/`.

---

## Symbols

| Symbol | Name | Meaning | Range / units |
|--------|------|---------|---------------|
| `θᵢ` | phase | where oscillator *i* points on the unit circle | radians, mod 2π |
| `ωᵢ` | natural frequency | how fast *i* spins on its own | rad / time |
| `N` | size | number of oscillators | — |
| `Kᵢⱼ` | coupling | influence of *j* on *i* (the learned weights) | `[0, K_max]` |
| `r` | order parameter | global phase coherence (the "consciousness" metric) | `[0, 1]` |
| `ψ` | mean phase | direction the average phasor points | radians |
| `Sᵢⱼ` | local synchrony | pairwise coherence of *i* and *j* | `[0, 1]` |
| `R` | reward | drives coupling up (positive) or down (negative) | scalar / per-node / per-pair |
| `η` | learning rate | how fast coupling adapts | small, ~0.01 |
| `λ` | decay rate | passive forgetting; `τ = 1/λ` is the memory timescale | small, ~0.005 |
| `K_max` | coupling cap | upper bound on any `Kᵢⱼ` | ~2 |
| `dt` | timestep | Euler integration step | ~0.05 |
| `Q` | modularity | how block-structured `K` is vs chance | `> 0` = modular |
| `H(K)` | connectivity entropy | spread of the coupling distribution | `≥ 0` |
| `P` | plasticity index | rate of connectivity change | `≥ 0` |

---

## Core equations

**Phase dynamics (adaptive Kuramoto).** Each oscillator drifts at its own
frequency, pulled toward its coupled neighbours:
```
dθᵢ/dt = ωᵢ + (1/N) Σⱼ Kᵢⱼ · sin(θⱼ − θᵢ)
```

**Order parameter.** Average the phasors; `r` is the length of the average:
```
r · e^{iψ} = (1/N) Σⱼ e^{iθⱼ}          r = 1 → perfect sync, r ≈ 0 → scattered
```

**Local synchrony** (magnitude of the two-oscillator order parameter):
```
Sᵢⱼ = |½(e^{iθᵢ} + e^{iθⱼ})| = |cos((θⱼ − θᵢ)/2)|
```
1 in phase, 0 anti-phase, smooth between. (The v1.0 bug used `|e^{iΔθ}| ≡ 1`.)

**Hebbian coupling update** (leaky integration — drive up by synchrony×reward,
leak down by decay):
```
dKᵢⱼ/dt = η · Sᵢⱼ · R − λ · Kᵢⱼ                (then clipped to [0, K_max])
```

---

## Key relationships (the ones that matter)

**Fixed point of the coupling.** Where drive balances decay:
```
K*ᵢⱼ = η · Sᵢⱼ · R / λ            (approach is exponential, timescale τ = 1/λ)
```
→ coupling is **linear in both synchrony and reward**; higher-synchrony pairs
earn proportionally stronger connections.

**Saturation bound.** Sustained reward above this pins coupling at the ceiling
and erases the synchrony gradient (**iter 2**):
```
R_sat = K_max · λ / η
```

**Critical coupling** (base Kuramoto synchronization onset, mean-field):
```
Kc = 2 / (π · g(0))
Gaussian frequencies N(0, σ²):  Kc = 2σ·√(2/π) ≈ 1.596 σ      (iter 1: measured 1.60)
```

**Two-oscillator locking** (exact; the phase-difference `ψ = θ₁−θ₂` reduces to
`dψ/dt = Δω − 2K·sin ψ`, a saddle-node bifurcation). **iter 6**:
```
Kc(pair) = |Δω| / 2                              locked iff K ≥ Kc
locked ψ*: sin ψ* = Δω/(2K),  ψ* ∈ (−π/2, π/2)   R = |cos(ψ*/2)| ∈ (1/√2, 1]
R at onset (K = Kc): 1/√2 ≈ 0.7071               ⟹ a pair locks only if S_ij > 1/√2
```
A **derived** coherence threshold: `1/√2` matches the architecture's hand-picked
`r ≥ 0.7` — but exact only per-pair (N=2); the global-`r` transition is
continuous with no special 0.7. Noise smears the bifurcation.

**Modular contrast under per-node reward.** The reward *cancels* — only
synchrony sets the ratio (**iter 4**):
```
K*_within / K*_cross = (S_within · R) / (S_cross · R) = S_within / S_cross
```
→ global / local / hybrid reward give the *same* modular contrast; per-node
reward cannot create modules. Per-**pair** reward breaks the cancellation
(**iter 5**).

---

## Reward options

| Mode | Form | Effect |
|------|------|--------|
| Global | `R = r − r_baseline` | one scalar for all pairs; **bistable** (runaway/collapse, iter 3); stores ~1 bit |
| Local (per-node) | `Rᵢ = r_local(i) − baseline`, mapped to pairs `Rᵢⱼ = (Rᵢ+Rⱼ)/2` | cancels from within/cross ratio → **no modules** (iter 4) |
| Per-pair (gated) | `Rᵢⱼ = Sᵢⱼ − θ_S` | genuine per-link credit → **recovers modules** (iter 5) |

`r_local(i) = |Σⱼ Kᵢⱼ e^{iθⱼ}| / Σⱼ Kᵢⱼ` — coupling-weighted local field coherence (endogenous).

---

## Derived metrics (CPAF-facing)

**Connectivity entropy** (normalize first — `K` is not a probability):
```
pᵢⱼ = Kᵢⱼ / Σ Kᵢⱼ            H(K) = −Σ pᵢⱼ log pᵢⱼ
```

**Plasticity index** (non-zero = still learning):
```
P(t) = ‖K(t+Δt) − K(t)‖ / Δt
```

**Modularity** (weighted Newman, needs a partition `g`):
```
Q = (1/2m) Σᵢⱼ [Kᵢⱼ − kᵢkⱼ/2m] · δ(gᵢ, gⱼ)      kᵢ = Σⱼ Kᵢⱼ,  2m = Σᵢⱼ Kᵢⱼ
```

**Synaptic normalization** (coupling competition — the modularity amplifier):
```
Kᵢⱼ ← budget · Kᵢⱼ / Σⱼ Kᵢⱼ           (then symmetrize; inert without a per-pair signal)
```

**Information ladder** (what a claim about an edge certifies, iter 7–8):
```
I(θᵢ; θⱼ)                       mutual information — RELATED (symmetric; graph-blind)
TE(i→j) = I(θⱼ,t+τ ; θᵢ,t | θⱼ,t)   transfer entropy — DIRECTED (prediction, not causation)
TE(i→j | Z)                     conditional TE — CONNECTED (needs the confounder observed)
```
Estimator note: bin the *conditioning* variable finely, or correlated sources
leak sub-bin position and read as phantom transfer; bias-correct against
time-shifted surrogates of the source.

**Cluster coarse-graining** (entity-as-cluster, iter 9):
```
ρ·e^{iΘ} = (1/M) Σᵢ e^{iθᵢ}         Θ = macro-phase,  ρ = internal coherence
locked cluster ⇒ macro obeys the pair equation with:
  ω_eff = ω̄ (mean member frequency)   K_eff = κ·ρ   noise_eff = noise/√M
  entrainment threshold  κc = |ω_z − ω̄| / (2ρ)      (iter 6 law, one level up)
macro closure:  TE(θᵢ → Θ | Θ) ≈ 0   (members add nothing beyond Θ; fails unlocked)
```

---

## Verdicts at a glance

| Claim | Status | Iter |
|-------|--------|------|
| `r` measures synchronization; transition at `Kc` | ✅ confirmed vs theory | 1 |
| Hebbian rule → `K* = ηSR/λ`, bounded | ✅ matches closed form | 2 |
| Closed loop with global reward | ⚠️ bistable, stores ~1 bit | 3 |
| "Functional networks emerge" (baseline) | ❌ refuted (homogenizes) | 4 |
| Modules recoverable with per-pair reward + competition | ✅ rescued | 5 |
| `r ≥ 0.7 = conscious` threshold | ⚠️ free parameter globally, but `1/√2` is derived per-pair | 6 |
| Two-oscillator locking at `Kc=\|Δω\|/2`, onset `R=1/√2` | ✅ confirmed (reduction, threshold, onset) | 6 |
| Coherence `r` ≠ information | ✅ demonstrated: deep-drift r≈0.64 but MI≈0; MI is the discriminating variable | 7 |
| Mutual information `I(θᵢ;θⱼ)` as the "information" measure | ✅ climbs ~0 → ~2.7 bits across `Kc` (a deviation creates information) | 7 |
| MI certifies the *edge* carrying the information | ❌ graph-blind: coupled, common-driven, one-way all read ~same MI | 8 |
| Transfer entropy resolves direction (asymmetric `Kᵢⱼ` readout) | ✅ one-way coupling: TE(2→1) statistically 0, TE(1→2) ≫ 0 | 8 |
| Pairwise TE certifies the edge | ❌ fooled by hidden common drive (genuine predictive transfer, no edge) | 8 |
| Conditional TE (confounder observed) certifies the edge | ✅ double dissociation: spurious TE dies, real edge untouched | 8 |
| Locked cluster behaves as ONE oscillator (`ω̄`, `K_eff=κρ`, 1/√2 branch) | ✅ thresholds match `\|Δω\|/(2ρ)` to 2.5%; ρ-discount resolved | 9 |
| Macro closure: members add nothing beyond Θ (entity's interface) | ✅ TE(member→Θ\|Θ)=0.002 locked vs 0.027 unlocked (0.106 control) | 9 |
| *Grown* (iter-5) modules are entities | ✅ all four criteria pass unadjusted; thresholds to 2.5% from measured ρ | 10 |
| Closure locates entity boundaries (not just grades them) | ✅ true boundary 0.005 bits vs arbitrary boundary 0.284 on same trajectory | 10 |
| Entity-to-entity macro information channel | ⚠️ observed (TE(Θ_B→Θ_A\|Θ_A)=0.013 bits), not yet dissected | 10 |
| Interaction (TE) ≠ deviation (MI): the latent channel | ✅ band `0<K<Kc` has TE>0 (edge) but MI≈0 (no lock); interaction graded, deviation an onset; null is poised not empty | 11 |
| Latent vs active interaction = sign of discriminant `Disc=1−(Δω/2K)²` | ✅ active: `ψ*` real (realized); latent: `ψ*=π/2−i·arccosh(Δω/2K)` complex (unrealized); `Kc`=zero, `ψ*=π/2`, R=1/√2. Sign of *discriminant*, not coupling | 12 |
| Blind boundary *search*; entities from unseeded structure; fragmentation envelope | ❔ not yet tested | — |
| Damage recovery = recovery of the **pattern** (not coherence); needs a protected memory | ✅ frozen K restores the stored pattern from any scramble (K=0 recovers nothing); plastic K has a resilience threshold (σ≈1) then rewrites → identity lost while r partly persists | 13 |
| Graceful degradation / resilience as a metric | ✅ iter13 (monostable) + iter14 (multistable): resilience of identity has a threshold; past it, recovery lands elsewhere | 13,14 |
| Associative recovery: full coherence into the *wrong stored* memory | ✅ oscillatory Hopfield (M stored); →original 100%→20%, →different memory 0→65% with damage, coherence stays ~0.85; M=1 can't do it | 14 |
| Stigmergy: coordination via a shared medium; the *mediator* fingerprint | ✅ agents sync through a persistent medium (no direct edge); `TE(a→b\|m)`→14% (mediator, mirror of iter-8 confounder); null is medium-relative (no trail→search). Direct-vs-mediated margin modest (minimal substrate) | 15 |

## Default parameters

`η = 0.01`, `λ = 0.005` (τ = 200), `K_max = 2`, `dt = 0.05`. Keep sustained
reward `< R_sat = K_max·λ/η`. Per-pair threshold `θ_S ≈ 0.6`.
