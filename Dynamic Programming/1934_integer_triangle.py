import sys

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] += dp[i-1][j]  # 삼각형의 왼쪽 끝 값은 바로 위에서만 내려올 수 있음
        elif j == i:
            dp[i][j] += dp[i-1][j-1]  # 오른쪽 끝 값은 대각선 왼쪽 위에서만 내려올 수 있음
        else:
            # 중간 위치는 위 또는 대각선 왼쪽 위 중 더 큰 값 선택
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[n-1]))