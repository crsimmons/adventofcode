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

p1 = p2 = 0

def solve(x, part2):
    for i in range(len(x)-2,-1,-1):
        if part2:
            x[i].appendleft(x[i][0] - x[i+1][0])
        else:
            x[i].append(x[i+1][-1] + x[i][-1])

    return x[0][0 if part2 else -1]

for l in L:
    s = deque([int(x) for x in l.split()])

    x = [s]
    while any(n != 0 for n in s):
        d = deque([s[i+1]-s[i] for i in range(len(s)-1)])
        x.append(d)
        s=d

    p1 += solve(x, False)
    p2 += solve(x, True)

print(p1)
print(p2)
