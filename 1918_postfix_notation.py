n = list(input())
stack = []
for i in range(len(n)):
    if n[i].isalpha():
        print(n[i],end="")
    else:
        if n[i] == "(":
            stack.append(n[i])
        elif n[i] == "*" or n[i] == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                print(stack.pop(),end="")
            stack.append(n[i])
        elif n[i] == "+" or n[i] == "-":
            while stack and (stack[-1] == "*" or stack[-1] == "/" or stack[-1] == "+" or stack[-1] == "-"):
                print(stack.pop(),end="")
            stack.append(n[i])
        elif n[i] == ")":
            while stack and (stack[-1] == "*" or stack[-1] == "/" or stack[-1] == "+" or stack[-1] == "-"):
                print(stack.pop(),end="")
            stack.pop()
while stack:
    print(stack.pop(),end="")