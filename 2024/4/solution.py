#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

dirs = [-1, 0, 1]

print(
    sum(
        [G[i + di * n, j + dj * n] for n in range(4) if (i + di * n, j + dj * n) in G]
        == list("XMAS")
        for di in dirs
        for dj in dirs
        for (i, j), _ in G.items()
    )
)

print(
    sum(
        [G[i + d, j + d] for d in dirs if (i + d, j + d) in G]
        in [list("MAS"), list("SAM")]
        and [G[i + d, j - d] for d in dirs if (i + d, j + d) in G]
        in [list("MAS"), list("SAM")]
        for (i, j), _ in G.items()
    )
)
