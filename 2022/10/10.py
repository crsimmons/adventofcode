#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

D = [[" " for _ in range(40)] for _ in range(6)]
p1 = 0


def tick(x, t):
    global p1
    global D
    d = t - 1
    if abs(X - (d % 40)) <= 1:
        D[d // 40][d % 40] = "#"
    if t in [20, 60, 100, 140, 180, 220]:
        p1 += x * t


X = 1
t = 0
for l in lines:
    if l == "noop":
        t += 1
        tick(X, t)
    else:
        t += 1
        tick(X, t)
        t += 1
        tick(X, t)
        X += int(l.split()[1])

print(p1)
for y in range(6):
    print("".join(D[y]))
