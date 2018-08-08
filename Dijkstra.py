from collections import defaultdict
from heapq import *
from nxpd import draw, nxpdParams
import networkx as nx
# nxpdParams['show'] = 'ipynb'
import matplotlib.pyplot as plt
import numpy as np
# import graphviz

def MyGraph(edges , mode):

    Graph = defaultdict(list)
    for v1,v2,cost in edges:

        Graph[v1].append((cost,v2))
        if 'unDirected' in mode:
            Graph[v2].append((cost,v1))

    return Graph

def NetworkXGraph(edges , mode):

    if 'unDirected' in mode:
        Graph2 = nx.Graph()
    else:
        Graph2 = nx.DiGraph()

    for v1,v2,cost in edges:
        Graph2.add_edges_from([(v1 , v2 , {'weight':cost , 'label': cost})])

    return Graph2

def NetworkXDijkstra(Graph2, vertice_origin, vertice_destination, mode):

    try:
        if 'unDirected' in mode:
            a = nx.bidirectional_dijkstra(Graph2, vertice_origin, vertice_destination , weight='weight')
        else:
            a1 = nx.dijkstra_path(Graph2, vertice_origin, vertice_destination , weight='weight')
            a2 = nx.shortest_path_length(Graph2, vertice_origin, vertice_destination , weight='weight')
            a = (a2,a1)
    except:
        a = 'No path exists'

    return a

def root(a):
    b = a[1]
    path = ''
    path_vertices = []
    while len(b) == 2:
        PathRoot = path
        path = b[0] + ' -> ' + PathRoot
        path_vertices = np.append(b[0],path_vertices)
        b = b[1]

    PathRoot = path
    path = PathRoot + str(a[0])

    return path, path_vertices

def main(edges , vertice_origin, vertice_destination , mode = 'unDirected'):

    Graph = MyGraph(edges , mode)  # mode = 'Directed' ,'unDirected'
    myPath, myPath_VerX = Dijkstra(Graph, vertice_origin, vertice_destination)
    print('my Path: ' , myPath)

    Graph2 = NetworkXGraph(edges , mode)
    NetworkXPath = NetworkXDijkstra(Graph2, vertice_origin, vertice_destination, mode)
    print('NetworkX Path: ' , NetworkXPath )

    return Graph2 , myPath, myPath_VerX

def myPlot(Graph2 , myPath , myPath_VerX):

    if 'No path exists' not in myPath:
        Graph2.node[myPath_VerX[0]]['color'] = 'green'
        Graph2.node[myPath_VerX[len(myPath_VerX)-1]]['color'] = 'red'
    else:
        Graph2.node[vertice_origin]['color'] = 'green'
        Graph2.node[vertice_destination]['color'] = 'red'

    for e in range(len(myPath_VerX)-1):
        Graph2[myPath_VerX[e]][myPath_VerX[e+1]]['color'] = 'blue'

    draw(Graph2, layout='circo')

def Dijkstra(Graph, origin, destination):

    FullPathCost = [(0,origin,())]
    seenSet = set()
    minCost = {origin: 0}
    while FullPathCost:

        (cost,v1,path) = heappop(FullPathCost)
        print(FullPathCost)
        if v1 not in seenSet:
            seenSet.add(v1)
            path = (v1, path)
            print(path)
            if v1 == destination:
                return root((cost, path))

            for cost_Vertice, v2 in Graph[v1]:
                if v2 in seenSet:
                    continue
                CostBefore = minCost.get(v2, None)
                CostAfter = cost + cost_Vertice
                if CostBefore is None or CostAfter < CostBefore:
                    minCost[v2] = CostAfter
                    heappush(FullPathCost, (CostAfter, v2, path))

    return 'No path exists' , '_'

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
if 1:
    print('---------  unDirected   --------- ')
    Graph2 , myPath, myPath_VerX = main(edges , vertice_origin, vertice_destination, mode = 'unDirected')
    myPlot(Graph2 , myPath , myPath_VerX)
if 0:
    print('---------  Directed   --------- ')
    Graph2 , myPath, myPath_VerX = main(edges , vertice_origin, vertice_destination, mode = 'Directed')
    myPlot(Graph2 , myPath , myPath_VerX)

seenSet = set()
seenSet.add(v1)
v1 = vertice_origin
PathCost = {v2: 5}
Graph = MyGraph(edges , 'unDirected')

if v1 is not vertice_destination:
    for cost, v2 in Graph[v1]:
        if PathCost.get(v1 , None) is not None:
            PathCost[v2] = ( cost + PathCost.get(v1 , None) , v1)
        else:
            PathCost[v2] = ( cost , v1 )

PathCost
