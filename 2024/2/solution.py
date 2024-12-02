#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

def is_safe(n):
    ok = n == sorted(n) or n == sorted(n, reverse=True)
    for a, b in zip(n, n[1:]):
        diff = abs(b - a)
        if not 1 <= diff <= 3:
            ok = False
    return ok


p1 = 0
p2 = 0

for l in L:
    n = nums(l)
    if is_safe(n):
        p1 += 1

    safe = False
    for i in range(len(n)):
        if is_safe(rm_element(n, i)):
            safe = True
    if safe:
        p2 += 1

print(p1)
print(p2)
