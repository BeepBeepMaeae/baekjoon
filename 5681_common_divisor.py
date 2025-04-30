import sys
import math

n = int(input())
li = list(map(int, sys.stdin.readline().split()))

result = li[0]
for i in range(1, len(li)):
    result = math.gcd(result, li[i])

divisors = set()
for i in range(1, int(math.sqrt(result)) + 1):
    if result % i == 0:
        divisors.add(i)
        divisors.add(result // i)

for d in sorted(divisors):
    print(d)