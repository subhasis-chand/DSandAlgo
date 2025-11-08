
def dfsRec(adjList, visited, startIndex, result):
    visited[startIndex] = True
    result.append(startIndex)

    for neighbor in adjList[startIndex]:
        print("Checking node:", neighbor, 'neighbor of', startIndex )
        if not visited[neighbor]:
            dfsRec(adjList, visited, neighbor, result)


def dfs(adjList):
    visited = [False] * len(adjList)
    result = []
    dfsRec(adjList, visited, 2, result)
    return result

adjList = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]



if __name__ == "__main__":
    result = dfs(adjList)
    print("DFS Result Array:", result)

    
    