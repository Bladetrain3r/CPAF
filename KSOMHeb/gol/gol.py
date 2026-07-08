"""
Conway's Game of Life -- engine + measurement primitives (substrate #2 seed).

This is the CA counterpart to `../ksomheb.py`: the canonical, checked
implementation that the experiments under `experiments/` build on. The purpose
of the whole `gol/` subfolder is to test whether CPAF's basic-layer dictionary
(deviation, information, interaction, entity, closure), operationalized on
oscillators in the textbook, *reproduces* in a genuinely different substrate --
discrete cells, a deterministic local rule, synchronous time. See
`CONCEPT_MAPPING.md` for the term-by-term mapping and `README.md` for the plan.

Conventions
-----------
grid : (H, W) uint8 array, 1 = alive, 0 = dead.
rule : B3/S23 (Conway). A dead cell with exactly 3 live neighbours is born;
       a live cell with 2 or 3 survives; all else dies.
Neighbourhood: Moore (the 8 surrounding cells).
Boundary: 'bounded' (dead cells beyond the edge -- the default, because entity
       isolation and closure are cleaner without wrap-around) or 'toroidal'.
"""
import numpy as np


# ----------------------------------------------------------------------------
# core dynamics
# ----------------------------------------------------------------------------
def neighbour_count(grid, boundary="bounded"):
    """8-neighbour live-count for every cell (same shape as grid)."""
    g = np.asarray(grid, dtype=np.int64)
    if boundary == "toroidal":
        return sum(np.roll(np.roll(g, di, 0), dj, 1)
                   for di in (-1, 0, 1) for dj in (-1, 0, 1)
                   if not (di == 0 and dj == 0))
    if boundary == "bounded":
        p = np.pad(g, 1)
        return (p[:-2, :-2] + p[:-2, 1:-1] + p[:-2, 2:] +
                p[1:-1, :-2] + p[1:-1, 2:] +
                p[2:, :-2] + p[2:, 1:-1] + p[2:, 2:])
    raise ValueError(f"unknown boundary {boundary!r}")


def step(grid, boundary="bounded"):
    """One synchronous B3/S23 update."""
    g = np.asarray(grid, dtype=np.uint8)
    n = neighbour_count(g, boundary)
    return ((n == 3) | ((g == 1) & (n == 2))).astype(np.uint8)


def evolve(grid, steps, boundary="bounded"):
    """Return the grid after `steps` updates."""
    g = np.asarray(grid, dtype=np.uint8).copy()
    for _ in range(steps):
        g = step(g, boundary)
    return g


def trajectory(grid, steps, boundary="bounded"):
    """List of grids [g0, g1, ..., g_steps] (length steps+1)."""
    g = np.asarray(grid, dtype=np.uint8).copy()
    out = [g.copy()]
    for _ in range(steps):
        g = step(g, boundary)
        out.append(g.copy())
    return out


# ----------------------------------------------------------------------------
# pattern zoo -- entities of different periods and velocities
# (coordinates are (row, col) of live cells, top-left anchored)
# ----------------------------------------------------------------------------
PATTERNS = {
    # still lifes -- period 1, velocity 0 (static boundary)
    "block":    [(0, 0), (0, 1), (1, 0), (1, 1)],
    "beehive":  [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2)],
    "loaf":     [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 3), (3, 2)],
    "boat":     [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)],
    # oscillators -- static position, distinct PERIODS (entity "frequencies")
    "blinker":  [(0, 0), (0, 1), (0, 2)],                       # period 2
    "toad":     [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2)],  # period 2
    "beacon":   [(0, 0), (0, 1), (1, 0), (2, 3), (3, 2), (3, 3)],  # period 2
    "pulsar": [  # period 3
        (0, 2), (0, 3), (0, 4), (0, 8), (0, 9), (0, 10),
        (2, 0), (2, 5), (2, 7), (2, 12),
        (3, 0), (3, 5), (3, 7), (3, 12),
        (4, 0), (4, 5), (4, 7), (4, 12),
        (5, 2), (5, 3), (5, 4), (5, 8), (5, 9), (5, 10),
        (7, 2), (7, 3), (7, 4), (7, 8), (7, 9), (7, 10),
        (8, 0), (8, 5), (8, 7), (8, 12),
        (9, 0), (9, 5), (9, 7), (9, 12),
        (10, 0), (10, 5), (10, 7), (10, 12),
        (12, 2), (12, 3), (12, 4), (12, 8), (12, 9), (12, 10),
    ],
    "pentadecathlon": [  # period 15 -- the classic 3x10 form
        (0, 2), (0, 7),
        (1, 0), (1, 1), (1, 3), (1, 4), (1, 5), (1, 6), (1, 8), (1, 9),
        (2, 2), (2, 7),
    ],
    # spaceships -- periodic AND moving (a MOVING closure boundary)
    "glider":   [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)],       # period 4, (1,1)/p
    "lwss": [  # lightweight spaceship, period 4, moves orthogonally at c/2
        (0, 0), (0, 3), (1, 4), (2, 0), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4),
    ],
    # methuselahs -- small seeds, long chaotic transient before settling
    "r_pentomino": [(0, 1), (0, 2), (1, 0), (1, 1), (2, 1)],
    "acorn": [(0, 1), (1, 3), (2, 0), (2, 1), (2, 4), (2, 5), (2, 6)],
    # an "eater 1" still life -- absorbs a glider and is restored: the
    # maximally ASYMMETRIC interaction (one entity destroyed, one unchanged)
    "eater":    [(0, 0), (0, 1), (1, 0), (1, 2), (2, 2), (3, 2), (3, 3)],
}

