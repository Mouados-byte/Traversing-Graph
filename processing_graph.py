from dfs import dfsGraph
from bfs import bfsGraph

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

edges = [
  [1, 2],
  [1, 4],
  [1, 5],
  [2, 4],
  [3, 1],
  [4, 3],
  [5, 4],
  [6, 7],
  [6, 8],
  [7, 5],
  [8, 4],
  [8, 7],
  [8, 6],
]

# edges = [
#   [1, 3],
#   [2, 4],
#   [2, 8],
#   [3, 5],
#   [4, 5],
#   [4, 8],
#   [5, 8],
#   [6, 4],
#   [6, 5],
#   [7, 1],
#   [7, 2],
#   [7, 3],
#   [7, 4],
#   [7, 6],
#   [8, 10],
#   [9, 7],
#   [10, 2],
#   [10, 9],
# ]

dfsgraph = dfsGraph()
bfsgraph = bfsGraph()


for edge in edges:
    dfsgraph.add_edge(edge[0], edge[1])
    bfsgraph.add_edge(edge[0], edge[1])

starting_point = 1
print("Traverer le graphe par profondeur en ordre croissant:")
dfsgraph.traverse(starting_point)
print("Traverer le graphe par profondeur en ordre decroissant:")
dfsgraph.traverse(starting_point, "decrement") 
print("Traverer le graphe par langueur en ordre croissant:")
bfsgraph.traverse(starting_point)
print("Traverer le graphe par langueur en ordre decroissant:")
bfsgraph.traverse(starting_point, "decrement") 