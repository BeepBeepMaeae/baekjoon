a, b, c, m = map(int,input().split())

fati = 0
result = 0
for _ in range(24):
    if fati+a>m:
        fati-=c
        if(fati<0):
            fati=0
    else:
        fati+=a
        result+=b
print(result)