stack = []
cnt = 0
str = list(input().strip())
for i in range(len(str)):
    if str[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if str[i-1] == "(":
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)