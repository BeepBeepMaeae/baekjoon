import sys

n = int(input())

li = []
for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

# 종료 시간 기준 정렬, 같으면 시작 시간 기준 정렬
li.sort(key=lambda x: (x[1], x[0]))

result = 0
end = 0 # 마지막으로 배정된 회의 종료 시간

for a, b in li:
    if end <= a: # 직전 회의가 끝난 이후에 시작하는 회의면 선택
        result += 1
        end = b # 회의 종료료 시간 갱신

print(result)