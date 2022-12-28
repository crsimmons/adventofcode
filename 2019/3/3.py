#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

W1 = set()
W2 = set()

S1 = {}
S2 = {}

D = {"R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}

c = 0
r = 0
d = 0
for ins in lines[0].split(","):
    (dr, dc) = D[ins[0]]
    for _ in range(int(ins[1:])):
        d += 1
        r += dr
        c += dc
        W1.add((r, c))
        if (r, c) not in S1:
            S1[(r, c)] = d

c = 0
r = 0
d = 0
for ins in lines[1].split(","):
    (dr, dc) = D[ins[0]]
    for _ in range(int(ins[1:])):
        d += 1
        r += dr
        c += dc
        W2.add((r, c))
        if (r, c) not in S2:
            S2[(r, c)] = d

d = float("inf")
for (r, c) in W1 & W2:
    d = min(d, abs(r) + abs(c))

print(d)

s = float("inf")
for (r, c) in W1 & W2:
    s = min(s, S1[(r, c)] + S2[(r, c)])

print(s)
