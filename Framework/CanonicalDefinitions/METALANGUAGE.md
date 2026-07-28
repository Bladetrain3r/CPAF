# CPAF Canonical Metalanguage

**Status:** Draft 0.2
**Purpose:** typed vocabulary for canonical definitions  
**Ontology note:** observer relativity is explicitly deferred

## 1. Why a metalanguage is needed

The legacy documents overload the same letters for systems, states, data,
deviations, entities, experience, and functions. They also define system from
entity while defining entity only inside a system.

This metalanguage supplies a minimal analysis scaffold. It does not claim that
every real system has one objectively unique boundary, state space, scale, null
state, or decomposition.

## 2. Claim notation

Use prefixes in drafts when ambiguity is likely:

```text
[PRIM] primitive
[DEF]  definition
[ASM]  assumption
[PROP] derived proposition
[CONJ] conjecture
[OP]   operational criterion
[AN]   analytic result
[CW]   computational witness
[EMP]  empirical result
[EX]   example
```

Use `≔` for definition and `=` for asserted equality.

## 3. Analysis context

[PRIM] An analysis context is:

```text
C ≔ (s, B_s, X_s, T_s, λ, W, O_s, N_s, δ_s, ε)
```

where:

| Term | Type | Role |
|---|---|---|
| `s ∈ 𝒮` | system candidate | object under analysis |
| `B_s` | boundary specification | internal/external distinction |
| `X_s` | state space | possible states |
| `T_s` | transition rule or kernel | deterministic or stochastic evolution |
| `λ` | descriptive scale | component, entity, subsystem, macro-system, etc. |
| `W` | time window | interval over which a claim is evaluated |
| `O_s : X_s → Y_s` | observation/feature map | accessible state description |
| `N_s` | reference regime | baseline subset, orbit, basin, or distribution |
| `δ_s : Y_s × Y_s → ℝ≥0` | difference/divergence | context-appropriate comparison |
| `ε ≥ 0` | criterion | threshold or tolerance |

`O_s` is included because every practical verification uses some state
representation. Including it does not yet decide whether CPAF properties are
fundamentally observer-relative. That question remains Deferred.

For clock-sensitive analysis, extend rather than overload the context:

```text
C_clock ≔ (C, 𝕋_phys, {κ_p}, {A_p}, κ_o, q_o)
```

The added terms are typed in §4. `O_s`/`O_o` selects features; `κ_o` timestamps
physical events; `q_o` selects which physical events are sampled. Keeping these
maps separate prevents a change of feature, clock, or resolution from being
silently classified as a change in the system.

## 4. Physical time, clocks, sampling, and state

```text
t ∈ 𝕋_phys
x : 𝕋_phys → X_s
x_t ≔ x(t)
x_[t0,t1] ≔ trajectory segment over a window
```

For stochastic systems, `x_t` may be replaced or supplemented by a
distribution `μ_t ∈ 𝒫(X_s)`.

The physical time parameter, a participant's clock, an observer's clock, and a
sampling schedule are different types:

```text
κ_p : 𝕋_phys → 𝕋_p       participant-p clock assignment
κ_o : 𝕋_phys → 𝕋_o       observer-o clock assignment
q_o : I_o → 𝕋_phys       observer-o sampling schedule
O_o : X_s → Y_o           observer-o feature map
D_o[k] ≔ (κ_o(q_o(k)), O_o(x(q_o(k))))
                            timestamped record, k ∈ I_o
```

`κ_p` does not by itself say when participant `p` can act. Physical
availability or co-presence requires a schedule such as:

```text
A_p : 𝕋_phys → {0,1}
CoPresent(p,r,t) ≔ A_p(t)=1 ∧ A_r(t)=1
```

Changing `A_p`, delay, or medium persistence changes the physical interaction
conditions. Changing only `κ_o`, `q_o`, or `O_o` changes how a fixed trajectory
is represented or measured.

### 4.1 Clock transformations

[DEF] An observer re-clocking over a window is a map:

```text
h : 𝕋_o → 𝕋_o'
```

that relabels the timestamps of the same physical events. A standard admissible
candidate is an order-preserving bijection that is differentiable where rates
are used and has finite, strictly positive derivative:

```text
0 < m ≤ dh/dτ ≤ M < ∞.
```

Where `κ_o` is invertible on the window, the continuously represented trace and
its re-clocked form are:

```text
z_o(τ) ≔ O_o(x(κ_o⁻¹(τ)))
z_o'(τ') ≔ z_o(h⁻¹(τ')).
```

This is a representational transformation, not a second physical trajectory.
Independent clock changes preserve simultaneous relations only when the event
correspondence through `𝕋_phys` is retained.

Decimation or irregular sampling is not a bijective clock transformation. It
is a change from `q_o` to `q_o'` and must be typed as **resampling**. A
re-clocking or resampling is operationally admissible for a claim only when it
retains the event ordering and resolution required by that claim. Monotonicity
alone cannot prevent aliasing or loss of a medium's bandwidth.

### 4.2 Invariant, covariant, and representation-sensitive claims

Let `D_o` be observations of one physical trajectory and `D_o'` a
representation produced by a declared operation `g` (a re-clocking `h`, a
sampling change `q_o → q_o'`, a feature transformation, or a stated
composition).

```text
g : D_o → D_o'

Invariant(P; g, C) ≔ P(D_o; C) ↔ P(D_o'; C')

Covariant(Q; g, C) ≔ Q(D_o'; C') = 𝒯_g(Q(D_o; C))
```

`P` is an invariant predicate when its verdict is unchanged. `Q` is covariant
when it changes by a declared transformation law `𝒯_g`. A quantity is
**representation-sensitive** over a transformation class when neither claim
has been established.

