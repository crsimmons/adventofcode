#!/usr/bin/env python3
import sys
from collections import defaultdict

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

p1=0
C = defaultdict(lambda:1)

for l in lines:
    c, n = l.split(":")
    c = int(c.split()[-1])
    # defaultdict gives a default value but doesn't count
    # the element as existing in .values unless it has
    # actually been accessed/set
    if c not in C:
        C[c]=1
    w,h = n.split("|")
    w = [int(x) for x in w.split()]
    h = [int(x) for x in h.split()]

    s = len(set(w) & set(h))

    if s > 0:
        p1 += 2**(s-1)

    # defaultdict makes this work
    for j in range(c+1,c+s+1):
        C[j]+=C[c]

print(p1)
print(sum(C.values()))
