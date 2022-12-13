#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]
p1 = 0
p2 = 0

grid = [list(map(int, l)) for l in lines]

rnum = len(grid)
cnum = len(grid[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for r in range(rnum):
    for c in range(cnum):
        tree = grid[r][c]
        if (
            all(grid[r][i] < tree for i in range(c))
            or all(grid[r][i] < tree for i in range(c + 1, cnum))
            or all(grid[i][c] < tree for i in range(r))
            or all(grid[i][c] < tree for i in range(r + 1, rnum))
        ):
            p1 += 1
        s = 1
        for (dr, dc) in directions:
            dist = 1
            nr = r + dr
            nc = c + dc
            while True:
                if not (0 <= nr < rnum and 0 <= nc < cnum):
                    dist -= 1
                    break
                if grid[nr][nc] >= tree:
                    break
                dist += 1
                nr += dr
                nc += dc
            s *= dist
        p2 = max(p2, s)

print(p1)
print(p2)
