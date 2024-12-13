#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip().split("\n\n")
B = [nums(l) for l in D]


def solve(part2=False):
    ans = 0
    for b in B:
        a, c, b, d, px, py = b
        if part2:
            px += 10000000000000
            py += 10000000000000
        assert a * d != b * c
        determinant = a * d - b * c
        m = (px * d - py * b) / determinant
        n = (py * a - px * c) / determinant
        if m.is_integer() and n.is_integer():
            ans += 3 * m + n

    return int(ans)


print(solve())
print(solve(True))
