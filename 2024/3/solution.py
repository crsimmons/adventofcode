#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import re
import sys

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()


def part1(l):
    return sum(
        a * b
        for a, b in [
            tuple(match)
            for match in map(nums, re.findall(r"mul\(\d{1,3},\d{1,3}\)", l))
        ]
    )


print(part1(D))


def part2(l):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", l)
    # At the beginning of the **program**, mul instructions are enabled
    enabled = True
    out = 0
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        else:
            if enabled:
                a, b = nums(match)
                out += a * b
    return out


print(part2(D))
