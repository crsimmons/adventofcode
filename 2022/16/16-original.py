#!/usr/bin/env python3
import sys, re, itertools, math

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

valves = {}
# valves -> {'AA': (0, {'DD': 1, 'II': 1, 'BB': 1})}
# cur valve: (flow, {connections with initial dist of 1})
# valves[i][j][k] -> i: cur valve / j: 0 for flow, 1 for paths / k: dist of path i-k
for l in lines:
    v, f, *c = re.findall("-?\d+|[A-Z]{2}", l)
    valves[v] = (int(f), {p: 1 for p in c})

# Floyd-Warshall: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
# finds shortest path between each valve
for k, i, j in itertools.product(valves, valves, valves):
    if i != j and j != k and k != i and k in valves[i][1] and j in valves[k][1]:
        valves[i][1][j] = min(
            valves[i][1].get(j, math.inf), valves[i][1][k] + valves[k][1][j]
        )

# Remove valves with 0 flow other than AA
# doing it in place was hurting my brain so I make a new graph
graph = {}
for valve, valve_info in valves.items():
    flow, paths = valve_info
    if flow != 0 or valve == "AA":
        graph[valve] = (flow, {k: v for k, v in paths.items() if valves[k][0] != 0})

memo = {}


def dfs(node, time, pressure, maxtime, visited, p2):
    print(node, time, pressure, visited)
    global max_pressure
    max_pressure = max(max_pressure, pressure)
    for nxt, dist in graph[node][1].items():
        if nxt not in visited and time + dist + 1 < maxtime:
            dfs(
                nxt,
                time + dist + 1,
                pressure + (maxtime - time - dist - 1) * graph[nxt][0],
                maxtime,
                visited | set([nxt]),
                p2,
            )
    if p2:
        dfs(visited, "AA", 0, pressure, maxtime, 0)


max_pressure = 0
dfs("AA", 0, 0, 30, set(), 0)
# print(max_pressure)

max_pressure = 0
# dfs("AA", 0, 0, 26, set(), 1)
# print(max_pressure)
