import networkx as nx
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

def csv_val_reader(infile):
    """
    names = []
    with open(infile,newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=',',quotechar="|")
        for row in reader:
            names.append(row[0])
        csvfile.seek(0)
        adj_matrix = pd.DataFrame(columns=names,index=names,dtype='float64')        #Make a matrix  with the rows and columns as the names of the currencies. 
        k=0
        for row in reader:
            for i in range(1,len(row)):
                try:
                    adj_matrix[names[i-1]][row[0]] = float(row[i])         #names[i-1] will be the names of the currency and row will be the currnecy we are currently looking at.
                except KeyError:
                    print(f"Error for {names[i-1]}/{row[0]} rate ")
                    continue
            k+=1
    """
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