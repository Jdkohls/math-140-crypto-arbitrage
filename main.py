import networkx as nx
import numpy as np
import pandas
import csv

import bellman
import data

#Step 1: prepare data
graph = data.csv_val_reader('Exchange rates.csv')
data.image_graph("graph.png",graph)

#Step 2: Bellman ford

#Step 3: interpret
