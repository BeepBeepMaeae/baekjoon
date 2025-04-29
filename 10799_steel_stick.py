stack = []
cnt = 0
str = list(input().strip())
for i in range(len(str)):
    if str[i] == "(":       
        stack.append("(") # 스택에 추가 (쇠막대기의 시작 혹은 레이저의 시작)
    else:      
        stack.pop() # 열린 괄호를 스택에서 제거 (쇠막대기 끝 또는 레이저)
        if str[i-1] == "(": # 바로 직전 문자가 열린 괄호라면, 레이저인 경우
            cnt += len(stack) # 현재 스택의 길이만큼 쇠막대기가 잘리므로 더해줌
        else: # 바로 직전 문자가 닫힌 괄호라면, 쇠막대기가 끝나는 지점
            cnt += 1 # 쇠막대기의 끝 조각이므로 1을 더해줌

print(cnt)