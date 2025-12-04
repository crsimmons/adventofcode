#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

sys.setrecursionlimit(10**6)

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

p1, p2 = 0, 0


def solve(bank, n):
    jolts = 0
    for i in range(n - 1):
        digit = max(bank[: i - (n - 1)])
        bank = bank[bank.index(digit) + 1 :]
        jolts = (jolts * 10) + digit

    return (jolts * 10) + max(bank)


for l in L:
    bank = list(map(int, re.findall(r"\d", l)))

    p1 += solve(bank, 2)
    p2 += solve(bank, 12)

print("Part 1:", p1)
print("Part 2:", p2)
