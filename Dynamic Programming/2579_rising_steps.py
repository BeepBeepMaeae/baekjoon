import sys

n = int(input())
score = []
for _ in range(n):
    score.append(int(sys.stdin.readline()))

dp = []

dp.append(score[0])  # 첫 번째 계단
dp.append(score[0] + score[1])  # 첫 번째 + 두 번째 계단
dp.append(max(score[0] + score[2], score[1] + score[2]))  # 세 번째 계단까지의 최대 점수

for i in range(3, n):
    # 두 계단 전에서 한 칸 올라오기 또는 세 계단 전에서 두 칸 연속으로 올라오기
    dp.append(max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i]))

print(dp[-1])