#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import Counter, defaultdict, deque

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

# TIL about Counter
# def count(s):
#     d = defaultdict(int)
#     for c in s:
#         d[c] += 1
#     return dict(sorted(d.items(), key=lambda x: x[1], reverse=True)[:2])

def score_type(c):
    scores = {
        (5,  ): 7,
        (4, 1): 6,
        (3, 2): 5,
        (3, 1): 4,
        (2, 2): 3,
        (2, 1): 2
    }
    return scores.get(tuple(sorted(c.values(), reverse=True)[:2]), 1)

def strength(hand, part2):
    hand = hand.replace('T',chr(ord('9')+1))
    hand = hand.replace('J',chr(ord('2')-1) if part2 else chr(ord('9')+2))
    hand = hand.replace('Q',chr(ord('9')+3))
    hand = hand.replace('K',chr(ord('9')+4))
    hand = hand.replace('A',chr(ord('9')+5))

    C = Counter(hand)

    if part2:
        for card,_ in C.most_common(2):
            if card != '1':
                C[card]+=C['1']
                del C['1']
                break

    return score_type(C), hand


for part2 in [False, True]:
    H = []

    for l in L:
        h,b = l.split()
        H.append((h,b))

    # tuple comparison checks the first element of the tuple
    # then the second if there's a tie
    H = sorted(H, key=lambda hb:strength(hb[0], part2))

    p = 0
    for i,(h,b) in enumerate(H):
        p += (i+1)*int(b)
    print(p)
