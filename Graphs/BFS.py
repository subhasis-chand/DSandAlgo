adjList = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

def bfs(adjList):
    visited = [False] * len(adjList)
    queue = []

    start_node = 0
    queue.append(start_node)
    visited[start_node] = True

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=' ')

        for neighbor in adjList[current_node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

if __name__ == "__main__":
    print("BFS Traversal of the graph:")
    bfs(adjList)