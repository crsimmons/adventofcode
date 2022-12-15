#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile).read().strip()
pairs = data.split("\n\n")
lines = list(map(eval, data.split()))


def compare(l, r):
    if type(l) == int:
        if type(r) == int:
            # in right order l<r so this is <0
            return l - r
        else:
            return compare([l], r)
    elif type(r) == int:
        return compare(l, [r])
    else:
        for a, b in zip(l, r):
            v = compare(a, b)
            # 0 is falsey in Python. !0 is truthy
            if v:
                return v
    # if len(r)<len(l) r will run out of items first
    # which means it's not the right order
    return len(l) - len(r)


p1 = 0
for i, pair in enumerate(pairs):
    l, r = pair.split("\n")
    l = eval(l)
    r = eval(r)
    if compare(l, r) < 0:
        p1 += i + 1
print(p1)

d1 = 1
d2 = 2
for l in lines:
    if compare(l, [[2]]) < 0:
        d1 += 1
        d2 += 1
    elif compare(l, [[6]]) < 0:
        d2 += 1

print(d1 * d2)
