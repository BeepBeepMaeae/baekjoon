n, k = map(int,input().split())

array = [False for _ in range(n + 1)]
cnt = 0

for i in range(2, n+1):
    for j in range(i, n+1, i):
        if array[j] == False:
            array[j] = True
            cnt+=1
            if(cnt == k):
                print(j)