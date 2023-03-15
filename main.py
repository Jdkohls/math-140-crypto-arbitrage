import networkx as nx
import numpy as np
import pandas as pd
import csv


import bellman
import data

#Step 1: prepare data       
coinlist = ["ETH","BTC","BUSD","USDT","XRP","LTC","SOL","BNB","INU","APT","DOGE"]
length = 0
for item in coinlist:
    length += len(item)
assert(length <= 50)

print("Getting Data!")
r = data.get_request_cc(*coinlist)
print("Parsing data!")
g = data.parse_request(r)

#g = data.csv_val_reader("Exchange rates.csv")


#Step 2: Bellman ford

print("Finding opportunities!")

cycles = bellman.all_negative_cycles(g)

arb_list = bellman.setify(cycles)
print(f"There are {len(arb_list)} opportunities!")


#Step 3: interpret
bellman.evaluate_arbitrage(g,arb_list)




#print(r.json())

"""
while(true)
    wait 5 seconds
    graph = call_api function
    loops = bellmanford(graph)
    print loops
"""