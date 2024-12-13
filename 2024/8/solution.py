#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from itertools import combinations

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

antennas = {}

for r in range(R):
    for c in range(C):
        if G[r, c] != ".":
            if G[r, c] in antennas:
                antennas[G[r, c]].append((r, c))
            else:
                antennas[G[r, c]] = [(r, c)]

antinodes1 = set()
antinodes2 = set()


def antinode(pos1, pos2):
    (r1, c1) = pos1
    (r2, c2) = pos2
    nr = r2 + (r2 - r1)
    nc = c2 + (c2 - c1)
    antinodes2.add((r2, c2))
    if (nr, nc) in G:
        antinodes1.add((nr, nc))
    while (nr, nc) in G:
        antinodes2.add((nr, nc))
        nr += r2 - r1
        nc += c2 - c1


for signal, positions in antennas.items():
    for node1, node2 in combinations(positions, 2):
        antinode(node1, node2)
        antinode(node2, node1)

print(len(antinodes1))
print(len(antinodes2))
