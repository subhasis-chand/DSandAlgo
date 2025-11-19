def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fibMemo(n, memo):
    print("memo: ", n, memo)
    if n <= 1:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo)
    return memo[n]

def fibTab(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    print("dp after initialization:", dp)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        print("dp after computation:", dp)
    return dp[n]

def fibSpaceOptimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


if __name__ == "__main__":
    n = 8
    memo = [-1] * (n + 1)
    fibMemo(n, memo)
    print(f"The {n}th Fibonacci number is: {memo[n]}")
    print("Memoization Array:", memo)
    # result = fibTab(n)
    # print(f"The {n}th Fibonacci number is: {result}")
