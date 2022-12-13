#!/usr/bin/env python3
import sys
from copy import deepcopy

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile).read().strip()

Monkey = []
OP = []
TEST = []
TRUE = []
FALSE = []
for monkey in data.split("\n\n"):
    num, items, op, test, true, false = monkey.split("\n")
    Monkey.append([int(i) for i in items.split(":")[1].split(",")])
    words = op.split()
    op = "".join(words[-3:])
    OP.append(eval("lambda old:" + op))
    TEST.append(int(test.split()[-1]))
    TRUE.append(int(true.split()[-1]))
    FALSE.append(int(false.split()[-1]))

lcm = 1
for x in TEST:
    lcm *= x

for part in [1, 2]:
    M = deepcopy(Monkey)
    COUNT = [0 for _ in range(len(M))]
    for _ in range(20) if part == 1 else range(10000):
        for m in range(len(M)):
            for item in M[m]:
                COUNT[m] += 1
                item = OP[m](item)
                if part == 1:
                    item //= 3
                else:
                    item %= lcm
                if item % TEST[m] == 0:
                    M[TRUE[m]].append(item)
                else:
                    M[FALSE[m]].append(item)
            M[m] = []
    print(sorted(COUNT)[-1] * sorted(COUNT)[-2])
