#!/usr/bin/env python3

import sys

import networkx as nx

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
starting_values, connections = open(inputfile).read().strip().split("\n\n")

BITOP = {"AND": "&", "OR": "|", "XOR": "^"}

gates = {}

for line in starting_values.splitlines():
    gate, value = line.split(": ")
    gates[gate] = int(value)

G = nx.DiGraph()

for line in connections.splitlines():
    inputs, output_gate = line.split(" -> ")  # "tgd XOR rvg" "z01"
    input_one, logic, input_two = inputs.split()
    G.add_edge(input_one, output_gate, type=BITOP[logic])
    G.add_edge(input_two, output_gate, type=BITOP[logic])


def simulate_graph(graph, gate_values):
    values = gate_values.copy()
    while not len(values) == len(G.nodes()):
        for node in G.nodes():
            if G.in_degree(node) == 2 and values.get(node) is None:
                inputs = []
                for nbr, datadict in G.pred[node].items():
                    inputs.append(nbr)
                if (
                    values.get(inputs[0]) is not None
                    and values.get(inputs[1]) is not None
                ):
                    values[node] = eval(
                        str(values.get(inputs[0]))
                        + datadict["type"]
                        + str(values.get(inputs[1]))
                    )

    return values


def get_num(letter):
    nodes = sorted(
        [node for node in G.nodes if node.startswith(letter)],
        key=lambda x: int(x[1:]),
    )
    return int("".join(str(gates[node]) for node in nodes[::-1]), 2)


def find_diff_bits(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    return [
        i + 1
        for i, bit in enumerate(bin((int(a, 2) ^ int(b, 2)))[2:].zfill(max_len))
        if bit == "1"
    ]


original_values = simulate_graph(G, gates)

z_nodes = sorted(
    [node for node in G.nodes if node.startswith("z")], key=lambda x: int(x[1:])
)

z = int("".join(str(original_values[node]) for node in z_nodes[::-1]), 2)

print(z)
