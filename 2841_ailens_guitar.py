import sys

n, p = map(int, sys.stdin.readline().split())
stack = [[] for _ in range(n)]
cnt = 0

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    
    # 현재 줄의 스택이 비어있지 않고, 누르고 있는 프렛이 입력받은 프렛(b)보다 클 때
    while stack[a-1] and b < stack[a-1][-1]:
        stack[a-1].pop()
        cnt += 1
    
    # 스택이 비어있거나, 현재 누른 프렛이 스택의 마지막 프렛보다 클 때
    if not stack[a-1] or b > stack[a-1][-1]:
        stack[a-1].append(b)
        cnt += 1

print(cnt)