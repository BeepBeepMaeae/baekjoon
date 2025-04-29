from collections import deque
import sys

n = int(input())
queue = deque()
for i in range(n):
    cm = list(sys.stdin.readline().split())
    if cm[0] == "push":
        queue.append(cm[1])
    if cm[0] == "pop":
        if(len(queue)<1):
            print(-1)
        else:
            print(queue.popleft())
    if cm[0] == "size":
        print(len(queue))
    if cm[0] == "empty":
        if(len(queue)<1):
            print(1)
        else:
            print(0)
    if cm[0] == "front":
        if(len(queue)<1):
            print(-1)
        else:
            print(queue[0])
    if cm[0] == "back":
        if(len(queue)<1):
            print(-1)
        else:
            print(queue[-1])