# Legacy JS visualiser (retired)

The original single-page visualiser for the global-reward closed loop
(iterations 1–3): `ksomheb_visualiser.html` + `ksomheb.js`, a hand port of
`ksomheb.py` kept honest by `parity_check.js` (`node parity_check.js` →
`PARITY OK`). Still works stand-alone by opening the HTML in a browser.

Retired because the port-and-parity architecture scales with the number of
labs, not with the evidence ledger: every new iteration would need a second
JS implementation and its own parity check. The replacement suite one level
up runs the verified Python directly (see `../README.md` and DECISIONS.md
D25). Kept for provenance; the equivalent interactive now lives in the
Ch 3 · Closed loop tab.
