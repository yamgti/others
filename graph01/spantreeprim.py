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

connected_nodes.append(start_node)
while len(connected_nodes) < len(all_nodes):
    min_weight = 9999999999
    min_edge = None

    for from_node in connected_nodes:
        for to_node in list(Graph.neighbors(from_node)):
            if to_node not in connected_nodes:
                w = Graph[from_node][to_node]['weight']
                #print('({0},{1}):{2}'.format(from_node, to_node, w))
                if w < min_weight:
                    min_weight = w
                    min_edge = [from_node, to_node]

    #print('min: ({0}):{1}'.format(min_edge, min_weight))
    if min_edge == None:
        print('ERROR: Node {0} is closed.'.format(from_node))
        break
    connected_nodes.append(min_edge[1])
    connected_edges.append(min_edge)
    Graph.add_edge(min_edge[0], min_edge[1], weight=min_weight, color='red')

print('-- minimum spanning tree by normal Prim --')
print(connected_edges)

for u,v,d in Graph.edges(data=True):
    d['label'] = d.get('weight','')

A = nx.nx_agraph.to_agraph(Graph)
# A.layout(prog='dot')
svg = SVG(A.draw(prog='fdp', format='svg'))
display(svg)


# In[ ]:




