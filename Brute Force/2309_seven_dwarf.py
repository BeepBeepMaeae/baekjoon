def dwarf():
    li = []
    for _ in range(9):
        li.append(int(input()))

    s = sum(li)

    # 두 명을 뺐을 때 나머지 7명의 합이 100이 되는 경우를 찾음
    for i in range(0, 9):
        for j in range(i + 1, 9):
            result = s - li[i] - li[j]  # i번째와 j번째 난쟁이를 제외한 합
            if result == 100:
                li.pop(j)      # j번째 난쟁이 제거
                li.pop(i)      # i번째 난쟁이 제거 (j보다 앞에 있어야 함)
                li.sort()
                for i in range(7):
                    print(li[i])
                exit() 

dwarf()