#!/usr/bin/env python3
import sys

from collections import defaultdict

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

tree = defaultdict(int)
path = []
for l in lines:
    e = l.split()
    if e[1] == "cd":
        if e[2] == "..":
            path.pop()
        else:
            path.append(e[2])
    elif e[1] == "ls" or e[0] == "dir":
        continue
    else:
        size = int(e[0])
        for i in range(1, len(path) + 1):
            # [:i] == from beginning to pos i (excluded)
            tree["/".join(path[:i]).replace("//", "/")] += size

total_used = tree["/"]
unused = 70000000 - total_used
required = 30000000 - unused

p1 = 0
p2 = total_used
for k, v in tree.items():
    if v <= 100000:
        p1 += v
    if v >= required:
        p2 = min(p2, v)

print(p1)
print(p2)
