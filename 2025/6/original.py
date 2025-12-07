#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import itertools
import operator
import sys
from functools import reduce

from lib.util import *

sys.setrecursionlimit(10**6)

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
lines = D.split("\n")
# Keep raw lines for part 2, use split for part 1
split_lines = [line.split() for line in lines]
C = len(split_lines[0])
R = len(split_lines)

ops = split_lines[R - 1]

p1 = 0
p2 = 0

def digits2int(digits):
    return int("".join(str(d) for d in digits))


def extract_vertical_numbers(matrix):
    """Extract vertical numbers from character matrix.

    Spaces in the input indicate alignment - characters are transposed
    as-is, then spaces are filtered out to get the vertical numbers.
    """
    sentinel = object()
    transposed = [
        [val for val in col if val is not sentinel and val != " "]
        for col in itertools.zip_longest(*matrix, fillvalue=sentinel)
    ]
    return transposed[::-1]


def calc(nums, op):
    if op == "*":
        return reduce(operator.mul, nums, 1)
    elif op == "+":
        return reduce(operator.add, nums, 0)


for c in range(C):
    p1_nums = []
    for r in range(R - 1):
        p1_nums.append(int(split_lines[r][c]))

    op = ops[c]

    p1 += calc(p1_nums, op)

# For part 2, we need to parse by character positions to preserve alignment
# First, find column boundaries (positions that are all spaces)
max_len = max(len(line) for line in lines[: R - 1])
padded_lines = [line.ljust(max_len) for line in lines[: R - 1]]

# Find separator positions (all spaces vertically)
separators = []
for pos in range(max_len):
    if all(line[pos] == " " for line in padded_lines):
        separators.append(pos)

# Extract problems (ranges between separators)
problems = []
start = 0
for sep in separators:
    if sep > start:
        problems.append((start, sep))
    start = sep + 1
if start < max_len:
    problems.append((start, max_len))

# Process each problem
for prob_idx, (start_pos, end_pos) in enumerate(problems):
    chars = []
    for r in range(R - 1):
        line = padded_lines[r]
        problem_str = line[start_pos:end_pos]
        chars.append(list(problem_str))

    p2_nums = [digits2int(x) for x in extract_vertical_numbers(chars)]
    op = ops[prob_idx]
    result = calc(p2_nums, op)
    p2 += result

print("Part 1:", p1)
print("Part 2:", p2)
