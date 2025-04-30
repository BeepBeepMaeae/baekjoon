n, b = input().split()
num = list(n)

result = 0
for i in range(len(num)):
    if ord(num[i])>=65 and ord(num[i])<=90:
        result += (int(b)**(len(num)-i-1)) * (ord(num[i])-55)
    else:
        result += (int(b)**(len(num)-i-1)) * int(num[i])

print(result)