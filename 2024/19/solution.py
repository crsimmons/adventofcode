#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
T, P = D.split("\n\n")

TOWELS = T.split(", ")
PATTERNS = P.split("\n")

p1 = 0
p2 = 0
DP = {}


def ways(towels, want):
    if want in DP:
        return DP[want]
    ans = 0
    if not want:
        ans = 1
    for towel in towels:
        if want.startswith(towel):
            ans += ways(towels, want[len(towel) :])
    DP[want] = ans
    return ans


for pattern in PATTERNS:
    target_ways = ways(TOWELS, pattern)
    if target_ways > 0:
        p1 += 1
    p2 += target_ways

print(p1)
print(p2)
