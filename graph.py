from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, source, direction):
        self.graph[source].append(direction)
        
    
    def draw_graph(self):
        G = nx.DiGraph()
        for source, targets in self.graph.items():
            for target in targets:
                G.add_edge(source, target)
        nx.draw_kamada_kawai(G, with_labels=True)
        plt.show()