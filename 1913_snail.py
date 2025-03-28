import sys
input = sys.stdin.readline

size = int(input())
target = int(input())
snail = [[0] * size for _ in range(size)]

center = size // 2
x, y = center, center
snail[x][y] = 1

move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

current_num = 2
move_length = 1
direction = 0

while current_num <= size * size:
    for _ in range(2):
        for _ in range(move_length):
            if current_num > size * size:
                break
            x += move_x[direction]
            y += move_y[direction]
            snail[x][y] = current_num
            current_num += 1
        direction = (direction + 1) % 4
    move_length += 1

for row in snail:
    print(*row)

for i in range(size):
    for j in range(size):
        if snail[i][j] == target:
            print(i + 1, j + 1)
            break