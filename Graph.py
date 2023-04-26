
#5)Detect Cycle in a Directed Graph

def has_cycle(graph):
    visited = set()
    stack = set()

    def dfs(node):
        visited.add(node)
        stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in stack:
                return True

        stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False
graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]
}

if has_cycle(graph):
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")

#4)Count number of trees in a forest

def count_trees(graph):
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count
    graph = {
    0: [1],
    1: [2],
    2: [],
    3: []
}

num_trees = count_trees(graph)
print("The forest contains", num_trees, "trees.")
#3)Count the number of nodes at given level in a tree using BFS
def count_nodes_at_level(root, level):
    if not root:
        return 0

    queue = [(root, 0)]
    count = 0

    while queue:
        node, node_level = queue.pop(0)
        if node_level == level:
            count += 1
        elif node_level > level:
            break

        for child in node.children:
            queue.append((child, node_level + 1))

    return count

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []

root = Node(1)
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]
root.children[1].children = [Node(7)]
root.children[2].children = [Node(8), Node(9)]

level = 2
count = count_nodes_at_level(root, level)
print("There are", count, "nodes at level", level, "in the tree.")

#2)Depth First Traversal for a Graph
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

dfs(graph, 2)
#1)Breadth First Traversal for a Graph
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

bfs(graph, 2)
