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

# 0 up
# 1 down
# 2 left
# 3 right
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start):
    Q = deque()
    S = set()
    E = set()

    Q.append(start)
    while Q:
        d, (r, c) = Q.popleft()
        if (r,c) not in G:
            continue
        if (d, (r, c)) in S:
            continue
        S.add((d, (r, c)))
        E.add((r,c))

        if G[r,c] == "-" and d in [0,1]:
            Q.append((2, (r, c-1)))
            Q.append((3, (r, c+1)))
        elif G[r,c] == "|" and d in [2,3]:
            Q.append((0, (r-1, c)))
            Q.append((1, (r+1, c)))
        elif (G[r,c] == "/" and d == 0) or (G[r,c] == "\\" and d == 1):
            # right
            Q.append((3, (r,c+1)))
        elif (G[r,c] == "/" and d == 1) or (G[r,c] == "\\" and d == 0):
            # left
            Q.append((2, (r,c-1)))
        elif (G[r,c] == "/" and d == 2) or (G[r,c] == "\\" and d == 3):
            # down
            Q.append((1, (r+1,c)))
        elif (G[r,c] == "/" and d == 3) or (G[r,c] == "\\" and d == 2):
            # up
            Q.append((0, (r-1,c)))
        else:
            # straight
            dr,dc = D[d]
            Q.append((d, (r+dr, c+dc)))

    return len(E)

print(bfs((3,(0,0))))

p2 = 0
for r in range(R):
    # left edge
    p2 = max(p2, bfs((3,(r,0))))
    # right edge
    p2 = max(p2, bfs((2,(r,C-1))))
for c in range(C):
    # top edge
    p2 = max(p2, bfs((1,(0,c))))
    # bottom edge
    p2 = max(p2, bfs((0,(R-1,c))))

print(p2)
