#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

A = []

for i, l in enumerate(lines):
    A.append(int(l))


def mix(A, n=1):
    l = len(A)
    # A is the original list
    # B holds the indexes of the elements in A as they mix
    B = [i for i in range(l)]
    for _ in range(n):
        # for each pass of the original list A:
        #   for each (i,e) in A:
        #       current index (ci) of e in mixed list is the index of i in B
        #       remove i from B
        #       calculate new index (ni) as ci + e mod the length of the list
        #       add ni to B at index i
        #
        # by the end of a pass B has had one insertion per index in A
        for i, e in enumerate(A):
            # i is index of current element
            # e is value of current element
            if e == 0:
                continue
            # ci is current index of e in the mixed list
            ci = B.index(i)
            # remove the current index from B
            B.pop(ci)
            # ni is the new index of e in the mixed list
            ni = (ci + e) % (len(A) - 1)
            # add the new index to B before index i
            B.insert(ni, i)
    return [A[i] for i in B]


def grove(A):
    l = len(A)
    s = 0
    for n in [1000, 2000, 3000]:
        s += A[(A.index(0) + n) % l]
    return s


print(grove(mix(A)))

key = 811589153

A = [i * key for i in A]
print(grove(mix(A, 10)))
