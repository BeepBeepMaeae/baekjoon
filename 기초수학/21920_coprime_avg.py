import sys
import math

n = int(input())
li = list(map(int,sys.stdin.readline().split()))
x = int(input())
result = []

for i in range(n):
    if(math.gcd(li[i],x) == 1):
        result.append(li[i])

print(sum(result)/len(result))