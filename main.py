import networkx as nx
import numpy as np
import pandas as pd
import csv


import bellman
import data

#Step 1: prepare data
coinlist = ["ETH","BTC","XRP","USDT","LTC","ADA","LINK","BUSD","DOT","APT","BNB","CFX","T","SOL","GMT","EOS"]
r = data.get_request_cc(*coinlist)
g = data.parse_request(r)

#g = data.csv_val_reader("Exchange rates.csv")


#Step 2: Bellman ford

cycles = bellman.all_negative_cycles(g)
print(cycles)

#Step 3: interpret





#print(r.json())

"""
while(true)
    wait 5 seconds
    graph = call_api function
    loops = bellmanford(graph)
    print loops
"""