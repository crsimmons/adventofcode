#!/usr/bin/env python3
import sys

from collections import deque

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

offsets = [
    (0.5, 0, 0),
    (0, 0.5, 0),
    (0, 0, 0.5),
    (-0.5, 0, 0),
    (0, -0.5, 0),
    (0, 0, -0.5),
]
minx = miny = minz = float("inf")
maxx = maxy = maxz = -float("inf")

# the coords of the centres of the cubes of lava
CUBES = set()
# the coords of each face of each cube of lava
FACES = {}

for l in lines:
    x, y, z = coords = tuple(map(int, l.split(",")))
    CUBES.add(coords)

    minx = min(minx, x)
    miny = min(miny, y)
    minz = min(minz, z)

    maxx = max(maxx, x)
    maxy = max(maxy, y)
    maxz = max(maxz, z)

    for dx, dy, dz in offsets:
        key = (x + dx, y + dy, z + dz)
        if key in FACES:
            FACES[key] = 0
        else:
            FACES[key] = 1

print(sum(FACES.values()))

# expand bounding box by 1 on all sides
minx -= 1
miny -= 1
minz -= 1

maxx += 1
maxy += 1
maxz += 1

Q = deque([(minx, miny, minz)])

# AIR will be a list of coords marking the centres of the first layer of air cubes beyond the lava structure
AIR = {(minx, miny, minz)}

# we floodfill from the "bottom left corner" of our bounding box
# if a cube is not already in AIR and is not part of the lava structure (in CUBES) then we add to AIR and look at it's neighbours
# if it is already in AIR or is part of CUBES then we skip
# air pockets are never reached as the floodfill would need to pass over at least one member of CUBE to get there
while Q:
    x, y, z = Q.popleft()

    # we're dealing with cubes rather than FACES so multiply offsets by 2
    for dx, dy, dz in [(x * 2, y * 2, z * 2) for x, y, z in offsets]:
        nx, ny, nz = coords = (x + dx, y + dy, z + dz)

        # if cube is outside bounded box we skip
        if not (minx <= nx <= maxx and miny <= ny <= maxy and minz <= nz <= maxz):
            continue

        # if cube is a known cube or is already known as part of surrounding air with skip
        if coords in CUBES or coords in AIR:
            continue

        AIR.add(coords)
        Q.append(coords)

# FREE is a transformation on AIR containing coords of the FACES of the first layer of air
FREE = set()
for x, y, z in AIR:
    for dx, dy, dz in offsets:
        FREE.add((x + dx, y + dy, z + dz))

# so the intersection between the FACES of the lava structure and the FACES of the first layer of air
# is the external surface area of the structure
print(len(set(FACES) & FREE))
