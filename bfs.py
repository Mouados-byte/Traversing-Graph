from graph import Graph
from collections import deque

class bfsGraph(Graph):
    def traverse(self, start, order="increment"):
        queue = deque()
        all_nodes = list(self.graph.keys()) + [item for sublist in self.graph.values() for item in sublist]
        visited = [False] * (max(all_nodes) + 1)
        
        queue.append(start)
        visited[start] = True
        
        while queue:
            start = queue.popleft()
            print(start, end=" ")
            
            neighbors = sorted(self.graph[start], reverse=(order == 'decrement'))
            for i in neighbors:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print()
        
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
    graph.addEdge(edge[0], edge[1])
    
graph.traverse(1)
graph.traverse(1, "decrement")