import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'

# G=nx.Graph()
# i=1
# # G.add_node(i,pos=(i,i))
# # G.add_node(2,pos=(2,2))
# # G.add_node(3,pos=(1,0))
# G.add_edge(1,2,weight=0.5)
# G.add_edge(1,3,weight=9.8)
# pos=nx.get_node_attributes(G,'pos')
# nx.draw(G,pos)
# labels = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)


G = nx.Graph()
G.add_path([0,1,2])
G.add_edge(2,3,weight=5)
G.add_edge(3,1,weight=2)
# G.edges()
pos=nx.spring_layout(G)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

# nx.draw(G, with_labels=True, font_weight='bold')
# nx.algorithms.shortest_paths.weighted.all_pairs_dijkstra_path(G, cutoff=None, weight='weight')
# nx.all_pairs_dijkstra_path(G,)

G = nx.erdos_renyi_graph(7,5)
draw(G, layout='circo')

print('lllll')
## -----------------------------  method 2 ----------------------------- ##
# # function for adding edge to graph
# graph = defaultdict(list)
# def addEdge(graph,u,v):
#     graph[u].append(v)
#     # graph[v].append(u)
#
# # definition of function
# def generate_edges(graph):
#     edges = []
#
#     # for each node in graph
#     for node in graph:
#
#         # for each neighbour node of a single node
#         for neighbour in graph[node]:
#
#             # if edge exists then append
#             edges.append((node, neighbour))
#     return edges
#
#
# # function to find path
# def find_path(graph, start, end, path =[]):
#     path = path + [start]
#     if start == end:
#         return path
#     for node in graph[start]:
#         if node not in path:
#             newpath = find_path(graph, node, end, path)
#             if newpath:
#                 return newpath
#             return None
#
# # function to generate all possible paths
# def find_all_paths(graph, start, end, path =[]):
#     path = path + [start]
#     if start == end:
#         return [path]
#     paths = []
#     for node in graph[start]:
#         if node not in path:
#             newpaths = find_all_paths(graph, node, end, path)
#             for newpath in newpaths:
#                 paths.append(newpath)
#     return paths
#
# # declaration of graph as dictionary
# addEdge(graph,'a','c')
# addEdge(graph,'b','c')
# addEdge(graph,'b','e')
# addEdge(graph,'c','d')
# addEdge(graph,'c','e')
# addEdge(graph,'e','b')
# addEdge(graph,'d','c')
# addEdge(graph,'e','r')
# addEdge(graph,'r','f')
# addEdge(graph,'d','r')
#
#
# print(generate_edges(graph))
# print(find_all_paths(graph, 'c', '`b`'))


## -----------------------------  method 3 ----------------------------- ##
# dot = graphviz.Digraph()
# dot.node('A','product A')
# dot.node('B','customer B')
# dot.node('C','customer C')
# dot.edges(['AB','AC'])
# dot.edge('B','C' , constraint='false')
# print(dot.source)
# dot.render('test-output/round-table.gv', view=True)
