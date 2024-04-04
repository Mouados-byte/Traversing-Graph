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
        if start not in self.graph: # Si le nœud de départ n'est pas dans le graphe
            print("Noeud non trouvé dans le graphe") # Affichez un message d'erreur
            return
        
        queue = deque([start]) # Créez une file d'attente pour le parcours en largeur d'abord
        visited = set([start]) # Créez un ensemble pour garder une trace des nœuds visités
        
        while queue:
            start = queue.popleft() # Obtenez le premier nœud de la file d'attente
            print(start, end=" ") # Affichez le nœud
            
            neighbors = sorted(self.graph[start], reverse=(order == 'decrement')) # Obtenez les voisins du nœud
            for next_node in neighbors:
            if not visited[next_node]: # Si le voisin n'a pas été visité
                queue.append(next_node) # Ajoutez le voisin à la file d'attente, afin qu'il puisse être visité ultérieurement
                visited.add(next_node) # Marquez le voisin comme visité
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
    graph.add_edge(edge[0], edge[1]) # Ajoutez les arêtes au graphe
    
graph.traverse(1) 
graph.traverse(1, "decrement") 