import sys

input = sys.stdin.readline

curv_n = int(input())
curves = [list(map(int, input().split())) for _ in range(curv_n)]
matrix = [[0 for _ in range(101)] for _ in range(101)]

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3


def get_dxdy(direction):
    if direction == RIGHT:
        return (0, 1)
    if direction == UP:
        return (-1, 0)
    if direction == LEFT:
        return (0, -1)
    if direction == DOWN:
        return (1, 0)


def turn_move(direction):
    if direction == RIGHT:
        return UP
    if direction == UP:
        return LEFT
    if direction == LEFT:
        return DOWN
    if direction == DOWN:
        return RIGHT


# def one_move(direction):
#     if direction == RIGHT:
#         return ((0, 0), (0, 1), (-1, 1))
#     if direction == UP:
#         return ((0, 0), (-1, 0), (-1, -1))
#     if direction == LEFT:
#         return ((0, 0), (0, -1), (1, -1))
#     if direction == DOWN:
#         return ((0, 0), (1, 0), (1, 1))


# def two_move(direction):
#     if direction == RIGHT:
#         return ((0, 0), (0, 1), (-1, 1), (-1, 0), (-2, 0))
#     if direction == UP:
#         return ((0, 0), (-1, 0), (-1, -1), (0, -1), (0, -2))
#     if direction == LEFT:
#         return ((0, 0), (0, -1), (1, -1), (1, 0), (2, 0))
#     if direction == DOWN:
#         return ((0, 0), (1, 0), (1, 1), (0, 1), (0, 2))


# def three_move(direction):
#     if direction == RIGHT:
#         return (
#             (0, 0),
#             (0, 1),
#             (-1, 1),
#             (-1, 0),
#             (-2, 0),
#             (-2, -1),
#             (-1, -1),
#             (-1, -2),
#             (-2, -2),
#         )
#     if direction == UP:
#         return (
#             (0, 0),
#             (-1, 0),
#             (-1, -1),
#             (0, -1),
#             (0, -2),
#             (1, -2),
#             (1, -1),
#             (2, -1),
#             (2, -2),
#         )
#     if direction == LEFT:
#         return (
#             (0, 0),
#             (0, -1),
#             (1, -1),
#             (1, 0),
#             (2, 0),
#             (2, 1),
#             (1, 1),
#             (1, 2),
#             (2, 2),
#         )
#     if direction == DOWN:
#         return (
#             (0, 0),
#             (1, 0),
#             (1, 1),
#             (0, 1),
#             (0, 2),
#             (-1, 2),
#             (-1, 1),
#             (-2, 1),
#             (-2, 2),
#         )


def get_movement(generation, direction):
    movement = [direction]

    for cnt in range(generation):
        next_movement = []
        for idx in range(len(movement) - 1, -1, -1):
            move = movement[idx]
            next_movement.append(turn_move(move))
        movement.extend(next_movement)
    return movement


for y, x, direction, generation in curves:

    movement = get_movement(generation, direction)

    matrix[x][y] = 1
    for next_dir in movement:
        dx, dy = get_dxdy(next_dir)
        x += dx
        y += dy
        matrix[x][y] = 1

square_cnt = 0
for i in range(100):
    for j in range(100):
        if (
            matrix[i][j]
            and matrix[i + 1][j]
            and matrix[i][j + 1]
            and matrix[i + 1][j + 1]
        ):
            square_cnt += 1

print(square_cnt)
