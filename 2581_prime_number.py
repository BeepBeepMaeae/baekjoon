import sys

n = int(input())
a = int(input())
b = int(input())
li = list(map(int,sys.stdin.readline().split()))
prime = []
array = [True for _ in range(b + 1)]

for i in range(a,b+1):
    if array[i]:
        prime.append(i)

if(len(prime)>0):
    print(sum(prime))
    print(min(prime))
else:
    print(-1)