class Node:
    def __init__(self, name):
        self.name = name
        self.arcs = {}

    def add_arc(self, other, weight):
        self.arcs[other] = weight

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def get_node(self, name):
        return self.nodes.get(name)

def dfs(node, path):
    path.append(node.name)

    for other, weight in node.arcs.items():
        if other.name in path:
            print(f"Cycle detected: {' -> '.join(path)}")
            return
        dfs(other, path)

    path.pop()

graph = Graph()

# Example nodes
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

# Add nodes to the graph
graph.add_node(a)
graph.add_node(b)
graph.add_node(c)
graph.add_node(d)

# Example arcs
a.add_arc(b, 3)
a.add_arc(c, 2)
b.add_arc(c, 1)
b.add_arc(d, 2)
c.add_arc(d, 3)

# Start depth-first search from node A
path = []
dfs(a, path)