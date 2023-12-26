#!/usr/bin/env python3
# ruff: noqa: F405, F403, E402
import sys

import networkx as nx

from lib.util import *

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
D = open(inputfile).read().strip()
L = D.split("\n")

verts = set()
edges = set()

for l in L:
    a, b = l.split(': ')
    bs = b.split()

    verts.add(a)
    for b in bs:
        verts.add(b)
        edges.add((a, b))

G = nx.Graph()

G.add_nodes_from(verts)
G.add_edges_from(edges)
G.remove_edges_from(nx.minimum_edge_cut(G))

group = [len(c) for c in nx.connected_components(G)]

print(group[0] * group[1])
