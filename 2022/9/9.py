#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]


def rope(length):
    s = set([(0, 0)])
    r = [[0, 0] for _ in range(length)]
    for (d, c) in (l.split() for l in lines):
        for _ in range(int(c)):
            dx = 1 if d == "R" else -1 if d == "L" else 0
            dy = 1 if d == "U" else -1 if d == "D" else 0

            r[0][0] += dx
            r[0][1] += dy

            for i in range(length - 1):
                h = r[i]
                t = r[i + 1]

                dtx = h[0] - t[0]
                dty = h[1] - t[1]

                if abs(dtx) > 1 or abs(dty) > 1:
                    if dtx == 0:
                        t[1] += dty // 2
                    elif dty == 0:
                        t[0] += dtx // 2
                    else:
                        t[0] += 1 if dtx > 0 else -1
                        t[1] += 1 if dty > 0 else -1
            s.add(tuple(r[-1]))
    return len(s)


print(rope(2))
print(rope(10))
