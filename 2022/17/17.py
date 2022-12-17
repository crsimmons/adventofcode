#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile).read().strip()

# Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).
def get_rock(n, y):
    if n == 0:
        # ####
        return set([(2, y), (3, y), (4, y), (5, y)])
    if n == 1:
        # .#.
        # ###
        # .#.
        return set([(3, y + 2), (2, y + 1), (3, y + 1), (4, y + 1), (3, y)])
    if n == 2:
        # ..#
        # ..#
        # ###
        return set([(4, y + 2), (4, y + 1), (2, y), (3, y), (4, y)])
    if n == 3:
        # #
        # #
        # #
        # #
        return set([(2, y + 3), (2, y + 2), (2, y + 1), (2, y)])
    if n == 4:
        # ##
        # ##
        return set([(2, y + 1), (3, y + 1), (2, y), (3, y)])


def shift_left(rock):
    if any([x == 0 for (x, y) in rock]):
        return rock
    return set([(x - 1, y) for (x, y) in rock])


def shift_right(rock):
    if any([x == 6 for (x, y) in rock]):
        return rock
    return set([(x + 1, y) for (x, y) in rock])


def shift_down(rock):
    return set([(x, y - 1) for (x, y) in rock])


def shift_up(rock):
    return set([(x, y + 1) for (x, y) in rock])


# set showing top 30 rows of cave
def top_pattern(C):
    maxY = max([y for (_, y) in C])
    return frozenset([(x, maxY - y) for (x, y) in C if maxY - y <= 30])


def show(C):
    maxY = max([y for (_, y) in C])
    for y in range(maxY, 0, -1):
        row = ""
        for x in range(7):
            if (x, y) in C:
                row += "#"
            else:
                row += "."
        print(row)


CAVE = set([(x, 0) for x in range(7)])

top = 0
n = 0
i = 0
added = 0

N = 1000000000000

SEEN = {}

while n < N:
    # The floor is one line lower than I originally thought
    # so the rock starts at top + 4 rather than +3
    rock = get_rock(n % 5, top + 4)

    while True:
        if data[i] == "<":
            rock = shift_left(rock)
            if rock & CAVE:
                rock = shift_right(rock)
        else:
            rock = shift_right(rock)
            if rock & CAVE:
                rock = shift_left(rock)
        i = (i + 1) % len(data)
        rock = shift_down(rock)
        if rock & CAVE:
            rock = shift_up(rock)
            CAVE |= rock
            top = max([y for (_, y) in CAVE])

            key = (n % 5, i, top_pattern(CAVE))
            if key in SEEN and n >= 2022:
                (prev_n, prev_top) = SEEN[key]
                top_per_cycle = top - prev_top
                rocks_per_cycle = n - prev_n

                # number of times this cycle can occur
                cycle_repeats = (N - n) // rocks_per_cycle

                # amount to add to top by repeating cycle =
                # times we apply this cycle * increase to top per cycle
                added += cycle_repeats * top_per_cycle

                # number of rocks dropped =
                # number of rocks dropped to this point + (
                # times we apply this cycle * rocks that drop per cycle
                # )
                n += cycle_repeats * rocks_per_cycle
            SEEN[key] = (n, top)
            break
    n += 1
    if n == 2022:
        print(top)

print(top + added)
