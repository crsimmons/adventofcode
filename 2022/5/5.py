#!/usr/bin/env python3
import sys
import re
from copy import deepcopy

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)

stacks = []

for l in data:
    if l == "\n":
        break
    # every 4th element of l starting at index 1
    # [ N ]   [
    # 0 1 2 3 4
    stacks.append(l[1::4])

stacks.pop()

# stacks = [' D ', 'NC ', 'ZMP']

# zip(*stacks) gives a list of tuples: first tuple = first element in each list in stacks
# [(' ', 'N', 'Z'), ('D', 'C', 'M'), (' ', ' ', 'P')]
# so here we build a new list of stacks by joining the zip tuples in reverse order
# [['Z', 'N'], ['M', 'C', 'D'], ['P']]
# so the last element in each subarray corresponds to the top of the column
stacks = [list("".join(c).strip()[::-1]) for c in zip(*stacks)]

stacks2 = deepcopy(stacks)

for l in data:
    q, f, t = map(int, re.findall("\\d+", l))
    # add the last q elements from column f to the end of column t (reversed for part 1)
    stacks[t - 1].extend(stacks[f - 1][-q:][::-1])
    stacks[f - 1] = stacks[f - 1][:-q]
    stacks2[t - 1].extend(stacks2[f - 1][-q:])
    stacks2[f - 1] = stacks2[f - 1][:-q]

print("".join([a[-1] for a in stacks]))
print("".join([a[-1] for a in stacks2]))
