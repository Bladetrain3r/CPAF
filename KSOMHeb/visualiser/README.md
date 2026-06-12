# K-SOM-Heb closed-loop visualiser

Interactive view of the global-reward closed loop verified in iterations 1–3.
Drag the sliders and watch the system either run away to full synchrony or
collapse — the bistability from iteration 3, made tactile.

## Run it

Open `ksomheb_visualiser.html` in any browser (double-click, or
`file://…/ksomheb_visualiser.html`). It loads `ksomheb.js` from the same
folder — keep the two files together. No build, no server, no install.

## What you see

- **Phasors** — each oscillator as a dot on the unit circle; the gold arrow is
  the order parameter (its length *is* `r`).
- **Coupling matrix K** — heatmap, dark = 0, bright = K_max.
- **r(t) and mean K(t)** — time series, with the `r_baseline` line marked.
- **Stats + regime label** — live `r`, reward `R`, mean `K`, % of pairs pinned
  at K_max, and whether the run is heading for runaway / collapse / transition.

Sliders cover everything that decides the outcome: η, λ, K_max, r_baseline, N,
σ (frequency spread), initial K₀, dt, and steps-per-frame. The **Supercritical**
/ **Subcritical** buttons jump K₀ across the tipping point so you can flip the
fate directly. Kc(theory) and the R_sat saturation bound are shown live.

## Trust / provenance

The dynamics live in `ksomheb.js`, a direct port of the verified `ksomheb.py`.
`parity_check.js` confirms the JS reproduces the Python reference numbers to
floating-point tolerance:

```
node parity_check.js     # -> PARITY OK
```

This is the single source for the JS math — the HTML does not inline a second
copy. If you change the model in Python, re-port here and re-run the parity
check.

Scope: this visualiser shows the **global-reward** model only (the one verified
so far). Local/hybrid and target-band reward modes are a later iteration.
