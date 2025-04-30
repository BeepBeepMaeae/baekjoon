import math
import sys

n = int(input())
num = list(map(int, sys.stdin.readline().split()))
array = [True for _ in range(max(num) + 1)]
cnt = 0

array[0] = False
array[1] = False

for i in range(2, int(math.sqrt(max(num))) + 1):
    if array[i]:
        for j in range(i * i, max(num) + 1, i):
            array[j] = False

for i in num:
    if array[i]:
        cnt += 1

print(cnt)