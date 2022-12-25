#!/usr/bin/env python3
import sys

from sympy import symbols, solve, Integer

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]


def calc(A, op):
    while True:
        if len(op.split()) == 1:
            return int(op)
        assert len(op.split()) == 3
        l, o, r = op.split()
        l = A.pop(l)
        r = A.pop(r)
        return eval("%d %s %d" % (calc(A, l), o, calc(A, r)))


A = {}
for l in lines:
    k, v = l.split(": ")
    A[k] = v

op = A.pop("root")
print(calc(A, op))

M = {"humn": symbols("x")}

ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

for m in lines:
    name, expr = m.split(": ")
    if name in M:
        continue
    if len(expr.split()) == 1:
        M[name] = Integer(expr)
    else:
        l, op, r = expr.split()
        if l in M and r in M:
            if name == "root":
                # print("%s == %s" % (M[l], M[r]))
                if symbols("x") in M[l].free_symbols:
                    print(solve(M[l] - M[r])[0])
                else:
                    print(solve(M[r] - M[l])[0])
                break
            M[name] = ops[op](M[l], M[r])
        else:
            lines.append(m)
