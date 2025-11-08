
def dfsRec(adjList, visited, startIndex, result):
    visited[startIndex] = True
    result.append(startIndex)

    for neighbor in adjList[startIndex]:
        print("Checking neighbor:", neighbor, 'neighbor of', startIndex )
        if not visited[neighbor]:
            dfsRec(adjList, visited, neighbor, result)


def dfs(adjList):
    visited = [False] * len(adjList)
    result = []
    for i in range(len(adjList)):
    # for i in range(len(adjList) - 1, -1, -1):
        if not visited[i]:
            dfsRec(adjList, visited, i, result)
    return result


if __name__ == "__main__":
    adjList = [[2], [0], [3], [], [2]]
    result = dfs(adjList)
    
    print("DFS Result Array:", result)


    
    