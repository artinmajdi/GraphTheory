from collections import defaultdict
from heapq import *
from nxpd import draw, nxpdParams
import networkx as nx
# nxpdParams['show'] = 'ipynb'
import matplotlib.pyplot as plt
import numpy as np

def GraphMake(edges , mode):

    Graph = defaultdict(list)
    for v1,v2,cost in edges:

        Graph[v1].append((cost,v2))
        if 'unDirected' in mode:
            Graph[v2].append((cost,v1))

    return Graph

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

def Dijkstra(Graph, origin, destination):

    FullPathCost = [(0,origin,())]
    seenSet = set()
    minCost = {origin: 0}
    while FullPathCost:
        # cost = FullPathCost[0][0]
        # v1 = FullPathCost[0][1]
        # path = FullPathCost[0][2]
        (cost,v1,path) = heappop(FullPathCost)
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
                    # FullPathCost[0] = CostAfter
                    # FullPathCost[1] = v2
                    # FullPathCost[2] = path
    return 'No path exists' , '_'

def main(edges , vertice_origin, vertice_destination , mode = 'unDirected'):
    Graph = GraphMake(edges , mode)  # mode = 'Directed' ,'unDirected'
    myPath, myPath_VerX = Dijkstra(Graph, vertice_origin, vertice_destination)
    print('my Path: ' , myPath)

    ## ----------------------- plot ----------------------- ##
    if 'unDirected' in mode:
        Graph2 = nx.Graph()
    else:
        Graph2 = nx.DiGraph()

    for v1,v2,cost in edges:
        Graph2.add_edges_from([(v1 , v2 , {'weight':cost , 'label': cost})])

    try:
        if 'unDirected' in mode:
            a = nx.bidirectional_dijkstra(Graph2, vertice_origin, vertice_destination , weight='weight')
        else:
            a1 = nx.dijkstra_path(Graph2, vertice_origin, vertice_destination , weight='weight')
            a2 = nx.shortest_path_length(Graph2, vertice_origin, vertice_destination , weight='weight')
            a = (a2,a1)
    except:
        a = 'No path exists'

    print('NetworkX Path: ',a)

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
    ("A", "B", 4)]


vertice_origin = 'K'
vertice_destination = 'G'

if 0:
    print('---------  unDirected   --------- ')
    Graph2 , myPath, myPath_VerX = main(edges , vertice_origin, vertice_destination, mode = 'unDirected')
    myPlot(Graph2 , myPath , myPath_VerX)

if 1:
    print('---------  Directed   --------- ')
    Graph2 , myPath, myPath_VerX = main(edges , vertice_origin, vertice_destination, mode = 'Directed')
    myPlot(Graph2 , myPath , myPath_VerX)


# Graph = GraphMake(edges , mode = 'Directed')  # mode = 'Directed' ,'unDirected'
#
# Graph['E']
