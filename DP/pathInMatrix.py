def printdp(dp):
    for row in dp:
        print(row)
    print()


def numberOfPaths(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    printdp(dp)

    for i in range(m):
        dp[i][0] = 1
    printdp(dp)

    for j in range(n):
        dp[0][j] = 1
    printdp(dp)

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            printdp(dp)

    

    return dp[m - 1][n - 1]

if __name__ == "__main__":
    m = 3
    n = 4
    print(f"Number of unique paths in a {m}x{n} matrix is:", numberOfPaths(m, n))