#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402

import sys
from collections import deque

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

Elevations = grid.FixedGrid.default_fill(C, R, 0)

for r in range(R):
    for c in range(C):
        if G[r, c] == "S":
            Elevations[r, c] = 1
        elif G[r, c] == "E":
            Elevations[r, c] = 26
        else:
            Elevations[r, c] = ord(G[r, c]) - ord("a") + 1


def bfs(part):
    Q = deque()
    for r in range(R):
        for c in range(C):
            if (part == 1 and G[r, c] == "S") or (part == 2 and Elevations[r, c] == 1):
                Q.append((0, (r, c)))

    S = set()
    while Q:
        d, (r, c) = Q.popleft()
        if (r, c) in S:
            continue
        S.add((r, c))
        if G[r, c] == "E":
            return d
        for nr, nc in G.adj(r, c):
            if Elevations[nr, nc] <= Elevations[r, c] + 1:
                Q.append((d + 1, (nr, nc)))


print(bfs(1))
print(bfs(2))
