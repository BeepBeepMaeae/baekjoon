import sys

n = int(input())

for i in range(n):
    str = sys.stdin.readline().strip()
    num_a = str.count("a")
    if num_a>len(str)-num_a:
        print(len(str)-num_a)
    else:
        print(num_a)