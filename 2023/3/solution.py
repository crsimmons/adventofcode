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

def concat(a, b):
    return int(str(a) + str(b))

is_part = False
p1 = p2 = 0
gears = defaultdict(list)

for r in range(R):
    gear_coords = set()
    num = 0
    # need to iterate the cnum+1 because we need to evaluate
    # digits in the final column
    for c in range(C+1):
        if c < C and G[r,c].isdigit():
            num = concat(num, G[r,c])
            for (nr,nc) in G.adj(r,c,True):
                if 0 <= nr < R and 0 <= nc < C:
                    if not G[nr,nc].isdigit() and not G[nr,nc] == ".":
                        is_part = True
                    if G[nr,nc] == "*":
                        gear_coords.add((nr,nc))
        elif num > 0:
            if is_part:
                p1 += num
            is_part = False
            for gear in gear_coords:
                gears[gear].append(num)
            num = 0
            gear_coords = set()

for _, v in gears.items():
    if len(v) == 2:
        p2 += v[0]*v[1]

print(p1)
print(p2)

# original solution
# for r in range(rnum):
#     for c in range(cnum):
#         if not grid[r][c].isdigit():
#             if not part:
#                 print(num)
#                 p1+=num
#             part=True
#             num=0
#             continue
#         num=concat(num,int(grid[r][c]))
#         for (dr, dc) in directions:
#             nr = r + dr
#             nc = c + dc
#             if 0 <= nr < rnum and 0 <= nc < cnum:
#                 if not grid[nr][nc].isdigit() and not grid[nr][nc] == ".":
#                     part=False

# print(p1)
