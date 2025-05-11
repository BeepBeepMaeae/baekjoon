n = int(input())
arr = input()

couple = arr.count("LL")

if couple <= 1:
    print(n)
else:
    print(n+1-couple)