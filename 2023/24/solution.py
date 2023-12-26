#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from itertools import combinations

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

S = []
for l in L:
    S.append(nums(l))

MIN = 7 if len(sys.argv) > 1 else 200000000000000
MAX = 27 if len(sys.argv) > 1 else 400000000000000

ans=0

for p1, p2 in combinations(S,2):
    x1, y1, z1, vx1, vy1, vz1 = p1
    x2, y2, z2, vx2, vy2, vz2 = p2

    assert vx1 != 0 and vy1 != 0
    assert vx2 != 0 and vy2 != 0

    m1 = vy1 / vx1
    b1 = y1 - m1 * x1
    m2 = vy2 / vx2
    b2 = y2 - m2 * x2

    if m1 == m2:
        # print("NO INTERSECTION")
        continue

    x = (b1 - b2) / (m2 - m1)
    y = m1 * x + b1

    if (x - x1) / vx1 < 0 or (x - x2) / vx2 < 0 or (y - y1) / vy1 < 0 or (y - y2) / vy2 < 0:
        # print("INTERSECTION IN PAST")
        continue

    if MIN <= x <= MAX and MIN <= y <= MAX:
        # print("INSIDE")
        ans += 1
    else:
        # print("OUTSIDE")
        pass

print(ans)

from z3 import *

# We have x,y,z,vx,vy,vz as the position and velocity of the pebble
# and hx,hy,hz,hvx,hvy,hvz as the position and velocity of each hailstone
# and t_i as the time the pebble will collide with each hailstone

# We want to solve for t_i such that the pebble and hailstone_i have matching
# coords at time t_i

# This is when x + t_i*vx = hx + t_i*hvx -> x + t_i*vx - hx - t_i*hvx = 0
# for the x coord and similar for y and z

# Each new hailstone adds 3 new equations but only one new unknown (t_i) to then
# 6 base unknowns (x,y,z,vx,vy,vz), so assuming
# there is an answer (wouldn't be a good puzzle if there wasn't) then we only need to
# consider the first 3 hailstones (9 equations with 6 + 3 unknowns)

# Reals is about 2s faster than Ints and I don't know why.

x,y,z,vx,vy,vz = Reals('x y z vx vy vz')
T = [Real(f'T{i}') for i in range(3)]
SOLVER = Solver()
for i in range(3):
    hx, hy, hz, hvx, hvy, hvz = S[i]
    SOLVER.add(x + T[i]*vx - hx - T[i]*hvx == 0)
    SOLVER.add(y + T[i]*vy - hy - T[i]*hvy == 0)
    SOLVER.add(z + T[i]*vz - hz - T[i]*hvz == 0)
SOLVER.check()
M = SOLVER.model()
print(M.eval(x+y+z))
