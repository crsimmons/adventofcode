#!/usr/bin/env python3
import sys

from copy import deepcopy

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

CODE = list(map(int, lines[0].split(",")))


def params(c, ins, i):
    ins = list(str(ins))

    paramter_modes = ([0] * (5 - len(ins))) + ins

    param1 = c[i + 1] if int(paramter_modes[2]) == 0 else (i + 1)
    param2 = c[i + 2] if int(paramter_modes[1]) == 0 else (i + 2)
    param3 = c[i + 3] if int(paramter_modes[0]) == 0 else (i + 3)

    return param1, param2, param3


def solve(c, inp):
    i = 0
    while i < len(c):
        e = str(c[i])
        ins = int(e[-2:])
        p1, p2, p3 = params(c, e, i)
        if ins == 99:
            break
        elif ins == 1:
            c[p3] = c[p1] + c[p2]
            i += 4
        elif ins == 2:
            c[p3] = c[p1] * c[p2]
            i += 4
        elif ins == 3:
            c[p1] = inp
            i += 2
        elif ins == 4:
            if c[p1] != 0 and c[i + 2] == 99:
                print(c[p1])
                break
            elif c[p1] != 0 and c[i + 2] != 99:
                assert False, c[p1]
            else:
                i += 2
        elif ins == 5:
            if c[p1] != 0:
                i = c[p2]
            else:
                i += 3
        elif ins == 6:
            if c[p1] == 0:
                i = c[p2]
            else:
                i += 3
        elif ins == 7:
            if c[p1] < c[p2]:
                c[p3] = 1
            else:
                c[p3] = 0
            i += 4
        elif ins == 8:
            if c[p1] == c[p2]:
                c[p3] = 1
            else:
                c[p3] = 0
            i += 4
        else:
            i += 1
    return c


ins = deepcopy(CODE)
solve(ins, 1)
ins = deepcopy(CODE)
solve(ins, 5)
