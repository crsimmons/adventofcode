#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import Counter

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

def mix(s, n):
    return n ^ s


def prune(s):
    return s % 16777216


def step(s):
    # * 64
    s = prune(mix(s << 6, s))
    # // 32
    s = prune(mix(s >> 5, s))
    # * 2048
    s = prune(mix(s << 11, s))
    return s


def build_sell_map(prices):
    c = Counter()

    deltas = [b - a for a, b in zip(prices, prices[1:])]

    for i in range(len(prices)):
        if i + 4 >= len(deltas):
            break
        key = tuple(deltas[i + dd] for dd in range(4))
        if key in c:
            continue
        c[key] = prices[i + 4]

    return c


sellers = []
p1 = 0
for l in L:
    s = int(l)
    prices = [(s % 10)]
    for i in range(2000):
        ns = step(s)
        prices.append((ns % 10))
        s = ns
    p1 += s
    sellers.append(prices)

print(p1)

c = Counter()
for prices in sellers:
    c += build_sell_map(prices)

print(max(c.values()))
