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


# In[ ]:


x = np.linspace(0, 10, 100)
y = x + np.random.randn(100)


# In[ ]:


plt.plot(x, y, label="test")
plt.legend()
plt.show()


# In[ ]:


Graph = nx.DiGraph()
Graph.add_node('foo')
Graph.add_node('bar')


# In[ ]:


Graph.nodes()


# In[ ]:


Graph.nodes(data=False)


# In[ ]:


Graph.nodes(data=True)


# In[ ]:


Graph.add_nodes_from(['baz', 'cook', 'spawn'])


# In[ ]:


Graph.nodes(data=True)


# In[ ]:


Graph.add_node('foo', color='green')


# In[ ]:


Graph.add_node('baz', colot='lightblue')


# In[ ]:


Graph.remove_node('baz')


# In[ ]:


Graph.add_node('baz', color='lightblue')


# In[ ]:


Graph.add_edge('foo','baz')
Graph.add_edge('foo','bar')


# In[ ]:


Graph.add_edge('bar', 'cook')
Graph.add_edge('spawn', 'baz')


# In[ ]:


Graph.edges()


# In[ ]:


Graph.add_edge('spawn', 'cook', weight=0.7)
Graph.add_edge('baz', 'cook', weight=0.5)


# In[ ]:


Graph.edges(data=True)


# In[ ]:


Graph.clear()
Graph.nodes()
Graph.edges()


# In[ ]:


Graph.nodes()


# In[ ]:


Graph.add_nodes_from(['a','b','c','d'])
Graph.add_edges_from([('a','b'),('a','c'),('a','d'),('b','c'),('b','d'),('d','c')])
print('all paths')
for path in nx.all_simple_paths(Graph, source='a', target='c'):
    print(path)


# In[ ]:


nx.draw_networkx(Graph)
plt.show()


# In[ ]:


Graph.clear()


# In[ ]:


Graph.add_path([3, 5, 4, 1, 0, 2, 7, 8, 9, 6])
Graph.add_path([3, 0, 6, 4, 2, 7, 1, 9, 8, 5])


# In[ ]:


nx.nx_agraph.view_pygraphviz(Graph, prog='fdp')


# In[ ]:


Graph = nx.DiGraph()


# In[ ]:


Graph.add_path([3, 5, 4, 1, 0, 2, 7, 8, 9, 6])
Graph.add_path([3, 0, 6, 4, 2, 7, 1, 9, 8, 5])


# In[ ]:


nx.nx_agraph.view_pygraphviz(Graph, prog='fdp')


# In[ ]:


svg = SVG(nx.nx_agraph.to_agraph(Graph).draw(prog='fdp', format='svg'))
display(svg)


# In[ ]:


print(list(Graph.nodes))


# In[ ]:


print(list(Graph.edges))


# In[ ]:


print(list(Graph.succ[0]), Graph.out_edges(0))


# In[ ]:


print(list(Graph.pred[0]), Graph.in_edges(0))


# In[ ]:


print(Graph.degree(0), list(nx.all_neighbors(Graph, 0)))


# In[ ]:


Graph.clear()


# In[ ]:


Graph.add_nodes_from(['1', '2', '3', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])
Graph.add_edge( '1',  '2', weight=2)
Graph.add_edge( '1',  '3', weight=5)
Graph.add_edge( '1',  '4', weight=1)
Graph.add_edge( '1',  '7', weight=4)
Graph.add_edge( '2',  '3', weight=2)
Graph.add_edge( '2',  '7', weight=2)
Graph.add_edge( '3',  '4', weight=3)
Graph.add_edge( '4',  '5', weight=6)
Graph.add_edge( '5',  '6', weight=1)
Graph.add_edge( '5',  '8', weight=8)
Graph.add_edge( '5', '11', weight=8)
Graph.add_edge( '6',  '8', weight=4)
Graph.add_edge( '7',  '8', weight=9)
Graph.add_edge( '7',  '9', weight=8)
Graph.add_edge( '8',  '9', weight=2)
Graph.add_edge( '8', '10', weight=4)
Graph.add_edge( '8', '11', weight=8)
Graph.add_edge( '9', '13', weight=5)
Graph.add_edge('10', '12', weight=1)
Graph.add_edge('10', '13', weight=3)
Graph.add_edge('11', '12', weight=4)
Graph.add_edge('12', '13', weight=5)


# In[ ]:


svg = SVG(nx.nx_agraph.to_agraph(Graph).draw(prog='fdp', format='svg'))
display(svg)


# In[ ]:


Graph.clear()


# In[ ]:


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


# In[ ]:


for u,v,d in Graph.edges(data=True):
    d['label'] = d.get('weight','')

A = nx.nx_agraph.to_agraph(Graph)
# A.layout(prog='dot')
svg = SVG(A.draw(prog='fdp', format='svg'))
display(svg)


# In[ ]:


Graph = nx.Graph()


# In[ ]:


start_node = 2
from_node = start_node


# In[ ]:


print(list(Graph.edges()))


# In[ ]:


print(list(Graph.neighbors(from_node)))


# In[ ]:


for to_node in list(Graph.neighbors(from_node)):
	print(from_node, to_node, Graph[from_node][to_node]['weight'])


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

print('-- minimum spanning tree --')
print(connected_edges)


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

print('-- minimum spanning tree --')
print(connected_edges)


# In[ ]:


GraphMST = nx.Graph()
GraphMST.add_nodes_from(range(1,13))
GraphMST.add_weighted_edges_from(connected_edges)

for u,v,d in GraphMST.edges(data=True):
    d['label'] = d.get('weight','')

A = nx.nx_agraph.to_agraph(GraphMST)
# A.layout(prog='dot')
svg = SVG(A.draw(prog='fdp', format='svg'))
display(svg)


# In[ ]:





# In[ ]:




