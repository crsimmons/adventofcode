#!/usr/bin/env python3
import sys
import math

from collections import deque

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

BLIZZARDS = tuple(set() for _ in range(4))
for R, line in enumerate(lines[1:-1]):
    for C, e in enumerate(line[1:-1]):
        if e in "<>^v":
            BLIZZARDS["<>^v".find(e)].add((R, C))

R += 1
C += 1

START = (-1, 0)
END = (R, C - 1)
TARGETS = [END, START]

VALID = set()
for r in range(R):
    for c in range(C):
        VALID.add((r, c))
VALID.add(START)
VALID.add(END)

lcm = R * C // math.gcd(R, C)

D = ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0))

# blizzard #, tr, tc
# Blizzard '<' (0): each minute r doesn't change and c decreases
# Blizzard '>' (1): each minute r doesn't change and c increases
# Blizzard '^' (2): each minute r decreases and c doesn't change
# Blizzard 'v' (3): each minute r increases and c doesn't change
B = ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0))

Q = deque([(0, -1, 0, 0)])
SEEN = set()
p1 = False

while Q:
    t, r, c, stage = Q.popleft()

    t += 1

    for dr, dc in D:
        nr = r + dr
        nc = c + dc

        if (nr, nc) == TARGETS[stage % 2]:
            if stage == 0 and not p1:
                print(t)
                p1 = True
            if stage == 2:
                print(t)
                exit(0)
            stage += 1

        if (nr, nc) not in VALID:
            continue

        fail = False

        if (nr, nc) not in TARGETS:
            for i, tr, tc in B:
                # check if (nr,nc) minus the blizzard movement over t is the starting point of a blizzard
                if ((nr - tr * t) % R, (nc - tc * t) % C) in BLIZZARDS[i]:
                    fail = True
                    break
        if not fail:
            key = (nr, nc, stage, t % lcm)

            if key in SEEN:
                continue

            SEEN.add(key)
            Q.append((t, nr, nc, stage))
