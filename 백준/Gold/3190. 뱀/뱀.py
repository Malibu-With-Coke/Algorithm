import sys

input = sys.stdin.readline

from collections import deque

n = int(input())
apple_count = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(apple_count):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = 1  # apple
move_total_count = int(input())
moves = []
for _ in range(move_total_count):
    move_time, direction = input().split()
    moves.append((int(move_time), direction))
moves.append((10e9, "E"))


def change(dx, dy, next_dir):
    if next_dir == "L":  # left
        if dx == -1 and dy == 0:
            return 0, -1
            dx = 0
            dy = -1
        elif dx == 0 and dy == -1:
            return 1, 0
            dx = 1
            dy = 0
        elif dx == 1 and dy == 0:
            return 0, 1
            dx = 0
            dy = 1
        elif dx == 0 and dy == 1:
            return -1, 0
            dx = -1
            dy = 0
    else:  # left
        if dx == -1 and dy == 0:
            return 0, 1
            dx = 0
            dy = 1
        elif dx == 0 and dy == 1:
            return 1, 0
            dx = 1
            dy = 0
        elif dx == 1 and dy == 0:
            return 0, -1
            dx = 0
            dy = -1
        elif dx == 0 and dy == -1:
            return -1, 0
            dx = -1
            dy = 0


cur_time = 0
move_lst_idx = 0
cur_dx = 0
cur_dy = 1
cur_x = 0
cur_y = 0
snake = deque()
snake.append((0, 0))

while True:
    # print(cur_time)
    # print(matrix)
    # print(cur_dx, cur_dy)
    # print()
    cur_time += 1
    cur_x += cur_dx
    cur_y += cur_dy

    if (not (0 <= cur_x < n) or not (0 <= cur_y < n)) or matrix[cur_x][cur_y] == -1:
        break

    if matrix[cur_x][cur_y] != 1:
        tail_left_x, tail_left_y = snake.popleft()
        matrix[tail_left_x][tail_left_y] = 0
    matrix[cur_x][cur_y] = -1
    snake.append((cur_x, cur_y))

    if moves[move_lst_idx][0] == cur_time:

        cur_dx, cur_dy = change(cur_dx, cur_dy, moves[move_lst_idx][1])
        move_lst_idx += 1

print(cur_time)