For `τ'=h(τ)`, an instantaneous rate obeys the candidate covariance law:

```text
dθ/dτ' = (dθ/dτ) / (dh/dτ).
```

Relations evaluated at the same physical event, such as a simultaneous phase
difference, are candidate invariants under a common admissible re-clocking.
Estimator magnitudes, thresholds expressed per sample, and rates must not be
assumed invariant.

These labels apply to a specified transformation class, observation map,
sampling schedule, scale, and window. Invariance under one class does not prove
observer-independent ontology.

## 5. Reference regimes

A reference regime may be represented as:

```text
N_s ⊆ X_s
```

or, when the baseline is statistical:

```text
μ_N ∈ 𝒫(X_s)
```

Examples include a fixed point, equilibrium region, limit cycle, attractor,
metastable basin, frequently recurrent phase, learned operating range, or
externally selected baseline.

Distance to a set may be written:

```text
Δ_N(x_t) ≔ inf_{n ∈ N_s} δ_s(O_s(x_t), O_s(n))
```

A distributional baseline requires a suitable divergence rather than this
set-distance form.

## 6. Deviation types

```text
Δ_N(x_t) ∈ ℝ≥0      deviation magnitude
Dev_s(t; C)          deviation event predicate
Detectable(Dev; C)   distinction available under the context
Observed(Dev; C)     distinction actually registered
```

The default threshold-crossing witness is:

```text
Dev_s(t; C) ≔
    Δ_N(x_t) > ε
    ∧ previously Δ_N(x) ≤ ε within the declared comparison interval.
```

A regime-change, bifurcation, structural lesion, or relational transition may
require a different operational criterion. The criterion must be named.

## 7. Influence and interaction types

For entity or subsystem candidates `a` and `b`:

```text
Ch_s(a → b; C)       channel/capacity for influence
Int_lat(a → b; C)    latent interaction
Int_act(a → b,t; C)  active interaction event
```

Provisional relations:

```text
Int_lat(a → b; C) ≔ Ch_s(a → b; C) ∧ ¬Int_act(a → b; C)

Int_act(a → b,t; C) ≔
    Ch_s(a → b; C)
    ∧ a channel-mediated relevant deviation in b is certified at t.
```

The phrase “relevant deviation” is scale-indexed. Active micro-interactions may
maintain a macro-level null regime.

## 8. Information candidates and certificates

```text
j ∈ 𝓙_s
Processable_s(j; C)
Effect_s(j; C)
```

A provisional modal form is:

```text
Info_s(j; C) ≔
    Processable_s(j; C)
    ∧ there exists an admissible context variation in which j changes
      a system trajectory or state distribution beyond ε_info.
```

This treats information as system-relative and counterfactual without requiring
an effect on every presentation.

Certificate predicates:

```text
Related(a,b; C)
Directed(a → b; C)
Connected(a → b | Z; C)
```

`Z` is the observed conditioning set. Connectedness is certified relative to
the available context, not declared absolutely.

## 9. Entity candidates

```text
e ⊆ s
φ_e : X_e → M_e
```

`φ_e` is a coarse-graining from microstate to macrostate.

Entity-hood will be defined later through a combination of:

- persistence or recoverable identity;
- supported boundary;
- macro-level predictive adequacy;
- interface/closure;
- ability to participate recursively in a higher-level system description.

Entities may be composite. Minimality is optional.

## 10. System descriptions

At the metalanguage level, the system boundary is supplied:

```text
s_C ≔ (B_s, X_s, T_s)
```

A CPAF-qualified organizational description may later add:

```text
s_CPAF ≔ (B_s, X_s, T_s, 𝓔_s, 𝓒_s, Interface_s)
```

This avoids defining system and entity circularly at the primitive level while
still allowing entity boundaries to be discovered inside the candidate system.

## 11. Scale rule

Every claim that can change under coarse-graining should be indexable by `λ`.

Examples:

```text
Null_s(x_t; λ)
Dev_s(t; λ)
Entity_s(e; λ)
Connected(a → b; λ)
```

The canonical documents may omit `λ` in prose where the scale is fixed and
obvious, but formal definitions should retain it.

## 12. Observer-relativity scaffold; ontology deferred

For now:

- every operational result states its physical-time assumptions, observation
  map, clock assignment, sampling schedule, and accessible variables;
- canonical definitions do not claim that changing representation always
  changes the underlying property;
- operational predicates and measurements are tagged invariant, covariant, or
  representation-sensitive relative to a declared transformation class;
- invariance across a class of representations is a proposition to prove, not
  an assumption or a synonym for ontic reality;
- a later decision may distinguish ontic, epistemic, and operational versions
  of each concept.

### K-SOM-Heb witness

[CW] Iteration 16 separates two axes. Participant availability changes the
physical channel: a persistent stigmergic medium buffers non-co-presence while
a co-presence-gated direct edge does not. Observer decimation and a smooth
monotone time-warp re-express one trajectory: within the tested range they
preserve regime and screening verdicts plus the phase-difference distribution,
while TE magnitudes and rates change.

This witness supports the distinction and supplies counterexamples to naive
measurement invariance. It does not establish that every monotone re-clocking
is admissible, that the tested predicates are universally invariant, or that
operational invariance settles the deferred ontology.

## Change log

- **Draft 0.2:** separates physical time, participant and observer clocks,
  availability, feature maps, and sampling; types re-clocking and resampling;
  and introduces transformation-indexed invariant and covariant claims with an
  iteration-16 witness.
- **Draft 0.1:** introduced the analysis context and deferred observer
  relativity.
