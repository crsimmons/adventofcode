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

(sr, sc) = G.find("S")
(er, ec) = G.find("E")


Q = deque()
Q.append((0, (sr, sc)))
TIMES = {}

while Q:
    t, (r, c) = Q.popleft()
    if (r, c) in TIMES:
        continue
    TIMES[(r, c)] = t
    if (r, c) == (er, ec):
        continue
    for nr, nc in G.adj(r, c):
        if G[nr, nc] != "#":
            Q.append((t + 1, (nr, nc)))

TIMES = list(TIMES.items())

p1 = 0
p2 = 0
for i, (n1, t1) in enumerate(TIMES):
    for n2, t2 in TIMES[i:]:
        d = mdist(n1, n2)
        # time save is time to get to end of cheat by normal path (t2)
        # minus time to get to start of cheat (t1)
        # minus distance traversed through walls (d)
        if t2 - t1 - d >= 100:
            if d == 2:
                p1 += 1
            if d < 21:
                p2 += 1

print(p1)
print(p2)
