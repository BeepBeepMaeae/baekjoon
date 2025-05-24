n = int(input())
dp = []

dp.append(1)
dp.append(1)

for i in range(2, n):
    dp.append(dp[i-2] + dp[i-1])

if n == 0:
    print(0)
else:
    print(dp[-1])