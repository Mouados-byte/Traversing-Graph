from collections import defaultdict
# import networkx as nx
# import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, source, direction):
        self.graph[source].append(direction)

    def output_as_matrix(self):
        for source, targets in self.graph.items():
            print(f'{source}: {targets}')
        self.draw_graph()

    # def draw_graph(self):
    #     G = nx.DiGraph()
    #     for source, targets in self.graph.items():
    #         for target in targets:
    #             G.add_edge(source, target)
    #     nx.draw(G, with_labels=True)
    #     plt.show()
        
    def dfs(self, start, order='increment'):
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
        

graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 10)
graph.addEdge(2, 3)
graph.addEdge(3, 3)
graph.addEdge(3, 4)
graph.addEdge(3, 5)
graph.addEdge(4, 5) 
graph.addEdge(5, 6) 
graph.addEdge(5, 9)
graph.addEdge(6, 7)
graph.addEdge(7, 8)
graph.addEdge(8, 9)
graph.addEdge(9, 4) 
graph.addEdge(4, 10)
graph.addEdge(10, 11)
graph.addEdge(10, 14)
graph.addEdge(11, 12)
graph.addEdge(12, 13)
graph.addEdge(13, 14)
graph.addEdge(14, 9)
graph.addEdge(6, 15)
graph.addEdge(15, 16)
graph.addEdge(16, 17)
graph.addEdge(17, 18)
graph.addEdge(17, 21)
graph.addEdge(18, 19)
graph.addEdge(19, 20)
graph.addEdge(19, 1)
graph.addEdge(20, 21)
graph.dfs(1)
graph.dfs(1, "decrement")

