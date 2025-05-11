import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

dp = [sys.maxsize] * n
dp[0] = 0

for i in range(n):
    for j in range(arr[i]):  # arr[i]칸 만큼 앞으로 점프 가능
        if i + j + 1 < n:
            # i에서 i+j+1로 이동할 때, 기존보다 더 적은 점프로 도달 가능하면 갱신
            dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)

if dp[-1] < sys.maxsize:
    print(dp[-1])
else:
    print(-1)