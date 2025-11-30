#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque
from functools import lru_cache

import lib.grid as grid
from lib.util import *

sys.setrecursionlimit(10**6)

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width
