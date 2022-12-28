#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

l, u = map(int, lines[0].split("-"))

p1 = 0
p2 = 0

for i in range(l, u + 1):
    n = str(i)
    if any(n[j] > n[j + 1] for j in range(5)):
        continue
    groups = [n.count(d) for d in set(n)]
    if any(group >= 2 for group in groups):
        p1 += 1
    if any(group == 2 for group in groups):
        p2 += 1

print(p1)
print(p2)
