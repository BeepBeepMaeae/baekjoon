n = int(input())
dp = []

dp.append(1)
dp.append(1)

for i in range(2, n):
    # i자리 이친수는 (i-1자리 이친수) + (i-2자리 이친수), 피보나치 수열과 같음.
    dp.append(dp[i-2] + dp[i-1])

print(dp[-1])