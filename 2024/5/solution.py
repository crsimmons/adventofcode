#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import functools
import sys

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
S = D.split("\n\n")

rules = [(a, b) for a, b in [x.split("|") for x in S[0].split("\n")]]
updates = [list(line.split(",")) for line in S[1].split("\n")]


def is_valid(u):
    valid = True
    for r in rules:
        b, a = r
        if b in u and a in u:
            if u.index(b) > u.index(a):
                valid = False
                break
    return valid


# -1: First element is less than the second.
#  1: First element is greater than the second.
#  0: Both elements are equal.
def compare(a, b):
    return -1 if (a, b) in rules else 1 if (b, a) in rules else 0


p1 = 0
p2 = 0
for u in updates:
    assert len(u) % 2 == 1
    if is_valid(u):
        p1 += int(find_middle(u))
    else:
        p2 += int(find_middle(sorted(u, key=functools.cmp_to_key(compare))))

print(p1)
print(p2)
