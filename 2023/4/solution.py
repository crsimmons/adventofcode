#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

p1=0
CARDS = defaultdict(lambda:1)

for l in L:
    c, n = l.split(":")
    c = int(c.split()[-1])
    # defaultdict gives a default value but doesn't count
    # the element as existing in .values unless it has
    # actually been accessed/set
    if c not in CARDS:
        CARDS[c]=1
    w,h = n.split("|")
    w = [int(x) for x in w.split()]
    h = [int(x) for x in h.split()]

    s = len(set(w) & set(h))

    if s > 0:
        p1 += 2**(s-1)

    # defaultdict makes this work
    for j in range(c+1,c+s+1):
        CARDS[j]+=CARDS[c]

print(p1)
print(sum(CARDS.values()))
