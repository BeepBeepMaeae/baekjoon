import sys

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(3):
        # 현재 집 i를 j색으로 칠할 경우, 이전 집은 j가 아닌 색 중 최소 비용 선택
        if j == 0:
            dp[i][j] += min(dp[i-1][1], dp[i-1][2])
        elif j == 1:
            dp[i][j] += min(dp[i-1][0], dp[i-1][2])
        else:
            dp[i][j] += min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))