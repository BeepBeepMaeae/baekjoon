import sys

n = int(input())
A= list(map(int,sys.stdin.readline().split()))
B= list(map(int,sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)
result = 0

# 하나는 오름차순, 다른 하나는 내림차순으로 곱하면 최소
for i in range(n):
    result+=A[i]*B[i]

print(result)