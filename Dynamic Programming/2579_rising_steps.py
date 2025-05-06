import sys

n = int(input())
score = []
for _ in range(n):
    score.append(int(sys.stdin.readline()))

dp = []

dp.append(score[0])
dp.append(score[0]+score[1])
dp.append(max(score[0]+score[2],score[1]+score[2]))

for i in range(3, n):
    dp.append(max(dp[i-2]+score[i], dp[i-3]+score[i]+score[i-1]))

print(dp[-1])