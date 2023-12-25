#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque
from itertools import cycle
from math import lcm

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

dirs, lines = D.split("\n\n")

dirs = [0 if c == "L" else 1 for c in dirs]
lines = lines.split("\n")

M = {}

for l in lines:
    a, b = l.split(" = ")
    lr = tuple(re.findall(r"[0-9A-Z]{3}", b))
    M[a] = lr

def solve(part2):
    starts = []
    for s in M.keys():
        if s.endswith("A" if part2 else "AAA"):
            starts.append(s)

    steps_taken = []

    for start in starts:
        steps = 0
        for d in cycle(dirs):
            # the number of steps to get from the start to the element ending in Z
            # is the same as the number of steps taken to get from Z element back to itself
            # so we keep track of the number of steps for each starting point to reach Z
            if start.endswith("Z"):
                steps_taken.append(steps)
                break
            start = M[start][d]
            steps += 1
    print(lcm(*steps_taken))


for part2 in [False, True]:
    solve(part2)
