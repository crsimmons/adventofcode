#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from functools import lru_cache

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()

stones = list(map(int, D.split()))


@lru_cache(maxsize=None)
def solve(stone, blinks):
    if blinks == 0:
        return 1
    elif stone == 0:
        return solve(1, blinks - 1)
    elif int(len(str(stone))) % 2 == 0:
        stone_str = str(stone)
        left = stone_str[: len(stone_str) // 2]
        right = stone_str[len(stone_str) // 2 :]
        left, right = (int(left), int(right))
        return solve(left, blinks - 1) + solve(right, blinks - 1)
    else:
        return solve(stone * 2024, blinks - 1)


print(sum(solve(stone, 25) for stone in stones))
print(sum(solve(stone, 75) for stone in stones))
