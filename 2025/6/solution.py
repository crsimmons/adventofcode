#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

sys.setrecursionlimit(10**6)

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
rows = open(inputfile).read().splitlines()
split_rows = [line.split() for line in rows]

p1 = 0

cols = list(zip(*split_rows))

for *nums, op in cols:
    p1 += eval(op.join(nums))

p2 = 0

cols = list(zip(*rows))

groups = []
group = []

for col in cols:
    if set(col) == {" "}:
        groups.append(group)
        group = []
    else:
        group.append(col)

groups.append(group)

for group in groups:
    op = group[0][-1]
    nums = ["".join(row[:-1]) for row in group]
    p2 += eval(op.join(nums))

print("Part 1:", p1)
print("Part 2:", p2)
