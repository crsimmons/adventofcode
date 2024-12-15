#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import deque

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
B = D.split("\n\n")

G = grid.FixedGrid.parse(B[0])

MOVES = [x for x in B[1] if x != "\n"]

DIRS = {"^": (-1, 0), "<": (0, -1), "v": (1, 0), ">": (0, 1)}


def expand_grid(G):
    R = G.height
    C = G.width
    BIG_G = []
    char_map = {"#": ["#", "#"], "O": ["[", "]"], ".": [".", "."], "@": ["@", "."]}
    for r in range(R):
        row = []
        for c in range(C):
            row.extend(char_map[G[r, c]])
        BIG_G.append(row)
    return grid.FixedGrid(BIG_G)


def can_move(G, r, c, dr, dc):
    Q = deque([(r, c)])
    SEEN = set()
    while Q:
        r, c = Q.popleft()
        if (r, c) in SEEN:
            continue
        SEEN.add((r, c))
        nr, nc = r + dr, c + dc
        if G[nr, nc] == "#":
            return False, SEEN
        elif G[nr, nc] == "O":
            Q.append((nr, nc))
        elif G[nr, nc] == "[":
            Q.append((nr, nc))
            Q.append((nr, nc + 1))
        elif G[nr, nc] == "]":
            Q.append((nr, nc))
            Q.append((nr, nc - 1))
    return True, SEEN


def move_boxes(G, SEEN, dr, dc):
    while len(SEEN) > 0:
        for r, c in sorted(SEEN):
            nr, nc = r + dr, c + dc
            if (nr, nc) not in SEEN:
                assert G[nr, nc] == "."
                G[nr, nc] = G[r, c]
                G[r, c] = "."
                SEEN.remove((r, c))


def solve(G, part2):
    G = G.quick_copy()
    if part2:
        G = expand_grid(G)

    R = G.height
    C = G.width

    r, c = G.find("@")
    G[r, c] = "."

    for ins in MOVES:
        dr, dc = DIRS[ins]
        nr, nc = r + dr, c + dc

        if G[nr, nc] == "#":
            continue
        elif G[nr, nc] == ".":
            r, c = nr, nc
        elif G[nr, nc] in ["O", "[", "]"]:
            ok, SEEN = can_move(G, r, c, dr, dc)
            if not ok:
                continue
            move_boxes(G, SEEN, dr, dc)
            r, c = nr, nc

    return sum(100 * r + c for r in range(R) for c in range(C) if G[r, c] in ["O", "["])


print(solve(G, False))
print(solve(G, True))
