n = int(input())

dp = [0] * 1000001

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1  # 1을 빼는 연산
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)  # 2로 나누는 연산과 비교하여 최소값 선택
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)  # 3으로 나누는 연산과 비교하여 최소값 선택

print(dp[n])