# known periods for the classifier's sanity (velocity, period) -- displacement
# per period in (row, col); |disp| > 0 means a spaceship (moving boundary)
KNOWN = {
    "block": (1, (0, 0)), "beehive": (1, (0, 0)), "loaf": (1, (0, 0)),
    "boat": (1, (0, 0)),
    "blinker": (2, (0, 0)), "toad": (2, (0, 0)), "beacon": (2, (0, 0)),
    "pulsar": (3, (0, 0)), "pentadecathlon": (15, (0, 0)),
    "glider": (4, (1, 1)), "lwss": (4, (0, 2)),
}


def make_grid(h, w):
    return np.zeros((h, w), dtype=np.uint8)


def place(grid, pattern, r=0, c=0):
    """Stamp a named or coordinate-list pattern with top-left at (r, c)."""
    cells = PATTERNS[pattern] if isinstance(pattern, str) else pattern
    g = grid  # in place
    for (dr, dc) in cells:
        rr, cc = r + dr, c + dc
        if 0 <= rr < g.shape[0] and 0 <= cc < g.shape[1]:
            g[rr, cc] = 1
    return g


# ----------------------------------------------------------------------------
# measurement -- entities, boundaries, periods, velocities
# ----------------------------------------------------------------------------
def population(grid):
    return int(np.asarray(grid).sum())


def bounding_box(cells):
    """(rmin, cmin, rmax, cmax) of an iterable of (r, c). None if empty."""
    cells = list(cells)
    if not cells:
        return None
    rs = [r for r, _ in cells]; cs = [c for _, c in cells]
    return (min(rs), min(cs), max(rs), max(cs))


def _normalize(cells):
    """Translation-invariant signature: cells shifted so the bbox top-left is
    (0,0), returned as a frozenset -- so two patterns compare equal iff they
    are the same shape regardless of position."""
    bb = bounding_box(cells)
    if bb is None:
        return frozenset()
    r0, c0 = bb[0], bb[1]
    return frozenset((r - r0, c - c0) for (r, c) in cells)


def connected_components(grid):
    """Label Moore-connected live regions -- the CANDIDATE entities. Returns a
    list of components, each a list of (r, c). Two live cells are in the same
    component if they touch (including diagonally), i.e. if one sits in the
    other's interaction neighbourhood."""
    g = np.asarray(grid)
    seen = np.zeros_like(g, dtype=bool)
    comps = []
    live = list(zip(*np.where(g == 1)))
    live_set = set(live)
    for start in live:
        if seen[start]:
            continue
        stack = [start]; seen[start] = True; comp = []
        while stack:
            r, c = stack.pop(); comp.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nb = (r + dr, c + dc)
                    if nb in live_set and not seen[nb]:
                        seen[nb] = True; stack.append(nb)
        comps.append(comp)
    return comps


def classify(cells, boundary="bounded", max_period=40):
    """Isolate a pattern (its cells only, on a generous empty grid) and evolve
    it to detect (period, displacement). This is the operational test of an
    ENTITY: a bounded pattern whose ISOLATED future recurs -- period P, moved
    by `disp` per period. Returns a dict:
        kind      : 'still-life' | 'oscillator' | 'spaceship' | 'unstable'
        period    : P (1 = still) or None if it doesn't recur within max_period
        disp      : (dr, dc) per period; nonzero => moving boundary
    Isolation = closure: we test the pattern's future *by itself*, which is
    exactly the claim that a real entity is self-determined (see
    CONCEPT_MAPPING.md, 'closure')."""
    cells = list(cells)
    if not cells:
        return dict(kind="empty", period=None, disp=(0, 0))
    bb = bounding_box(cells)
    h = bb[2] - bb[0] + 1; w = bb[3] - bb[1] + 1
    pad = max_period + 4                      # room for a spaceship to travel
    g = np.zeros((h + 2 * pad, w + 2 * pad), dtype=np.uint8)
    for (r, c) in cells:
        g[r - bb[0] + pad, c - bb[1] + pad] = 1
    sig0 = _normalize(list(zip(*np.where(g == 1))))
    cur = g
    for p in range(1, max_period + 1):
        cur = step(cur, boundary)
        pts = list(zip(*np.where(cur == 1)))
        if not pts:
            return dict(kind="died", period=None, disp=(0, 0))
        if _normalize(pts) == sig0:
            bb1 = bounding_box(pts)
            # displacement of the bbox top-left from its original placement (pad)
            disp = (int(bb1[0] - pad), int(bb1[1] - pad))
            kind = ("still-life" if p == 1 and disp == (0, 0)
                    else "spaceship" if disp != (0, 0)
                    else "oscillator")
            return dict(kind=kind, period=p, disp=disp)
    return dict(kind="unstable", period=None, disp=(0, 0))


def entities(grid, boundary="bounded", max_period=40):
    """Detect and classify every candidate entity on the grid: connected
    components, each classified by isolated evolution. Returns a list of dicts
    with keys: cells, bbox, kind, period, disp. This is the full 'entity
    detector' -- what the visualiser draws boxes around."""
    out = []
    for comp in connected_components(grid):
        info = classify(comp, boundary, max_period)
        info["cells"] = comp
        info["bbox"] = bounding_box(comp)
        out.append(info)
    return out


if __name__ == "__main__":
    # tiny smoke test / demo
    g = make_grid(20, 20)
    place(g, "glider", 2, 2)
    place(g, "blinker", 2, 14)
    place(g, "block", 14, 14)
    print("initial population:", population(g))
    for label, info in [(e["kind"], e) for e in entities(g)]:
        print(f"  entity: kind={info['kind']:11s} period={info['period']} "
              f"disp={info['disp']} bbox={info['bbox']}")
