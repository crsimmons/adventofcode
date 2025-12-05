#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

sys.setrecursionlimit(10**6)

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
B = D.split("\n\n")

ranges = [tuple(map(int, r.split("-"))) for r in B[0].split("\n")]
ingredients = list(map(int, B[1].split("\n")))

collapsed = collapse_ranges(ranges)

p1 = []

for ingredient in ingredients:
    fresh = False
    for lo, hi in collapsed:
        if lo <= ingredient <= hi:
            fresh = True
            break
    if fresh:
        p1.append(ingredient)

print("Part 1:", len(p1))

p2 = 0
for lo, hi in collapsed:
    p2 += hi - lo + 1
print("Part 2:", p2)
