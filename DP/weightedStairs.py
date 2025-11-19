# Given an array of integers cost[] of length n, where cost[i] is the cost of the ith step on a staircase. Once the cost is paid, we can either climb one or two steps.
# We can either start from the step with index 0, or the step with index 1. The task is to find the minimum cost to reach the top.


def minCostClimbingStairs(cost):
    n = len(cost)
    
    if n == 1:
        return cost[0]
    
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[n - 1], dp[n - 2])

if __name__ == "__main__":
    cost = [5,3,1,6,2]
    result = minCostClimbingStairs(cost)
    print("Minimum cost to reach the top:", result)

