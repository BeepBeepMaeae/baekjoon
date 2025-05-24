import sys

n, m, k = map(int, sys.stdin.readline().split())

for _ in range(k):
    # 여자 2명 + 남자 1명으로 팀을 구성할 수 있다면
    if n // 2 >= m:
        n = n - 1
    else:
        m = m - 1

# (여자 수/2)와 남자 수 중 작은 값
print(min(n // 2, m))