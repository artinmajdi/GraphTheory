from collections import defaultdict
from heapq import *
from nxpd import draw, nxpdParams
import networkx as nx
# nxpdParams['show'] = 'ipynb'
import matplotlib.pyplot as plt
import numpy as np
# import graphviz

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance, mode):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

        if 'unDirected' in mode:
            self.edges[to_node].append(from_node)
            self.distances[(from_node, to_node)] = distance


def NetworkXGraph(edges , mode):

    if 'unDirected' in mode:
        Graph2 = nx.Graph()
    else:
        Graph2 = nx.DiGraph()

    for v1,v2,cost in edges:
        Graph2.add_edges_from([(v1 , v2 , {'weight':cost , 'label': cost})])

    return Graph2

def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distance[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

if 0:
    edges = [
        ("E", "A", 3),
        ("L", "D", 2),
        ("B", "C", 4),
        ("K", "D", 11),
        ("B", "E", 9),
        ("L", "E", 3),
        ("D", "E", 5),
        ("D", "K", 8),
        ("E", "F", 10),
        ("E", "L", 2),
        ("F", "G", 4),
        ("A", "F", 6),
        ("F", "A", 2),
        ("A", "B", 1)]
if 1:
    edges = [
        ("A", "C", 5),
        ("C", "D", 4),
        ("B", "D", 2),
        ("E", "C", 2),
        ("A", "E", 3),
        ("E", "B", 3)]

vertice_origin = 'A'
vertice_destination = 'D'

Graph = NetworkXGraph(edges , 'unDirected')
visited, path = dijsktra(Graph, vertice_origin)

graph = Graph()
for a,b,c in edges:
    print(a,b,c)
    graph.add_node(a)
    graph.add_node(a)
    graph.add_edge(a,b,c, mode)

graph.edges

draw(Graph, layout='circo')
nodes = set(Graph.nodes)
for node in nodes:
    Graph.edges[node]
