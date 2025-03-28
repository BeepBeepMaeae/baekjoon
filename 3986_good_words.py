n = int(input())
cnt = 0

for _ in range(n):
    stack = []
    str = list(input())
    for i in str:
        if not len(stack):
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)

    if not len(stack):
        cnt += 1 

print(cnt)