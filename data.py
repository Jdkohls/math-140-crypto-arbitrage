import networkx as nx
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import requests
import json


def get_request_cc(*argv):
    currency = ""
    for i in argv:
        currency += i
        currency += ','
    currency = currency[:-1:]
    with open("secret","r") as file:
        auth_key = file.readlines()
        r = requests.get(f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={currency}&tsyms={currency}&api_key={auth_key[0]}")
    return r


def parse_request(r):
    exchange_dict = r.json()
    #print(exchange_dict)
    names = [key for key in exchange_dict]
    adj_matrix = pd.DataFrame(columns=names,index=names, dtype='float64')
    for key in exchange_dict:
        for value in exchange_dict[key]:
            try:
                adj_matrix[key][value] = exchange_dict[value][key] 
            except KeyError:
                    print(f"Error for {key}/{value} rate ")
                    continue
    #print(adj_matrix)
    graph = nx.DiGraph(-np.log(adj_matrix).fillna(0).T)
    return graph

def csv_val_reader(infile):
    adj_matrix = pd.read_csv(infile, header=0, index_col=0)
    graph = nx.DiGraph(-np.log(adj_matrix).fillna(0).T)
    #print(-np.log(adj_matrix).fillna(0).T)
    return graph


def image_graph(outfile,graph, circular = True):
    pos = nx.random_layout(graph)
    if circular:
        pos = nx.circular_layout(graph)

    nx.draw(graph,pos, with_labels = True)
    labels = nx.get_edge_attributes(graph,'weight')
    labels = {key:'%.3f'%labels[key] for key in labels}
    #print(labels)
    nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
    plt.savefig(outfile)

#