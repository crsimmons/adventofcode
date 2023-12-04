#!/usr/bin/env python3
import sys
from collections import defaultdict

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

grid = [list(l) for l in lines]

rnum = len(grid)
cnum = len(grid[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1),(-1,-1),(1,1),(-1,1),(1,-1)]

def concat(a, b):
    return int(str(a) + str(b))

is_part=False
p1=0
p2=0
gears=defaultdict(list)

for r in range(rnum):
    gear_coords=set()
    num=0
    # need to iterate the cnum+1 because we need to evaluate
    # digits in the final column
    for c in range(cnum+1):
        if c<cnum and grid[r][c].isdigit():
            num=concat(num, grid[r][c])
            for (dr,dc) in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rnum and 0 <= nc < cnum:
                    if not grid[nr][nc].isdigit() and not grid[nr][nc] == ".":
                        is_part = True
                    if grid[nr][nc]=="*":
                        gear_coords.add((nr,nc))
        elif num>0:
            if is_part:
                p1+=num
            is_part=False
            for gear in gear_coords:
                gears[gear].append(num)
            num=0
            gear_coords=set()

for _,v in gears.items():
    if len(v)==2:
        p2+=v[0]*v[1]

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
