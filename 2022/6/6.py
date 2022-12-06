#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile).read()
p = 0
p1found = False

S = []
for c in data:
    p += 1
    if c in S:
        S = S[S.index(c) + 1 :]
    S.append(c)
    if len(S) == 4 and not p1found:
        print(p)
        p1found = True
    if len(S) == 14:
        print(p)
        break
