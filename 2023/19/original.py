#!/usr/bin/env python3
import sys
from collections import deque

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
workflows, parts = open(inputfile).read().strip().split("\n\n")

W = {}
for workflow in workflows.splitlines():
    name, steps = workflow.split("{")
    steps = steps.strip("}").split(",")
    W[name] = steps

def accepted(part):
    state = 'in'

    while True:
        workflow = W[state]
        for cmd in workflow:
            applies = True
            result = cmd
            if ':' in cmd:
                cond, result = cmd.split(':')
                var = cond[0]
                op = cond[1]
                n = int(cond[2:])
                if op == ">":
                    applies = part[var] > n
                elif op == "<":
                    applies = part[var] < n
                else:
                    assert False
            if applies:
                if result == "A":
                    return True
                if result == "R":
                    return False
                state = result
                break

def new_range(op, n, lo, hi):
    if op == ">":
        lo = max(lo, n + 1)
    elif op == "<":
        hi = min(hi, n - 1)
    elif op=='>=':
        lo = max(lo, n)
    elif op=='<=':
        hi = min(hi, n)
    else:
        assert False
    return (lo, hi)

def new_ranges(var, op, n, xl, xh, ml, mh, al, ah, sl, sh):
    if var == 'x':
        xl, xh = new_range(op, n, xl, xh)
    elif var == 'm':
        ml, mh = new_range(op, n, ml, mh)
    elif var == 'a':
        al, ah = new_range(op, n, al, ah)
    elif var == 's':
        sl, sh = new_range(op, n, sl, sh)
    return (xl, xh, ml, mh, al, ah, sl, sh)

ans = 0
for part in parts.splitlines():
    part = part[1:-1]
    part = {x.split('=')[0]:int(x.split('=')[1]) for x in part.split(',')}
    if accepted(part):
        ans += part['x']+part['m']+part['a']+part['s']
print(ans)

ans = 0
Q = deque([('in', 1, 4000, 1, 4000, 1, 4000, 1, 4000)])
while Q:
    state, xl, xh, ml, mh, al, ah, sl, sh = Q.popleft()
    if xl > xh or ml > mh or al > ah or sl > sh or state == 'R':
        continue
    if state == 'A':
        score = (xh-xl+1)*(mh-ml+1)*(ah-al+1)*(sh-sl+1)
        ans += score
        continue
    else:
        workflow = W[state]
        for cmd in workflow:
            result = cmd
            if ':' in cmd:
                cond, result = cmd.split(':')
                var = cond[0]
                op = cond[1]
                n = int(cond[2:])

                Q.append((result, *new_ranges(var, op, n, xl, xh, ml, mh, al, ah, sl, sh)))
                xl,xh,ml,mh,al,ah,sl,sh = new_ranges(var, '<=' if op=='>' else '>=', n, xl, xh, ml, mh, al, ah,sl, sh)
            else:
                Q.append((result, xl, xh, ml, mh, al, ah, sl, sh))
                break
print(ans)
