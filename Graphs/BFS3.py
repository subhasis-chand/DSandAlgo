from collections import deque

# Graph with two disconnected components
graph = {
    4: [6, 7, 3],
    6: [4, 7, 3],
    7: [4, 6, 3],
    3: [4, 6, 7],
    10: [11],
    11: [10]
}

def bfs(start, visited):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

def bfs_traversal():
    visited = set()
    print("BFS Traversal:", end=" ")
    for node in graph:
        if node not in visited:
            bfs(node, visited)
    print()

bfs_traversal()
