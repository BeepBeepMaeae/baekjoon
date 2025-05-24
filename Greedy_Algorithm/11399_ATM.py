import sys

n = int(input())
li = list(map(int, sys.stdin.readline().split()))

li.sort()  # 시간이 짧은 사람부터 정렬
result = 0


for i in range(n):
    result += sum(li[0:i+1]) # 앞 사람들 + 자기 시간

print(result)