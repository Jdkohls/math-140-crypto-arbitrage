import math
import pandas as pd
from collections import defaultdict
import networkx as nx
import numpy as np

def bellman_ford_return_cycle(g, s):
    n = len(g.nodes())
    d = defaultdict(lambda: math.inf)  # distances dict
    p = defaultdict(lambda: -1)  # predecessor dict
    d[s] = 0

    for _ in range(n - 1):
        for u, v in g.edges():
            # Bellman-Ford relaxation
            weight = g[u][v]["weight"]
            if d[u] + weight < d[v]:
                d[v] = d[u] + weight
                p[v] = u  # update pred

        # Find cycles if they exist
        all_cycles = []
        seen = defaultdict(lambda: False)

        for u, v in g.edges():
            if seen[v]:
                continue
            # If we can relax further there must be a neg-weight cycle
            weight = g[u][v]["weight"]
            if d[u] + weight < d[v]:
                cycle = []
                x = v
                while True:
                    # Walk back along preds until a cycle is found
                    seen[x] = True
                    cycle.append(x)
                    x = p[x]
                    if x == v or x in cycle:
                        break
                # Slice to get the cyclic portion
                idx = cycle.index(x)
                cycle.append(x)
                all_cycles.append(cycle[idx:][::-1])
        return all_cycles


def all_negative_cycles(g):
    all_paths = []
    for v in g.nodes():
        all_paths.append(bellman_ford_return_cycle(g, v))
    flattened = [item for sublist in all_paths for item in sublist]
    return [list(i) for i in set(tuple(j) for j in flattened)]


def calculate_arb(cycle, g, verbose=True):
    total = 0
    for (p1, p2) in zip(cycle, cycle[1:]):
        total += g[p1][p2]["weight"]
    arb = np.exp(-total) - 1
    if verbose:
        print("Path:", cycle)
        print(f"{arb*100:.2g}%\n")
    return arb

"""
def find_arbitrage(filename="snapshot.csv"):
    df = pd.read_csv(filename, header=0, index_col=0)
    g = nx.DiGraph(-np.log(df).fillna(0).T)

    if nx.negative_edge_cycle(g):
        print("ARBITRAGE FOUND\n" + "=" * 15 + "\n")
        for p in all_negative_cycles(g):
            calculate_arb(p, g)
    else:
        print("No arbitrage opportunities")
"""