# CPAF Canonical Metalanguage

**Status:** Draft 0.1  
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

## 4. Time and state

```text
t ∈ 𝕋
x_t ∈ X_s
x_[t0,t1] ≔ trajectory segment over a window
```

For stochastic systems, `x_t` may be replaced or supplemented by a
distribution `μ_t ∈ 𝒫(X_s)`.

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

## 12. Deferred observer-relativity decision

For now:

- every operational result states its observation map or accessible variables;
- canonical definitions do not claim that changing representation always
  changes the underlying property;
- invariance across a class of representations is treated as a proposition to
  prove, not assumed;
- a later decision may distinguish ontic, epistemic, and operational versions
  of each concept.
