import sys

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dp = [0] * (n + 1)

# n-1부터 0까지 역순으로 순회
for i in range(n - 1, -1, -1):
    time_needed = arr[i][0]  # 상담 일수
    profit = arr[i][1]       # 얻는 수익

    # 퇴사일을 초과한다면 상담을 할 수 없음
    if i + time_needed > n:
        dp[i] = dp[i + 1]  # 상담하지 않고 다음 날 최대 수익을 가져옴
    else:
        # 상담을 하지 않는 경우, 상담을 하는 경우 중 최대값
        dp[i] = max(dp[i + 1], dp[i + time_needed] + profit)

print(dp[0])
