import sys
import math

num = int(input())

for _ in range(num):
    li = list(map(int,sys.stdin.readline().split()))
    sum = 0
    n = li[0]
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            sum+=math.gcd(li[i],li[j])
    print(sum)