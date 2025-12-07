#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import deque
from functools import cache

import lib.grid as grid
from lib.util import *

sys.setrecursionlimit(10**6)

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

(sr, sc) = G.find("S")


def bfs():
    Q = deque()
    Q.append((sr + 1, sc))
    ret = 0

    S = set()
    while Q:
        (r, c) = Q.popleft()
        if r == R:
            continue
        if (r, c) in S:
            continue
        S.add((r, c))
        cur = G[r, c]
        if cur == ".":
            Q.append((r + 1, c))
        elif cur == "^":
            Q.append((r + 1, c + 1))
            Q.append((r + 1, c - 1))
            ret += 1

    return ret


@cache
def dfs(r, c):
    if r == R:
        return 1
    cur = G[r, c]
    if cur == ".":
        return dfs(r + 1, c)
    elif cur == "^":
        return dfs(r + 1, c + 1) + dfs(r + 1, c - 1)


print("Part 1:", bfs())
print("Part 2:", dfs(sr + 1, sc))
