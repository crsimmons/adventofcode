#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = list(map(int, D))

A = []
B = []
G = []
j = 0
k = 0
for i, n in enumerate(L):
    if i % 2 == 0:
        A.extend([j] * n)
        B.extend([(j, k, n)])
        j += 1
    else:
        A.extend([-1] * n)
        G.extend([(k, n)])
    k += n


def part1(lst):
    i, j = 0, len(lst) - 1
    while i < j:
        while i < len(lst) and lst[i] != -1:
            i += 1
        while j >= 0 and lst[j] == -1:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], -1
            i += 1
            j -= 1
    return lst


def part2(blocks, gaps):
    blocks = sorted(blocks, key=lambda x: -x[0])

    updated_blocks = blocks[:]

    for block_index, (_id, pos, l) in enumerate(blocks):
        for j, (gi, gl) in enumerate(gaps):
            if gl >= l and gi < pos:
                updated_blocks[block_index] = (_id, gi, l)
                gaps[j] = (gi + l, gl - l)
                break

    return sorted(updated_blocks, key=lambda x: x[1])


p1 = 0
for i, n in enumerate(part1(A)):
    if n != -1:
        p1 += i * n

print(p1)

p2 = 0
for v, s, l in part2(B, G):
    for i in range(s, s + l):
        p2 += v * i

print(p2)
