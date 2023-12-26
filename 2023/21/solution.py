#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

import lib.grid as grid
import lib.math
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

sr, sc = G.find('S')

def step(part2, coords):
    S = set()
    for (r,c) in coords:
        for nr, nc in G.adj(r, c, ignore_bounds=True):
            if part2:
                if G[nr%R,nc%C] != "#":
                    S.add((nr, nc))
            elif (nr,nc) in G:
                if G[nr,nc] != "#":
                    S.add((nr, nc))

    return S


def run(part2, n):
    points = [(sr, sc)]
    i = 0
    while i < n:
        i += 1

        points = step(part2, points)

    return len(points)


print(run(False, 64))

# original grid is a square
assert R == C
# the starting point is in the middle of the grid
assert sr == sc == R // 2

# It takes sr (R//2) steps to fill out the first grid
# In the input the row and column of the starting point are
# clear of all rocks. After the first grid is filled,
# the next step takes you into additional grids.
# After R steps, these additional grids are filled.
# This pattern can be modelled via a quadratic equation.
# A good explanation of this is https://www.youtube.com/watch?v=yVJ-J5Nkios

# We can derive a quadratic equation using the number of visited points
# after sr, sr + R, and sr + 2R steps. Originally I used wolfram alpha
# but here I'm using some numpy magic.

# looking for f(x) = run(True, x*R + sr) for x in range(3)
points = [(i, run(True, sr + i * R)) for i in range(3)]
# 26501365 = 202300 * R + sr
n = 202300
# Answer is the calculated f(x) when x = 202300
print(lib.math.evaluate_quadratic_equation(points, n))
