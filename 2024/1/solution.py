#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

left = []
right = []

for l in L:
    n = nums(l)
    left.append(n[0])
    right.append(n[1])

left.sort()
right.sort()

print(sum(abs(a - b) for a, b in zip(left, right)))

p2 = 0
for x in left:
    p2 += right.count(x) * x

print(p2)
