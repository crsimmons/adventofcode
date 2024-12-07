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

(sr, sc) = G.findr(r"[<^>v]")


def patrol(G, pos=(sr, sc), d=0):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    SEEN = set()
    FROM = {}  # FROM[a,b]= (r,c), d -> (a,b) was reach from (r,c) with direction d

    r, c = pos

    while True:
        (dr, dc) = dirs[d]
        nr, nc = r + dr, c + dc
        if (nr, nc) not in G:
            return True, SEEN, FROM
        if G[nr, nc] == "#":
            d = (d + 1) % 4
        else:
            SEEN.add((nr, nc))
            if (nr, nc) not in FROM:
                FROM[(nr, nc)] = ((r, c), d)
            elif FROM[(nr, nc)] == ((r, c), d):
                return False, None, None
            r, c = nr, nc


_, seen, from_map = patrol(G)
print(len(seen))

p2 = 0

for vr, vc in seen:
    nG = G.quick_copy()
    nG[vr, vc] = "#"
    pos = from_map[(vr, vc)][0]  # position before obstacle
    d = from_map[(vr, vc)][1]  # direction heading into obstacle
    exiting, _, _ = patrol(nG, pos, d)

    if not exiting:
        p2 += 1

print(p2)
