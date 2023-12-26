#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")
B = D.split("\n\n")

def solve(part2):
    ans = 0
    for block in B:
        G = grid.FixedGrid.parse(block)
        R = G.height
        C = G.width

        for c in range(C - 1):
            off = 0
            for dc in range(C):
                left = c - dc
                right = c + 1 + dc
                if 0 <= left < right < C:
                    for r in range(R):
                        if G[r,left] != G[r,right]:
                            off += 1
            if off == (1 if part2 else 0):
                ans += c + 1

        for r in range(R - 1):
            off = 0
            for dr in range(R):
                top = r - dr
                bottom = r + 1 + dr
                if 0 <= top < bottom < R:
                    for c in range(C):
                        if G[top,c] != G[bottom,c]:
                            off += 1
            if off == (1 if part2 else 0):
                ans += 100*(r + 1)

    print(ans)

solve(False)
solve(True)
