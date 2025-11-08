def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)

    # Recursively visit all adjacent vertices 
    # that are not visited yet
    for i in adj[s]:
        print("Checking neighbor:", i)
        if not visited[i]:
            dfsRec(adj, visited, i, res)


def dfs(adj):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj, visited, 0, res)
    return res

if __name__ == "__main__":
    adjList = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
    print("DFS Traversal of the graph:")
    result = dfs(adjList)
    print("DFS Result Array:", result)