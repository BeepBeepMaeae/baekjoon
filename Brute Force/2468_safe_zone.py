import sys
sys.setrecursionlimit(100000)

n = int(input())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# DFS,  연결된 안전 영역 전체 방문
def dfs(x, y, visited, area):
    visited[y][x] = True  # 방문 체크
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 지도 범위 안에 있고, 방문하지 않았고, 안전 영역인 경우
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[ny][nx] and area[ny][nx] == 1:
                dfs(nx, ny, visited, area)

max_safe = 0
max_height = max(map(max, li))

for rain in range(0, max_height):
    # 안전 지역은 1, 아닌 것은 0
    area = [[1 if li[y][x] > rain else 0 for x in range(n)] for y in range(n)]
    # 방문 여부 기록
    visited = [[False] * n for _ in range(n)]
    safe_zone_count = 0  # 현재 비의 높이에서 안전 영역 개수
    # 안전 영역 탐색
    for y in range(n):
        for x in range(n):
            if area[y][x] == 1 and not visited[y][x]:
                dfs(x, y, visited, area)  # 연결된 영역 전부 방문 처리
                safe_zone_count += 1
    max_safe = max(max_safe, safe_zone_count)

print(max_safe)