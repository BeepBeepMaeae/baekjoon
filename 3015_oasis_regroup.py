import sys

input = sys.stdin.readline
n = int(input())
heights = [int(input()) for _ in range(n)]

stack = [] # 사람 키만 저장
count_stack = [] # 같은 키 몇 명인지 저장
ans = 0

for h in heights:
    cnt = 1  # 현재 키의 사람 수 (기본적으로 한 명)

    while stack:
        if stack[-1] < h:
            ans += count_stack[-1]
            stack.pop()
            count_stack.pop()
        elif stack[-1] == h:
            # 같은 키면 쌍을 모두 더하고 그룹화
            ans += count_stack[-1]
            cnt += count_stack[-1]
            stack.pop()
            count_stack.pop()
        else:
            # 더 큰 사람은 하나만 볼 수 있음
            ans += 1
            break
        
    stack.append(h)
    count_stack.append(cnt)

print(ans)