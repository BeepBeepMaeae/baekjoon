import sys

n = int(input())
for _ in range(n):
    m = int(sys.stdin.readline())
    cnt = [0,0]
    for _ in range(m):
        a, b = sys.stdin.readline().split()
        if a == b:
            continue
        elif a == "R" and b == "P":
            cnt[1]+=1
        elif a == "P" and b == "S":
            cnt[1]+=1
        elif a == "S" and b == "R":
            cnt[1]+=1
        else:
            cnt[0]+=1
    if(cnt[0]>cnt[1]):
        print("Player 1")
    elif(cnt[0]==cnt[1]):
        print("TIE")
    else:
        print("Player 2")