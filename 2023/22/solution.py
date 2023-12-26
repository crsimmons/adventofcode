#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

def drop_brick(tallest, brick):
    sx, sy, sz, ex, ey, ez = brick
    # highest z for brick's (x,y) space
    peak = max(tallest[(x,y)] for x in range(sx, ex + 1) for y in range(sy, ey + 1))
    dz = max(sz - peak - 1, 0)
    return (sx, sy, sz - dz, ex, ey, ez - dz)

def stabilize(bricks):
    tallest = defaultdict(int)
    new_bricks = []
    falls = 0

    for brick in bricks:
        sx, sy, z, ex, ey, _ = brick
        new_brick = drop_brick(tallest, brick)
        _, _, new_z, _, _, max_z = new_brick
        if new_z != z:
            falls += 1

        new_bricks.append(new_brick)

        # for each point in (x,y) space update highest z
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                tallest[(x,y)] = max_z

    return falls, new_bricks

B = [nums(l) for l in L]

# sz <= ez
for b in B:
    assert b[2]<=b[5]

B = sorted(B, key=lambda brick: brick[2])

_, settled_bricks = stabilize(B)

p1 = p2 = 0

for i in range(len(settled_bricks)):
    # remove brick i and see if any bricks fall
    removed = settled_bricks[:i] + settled_bricks[i + 1:]
    falls, _ = stabilize(removed)
    if not falls:
        p1 += 1
    else:
        p2 += falls

print(p1)
print(p2)
