from collections import defaultdict, deque
# import networkx as nx
# import matplotlib.pyplot as plt

class Graph:
    def __init__(self, graph=None):
        if graph is None: # Si aucun graphe n'est fourni
            graph = defaultdict(list) # Créez un dictionnaire par défaut pour stocker les arêtes du graphe
        self.graph = graph # Stockez le graphe dans l'attribut de la classe
    
    def add_edge(self, source, direction):
        self.graph[source].append(direction) # Ajouter une arête du nœud source à la direction
        self.graph[direction] = self.graph.get(direction, []) # Ajouter la direction au graphe
        sorted(self.graph[source]) # Triez les voisins du nœud source
        
    
    def draw_graph(self):
        G = nx.DiGraph() # Graphe orienté
        for source, targets in self.graph.items(): # Ajouter les arêtes au graphe
            for target in targets:
                G.add_edge(source, target) # Ajouter une arête de la source à la cible
        nx.draw_kamada_kawai(G, with_labels=True) # Dessiner le graphe
        plt.show() # Afficher le graphe
