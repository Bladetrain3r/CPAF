# CPAF interactive companion — the textbook's lab bench

A tabbed suite of interactive labs, one per textbook chapter, each an
interactive version of a **verified experiment** from `../verification/`.
Sliders re-run the experiment; a scrub-able player animates the returned
trajectory (you can rewind through a tipping point); every tab carries a
"what to notice" panel written against its chapter and a provenance footer
naming the witness script and the claim.

## Run it

```
pip3 install -r ../requirements.txt     # numpy (matplotlib not needed here)
python3 serve.py                        # stdlib http server, port 8000
```

Open <http://localhost:8000>. No build step, no JS dependencies, no packages
beyond numpy.

## Current labs

| tab | textbook chapter | verified witness |
|---|---|---|
| Ch 1 · Transition | `textbook/01_phase_oscillators.md` | `verification/iter1_kuramoto_transition.py` |
| Ch 3 · Closed loop | `textbook/03_closing_the_loop.md` | `verification/iter3_closed_loop.py` |
| Ch 7 · Locking | `textbook/07_grounding_the_threshold.md` | `verification/iter6_locking_threshold.py` |

## Trust / provenance

The browser **never integrates the model** — it only renders. All dynamics
run server-side in Python and either call the verified `../ksomheb.py`
directly (ch03) or use a form a verification iteration proved equivalent
(ch01's O(N) mean-field identity for uniform coupling; ch07's exact
two-oscillator reduction from iter 6). `selfcheck.py` re-verifies every such
step plus each lab's headline behaviour:

```
python3 selfcheck.py     # -> ALL PASS
```

This replaces the old architecture (a JS port of `ksomheb.py` guarded by
`parity_check.js`, now archived under `legacy/` — see DECISIONS.md D25):
with the labs importing the reference implementation there is no second copy
of the math to keep in parity, and the suite scales with the evidence ledger
instead of trailing it.

## Layout

```
visualiser/
├── serve.py            stdlib HTTP server + JSON API (manifest, run)
├── selfcheck.py        stepper-equivalence + lab regression checks
├── labs/               one Python module per lab: metadata + run(params)
│   ├── __init__.py     the registry (add new labs here)
│   └── common.py       control specs, payload packing
├── static/             the tabbed shell (index.html, app.js, style.css)
│   └── labs/           one small canvas renderer per lab
└── legacy/             the retired JS visualiser (iter 1–3 demo)
```

## Adding a lab

1. Write `labs/chNN_topic.py`: a `LAB` dict (id, chapter, witness, claim,
   notice bullets, control specs, presets) and a `run(params) -> dict`.
   Ground it in an existing verification iteration; if it needs a stepper
   that is not a direct `ksomheb` call, add a check to `selfcheck.py`.
2. Write `static/labs/chNN.js`: register `window.Renderers.chNN`, build the
   panels from the returned data with the shared `UI` helpers (plot,
   phasors, heatmap, player).
3. Register the module in `labs/__init__.py`. The shell picks up tabs,
   sliders, presets, notice text, and provenance from the manifest.
