#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque
from functools import lru_cache

import lib.grid as grid
from lib.util import *

sys.setrecursionlimit(10**6)

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

p1 = 0
p2 = 0


def count_around(r, c):
    count = 0
    for nr, nc in G.adj(r, c, diagonals=True):
        if G[nr, nc] == "@":
            count += 1
    return count


i = 0
while True:
    G2 = G.quick_copy()
    count = 0
    for r in range(R):
        for c in range(C):
            if G[r, c] == "@" and count_around(r, c) < 4:
                G2[r, c] = "."
                if i == 0:
                    p1 += 1
                count += 1
    if count == 0:
        break
    G = G2
    p2 += count
    i += 1

print("Part 1:", p1)
print("Part 2:", p2)
