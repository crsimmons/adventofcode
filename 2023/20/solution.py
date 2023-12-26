#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys
from collections import deque
from math import lcm

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

class Module:
    def __init__(self, name, type, destinations):
        self.name = name
        self.type = type
        self.destinations = destinations

        # flip-flop modules are initially off
        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}

    def __repr__(self):
        return self.name + "{type=" + self.type + ",outputs=" + ",".join(self.destinations) + ",memory=" + str(self.memory) + "}"


modules = {}
broadcast_targets = []

for l in L:
    src, dests = l.split(" -> ")
    dests = dests.split(", ")
    if src == 'broadcaster':
        broadcast_targets = dests
    else:
        type = src[0]
        name = src[1:]
        modules[name] = Module(name, type, dests)

# Conjunction modules default to remembering lo for all inputs
for name, module in modules.items():
    for dest in module.destinations:
        if dest in modules and modules[dest].type == "&":
            modules[dest].memory[name] = "lo"

# print(modules)

# Say &ab -> rx AND &x -> ab, &y -> ab etc
# For a low pulse to be sent to rx ab must receive high pulses from x and y
# For this to happen, x and y must be getting low inputs.
# assumptions about the input
# - only one node leads to rx and it is a conjuction
# - all nodes leading to that node are also conjunctions
# - &ab receives a high from all its inputs on the same cycle
(rx_source,) = [name for name, module in modules.items() if "rx" in module.destinations]

# dict to track how many times each input to rx_source has been seen
seen = {name: 0 for name, module in modules.items() if rx_source in module.destinations}

# how many presses between 'hi' signals for each module
cycle_lengths = {}

lo = hi = 0
t = 0
while True:
    t += 1
    lo += 1
    Q = deque([("broadcaster", x, "lo") for x in broadcast_targets])

    while Q:
        src, target, signal = Q.popleft()

        if signal == "hi":
            hi += 1
        else:
            lo += 1

        if target not in modules:
            continue

        # get module receiving the signal
        module = modules[target]

        # target is the module that feeds into rx and src is sending 'hi' signal
        if module.name == rx_source and signal == "hi":
            seen[src] += 1

            if src not in cycle_lengths:
                cycle_lengths[src] = t
            else:
                # if we've already seen src sending a 'hi' signal
                # then we're assuming the cycle has repeated
                assert t == seen[src] * cycle_lengths[src]

            # once we've seen all the inputs to rx_source sending 'hi' signals
            # we can calculate the lcm of them which is the number of presses
            # needed for all of them to be sending 'hi' at the same time
            if all(seen.values()):
                print(lcm(*list(cycle_lengths.values())))
                exit(0)

        if module.type == "%":
            # If a flip-flop module receives a high pulse, it is ignored and nothing happens.
            if signal == "hi":
                continue
            else:
                # if a flip-flop module receives a low pulse, it flips between on and off
                module.memory = "on" if module.memory == "off" else "off"
                # If it was off, it sends a high pulse. If it was on, it sends a low pulse.
                output = "hi" if module.memory == "on" else "lo"
                for d in module.destinations:
                    Q.append((module.name, d, output))
        else:
            # if it remembers high pulses for all inputs, it sends a low pulse
            # otherwise, it sends a high pulse
            module.memory[src] = signal
            output = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
            for d in module.destinations:
                Q.append((module.name, d, output))
    if t == 1000:
        print(lo*hi)
