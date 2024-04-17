from graph import Graph
from collections import deque



class bfsGraph(Graph):
    """
    Une classe représentant un graphe qui effectue une traversée en largeur d'abord.

    Attributs:
        graph (dict): Un dictionnaire représentant la structure du graphe.
    """
    
    def process_queue(self, queue, order, visited):
      start = queue.popleft() # Obtenez le premier nœud de la file d'attente
      print(start, end=" ") # Affichez le nœud
      
      successors = sorted(self.graph[start])  # Obtenez les voisins du nœud
      if order == 'decrement':
          successors = reversed(successors)  # En fonction de l'ordre de tri, inversez les voisins
      
      for next_node in successors:
        if not next_node in visited: # Si le voisin n'a pas été visité
            queue.append(next_node) # Ajoutez le voisin à la file d'attente, afin qu'il puisse être visité ultérieurement
            visited.add(next_node) # Marquez le voisin comme visité

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
        
        while queue: # Tant qu'il y a des éléments dans la file d'attente
            self.process_queue(queue, order, visited) # Traitez la file d'attente
        
        unvisited_nodes = sorted(set(self.graph.keys()) - visited, reverse=(order=="decrement"))
        for node in unvisited_nodes:
            if node not in visited:
                queue.append(node)
                visited.add(node)
                while queue:
                  self.process_queue(queue, order, visited)

        print() # Affichez une nouvelle ligne
        
graph = bfsGraph()
# edges = [
#     [0, 1],
#     [0, 2],
#     [1, 2],
#     [2, 0],
#     [2, 10],
#     [2, 3],
#     [3, 3],
#     [3, 4],
#     [3, 5],
#     [4, 5],
#     [5, 6],
#     [5, 9],
#     [6, 7],
#     [7, 8],
#     [8, 9],
#     [9, 4],
#     [4, 10],
#     [10, 11],
#     [10, 14],
#     [11, 12],
#     [12, 13],
#     [13, 14],
#     [14, 9],
#     [6, 15],
#     [15, 16],
#     [16, 17],
#     [17, 18],
#     [17, 21],
#     [18, 19],
#     [19, 20],
#     [19, 1],
#     [20, 21]
# ]
# edges = [
#   [1, 2],
#   [1, 4],
#   [1, 5],
#   [2, 4],
#   [3, 1],
#   [4, 3],
#   [5, 4],
#   [6, 7],
#   [6, 8],
#   [7, 5],
#   [8, 4],
#   [8, 7],
#   [8, 6],
# ]
edges = [
  [1, 3],
  [2, 4],
  [2, 8],
  [3, 5],
  [4, 5],
  [4, 8],
  [5, 8],
  [6, 4],
  [6, 5],
  [7, 1],
  [7, 2],
  [7, 3],
  [7, 4],
  [7, 6],
  [8, 10],
  [9, 7],
  [10, 2],
  [10, 9],
]

for edge in edges:
    graph.add_edge(edge[0], edge[1])

print("Traverer le graphe en ordre croissant:")
graph.traverse(8)
print("Traverer le graphe en ordre decroissant:")
graph.traverse(8, "decrement") 
