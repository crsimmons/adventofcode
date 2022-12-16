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


def dfs(node, time, maxtime, visited, p2):
    memo_key = (node, time, tuple(visited), p2)
    if memo_key in memo:
        return memo[memo_key]

    max_pressure = 0
    next_pressure = 0
    for nxt, dist in graph[node][1].items():
        if nxt not in visited and time + dist + 1 < maxtime:
            next_pressure = (maxtime - time - dist - 1) * graph[nxt][0] + dfs(
                nxt,
                time + dist + 1,
                maxtime,
                visited | set([nxt]),
                p2,
            )
            max_pressure = max(max_pressure, next_pressure)
    # Once you've completed all your moves the elephant can start
    # at this point visited has been populated with whatever valves
    # you have visited so the elephant can't repeat them
    if p2:
        max_pressure = max(max_pressure, dfs("AA", 0, maxtime, visited, 0))

    memo[memo_key] = max_pressure
    return max_pressure


print(dfs("AA", 0, 30, set(), 0))
print(dfs("AA", 0, 26, set(), 1))
