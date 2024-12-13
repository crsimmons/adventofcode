#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

p1 = 0
p2 = 0

SEEN = set()

for r in range(R):
    for c in range(C):
        if (r, c) in SEEN:
            continue
        Q = deque([(r, c)])
        area = 0
        perimeter = 0
        name = G[r, c]
        SIDES = defaultdict(set)
        while Q:
            (r2, c2) = Q.popleft()
            if (r2, c2) in SEEN:
                continue
            SEEN.add((r2, c2))
            area += 1
            for dr, dc in DIRS:
                nr = r2 + dr
                nc = c2 + dc
                if (nr, nc) in G and G[nr, nc] == name:
                    Q.append((nr, nc))
                else:
                    perimeter += 1
                    # hit a side going from (r2,c2) in direction (dr,dc)
                    SIDES[(dr, dc)].add((r2, c2))

        sides = 0
        for d, boundaries in SIDES.items():
            SEEN_PERIMETER = set()
            for pr, pc in boundaries:
                if (pr, pc) not in SEEN_PERIMETER:
                    sides += 1
                    Q = deque([(pr, pc)])
                    while Q:
                        r2, c2 = Q.popleft()
                        if (r2, c2) in SEEN_PERIMETER:
                            continue
                        SEEN_PERIMETER.add((r2, c2))
                        for dr, dc in perp_dirs(d):
                            nr = r2 + dr
                            nc = c2 + dc
                            if (nr, nc) in boundaries:
                                Q.append((nr, nc))

        p1 += area * perimeter
        p2 += area * sides

print(p1)
print(p2)
