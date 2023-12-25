#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import defaultdict, deque

import lib.grid as grid
from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

G = grid.FixedGrid.parse(D)
R = G.height
C = G.width

inputs, *sections = D.split("\n\n")

# part 1

seeds = nums(inputs)

for section in sections:
    ranges = []
    next_input = []
    for line in section.splitlines()[1:]:
        ranges.append(nums(line))
    for seed in seeds:
        for destination, source, count in ranges:
            if seed in range(source, source + count):
                next_input.append(seed - source + destination)
                break
        else:
            next_input.append(seed)
    seeds = next_input

print(min(seeds))

# part 2

seeds = nums(inputs)

seedranges = []

for i in range(0, len(seeds), 2):
    seedranges.append((seeds[i], seeds[i] + seeds[i + 1]))

for section in sections:
    ranges = []
    next_input = []
    for line in section.splitlines()[1:]:
        ranges.append(nums(line))

    while len(seedranges) > 0:
        start, end = seedranges.pop()
        for destination, source, count in ranges:
            # looking for the overlap of this range and the seed range
            # the start will be the max of the start of the seed range
            # and the start of the source range
            overlap_start = max(start, source)
            # and the end will be the min of the end of the seed range
            # and the end of the source range (source + count)
            overlap_end = min(end, source + count)
            # if the overlap exists
            if overlap_start < overlap_end:
                # add the mapped destination range to the next input
                next_input.append((overlap_start - source + destination, overlap_end - source + destination))
                # if part of the seeds range hasn't been mapped we need
                # to add the remaining segments to be evaluated against
                # other ranges
                if overlap_start > start:
                    seedranges.append((start, overlap_start))
                if overlap_end < end:
                    seedranges.append((overlap_end, end))
                break
        else:
            next_input.append((start, end))
    seedranges = next_input

print(min(seedranges)[0])
