from graph import Graph
from collections import deque



class bfsGraph(Graph):
    """
    Une classe représentant un graphe qui effectue une traversée en largeur d'abord.

    Attributs:
        graph (dict): Un dictionnaire représentant la structure du graphe.
    """

    def traverse(self, start, order="increment"):
        """
        Effectuer une traversée en largeur d'abord sur le graphe.

        Args:
            start (int): Le nœud de départ pour la traversée.
            order (str, facultatif): L'ordre dans lequel les nœuds sont visités. Par défaut, "increment".

        Returns:
            None
        """
        queue = deque() # Créez une file d'attente pour le parcours en largeur d'abord
        all_nodes = list(self.graph.keys()) + [item for sublist in self.graph.values() for item in sublist] # Obtenez tous les nœuds du graphe
        visited = [False] * (max(all_nodes) + 1) # Créez une liste pour suivre les nœuds visités
        
        queue.append(start) # Ajoutez le nœud de départ à la file d'attente
        visited[start] = True # Marquez le nœud de départ comme visité
        
        while queue:
            start = queue.popleft() # Obtenez le premier nœud de la file d'attente
            print(start, end=" ") # Affichez le nœud
            
            neighbors = sorted(self.graph[start], reverse=(order == 'decrement')) # Obtenez les voisins du nœud
            for i in neighbors:
            if not visited[i]: # Si le voisin n'a pas été visité
                queue.append(i) # Ajoutez le voisin à la file d'attente, afin qu'il puisse être visité ultérieurement
                visited[i] = True # Marquez le voisin comme visité
        print() # Affichez une nouvelle ligne
        
graph = bfsGraph()
edges = [
    [0, 1],
    [0, 2],
    [1, 2],
    [2, 0],
    [2, 10],
    [2, 3],
    [3, 3],
    [3, 4],
    [3, 5],
    [4, 5],
    [5, 6],
    [5, 9],
    [6, 7],
    [7, 8],
    [8, 9],
    [9, 4],
    [4, 10],
    [10, 11],
    [10, 14],
    [11, 12],
    [12, 13],
    [13, 14],
    [14, 9],
    [6, 15],
    [15, 16],
    [16, 17],
    [17, 18],
    [17, 21],
    [18, 19],
    [19, 20],
    [19, 1],
    [20, 21]
]
for edge in edges:
    graph.addEdge(edge[0], edge[1]) # Add the edges to the graph
    
graph.traverse(1) # Perform BFS traversal starting from node 1
graph.traverse(1, "decrement") # Perform BFS traversal starting from node 1 in reverse order