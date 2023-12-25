#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque

from lib import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")
G = [[c for c in row] for row in L]
R = len(G)
C = len(G[0])

p1 = p2 = 0
for i,l in enumerate(L):
    p2_partial = 1
    valid = True
    game = l.split(':')[1]
    COLOURS = defaultdict(int)

    for drawing in game.split(";"):
        for balls in drawing.split(","):
            n, c = balls.split()
            n = int(n)

            COLOURS[c] = max(COLOURS[c],n)

            if n > {"red":12, "green":13, "blue":14}.get(c, 0):
                valid=False

    if valid:
        p1 += i + 1

    for v in COLOURS.values():
        p2_partial *= v

    p2 += p2_partial

print(p1)
print(p2)
