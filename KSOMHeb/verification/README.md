# K-SOM-Heb verification suite

Each script checks one claim of the architecture against either known theory or
the architecture's own stated properties. Run any of them directly with
`python3 <script>.py` (needs `numpy`; plots need `matplotlib`).

| Script | What it checks | Status |
|--------|----------------|--------|
| `verify_bugs.py` | Reproduces the four v1.0 bugs (S ≡ 1, per-step spatial blend, invalid entropy, etc.) | the bugs, demonstrated |
| `verify_fixes.py` | Confirms the v1.1 corrected update: coupling adapts, stays bounded, synchrony varies, entropy well-defined | passing |
| `iter1_kuramoto_transition.py` | **Foundation.** Base (fixed-coupling) dynamics reproduce the Kuramoto synchronization transition; empirical Kc matches mean-field theory Kc = 2σ√(2/π) ≈ 1.596σ | passing (Kc_emp ≈ 1.60) |

## Iteration plan

We verify bottom-up — each layer only after the one beneath it holds:

1. **Base synchronization** (done) — order parameter, fixed-coupling Kuramoto
   transition vs theory.
2. **Hebbian coupling, frozen phases** — does `dK/dt = ηSR − λK` move coupling
   toward the equilibrium `K* = ηSR/λ` as the math predicts, bounded by `K_max`?
3. **Full coupled system** — phases + coupling together: does reward-driven
   adaptation raise steady-state `r` relative to fixed coupling?
4. **Emergent-property claims** — the ones the doc still asserts on faith:
   functional modularity `Q`, memory traces in `K`, damage recovery.
