n = int(input())

dp = [[0]*10 for _ in range(n+1)]

for i in range(10):
    dp[1][i] = 1  # 한 자리 수 모두 가능

for i in range(2, n+1):
    for j in range(10):
        # j보다 작거나 같은 수로 끝나는 i-1 자리 수들을 j 뒤에 붙일 수 있음
        dp[i][j] = sum(dp[i-1][k] for k in range(j+1)) % 10007

print(sum(dp[n]) % 10007)