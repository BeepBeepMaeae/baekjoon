n = list(input())
stack = []

for i in range(len(n)):
    if n[i].isalpha():
        print(n[i], end="")
    else:
        if n[i] == "(":
            stack.append(n[i])
        elif n[i] == "*" or n[i] == "/":
            # 스택 최상단이 우선순위 이상이면 출력 후 현재 연산자를 스택에 추가
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                print(stack.pop(), end="")
            stack.append(n[i])
        elif n[i] == "+" or n[i] == "-":
            # 스택 최상단이 우선순위 이상이면 출력 후 현재 연산자를 스택에 추가
            while stack and (stack[-1] in ["*", "/", "+", "-"]):
                print(stack.pop(), end="")
            stack.append(n[i])
        elif n[i] == ")":
            # 열린 괄호를 만날 때까지 모든 연산자를 출력
            while stack and stack[-1] != "(":
                print(stack.pop(), end="")
            stack.pop()  # 열린 괄호 "(" 제거

# 스택에 남은 연산자를 모두 출력
while stack:
    print(stack.pop(), end="")