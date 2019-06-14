#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import scipy
import pandas
import numpy as np
import networkx as nx
import pygraphviz as pgv
from IPython.display import SVG, display

Graph = nx.Graph()

Graph.add_nodes_from(range(1,13))
Graph.add_edge( 1,  2, weight=2)
Graph.add_edge( 1,  3, weight=5)
Graph.add_edge( 1,  4, weight=1)
Graph.add_edge( 1,  6, weight=7)
Graph.add_edge( 1,  7, weight=4)
Graph.add_edge( 2,  3, weight=2)
Graph.add_edge( 2,  7, weight=2)
Graph.add_edge( 3,  4, weight=3)
Graph.add_edge( 4,  5, weight=6)
Graph.add_edge( 5,  6, weight=1)
Graph.add_edge( 5,  8, weight=8)
Graph.add_edge( 5, 11, weight=8)
Graph.add_edge( 6,  8, weight=4)
Graph.add_edge( 7,  8, weight=9)
Graph.add_edge( 7,  9, weight=8)
Graph.add_edge( 8,  9, weight=2)
Graph.add_edge( 8, 10, weight=4)
Graph.add_edge( 8, 11, weight=8)
Graph.add_edge( 9, 13, weight=5)
Graph.add_edge(10, 12, weight=1)
Graph.add_edge(10, 13, weight=3)
Graph.add_edge(11, 12, weight=4)
Graph.add_edge(12, 13, weight=5)

for u,v,d in Graph.edges(data=True):
    d['label'] = d.get('weight','')

A = nx.nx_agraph.to_agraph(Graph)
# A.layout(prog='dot')
svg = SVG(A.draw(prog='fdp', format='svg'))
display(svg)


# In[ ]:


start_node = 2

all_nodes = list(Graph.nodes)
connected_nodes = []
connected_edges = []

adopt_edges = []
temp_edges = {i+1: [-1, i+1, 9999999999] for i in range(len(all_nodes))}

start_node = 2
del temp_edges[start_node]
#print('temp {0}'.format(temp_edges))

from_node = start_node
while len(temp_edges) > 0:
    #print('-- {0} --'.format(from_node))
    for to_node in list(Graph.neighbors(from_node)):
        if to_node not in temp_edges:
            continue
        #print('    {0}: {1}'.format(to_node, temp_edges[to_node]))
        w = Graph[from_node][to_node]['weight']
        if temp_edges[to_node][2] > w:
            temp_edges[to_node] = [from_node, to_node, w]

    # temp_edges内の最小コストのエッジを探す
    min_weight = 9999999999
    min_edge = None
    for x in temp_edges.values():
        #print(x)
        if x[2] < min_weight:
            min_edge = x
            min_weight = x[2]
    #print('MIN: {0}'.format(min_edge))
    connected_edges.append(min_edge)
    Graph.add_edge(min_edge[0], min_edge[1], weight=min_edge[2], color='red')
    from_node = min_edge[1]
    del temp_edges[from_node]
    #print('temp {0}'.format(temp_edges))

print('-- minimum spanning tree Prim on Dijkstra--')
print(connected_edges)

for u,v,d in Graph.edges(data=True):
    d['label'] = d.get('weight','')

A = nx.nx_agraph.to_agraph(Graph)
# A.layout(prog='dot')
svg = SVG(A.draw(prog='fdp', format='svg'))
display(svg)


# In[ ]:




