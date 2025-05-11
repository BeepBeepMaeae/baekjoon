import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            # arr[i]를 뒤에 붙일 수 있는 증가 수열이 있을 경우, 길이 갱신
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))