from graph import Graph

class dfsGraph(Graph):
    def traverse(self, start, order='increment'):
        """
            Initie une recherche en profondeur à partir d'un nœud donné.

            Args:
                start (int): Le nœud de départ pour la traversée DFS.
                order (str): L'ordre de traversée, 'increment' pour croissant, 'decrement' pour décroissant.
        """
        visited = set() # Crée un ensemble pour garder une trace des nœuds visités
        
        self.dfs_recursive(start, visited, order) # Effectue une traversée DFS de manière récursive
        unvisited_nodes = set(self.graph.keys()) - visited
        # print(unvisited_nodes)
        
        for node in sorted(unvisited_nodes, reverse=(order == "decrement")): # If there are unvisited nodes
            if node not in visited: # Pick an unvisited node
              self.dfs_recursive(node, visited, order)
        print()
        
    def dfs_recursive(self, node, visited, order='increment'):
        """
            Visite récursivement les nœuds de manière parcours en profondeur.

            Args:
            node (int): Le nœud actuel à visiter.
            visited (set): L'ensemble des nœuds déjà visités.
            order (str): L'ordre de parcours, affecte le tri des voisins.
        """
        if node not in visited: # Si le nœud n'a pas été visité
            visited.add(node) # Marquez le nœud comme visité

            successors = self.graph[node]  # Obtenez les voisins du nœud
            if order == 'decrement':
                successors = reversed(successors)  # En fonction de l'ordre de tri, inversez les voisins
            
            for next_node in successors: # Pour chaque voisin du nœud
                self.dfs_recursive(next_node, visited, order) # Visitez le voisin de manière récursive
            print(node, end=" ") # Affichez le nœud

graph = dfsGraph()
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
#   [1, 3],
#   [1, 4],
#   [3, 5],
#   [3, 2],
#   [4, 5],
#   [5, 6],
#   [7, 8],
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