import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
    dp = []

    dp.append(1)
    dp.append(1)
    dp.append(1)

    for i in range(4, n+1):
        dp.append(dp[i-4]+dp[i-3])

    print(dp[-1])