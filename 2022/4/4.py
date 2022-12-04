#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]
p1 = 0
p2 = 0


def get_range(e):
    l, u = e.split("-")
    return [i for i in range(int(l), int(u) + 1)]


for l in lines:
    e1, e2 = l.split(",")
    r1 = get_range(e1)
    r2 = get_range(e2)
    if set(r1) <= set(r2) or set(r2) <= set(r1):
        p1 += 1
    if set(r1) & set(r2):
        p2 += 1

print(p1)
print(p2)
