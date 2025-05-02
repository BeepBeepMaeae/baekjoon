def trans(string, notation):
    tmp=0
    for i in range(len(string)):
        tmp+=((int(notation)**i)*numbers[string[-1-i]])
    return tmp

a, b= input().split()

numbers = dict()
count = 0
result = [0,0]

for i in range(0, 10):
    numbers[str(i)] = i
for i in range(26):
    numbers[chr(97+i)] = i+10

a_max = max(list(a))
b_max = max(list(b))

for i in range(numbers[a_max]+1,37):
    for j in range(numbers[b_max]+1,37):
        if i == j:
            continue
        if trans(a,i) == trans(b,j):
            if trans(a,i) >= 2**63:
                continue
            result[0]=i
            result[1]=j
            count += 1

if count == 0:
    print("Impossible")
elif count > 1:
    print("Multiple")
elif count == 1:
    print(trans(a,result[0]),result[0],result[1])