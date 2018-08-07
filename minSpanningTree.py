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

# def GraphMake_withoutWeight(edges , mode):
#
#     Graph = defaultdict(list)
#     for v1,v2,cost in edges:
#
#         Graph[v1].append(v2)
#         if 'unDirected' in mode:
#             Graph[v2].append(v1)
#
#     return Graph

def minSpanningTree(edges):

    Graph_forPlot = nx.Graph()
    Graph_checkForCycle = nx.Graph()

    for v1,v2,cost in edges:
        Graph_forPlot.add_edges_from([(v1 , v2 , {'weight':cost , 'label': cost})])

    seenSet = set()
    # Graph = GraphMake(edges , 'unDirected')


    CostFull = []
    for i in range(len(edges)):
        ver1 , Ver2 , cost = edges[i]
        CostFull.append(cost)

    edgesSub = edges.copy()
    CostFullSub = CostFull.copy()


    for edgInx in range( len(edges) ):
        ix = np.where( CostFullSub == np.min(CostFullSub) )[0][0]

        try:
            G_temp = Graph_checkForCycle.copy()
            G_temp.add_edges_from([( edgesSub[ix][0] , edgesSub[ix][1] , {'weight':CostFullSub[ix] , 'label': CostFullSub[ix]})])
            nx.find_cycle(G_temp, orientation='original')
        except:
            seenSet.add(edgesSub[ix][0])
            seenSet.add(edgesSub[ix][1])
            Graph_checkForCycle.add_edges_from([( edgesSub[ix][0] , edgesSub[ix][1] , {'weight':CostFullSub[ix] , 'label': CostFullSub[ix]})])
            Graph_forPlot[ edgesSub[ix][0] ][ edgesSub[ix][1] ]['color'] = 'red'
            Graph_forPlot[ edgesSub[ix][0] ][ edgesSub[ix][1] ]['style'] = 'dashed'


        del edgesSub[ix]
        del CostFullSub[ix]

        # edgesSub
        # CostFullSub
    print(seenSet)
    draw(Graph_forPlot, layout='circo')

# def cyclic(Graph_temp, ver1 , ver2):
#
#     for i in range(len(Graph_temp[ver1])):
#         if ver2 in Graph[ver1][i]:
#             return True
#     return False


if 1:
    edges = [
        ("A", "E", 3),
        #("L", "D", 2),
        ("C", "B", 4),
        ("K", "D", 11),
        ("B", "E", 9),
        ("L", "E", 3),
        ("D", "E", 5),
        ("D", "K", 8),
        ("E", "F", 1),
        ("E", "L", 2),
        ("F", "G", 4),
        ("A", "F", 6),
        ("F", "A", 2),
        ("A", "B", 8),
        ("L", "F", 5),
        ("G", "E", 7),
        ("K", "A", 2)]

if 0:
    edges = [
        ("A", "C", 5),
        ("C", "D", 4),
        ("B", "D", 2),
        ("E", "C", 4),
        ("A", "E", 3),
        ("E", "B", 5)]


minSpanningTree(edges)





# Graph_forPlot = nx.Graph()
# for v1,v2,cost in edges:
#     Graph_forPlot.add_edges_from([(v1 , v2 , {'weight':cost , 'label': cost})])
#
# Graph_WeightLess = GraphMake_withoutWeight(edges , 'unDirected')
#
# draw(Graph_forPlot)
#
# Graph_WeightLess
# ver1 = 'C'
# ver2 = 'B'
# Graph_temp = Graph_WeightLess
# Graph_temp[ver1]
#
# for neighbour in Graph_temp[ver1]:
#     if neighbour not in ver2:
#
#         for neighbour2 in Graph_temp[neighbour]:
#             del Graph_temp[neighbour][g]
#             if neighbour2 in ver2:
#                 print('circle')
#                 break
#             print('neighbour',neighbour,'neighbour2' , neighbour2)
#
#     # print(Graph_temp[neighbour])
#
#
#
#
#
# cyclic(GraphMake(edges , 'unDirected'))
