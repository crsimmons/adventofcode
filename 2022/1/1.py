#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)

elves = "\n".join([l.strip() for l in data]).split("\n\n")
s = []
for elf in elves:
    calories = 0
    for item in elf.split("\n"):
        calories += int(item)
    s.append(calories)

s = sorted(s)

print(s[-1])
print(s[-1] + s[-2] + s[-3])
