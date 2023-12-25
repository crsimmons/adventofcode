#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque
from itertools import combinations

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

memo = {}

# i == current index within springs
# bi == current index within block of broken springs
# curr == length of current block of '#'s
def solve(springs, blocks, i, bi, curr):
    key = (i,bi,curr)
    if key in memo:
        return memo[key]

    # reached last char of springs
    if i == len(springs):
        # evaluated all groups of broken springs and don't have current block of '#'s
        if bi == len(blocks) and curr == 0:
            return 1
        # on last block of broken springs and have it match the current block of '#'s
        elif bi == len(blocks) - 1 and curr == blocks[bi]:
            return 1
        # not valid
        else:
            return 0

    ans = 0
    for ch in ['.','#']:
        # ? can be . or #
        if springs[i] == ch or springs[i] == '?':
            # previous and current char are '.'s
            # move to next char
            if ch == '.' and curr == 0:
                ans += solve(springs, blocks, i+1, bi, 0)
            # ending a block
            # move on to next char and block
            elif ch == '.' and bi < len(blocks) and blocks[bi] == curr:
                ans += solve(springs, blocks, i+1, bi+1, 0)
            # add broken spring to current block
            # move on to next char
            elif ch == '#':
                ans += solve(springs, blocks, i+1, bi, curr+1)
    memo[key] = ans
    return ans



for part2 in [False, True]:
    ans = 0
    for l in L:
        springs, blocks = l.split(" ")
        if part2:
            springs = '?'.join([springs]*5)
            blocks = ','.join([blocks]*5)

        blocks = [int(x) for x in blocks.split(",")]

        memo.clear()
        ans += solve(springs, blocks, 0, 0, 0)

    print(ans)

