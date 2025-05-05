n = int(input())
cnt = 0

for _ in range(n):
    stack = []
    str = list(input())

    for i in str:
        if not len(stack):  # 스택이 비었으면 추가
            stack.append(i)
        elif stack[-1] == i:  # 같은 문자가 연속되면 제거
            stack.pop(-1)
        else:
            stack.append(i)  # 다르면 스택에 추가

    if not len(stack):  # 스택이 비었으면 좋은 단어
        cnt += 1

print(cnt)