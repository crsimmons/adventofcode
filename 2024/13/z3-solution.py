#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

import z3

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip().split("\n\n")
B = [nums(l) for l in D]


def solve(part2=False):
    ans = 0
    for ax, ay, bx, by, px, py in B:
        if part2:
            px += 10000000000000
            py += 10000000000000
        a, b = z3.Ints("a b")
        o = z3.Optimize()
        # the button presses limit in part 1 doesn't matter
        # and the solutiion is faster without it
        o.add([a * ax + b * bx == px, a * ay + b * by == py, a >= 0, b >= 0])
        o.minimize(3 * a + b)

        if o.check() == z3.sat:
            m = o.model()
            ans += 3 * m[a].as_long() + m[b].as_long()

    return ans

print(solve())
print(solve(True))
