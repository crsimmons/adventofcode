#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

p1 = 0
p2 = 0

lookup = {
    'one':"1",
    'two':"2",
    'three':"3",
    'four':"4",
    'five':"5",
    'six':"6",
    'seven':"7",
    'eight':"8",
    'nine':"9",
}

for l in lines:
    p1_digits=[]
    p2_digits=[]
    for i, c in enumerate(l):
        if c.isdigit():
            p1_digits.append(c)
            p2_digits.append(c)

        for k in lookup.keys():
            if l[i:].startswith(k):
                p2_digits.append(str(lookup[k]))

    p1 += int(p1_digits[0]+p1_digits[-1])
    p2 += int(p2_digits[0]+p2_digits[-1])

print(p1)
print(p2)
