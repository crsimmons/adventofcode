#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque
from itertools import combinations

import lib.grid as grid
from lib.cartesian import dist
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

er = []
ec = []

galaxies = G.find_all("#")

for r, row in enumerate(G.rows):
    if all(ch == "." for ch in row):
        er.append(r)

for c, col in enumerate(G.columns):
    if all(ch == "." for ch in col):
        ec.append(c)

pairs = list(combinations(galaxies, 2))

for part2 in [False, True]:
    factor = 10**6 - 1 if part2 else 1
    ans = 0
    for pair in pairs:
        r1 , c1 = pair[0]
        r2 , c2 = pair[1]
        ans += int(dist(*pair))
        for i in er:
            if min(r1, r2) <= i <= max(r1, r2):
                ans += factor
        for i in ec:
            if min(c1, c2) <= i <= max(c1, c2):
                ans += factor

    print(ans)
