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

def solve(arr, part2):
    if all(x==0 for x in arr):
        return 0

    deltas = [y-x for x,y in zip(arr,arr[1:])]
    diff = solve(deltas, part2)

    if part2:
        return arr[0]-diff
    else:
        return arr[-1]+diff


for part2 in [False, True]:
    ans=0
    for line in L:
        nums = [int(x) for x in line.split()]
        ans += solve(nums, part2)
    print(ans)
