# a = {'b': 1, 'c': 2}
# print(a.get('b', []))
# print(a['b'])

graph = {
    4: [6, 7, 3],
    6: [4, 7, 3],
    7: [4, 6, 3],
    3: [4, 6, 7]
}

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        # print("Queue state:", queue)
        node = queue.pop(0)
        if node not in visited:
            print("Visiting:", node)
            visited.add(node)
            for neighbor in graph.get(node):
                if neighbor not in visited:
                    queue.append(neighbor)
                    # print("  Queued:", neighbor)
    # print("BFS complete")
    return visited

graph2 = {
    4: [6, 7, 3],
    6: [4, 7, 3],
    7: [4, 6, 3],
    3: [4, 6, 7],
    10: [11],
    11: [10]
}



if __name__ == "__main__":
    print("BFS Traversal of the graph starting from node 4:")
    # bfs(graph, 4)
    bfs(graph2, 10)