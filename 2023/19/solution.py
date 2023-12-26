#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()

workflows, parts = D.split("\n\n")

W = {}
for workflow in workflows.splitlines():
    name, steps = workflow.split("{")
    steps = steps.strip("}").split(",")
    W[name] = steps


def accepted(part):
    state = 'in'
    x, m, a, s = part

    while True:
        if state == 'A':
            return True
        if state == 'R':
            return False

        workflow = W[state]
        for cmd in workflow:
            result = cmd
            if ':' in cmd:
                cond, result = cmd.split(':')
                if eval(cond):
                    state=result
                    break
            else:
                state = result


ans = 0
for part in parts.splitlines():
    part = part[1:-1]
    part = tuple(nums(part))
    if accepted(part):
        ans += sum(part)
print(ans)


def count(state, ranges):
    if state == 'R':
        return 0
    if state == 'A':
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product

    workflow = W[state]

    total = 0
    for cmd in workflow:
        result = cmd
        if ":" in cmd:
            cond, result = cmd.split(":")
            key = cond[0]
            op = cond[1]
            n = int(cond[2:])
            lo, hi = ranges[key]
            lo, hi, alo, ahi = split_range(op, n, lo, hi)
            alt = dict(ranges)
            alt[key] = (lo, hi)
            total += count(result, alt)
            ranges[key] = (alo, ahi)
        else:
            total += count(result, ranges)
    return total

ans = 0
ranges = {key: (1, 4000) for key in "xmas"}

print(count('in', ranges))
