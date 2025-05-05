import math

a = int(input())
b = int(input())
array = [True for _ in range(b+1)]
prime = []

array[0] = False
array[1] = False

for i in range(2, int(math.sqrt(b)) + 1):
    if array[i]:
        for j in range(i * i, b + 1, i):
            array[j] = False            

for i in range(a,b+1):
    if array[i]:
        prime.append(i)

if(len(prime)>0):
    print(sum(prime))
    print(min(prime))
else:
    print(-1)