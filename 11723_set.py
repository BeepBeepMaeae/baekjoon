import sys

n = int(input())
s = set()

for _ in range(n):
    li = sys.stdin.readline().strip().split()

    if len(li) == 1:
        if li[0] == "all":
            s = {i for i in range(1, 21)}
        elif li[0] == "empty":
            s.clear()
    else:
        a, b = li[0], int(li[1])

        if a == "add":
            s.add(b)
        elif a == "remove":
            s.discard(b)
        elif a == "check":
            print(1 if b in s else 0)
        elif a == "toggle":
            if b in s:
                s.remove(b)
            else:
                s.add(b)