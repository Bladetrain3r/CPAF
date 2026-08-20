"""
CPAF interactive companion -- lab server.

Serves the tabbed lab suite (static/) and runs the simulations server-side
with the SAME verified code the evidence ledger uses: every lab imports
`ksomheb.py` (or reproduces a reduction proved equivalent in a verification
iteration -- see selfcheck.py). There is no second implementation of the
model to keep in parity.

Run:
    python3 serve.py [--port 8000]
then open http://localhost:8000

stdlib + numpy only (numpy is already in KSOMHeb/requirements.txt).

API
---
GET  /api/manifest      -> lab registry: titles, chapter links, witness
                           scripts, control specs, presets, notice text.
POST /api/run/<lab_id>  -> body: JSON params -> runs the lab, returns the
                           full trajectory / curves as JSON. The browser
                           only renders; it never integrates the model.
"""
import argparse
import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))          # labs package
sys.path.insert(0, str(HERE.parent))   # verified ksomheb.py

from labs import REGISTRY, manifest    # noqa: E402  (needs sys.path above)

STATIC = HERE / "static"
MIME = {
    ".html": "text/html; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".json": "application/json; charset=utf-8",
}


class NumpyJSON(json.JSONEncoder):
    """Encode numpy scalars/arrays transparently (labs mostly pre-round)."""

    def default(self, o):
        import numpy as np
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        if isinstance(o, np.bool_):
            return bool(o)
        return super().default(o)


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _reply(self, code, body: bytes, ctype: str):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code, obj):
        self._reply(code, json.dumps(obj, cls=NumpyJSON).encode("utf-8"),
                    MIME[".json"])

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/api/manifest":
            return self._json(200, manifest())
        if path in ("/", "/index.html"):
            path = "/static/index.html"
        if path.startswith("/static/"):
            f = (STATIC / path[len("/static/"):]).resolve()
            if STATIC.resolve() in f.parents and f.is_file():
                ctype = MIME.get(f.suffix, "application/octet-stream")
                return self._reply(200, f.read_bytes(), ctype)
        self._json(404, {"error": f"not found: {path}"})

    def do_POST(self):
        path = self.path.split("?", 1)[0]
        if not path.startswith("/api/run/"):
            return self._json(404, {"error": f"not found: {path}"})
        lab_id = path[len("/api/run/"):]
        lab = REGISTRY.get(lab_id)
        if lab is None:
            return self._json(404, {"error": f"unknown lab: {lab_id}"})
        try:
            n = int(self.headers.get("Content-Length", 0))
            params = json.loads(self.rfile.read(n) or b"{}")
        except (ValueError, json.JSONDecodeError) as e:
            return self._json(400, {"error": f"bad request body: {e}"})
        try:
            self._json(200, lab.run(params))
        except Exception as e:  # surface lab errors to the page, keep serving
            self._json(500, {"error": f"{type(e).__name__}: {e}"})

    def log_message(self, fmt, *args):
        print(f"  {self.address_string()} {fmt % args}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"CPAF companion: {len(REGISTRY)} labs on "
          f"http://{args.host}:{args.port}  (Ctrl-C to stop)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")


if __name__ == "__main__":
    main()
