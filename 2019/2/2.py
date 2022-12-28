#!/usr/bin/env python3
import sys

from copy import deepcopy

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

CODE = list(map(int, lines[0].split(",")))


def solve(c, n, v):
    c[1] = n
    c[2] = v

    i = 0
    while i < len(c):
        e = c[i]
        if e == 99:
            break
        elif e == 1:
            c[c[i + 3]] = c[c[i + 1]] + c[c[i + 2]]
            i += 4
        elif e == 2:
            c[i + 3] = c[c[i + 1]] * c[c[i + 2]]
            i += 4
        else:
            i += 1
    return c[0]


ins = deepcopy(CODE)
print(solve(ins, 12, 2))

for n in range(100):
    for v in range(100):
        ins = deepcopy(CODE)
        s = solve(ins, n, v)
        if s == 19690720:
            print(100 * n + v)
            exit(0)
