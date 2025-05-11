import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n)

dp[0] = arr[0]
for i in range(1, n):
    # 현재 위치에서 연속합을 새로 시작할지, 이전까지의 합에 현재 값을 더할지 선택
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))