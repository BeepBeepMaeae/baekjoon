import sys

n, k = map(int, sys.stdin.readline().split())

A = []
result = 0 

for _ in range(n):
    A.append(int(input()))

# 큰 단위부터 사용
A.reverse()

for i in range(n):
    if k >= A[i]: # 현재 금액 k를 그 동전으로 나눌 수 있는 경우
        result += k // A[i] # 그 동전으로 나눌 수 있는 최대 개수
        k %= A[i] # 나머지 금액

print(result)