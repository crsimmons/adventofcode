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

sr, sc = G.find('S')

O = [[0]*C for _ in range(R)]
O[sr][sc] = 1

loop = set([(sr,sc)])
Q = deque([(sr,sc)])
s_type = {"|", "J", "L", "7", "F", "|", "-"}

while Q:
    r, c = Q.popleft()
    ch = G[r,c]

    # up
    if r>0 and ch in "S|JL" and G[r-1,c] in "|7F" and (r-1,c) not in loop:
        loop.add((r-1,c))
        Q.append((r-1, c))
        O[r-1][c] = 1
        if ch == "S":
            s_type &= {"|", "J", "L"}
    # down
    if r<R-1 and ch in "S|7F" and G[r+1,c] in "|JL" and (r+1,c) not in loop:
        loop.add((r+1,c))
        Q.append((r+1, c))
        O[r+1][c] = 1
        if ch == "S":
            s_type &= {"|", "7", "F"}
    # left
    if c>0 and ch in "S-7J" and G[r,c-1] in "-FL" and (r,c-1) not in loop:
        loop.add((r,c-1))
        Q.append((r, c-1))
        O[r][c-1] = 1
        if ch == "S":
            s_type &= {"-", "7", "J"}
    # right
    if c<C-1 and ch in "S-FL" and G[r,c+1] in "-7J" and (r,c+1) not in loop:
        loop.add((r,c+1))
        Q.append((r, c+1))
        O[r][c+1] = 1
        if ch == "S":
            s_type &= {"-", "F", "L"}

assert len(s_type) == 1

print(len(loop) // 2 )

(se,) = s_type

G[sr,sc]=se

p2 = 0
# This is effectively raycasting to determine if a point is inside the polygon formed by the loop
# For each row we track if the current column is inside the loop (inside)
# If (r,c) is part of the loop (O[r][c] == 1) and those coords are a vertical segment, we flip
# the value of inside as this is a crossing

# If (r,c) is not part of the loop (O[r][c] == 0) then we add inside to p2. Remember that True = 1
# and False = 0 in python so we are only incrementing when we've crossed an odd number of pipes.

# To avoid confusion with the corner pieces, assume we're crossing each pipe piece just above the
# modpoint. So |JL count as being crossed but 7 and F get crossed "above" the bend so they are not
# counted
for r in range(R):
    inside = False
    for c in range(C):
        if O[r][c]:
            if G[r,c] in "|JL":
                inside = not inside
        else:
            p2 += inside

print(p2)
