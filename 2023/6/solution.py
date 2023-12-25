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

times = nums(L[0])
records = nums(L[1])

p1=1

for i, t in enumerate(times):
    b = 0
    for n in range(t+1):
        if (t-n)*n > records[i]:
            b += 1
    p1*=b

print(p1)

time = int("".join(list(map(str,times))))
record = int("".join(list(map(str,records))))

p2=0

for n in range(time+1):
    if (time-n)*n > record:
        p2 += 1

print(p2)
