#!/usr/bin/env python3
import sys

from collections import deque

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

Grid = []
for l in lines:
    Grid.append(l)
Rows = len(Grid)
Columns = len(Grid[0])

Elevations = [[0 for _ in range(Columns)] for _ in range(Rows)]
for r in range(Rows):
    for c in range(Columns):
        if Grid[r][c] == "S":
            Elevations[r][c] = 1
        elif Grid[r][c] == "E":
            Elevations[r][c] = 26
        else:
            Elevations[r][c] = ord(Grid[r][c]) - ord("a") + 1


def bfs(part):
    Q = deque()
    for r in range(Rows):
        for c in range(Columns):
            if (part == 1 and Grid[r][c] == "S") or (
                part == 2 and Elevations[r][c] == 1
            ):
                Q.append((0, (r, c)))

    S = set()
    while Q:
        d, (r, c) = Q.popleft()
        if (r, c) in S:
            continue
        S.add((r, c))
        if Grid[r][c] == "E":
            return d
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc
            if (
                0 <= nr < Rows
                and 0 <= nc < Columns
                and Elevations[nr][nc] <= Elevations[r][c] + 1
            ):
                Q.append((d + 1, (nr, nc)))


print(bfs(1))
print(bfs(2))
