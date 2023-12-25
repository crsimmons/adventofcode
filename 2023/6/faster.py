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

time = int("".join(list(map(str,times))))
record = int("".join(list(map(str,records))))

def search(t,r):
    def f(n):
        return (t-n)*n

    lo = 0
    hi = t // 2

    if f(hi) < r:
        return 0

    while lo + 1 < hi:
        m = (lo + hi) // 2
        if f(m) > r:
            hi = m
        else:
            lo = m

    first = hi
    last = int((t/2) + (t/2-first))

    return last-first+1

p1 = 1

for i in range(len(times)):
    p1 *= search(times[i], records[i])

print(p1)
print(search(time, record))
