import sys

wine = []
n = int(input())
for _ in range(n):
    wine.append(int(sys.stdin.readline()))

dp = []

dp.append(wine[0])  # 첫 잔 마신 경우
if n > 1:
    dp.append(wine[0] + wine[1])  # 첫 잔 + 두 번째 잔 마신 경우
if n > 2:
    # 첫+세 번째, 둘+셋째, 첫+둘째 중 최대값 선택
    dp.append(max(wine[0] + wine[2], wine[1] + wine[2], wine[0] + wine[1]))

for i in range(3, n):
    # 세 가지 경우 중 최대값 선택:
    # 1) 현재 잔을 마시지 않음 (dp[i-1])
    # 2) 현재 잔만 마심 (dp[i-2] + wine[i])
    # 3) 현재 잔과 바로 앞 잔 마심 (dp[i-3] + wine[i-1] + wine[i])
    dp.append(max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i]))

print(max(dp))