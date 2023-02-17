import networkx as nx
import numpy as np
import pandas as pd
import csv

import bellman
import data

#Step 1: prepare data
graph = data.csv_val_reader('Exchange Rates.csv')
data.image_graph("graph.png",graph,True)
print("Done running!")

#Step 2: Bellman ford
cycles = bellman.all_negative_cycles(graph)
print(cycles)
#Step 3: interpret

"""
while(true)
    wait 5 seconds
    graph = call_api function
    loops = bellmanford(graph)
    print loops
"""