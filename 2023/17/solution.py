#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import heapq
import sys

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D, value_fn=int)
R = G.height
C = G.width

def solve(part2):
    Q = [(0,0,0,-1,-1)]
    S = set()

    while Q:
        dist, r, c, direc, straight = heapq.heappop(Q)

        # reached bottom right
        # must be min distance due to priority queue
        if r==R-1 and c==C-1:
            print(dist)
            break

        if (r, c, direc, straight) in S:
            continue

        S.add((r, c, direc, straight))

        for new_direc,(dr,dc) in enumerate([(-1, 0),(0, -1),(1, 0),(0, 1)]):
            nr = r + dr
            nc = c + dc

            # can't go backwards
            if ((new_direc + 2)%4 == direc):
                continue

            new_straight = (1 if new_direc!=direc else straight+1)

            part1_valid = new_straight<=3
            part2_valid = new_straight<=10 and (new_direc==direc or straight>=4 or straight==-1)
            valid = (part2_valid if part2 else part1_valid)

            if 0<=nr<R and 0<=nc<C and valid:
                cost = G[nr,nc]
                heapq.heappush(Q, (dist+cost, nr, nc, new_direc, new_straight))

solve(False)
solve(True)
