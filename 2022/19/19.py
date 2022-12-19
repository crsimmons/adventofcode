#!/usr/bin/env python3
import sys, re

from cpmpy import *
from math import prod

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

blueprints = []
for l in lines:
    blueprints.append(list(map(int, re.findall("-?\d+", l))))

# mapping resource names to integers
ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3


def solve(bps, STEPS):
    QLEVELS = []
    GLEVELS = []

    for bp in bps:
        (
            index,
            ore_cost,
            clay_cost,
            obsidian_ore_cost,
            obsidian_clay_cost,
            geode_ore_cost,
            geode_obsidian_cost,
        ) = bp

        # costArray[x,y] is the cost of machine x in resource y
        # costArray[1,0] is cost of ore robot in terms of ore (ore_cost)
        # first row is cost of not building anything
        costArray = cpm_array(
            [
                [0, 0, 0, 0],
                [ore_cost, 0, 0, 0],
                [clay_cost, 0, 0, 0],
                [obsidian_ore_cost, obsidian_clay_cost, 0, 0],
                [geode_ore_cost, 0, geode_obsidian_cost, 0],
            ]
        )

        # shape is the dimensional size of the array
        # a 'single' variable has shape 1
        # shape=(4, STEPS+1) means it is a 4 x STEPS+1 matrix
        # we use STEPS+1 so we can have starting values at time=0
        # there's 4 types of resources and 4 types of bots
        # so these variables represent arrays of the amount of bots/resources per step per type
        # var[x,y] -> amount of resource x in step y
        botsPerStep = intvar(0, 9999, shape=(4, STEPS + 1), name="bots")
        resourcesPerStep = intvar(0, 9999, shape=(4, STEPS + 1), name="resources")

        # what is being built each step
        # -1 means we aren't building anything
        # x: [0-3] means we are building a robot to harvest resource type x per step
        # buildingPerStep[step] + 1 -> 0 <= y <= 4
        # this is then used to select the appropriate row of costArray to determine how much this construction costs
        buildingPerStep = intvar(-1, 3, shape=(STEPS + 1), name="building")

        bpModel = Model()

        # CONSTRAINTS
        for resource in range(4):
            # at time=0 we start with 1 ore robot (resource == ORE)
            bpModel += botsPerStep[resource, 0] == (1 if resource == ORE else 0)
            # at time=0 we start with 0 resources
            bpModel += resourcesPerStep[resource, 0] == 0

            for step in range(1, STEPS + 1):
                # Don't spend resources before you have them
                # The resources at the end of the previous step must be greater or equal to
                # the amount of resources spent this step
                # This is because resources are spent at the start of the step
                bpModel += (
                    resourcesPerStep[resource, step - 1]
                    >= costArray[buildingPerStep[step] + 1, resource]
                )

                # Resources this step =
                # Resources in previous step
                # + generation from bots (each one generates 1 resource/step)
                # - cost of building new robots
                bpModel += (
                    resourcesPerStep[resource, step]
                    == resourcesPerStep[resource, step - 1]
                    + botsPerStep[resource, step - 1]
                    - costArray[buildingPerStep[step] + 1, resource]
                )

                # Robots this step =
                # Robots in previous step
                # + 1 if a robot is built this step
                bpModel += botsPerStep[resource, step] == (
                    botsPerStep[resource, step - 1]
                ) + (buildingPerStep[step] == resource)

        # OBJECTIVE
        bpModel.maximize(resourcesPerStep[GEODE][STEPS])

        if bpModel.solve():
            QLEVELS.append(index * resourcesPerStep[GEODE][STEPS].value())
            GLEVELS.append(resourcesPerStep[GEODE][STEPS].value())
        else:
            print("failed to solve")
            exit(1)
    return QLEVELS, GLEVELS


p1, _ = solve(blueprints, 24)
print(sum(p1))

_, p2 = solve(blueprints[:3], 32)
print(prod(p2))
