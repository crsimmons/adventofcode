#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

def is_valid(t, n, p2=False):
    if len(n) == 1:
        return n[0] == t
    if n[0] > t:
        return False
    if is_valid(t, [n[0] + n[1]] + n[2:], p2):
        return True
    if is_valid(t, [n[0] * n[1]] + n[2:], p2):
        return True
    if p2 and is_valid(t, [int(str(n[0]) + str(n[1]))] + n[2:], p2):
        return True
    return False


p1 = 0
p2 = 0
for l in L:
    x = nums(l)
    t = x[0]
    n = x[1:]
    if is_valid(t, n):
        p1 += t
    if is_valid(t, n, True):
        p2 += t

print(p1)
print(p2)
