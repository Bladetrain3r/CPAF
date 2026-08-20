"""Shared helpers for the lab modules: control specs and payload packing."""
import base64

import numpy as np


def slider(cid, label, mn, mx, step, value, unit="", note=""):
    """Spec for one sidebar slider; the front-end builds the control from it."""
    return {"id": cid, "type": "slider", "label": label, "min": mn, "max": mx,
            "step": step, "value": value, "unit": unit, "note": note}


def toggle(cid, label, value=False, note=""):
    """Spec for an on/off checkbox control."""
    return {"id": cid, "type": "toggle", "label": label, "value": value,
            "note": note}


def rounded(a, nd=4):
    """Round an array for the JSON payload (bandwidth, not physics)."""
    return np.round(np.asarray(a, dtype=float), nd).tolist()


def pack_unit_u8(a):
    """Pack an array of values in [0, 1] as base64 uint8 (for K heatmaps).

    Quantization is display-only: stats sent alongside (mean K, %saturated)
    are computed on the full-precision matrices server-side.
    """
    q = np.clip(np.asarray(a, dtype=float) * 255.0, 0, 255).astype(np.uint8)
    return base64.b64encode(q.tobytes()).decode("ascii")


def getp(params, spec, cid):
    """Read one param with the control spec's default (clamped for sliders)."""
    for c in spec:
        if c["id"] == cid:
            if c["type"] == "toggle":
                return bool(params.get(cid, c["value"]))
            v = float(params.get(cid, c["value"]))
            return min(max(v, c["min"]), c["max"])
    raise KeyError(cid)
