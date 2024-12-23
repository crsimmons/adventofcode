#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

import networkx as nx

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

conns = []

for l in L:
    (a, b) = l.split("-")
    conns.append((a, b))

G = nx.Graph()
G.add_edges_from(conns)

cliques = list(nx.enumerate_all_cliques(G))

triangles = [clique for clique in cliques if len(clique) == 3]

print(
    sum(1 for triangle in triangles if any(node.startswith("t") for node in triangle))
)

print(
    ",".join(
        sorted(
            max(
                cliques,
                key=len,
            )
        )
    )
)
