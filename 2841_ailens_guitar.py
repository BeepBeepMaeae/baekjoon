import sys

n, p = map(int,sys.stdin.readline().split())
stack = [[] for _ in range(n)]
cnt = 0
for i in range(n):
    a,b =  map(int,sys.stdin.readline().split())
    while stack[a-1] and b<stack[a-1][-1]:
        stack[a-1].pop()
        cnt+=1
    if not stack[a-1] or b>stack[a-1][-1]:
        stack[a-1].append(b)
        cnt+=1

print(cnt)