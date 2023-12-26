#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)

def roll(G):
    R = G.height
    C = G.width

    for c in range(C):
        for _ in range(R):
            for r in range(1,R):
                if G[r,c] == 'O' and G[r-1,c]=='.':
                    G[r,c] = '.'
                    G[r-1,c] = 'O'
    return G

def score(G):
    R = G.height
    C = G.width

    ans = 0
    for r in range(R):
        count = 0
        for c in range(C):
            if G[r,c] == 'O':
                count += 1
        ans += count*(R-r)
    return ans

memo = {}
target = 10**9
t = 0
while t < target:
    t += 1
    for rotation in range(4):
        G = roll(G)
        if t == 1 and rotation == 0:
            print(score(G))
        G = G.rotate()

    key = tuple(tuple(row) for row in G.rows)
    if key in memo:
        cycle_length = t - memo[key]
        iterations_remaining = target - t
        cycles_to_end = iterations_remaining // cycle_length
        t += cycles_to_end * cycle_length
    memo[key] = t

print(score(G))
