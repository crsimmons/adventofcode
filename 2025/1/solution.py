#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

sys.setrecursionlimit(10**6)

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

pos = 50

p1 = 0
p2 = 0

for l in L:
    d = 1 if l[0] == "R" else -1
    n = int(l[1:])
    for _ in range(n):
        pos = (pos + d) % 100
        if pos == 0:
            p2 += 1
    if pos == 0:
        p1 += 1

print("Part 1:", p1)
print("Part 2:", p2)
