from collections import deque
import sys

n = int(input())
cm = list(map(int, sys.stdin.readline().split()))
queue = deque()

for i in range(n - 1, -1, -1):
    card = n - i
    if cm[i] == 1:
        queue.appendleft(card)
    elif cm[i] == 2:
        temp = queue.popleft()
        queue.appendleft(card)
        queue.appendleft(temp)
    elif cm[i] == 3:
        queue.append(card)

print(*queue)