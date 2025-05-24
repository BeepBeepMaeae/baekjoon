li = input().split('-')  # '-' 기준으로 나눠서 리스트로 저장
result = 0

for i in range(len(li)):
    # '+' 기준으로 나눠서 리스트로 저장
    lis = list(map(int, li[i].split('+')))
    if i == 0:
        # 첫 번째 항목을 더함
        result += sum(lis)
    else:
        # 괄호로 묶어서 모두 뺄셈
        result -= sum(lis)

print(result)