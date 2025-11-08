#     0 1 2 3
# 0 [ 0 1 1 1 ]
# 1 [ 1 0 1 1 ]
# 2 [ 1 1 0 1 ]
# 3 [ 1 1 1 0 ]


graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

def bfs(graph, start, res_arr):
    visited = set()
    queue = []

    queue.append(start)
    visited.add(start)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=' ')
        res_arr.append(current_node)

        for i in range(len(graph[current_node])):
            if graph[current_node][i] == 1 and i not in visited:
                queue.append(i)
                visited.add(i)

if __name__ == "__main__":
    print("BFS Traversal of the graph:")
    result = []
    bfs(graph, 0, result)
    print("\nBFS Result Array:", result)