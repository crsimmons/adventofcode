#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from itertools import product

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip().split("\n\n")

locks = []
keys = []

for e in D:
    g = grid.FixedGrid.parse(e)
    if all(x == "#" for x in g.rows[0]):
        locks.append(g)
    elif all(x == "#" for x in g.rows[-1]):
        keys.append(g)
    else:
        assert False


def compare(lock, key):
    assert lock.height == key.height and lock.width == key.width
    for r in range(lock.height):
        for c in range(lock.width):
            if lock[r, c] == "#" and key[r, c] == "#":
                return False
    return True


p1 = 0
for k, l in [(a, b) for a, b in product(keys, locks)]:
    if compare(k, l):
        p1 += 1

print(p1)
