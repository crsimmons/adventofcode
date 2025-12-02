#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

sys.setrecursionlimit(10**6)

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
I = D.split(",")

ranges = [tuple(map(int, r.split("-"))) for r in I]

p1, p2 = 0, 0

for l, u in ranges:
    for x in range(l, u + 1):
        s = str(x)
        l = len(s)

        if l < 2:
            continue

        if l % 2 == 0 and s[: l // 2] == s[l // 2 :]:
            p1 += x

        # If a string S is composed of a repeating pattern of length P,
        # then S must overlap with itself perfectly if you shift it by P
        # Original:     1 2 3 1 2 3
        #               | | | | | |
        # Drop Last 3:  1 2 3 . . .  (Is strictly "123")
        # Drop First 3: . . . 1 2 3  (Is strictly "123")
        for i in range(1, l // 2 + 1):
            if l % i == 0 and s[:-i] == s[i:]:
                p2 += x
                break


print("Part 1:", p1)
print("Part 2:", p2)
