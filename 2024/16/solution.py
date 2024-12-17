#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import heapq
import sys
from collections import defaultdict

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

START = G.find("S")
END = G.find("E")
er, ec = END


def adjs(r, c, d):
    yield 1000, r, c, (d - 1) % 4
    yield 1000, r, c, (d + 1) % 4
    dr, dc = DIRS[d]
    nr, nc = r + dr, c + dc
    if (nr, nc) in G and G[nr, nc] != "#":
        yield 1, nr, nc, d


def solve():
    r, c = START
    Q = [(0, r, c, 0)]
    dists = defaultdict(lambda: float("inf"))
    from_ = defaultdict(lambda: set())
    p1 = None

    while Q:
        score, r, c, direc = heapq.heappop(Q)

        if (r, c) == END:
            if p1 is None:
                p1 = score
                print(p1)

        for s, nr, nc, d in adjs(r, c, direc):
            new_score = score + s
            if new_score < dists[(nr, nc, d)]:
                dists[(nr, nc, d)] = new_score
                heapq.heappush(Q, (new_score, nr, nc, d))
                from_[(nr, nc, d)] = {(r, c, direc)}
            elif new_score == dists[(nr, nc, d)]:
                from_[(nr, nc, d)].add((r, c, direc))

    return dists, from_


dists, from_ = solve()

# find direction best path got to end from
mind = float("inf")
for dr in range(4):
    if dists[(er, ec, dr)] < mind:
        mind = dr

stack = [(er, ec, mind)]
gnodes = set(stack)
while len(stack) > 0:
    some = stack.pop(-1)
    for other in from_[some]:
        if other not in gnodes:
            stack.append(other)
            gnodes.add(other)

# count nodes the same regardless of direction
gnodes = set(x[:2] for x in gnodes)

print(len(gnodes))
