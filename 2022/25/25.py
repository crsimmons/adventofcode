#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

s = 0
for l in lines:
    c = 1
    for v in l[::-1]:
        s += ("=-012".find(v) - 2) * c
        c *= 5

p1 = ""
while s:
    r = s % 5
    s //= 5

    if r <= 2:
        p1 = p1 + str(r)
    else:
        p1 = p1 + "=-"[r % 3]
        # add 5 to the next column
        s += 1

print(p1[::-1])
