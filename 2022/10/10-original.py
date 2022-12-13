#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

D = [["?" for _ in range(40)] for _ in range(6)]


def signal(n):
    X = 1
    v = 0
    i = 0
    d = 0
    skip = False
    for c in range(1, n + 1):
        if c >= n:
            break
        D[d // 40][d % 40] = "#" if abs(X - (d % 40)) <= 1 else " "
        d += 1
        ins = lines[i]
        if i + 1 > len(lines):
            i = 0
        if ins == "noop":
            i += 1
        elif skip:
            X += v
            skip = False
            i += 1
        else:
            v = int(ins.split()[1])
            skip = True
    return X * n


# print(signal(20) + signal(60) + signal(100) + signal(140) + signal(180) + signal(220))
signal((40 * 6) + 1)
for y in range(6):
    print("".join(D[y]))
