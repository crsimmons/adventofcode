#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

DIRS = {"U": (-1, 0),"L":(0, -1),"D":(1, 0),"R":(0, 1)}
DIRS2 = ['R', 'D', 'L', 'U']

def solve(part2):
    r,c = 0,0
    points = [(r,c)]
    perimeter = 0
    for l in L:
        d, n, colour = l.split()

        if part2:
            colour = colour[2:-1]
            n = int(colour[:-1],16)
            d = int(colour[-1:])
            dr, dc = DIRS[DIRS2[d]]
        else:
            n = int(n)
            dr, dc = DIRS[d]

        r += dr*n
        c += dc*n

        perimeter += n
        points.append((r,c))

    # shoelace formula
    # https://en.wikipedia.org/wiki/Shoelace_formula
    # sum of deteminants of pairs of points
    area = abs(sum(x[0]*y[1] - x[1]*y[0] for x, y in zip(points, points[1:])))//2
    # area = 0
    # for i in range(len(points) - 1):
    #     r,c = points[i]
    #     nr,nc = points[i+1]

    #     area += (c+nc)*(r-nr)
    # area = abs(area)
    # area //= 2

    # pick's theorem
    # A = i + b/2 -1 -> i = A + 1 - b/2
    # boundary points (b) = perimeter
    interior = area + 1 - perimeter // 2

    # points filled = points inside + points on perimeter
    print(interior + perimeter)

solve(False)
solve(True)
