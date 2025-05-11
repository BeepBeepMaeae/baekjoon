n = int(input())

dp = [0] * 1000001

dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    # i 길이의 이진 타일 경우의 수는 i-1 길이에 1 추가한 것 + i-2 길이에 00 추가한 것, 피보나치 수열과 같음.
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])