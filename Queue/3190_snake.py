from collections import deque
import sys

# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
k = int(input())

board = [[0 for _ in range(n)] for _ in range(n)] # 0은 빈 칸, 1은 뱀, 2는 사과
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 2 # 사과 위치 표시

l = int(input()) # 방향 변환 횟수
directions = []
for _ in range(l):
    x, c = sys.stdin.readline().split()
    directions.append((int(x), c)) # 방향 변환 시간과 방향 저장

# 뱀의 초기 위치와 방향
snake = deque([(0, 0)]) # 뱀의 초기 머리 위치 (0, 0)
board[0][0] = 1 # 뱀의 머리가 있는 곳
current_dir = 0 # 초기 방향 = 오른쪽
time = 0
dir_idx = 0 # 방향 변환 목록 인덱스

while True:
    time += 1  # 시간이 1초 증가
    # 뱀 이동
    head_x, head_y = snake[0] # 뱀 머리 위치
    new_x, new_y = head_x + dx[current_dir], head_y + dy[current_dir]
    
    # 게임 종료 조건: 벽 또는 자기 몸에 부딪혔을 때
    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or board[new_x][new_y] == 1:
        break
    
    # 뱀 이동
    snake.appendleft((new_x, new_y)) # 머리 추가
    if board[new_x][new_y] == 2: # 사과가 있을 때
        board[new_x][new_y] = 1 # 사과 제거
    else:  # 사과가 없으면 꼬리 위치 제거
        tail_x, tail_y = snake.pop()
        board[tail_x][tail_y] = 0  # 빈 칸으로
    
    board[new_x][new_y] = 1  # 뱀의 새로운 머리 위치
    
    # 방향 변경
    if dir_idx < l and time == directions[dir_idx][0]:
        if directions[dir_idx][1] == 'D':
            current_dir = (current_dir + 1) % 4 # 오른쪽 90도 회전
        else:
            current_dir = (current_dir - 1) % 4 # 왼쪽 90도 회전
        dir_idx += 1 # 방향 변환 인덱스 증가

print(time)