def countWaysTabular(n):
    dp = [0] * (n)
  
    # Base cases
    dp[0] = 1
    dp[1] = 2
    print(dp)
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]; 
        print(i, dp)
  
    return dp[n-1]


def countWaysOptimized(n):
    if n <= 1:
        return n
    a, b = 1, 2
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return b

if __name__ == "__main__":
    n = 5
    ways = countWaysTabular(n)
    print(f"Total ways to reach stair {n}:", ways)