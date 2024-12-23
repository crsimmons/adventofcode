#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import functools
import sys

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

DIR_MAP = dict(zip(DIRS, [">", "v", "<", "^"]))

npad = """789
456
123
 0A"""

NUM_PAD = grid.FixedGrid.parse(npad)

dpad = """ ^A
<v>"""

DIR_PAD = grid.FixedGrid.parse(dpad)


def find_path(grid, start_char, target_char):
    sr, sc = grid.find(start_char)
    er, ec = grid.find(target_char)

    def traverse(r, c, path_so_far):
        if (r, c) == (er, ec):
            yield path_so_far + "A"
        if ec < c and grid[r, c - 1] != " ":
            yield from traverse(r, c - 1, path_so_far + "<")
        if er < r and grid[r - 1, c] != " ":
            yield from traverse(r - 1, c, path_so_far + "^")
        if er > r and grid[r + 1, c] != " ":
            yield from traverse(r + 1, c, path_so_far + "v")
        if ec > c and grid[r, c + 1] != " ":
            yield from traverse(r, c + 1, path_so_far + ">")

    return min(
        traverse(sr, sc, ""),
        key=lambda path: sum(char1 != char2 for char1, char2 in zip(path, path[1:])),
    )

@functools.cache
def solve(code, depth, max_depth):
    if depth > max_depth:
        return len(code)

    total = 0
    for from_char, to_char in zip("A" + code, code):
        path_result = find_path(DIR_PAD if depth else NUM_PAD, from_char, to_char)
        total += solve(path_result, depth + 1, max_depth)
    return total


for depth in [2, 25]:
    total_score = 0
    for l in L:
        sequence = solve(l, 0, depth)
        weighted_score = sequence * int(l[:3])
        total_score += weighted_score
    print(total_score)
