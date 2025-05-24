import sys

n = int(input())

road = list(map(int, sys.stdin.readline().split()))
station = list(map(int, sys.stdin.readline().split()))

result = 0
min_station = station[0]  # 처음 도시의 주유소 가격

for i in range(len(road)):
    # 주유소 가격이 더 싸면 갱신
    if station[i] < min_station:
        min_station = station[i]
    # 현재 구간의 거리 * 최소 주유소 가격
    result += min_station * road[i]

print(result)
