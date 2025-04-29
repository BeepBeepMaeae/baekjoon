from collections import deque
import sys

n, m = map(int,input().split())
tar = list(map(int,sys.stdin.readline().split()))
queue = deque(i+1 for i in range(n))

cnt = 0
for i in range(m):
    if queue[0] != tar[i]:
        if queue.index(tar[i]) <= len(queue)//2:
            while queue[0] != tar[i]:
                queue.append(queue.popleft())
                cnt += 1
        else:
            while queue[0] != tar[i]:
                queue.appendleft(queue.pop())
                cnt += 1
    queue.popleft()

print(cnt)