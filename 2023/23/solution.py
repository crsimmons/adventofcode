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

slopes = {">": 0, "v": 1, "<": 2, "^": 3}

def solve(part1):
    V = set()

    for r in range(R):
        for c in range(C):
            if G[r,c] == "#":
                continue
            valid_branches = 0
            for nr, nc in G.adj(r,c):
                if G[nr,nc] != '#':
                    valid_branches += 1
                if valid_branches>2:
                    V.add((r,c))

    V.add((0,1)) # start
    V.add((R-1,C-2)) # end

    E = defaultdict(list)
    for (rv,cv) in V:
        Q = deque([(rv,cv,0)])
        SEEN = set()

        while Q:
            r, c, d = Q.popleft()

            if (r,c) in SEEN:
                continue
            SEEN.add((r,c))

            if (r,c) in V and (r,c) != (rv,cv):
                E[(rv,cv)].append(((r,c),d))
                continue

            if G[r,c] in slopes and part1:
                dr, dc = DIRS[slopes[G[r,c]]]
                Q.append((r+dr, c+dc, d+1))
                continue

            for nr,nc in G.adj(r,c):
                if G[nr,nc] == "#":
                    continue
                Q.append((nr, nc, d+1))

    ans = 0
    SEEN = [[False for _ in range(C)] for _ in range(R)]
    def dfs(v, d):
        nonlocal ans
        r,c = v

        if SEEN[r][c]:
            return
        SEEN[r][c] = True
        if r==R-1:
            ans = max(ans, d)
        for (e,ed) in E[v]:
            dfs(e, d+ed)
        SEEN[r][c] = False

    dfs((0,1), 0)

    return ans

print(solve(True))
print(solve(False))
