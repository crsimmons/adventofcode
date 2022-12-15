#!/usr/bin/env python3
import sys
import re

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

intervals = []

Y = 2000000
beacons = set()
sensors = set()

# check if a give set of (x,y) coords are beyond the distance to the closest
# beacon for each sensor in s (i.e. valid placement for a beacon)
def valid(x, y, s):
    for (sx, sy, d) in s:
        dxy = abs(x - sx) + abs(y - sy)
        if dxy <= d:
            return False
    return True


for l in lines:
    sx, sy, bx, by = map(int, re.findall("-?\d+", l))

    # manhattan distance
    d = abs(sx - bx) + abs(sy - by)

    sensors.add((sx, sy, d))

    radius = d - abs(sy - Y)
    if radius < 0:
        # sensor range doesn't touch target row
        continue

    for x in range(sx - radius, sx + radius + 1):
        beacons.add(x)

    if by == Y:
        beacons.remove(bx)
    if sy == Y:
        beacons.remove(sx)

print(len(beacons))

M = 4000000

for (sx, sy, d) in sensors:
    # look at each point that lies d+1 from the sensor
    for dx in range(d + 1 + 1):
        dy = (d + 1) - dx
        # get each (x,y) that lies on each edge of the d+1 diamond
        for signx, signy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            x = sx + (dx * signx)
            y = sy + (dy * signy)
            # skip if outside boundary box
            if not (0 <= x <= M and 0 <= y <= M):
                continue
            # solution is point where (x,y) lies:
            # - within the box
            # - d+1 away from this sensor
            # - at least d+1 away from any other sensor
            if valid(x, y, sensors):
                print(x * M + y)
                exit(0)
