import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import graphviz

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])

dot = graphviz.Digraph()
dot.node('A','product A')
dot.node('B','customer B')
dot.node('C','customer C')
dot.edges(['AB','AC'])
dot.edge('B','C' , constraint='false')
print(dot.source)
dot.render('test-output/round-table.gv', view=True)
