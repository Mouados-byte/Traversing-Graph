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
        print()
        
    def dfs_recursive(self, curr_edge, visited, order='increment'):
        """
            Visite récursivement les nœuds de manière parcours en profondeur.

            Args:
            node (int): Le nœud actuel à visiter.
            visited (set): L'ensemble des nœuds déjà visités.
            order (str): L'ordre de parcours, affecte le tri des voisins.
        """
        if node not in visited: # Si le nœud n'a pas été visité
            visited.add(node) # Marquez le nœud comme visité
            print(node, end=" ") # Affichez le nœud

            neighbors = sorted(self.graph[node], reverse=(order == 'decrement')) # Obtenez les voisins du nœud
            for next_node in neighbors: # Pour chaque voisin du nœud
                self.dfs_recursive(next_node, visited, order) # Visitez le voisin de manière récursive
        

graph = dfsGraph()
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
    graph.add_edge(edge[0], edge[1])

graph.traverse(1)
graph.traverse(1, "decrement") 