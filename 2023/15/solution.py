#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

INPUT = []
for l in L:
    INPUT.extend(l.split(","))

# Ignore newline characters when parsing the initialization sequence.
INPUT = [x for x in INPUT if x]

def calc(e):
    ans = 0
    for ch in e:
        ans += ord(ch)
        ans *= 17
        ans %= 256

    return ans

def inlist(label, lenses):
    for i,l in enumerate(lenses):
        if label == l[0]:
            return True, i
    return False, -1

p1 = 0
boxes = [[] for _ in range(256)]
for e in INPUT:
    p1 += calc(e)

    label = e
    for d in ['-',"="]:
        label = label.split(d)[0]
    box = calc(label)
    inside, i = inlist(label, boxes[box])

    if '-' in e:
        if inside:
            del(boxes[box][i])

    elif '=' in e:
        focal = int(e.split("=")[1])
        if inside:
            boxes[box][i] = (label, focal)
        else:
            boxes[box].append((label, focal))

print(p1)

p2 = 0
for i, box in enumerate(boxes):
    i+=1
    if box:
        ans = 0
        for slot, contents in enumerate(box):
            label, focal = contents
            slot += 1
            ans += (i * slot * focal)
        p2 += ans

print(p2)
