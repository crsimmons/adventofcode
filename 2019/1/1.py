#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

p1 = 0
p2 = 0
for l in map(int, lines):
    v = (l // 3) - 2
    p1 += v
    p2 += v

    while (v // 3) - 2 > 0:
        v = (v // 3) - 2
        p2 += v

print(p1)
print(p2)
