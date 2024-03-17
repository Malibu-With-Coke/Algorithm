import sys

input = sys.stdin.readline

from collections import deque

RIGHT = 1
LEFT = 2
BACK = 3
FRONT = 4

n, m, x, y, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

vertical = [0, 0, 0, 0]
horizontal = [0, 0, 0, 0]


def rotate_list(lst, turn_front=True):
    temp = deque(lst)
    if turn_front:
        temp.rotate(-1)
    else:
        temp.rotate()

    return list(temp)


def rolling_dice(vertical_dice, horizontal_dice, turn):
    if turn == LEFT:
        horizontal_dice = rotate_list(horizontal_dice, turn_front=False)
        vertical_dice[0] = horizontal_dice[0]
        vertical_dice[2] = horizontal_dice[2]
    elif turn == RIGHT:
        horizontal_dice = rotate_list(horizontal_dice, turn_front=True)
        vertical_dice[0] = horizontal_dice[0]
        vertical_dice[2] = horizontal_dice[2]
    elif turn == BACK:
        vertical_dice = rotate_list(vertical_dice, turn_front=False)
        horizontal_dice[0] = vertical_dice[0]
        horizontal_dice[2] = vertical_dice[2]
    elif turn == FRONT:
        vertical_dice = rotate_list(vertical_dice, turn_front=True)
        horizontal_dice[0] = vertical_dice[0]
        horizontal_dice[2] = vertical_dice[2]

    return vertical_dice, horizontal_dice


for order in orders:

    if order == LEFT:
        dx = 0
        dy = -1
    elif order == RIGHT:
        dx = 0
        dy = 1
    elif order == BACK:
        dx = -1
        dy = 0
    elif order == FRONT:
        dx = 1
        dy = 0

    if 0 <= x + dx < n and 0 <= y + dy < m:
        x += dx
        y += dy
        # print(vertical, horizontal)
        vertical, horizontal = rolling_dice(vertical, horizontal, order)
        # print(vertical, horizontal)
        # print()

        if matrix[x][y] == 0:
            matrix[x][y] = horizontal[0]

        else:
            horizontal[0] = vertical[0] = matrix[x][y]
            matrix[x][y] = 0
        print(horizontal[2])
