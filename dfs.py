from graph import Graph

class dfsGraph(Graph):
    def traverse(self, start, order='increment'):
        visited = set()
        
        self.dfs_recursive(start, visited, order)
        print()
        
    def dfs_recursive(self, curr_edge, visited, order='increment'):
        visited.add(curr_edge)
        print(curr_edge, end=" ")
        neighbors = sorted(self.graph[curr_edge], reverse=(order == 'decrement'))
        for edge in neighbors:
            if edge not in visited:
                self.dfs_recursive(edge, visited, order)
        

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
    graph.addEdge(edge[0], edge[1])

graph.traverse(1)
graph.traverse(1, "decrement")

