#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]


def priority(c):
    if "a" <= c <= "z":
        return ord(c) - ord("a") + 1
    return ord(c) - ord("A") + 27


p1 = 0
for l in lines:
    l, r = l[: len(l) // 2], l[len(l) // 2 :]
    for c in l:
        if c in r:
            p1 += priority(c)
            break
print(p1)

p2 = 0
i = 0
while i < len(lines):
    for c in lines[i]:
        if c in lines[i + 1] and c in lines[i + 2]:
            p2 += priority(c)
            break
    i += 3
print(p2)
