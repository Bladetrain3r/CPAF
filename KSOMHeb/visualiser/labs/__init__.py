"""
Lab registry for the CPAF interactive companion.

Each lab module exposes:
    LAB : dict  -- metadata: id, nav/title text, textbook chapter, witness
                   script, claim, notice bullets, renderer path, control
                   specs (sliders/toggles), presets.
    run(params) -> dict  -- run the simulation server-side with the verified
                   code and return everything the browser needs to render.

Adding a lab = one module here + one renderer under static/labs/ + an entry
in _MODULES. Keep labs grounded: every lab names the verification iteration
it descends from, and selfcheck.py must exercise any stepper that is not a
direct call into ksomheb.py.
"""
from . import ch01_kuramoto_transition, ch03_closed_loop, ch07_locking_threshold

_MODULES = [
    ch01_kuramoto_transition,
    ch03_closed_loop,
    ch07_locking_threshold,
]

REGISTRY = {m.LAB["id"]: m for m in _MODULES}


def manifest():
    """The lab list the front-end builds its tabs from."""
    return {"labs": [m.LAB for m in _MODULES]}
