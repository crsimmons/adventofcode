#!/usr/bin/env python3
import sys

from copy import deepcopy

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]
p1 = 0
p2 = 0

blocked = set()
abyss = 0

for l in lines:
    rocks = [list(map(int, pair.split(","))) for pair in l.split()[::2]]
    for (x1, y1), (x2, y2) in zip(rocks, rocks[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                blocked.add((x, y))
                abyss = max(abyss, y + 1)


def simulate(part, i, blocked):
    global abyss
    s = [500, 0]
    while True:
        if s[1] >= abyss:
            if part == 1:
                return i, True, blocked
            else:
                break
        if (s[0], s[1] + 1) not in blocked:
            s[1] += 1
        elif (s[0] - 1, s[1] + 1) not in blocked:
            s[0] -= 1
            s[1] += 1
        elif (s[0] + 1, s[1] + 1) not in blocked:
            s[0] += 1
            s[1] += 1
        else:
            break
    blocked.add(tuple(s))
    i += 1
    return i, False, blocked


start = deepcopy(blocked)
while True:
    p1, finished, start = simulate(1, p1, start)
    if finished:
        print(p1)
        break

start = deepcopy(blocked)
while (500, 0) not in start:
    p2, _, start = simulate(2, p2, start)

print(p2)
