#!/usr/bin/env python3
import sys
import re

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.rstrip() for l in data]


def getRegion(r, c):
    for i, (rr, cc) in enumerate(REGION):
        if rr * CUBE <= r < (rr + 1) * CUBE and cc * CUBE <= c < (cc + 1) * CUBE:
            return i + 1
    assert False, (r, c)


def solve(part):
    r = c = 0
    f = 0

    while M[c * 1j] != ".":
        c += 1

    for n, t in INS:
        n = int(n)
        for _ in range(n):
            dr, dc = F[f]
            if part == 1:
                nr = r
                nc = c
                while True:
                    nr = (nr + dr) % R
                    nc = (nc + dc) % C
                    if M[nr + nc * 1j] != " ":
                        break
                if M[nr + nc * 1j] == "#":
                    break
                r = nr
                c = nc
            else:
                region = getRegion(r, c)
                nf = f
                nr = r + dr
                nc = c + dc
                match region:
                    case 1:
                        # up to region 6
                        if nr < 0:
                            nf = RIGHT
                            nr, nc = nc + (2 * CUBE), 0
                        # right to region 2
                        elif nc == CUBE - 1:
                            nf = RIGHT
                            nr, nc = (3 * CUBE) - 1 - nr, 0
                    case 2:
                        # up to region 6
                        if nr < 0:
                            nr, nc = (4 * CUBE) - 1, nc - (2 * CUBE)
                        # right to region 4
                        elif nc == (3 * CUBE):
                            nf = LEFT
                            nr, nc = (3 * CUBE) - 1 - nr, (2 * CUBE) - 1
                        # down to region 3
                        elif nr == CUBE:
                            nf = LEFT
                            nr, nc = nc - CUBE, (2 * CUBE) - 1
                    case 3:
                        # right to region 2
                        if nc == (2 * CUBE):
                            nf = UP
                            nr, nc = CUBE - 1, nr + CUBE
                        # left to region 5
                        elif nc == CUBE - 1:
                            nf = DOWN
                            nr, nc = (2 * CUBE), nr - CUBE
                    case 4:
                        # up to region 3
                        if nr == (2 * CUBE) - 1:
                            nf = RIGHT
                            nr, nc = nc + CUBE, CUBE
                        # left to region 1
                        elif nc < 0:
                            nf = RIGHT
                            nr, nc = (3 * CUBE) - 1 - nr, CUBE
                    case 5:
                        # right to region 2
                        if nc == (2 * CUBE):
                            nf = LEFT
                            nr, nc = (3 * CUBE) - 1 - nr, (3 * CUBE) - 1
                        # down to region 6
                        elif nr == (3 * CUBE):
                            nf = LEFT
                            nr, nc = nc + (2 * CUBE), 49
                    case 6:
                        # left to region 1
                        if nc < 0:
                            nf = DOWN
                            nr, nc = 0, nr - (2 * CUBE)
                        # down to region 2
                        elif nr == (4 * CUBE):
                            nr, nc = 0, nc + (2 * CUBE)
                        # right to region 5
                        elif nc == CUBE:
                            nf = UP
                            nr, nc = (3 * CUBE) - 1, nr - (2 * CUBE)
                if M[nr + nc * 1j] == "#":
                    nf = f
                    break
                r = nr
                c = nc
                f = nf
        if t == "R":
            f = (f + 1) % 4
        elif t == "L":
            f = (f + 3) % 4

    return (r + 1) * 1000 + (c + 1) * 4 + f


M = {}
R = 0
C = 0

for r, l in enumerate(lines[:-2]):
    R = max(R, r)
    for c, e in enumerate(l):
        C = max(C, c)
        M[r + c * 1j] = e

R += 1
C += 1

for r in range(R + 1):
    for c in range(C + 1):
        if (r + c * 1j) not in M:
            M[r + c * 1j] = " "

# Doesn't work for example but whatever
CUBE = R // 4

INS = re.findall(r"(\d+)([RL]?)", lines[-1])

# .12
# .3.
# 45.
# 6..
REGION = [(0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (3, 0)]

F = [(0, 1), (1, 0), (0, -1), (-1, 0)]

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

print(solve(1))
print(solve(2))

# 136054
# 122153
