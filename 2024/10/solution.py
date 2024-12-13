#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D, value_fn=int)
R = G.height
C = G.width

starts = G.find_all(0)


def bfs(start, part1=True):
    ans = 0
    Q = deque()
    Q.append(start)

    S = set()
    while Q:
        (r, c) = Q.popleft()
        cur = G[r, c]
        if (r, c) in S and part1:
            continue
        S.add((r, c))
        if cur == 9:
            ans += 1
            continue
        for nr, nc in G.adj(r, c):
            if G[nr, nc] == cur + 1:
                Q.append((nr, nc))

    return ans


p1 = 0
p2 = 0
for start in starts:
    # total number of 9s reachable from start
    p1 += bfs(start)
    # total number of distinct paths from start to all 9s
    p2 += bfs(start, False)

print(p1)
print(p2)
