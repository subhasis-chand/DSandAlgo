def dfsRec(adj, visited, src, dest):
    if src == dest:
        return 1
    
    visited[src] = True
    totlPaths = 0

    for i in adj[src]:
        print("Checking neighbor:", i)
        if not visited[i]:
            totlPaths += dfsRec(adj, visited, i, dest)
    print("visited arr: ", visited)
    visited[src] = False
    return totlPaths


# def dfs(adj):
#     res = []
#     dfsRec(adj, visited, 0, res)
#     return res

def countPaths(adj, src, dest):
    visited = [False] * len(adj)
    return dfsRec(adj, visited, src, dest)


if __name__ == "__main__":
    adjList = [
        [1, 2], 
        [2],
        []
    ]
    print("DFS Traversal of the graph:")
    result = countPaths(adjList, 0, 2)
    print("Total Paths:", result)