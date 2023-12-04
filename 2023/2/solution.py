#!/usr/bin/env python3
import sys
from collections import defaultdict

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

p1=0
p2=0
for i,l in enumerate(lines):
    i=i+1
    p2_partial=1
    valid=True
    game = l.split(':')[1]
    C=defaultdict(int)
    for drawing in game.split(";"):
        for balls in drawing.split(","):
            n,c=balls.split()
            n=int(n)
            C[c]=max(C[c],n)

            if n > {"red":12, "green":13, "blue":14}.get(c, 0):
                valid=False

    if valid:
        p1+=i

    for v in C.values():
        p2_partial*=v
    p2+=p2_partial

print(p1)
print(p2)
