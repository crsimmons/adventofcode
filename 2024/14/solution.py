#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import math
import sys

import lib.grid as grid
from lib.math import crt
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

H = 103
mH = H // 2
W = 101
mW = W // 2

robots = []

for l in L:
    robots.append(nums(l))


def simulate(t):
    return [((sx + vx * t) % W, (sy + vy * t) % H) for sx, sy, vx, vy in robots]


p1 = [0, 0, 0, 0]

for r in simulate(100):
    x, y = r
    if x < mW and y < mH:
        p1[0] += 1
    elif x > mW and y > mH:
        p1[1] += 1
    elif x < mW and y > mH:
        p1[2] += 1
    elif x > mW and y < mH:
        p1[3] += 1


from statistics import variance

xt, xvar, yt, yvar = 0, math.inf, 0, math.inf

for t in range(max(H, W)):
    xs, ys = zip(*simulate(t))
    if variance(xs) < xvar:
        xt, xvar = t, variance(xs)
    if variance(ys) < yvar:
        yt, yvar = t, variance(ys)

p2 = crt([(xt, W), (yt, H)])

G = grid.FixedGrid.default_fill(W, H, ".")

for points in simulate(p2):
    x, y = points
    G[y, x] = "#"

G.print(line_spacing="")

print(math.prod(p1))
print(p2)
