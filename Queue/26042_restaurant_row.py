from collections import deque
import sys
n = int(input())

queue = deque()
cnt = 0
num = 0
for _ in range(n):
    cm = list(map(int,sys.stdin.readline().split()))
    if(cm[0] == 1):
        queue.append(cm[1])
    elif(cm[0] == 2):
        queue.popleft()
    if(len(queue)>cnt):
        cnt = len(queue)
        num = queue[-1]
    if(len(queue) == cnt):
        num = min(num,queue[-1])

print(cnt,num)