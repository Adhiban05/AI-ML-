from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            yield node
            visited.add(node)
            queue.extend(graph[node])


# Example Usage:
if __name__ == "__main__":
    # Create a simple graph
    g = Graph()
    g.add_edge('A', ['B', 'C'])
    g.add_edge('B', ['D', 'E'])
    g.add_edge('C', ['F'])
    g.add_edge('D', [])
    g.add_edge('E', [])
    g.add_edge('F', [])

    print("BFS:")
    for node in bfs(g.graph, 'A'):
        print(node, end=' ')


