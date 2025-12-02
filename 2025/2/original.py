#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

sys.setrecursionlimit(10**6)

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
I = D.split(",")

p1 = 0
p2 = 0

for r in I:
    l, u = r.split("-")
    for x in range(int(l), int(u) + 1):
        s = str(x)
        if len(s) < 2:
            continue
        if re.match(r"^(\d+)\1$", s):
            p1 += x
        if re.match(r"^(\d+)\1+$", s):
            p2 += x

print("Part 1:", p1)
print("Part 2:", p2)
