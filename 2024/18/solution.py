#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

R = 71
C = 71

if inputfile != "input.txt":
    R = 7
    C = 7

D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.default_fill(C, R, ".")


def solve(grid):
    Q = deque([(0, 0, 0)])
    SEEN = set()

    while Q:
        r, c, p = Q.popleft()
        if (r, c) in SEEN:
            continue
        SEEN.add((r, c))
        if r == R - 1 and c == C - 1:
            return p
        for nr, nc in grid.adj(r, c):
            if grid[nr, nc] == "#":
                continue
            Q.append((nr, nc, p + 1))
    return -1


def check(cursor):
    assert cursor < len(L)
    G = grid.FixedGrid.default_fill(C, R, ".")

    for i in range(cursor):
        c, r = nums(L[i])
        G[r, c] = "#"

    return solve(G)


def search(left, right):
    ans = -1
    while left <= right:
        mid = (left + right) // 2

        if check(mid) == -1:
            right = mid - 1
            # want last element before transition to -1
            ans = right
        else:
            left = mid + 1

    return ans


print(check(1024))

p2 = search(1024, len(L) - 1)
assert p2 != -1
print(L[p2])


# for i, b in enumerate(L):
#     c, r = nums(b)
#     G[r, c] = "#"
#     e = solve(G)

#     if i == 1024:
#         print(e)

#     if e is None:
#         print(f"{c},{r}")
#         break
