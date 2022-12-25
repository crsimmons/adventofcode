#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

E = set()

for r, l in enumerate(lines):
    for c, e in enumerate(l):
        if e == "#":
            E.add(r + c * 1j)

SCAN = {
    -1: [-1 - 1j, -1, -1 + 1j],
    1: [1 - 1j, 1, 1 + 1j],
    -1j: [-1 - 1j, -1j, 1 - 1j],
    1j: [-1 + 1j, 1j, 1 + 1j],
}

MOVES = [-1, 1, -1j, 1j]
ALL = [1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]

i = 1
while True:
    once = set()
    twice = set()
    free = set()

    for e in E:
        if all(e + x not in E for x in ALL):
            free.add(e)
            continue
        for m in MOVES:
            if all(e + x not in E for x in SCAN[m]):
                p = e + m
                if p in twice:
                    pass
                elif p in once:
                    twice.add(p)
                else:
                    once.add(p)
                break

    if len(free) == len(E):
        break

    ec = set(E)

    for e in ec:
        if all(e + x not in ec for x in ALL):
            continue
        for m in MOVES:
            if all(e + x not in ec for x in SCAN[m]):
                p = e + m
                if p not in twice:
                    E.remove(e)
                    E.add(p)
                break

    MOVES.append(MOVES.pop(0))

    if i == 10:
        mr = min(x.real for x in E)
        Mr = max(x.real for x in E)
        mc = min(x.imag for x in E)
        Mc = max(x.imag for x in E)

        mr, Mr, mc, Mc = map(int, [mr, Mr, mc, Mc])

        print((Mr - mr + 1) * (Mc - mc + 1) - len(E))

    i += 1

print(i)
