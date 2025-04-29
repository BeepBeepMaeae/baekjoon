def combination(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1  # C(i, 0) = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    return dp[n][k]

n, k = map(int, input().split())
print(combination(n, k)%1000000007)