import sys

input = sys.stdin.readline

import copy

n, m = map(int, input().split())  # 세로 가로
ori_matrix = [list(input().rstrip()) for _ in range(n)]


def left(red_ball, blue_ball, matrix):
    one_goal = False
    goal_color = "N"
    if red_ball[1] <= blue_ball[1]:
        first_move_ball = red_ball
        second_move_ball = blue_ball
        first_move_ball_color = "R"
        second_move_ball_color = "B"
    else:
        first_move_ball = blue_ball
        second_move_ball = red_ball
        first_move_ball_color = "B"
        second_move_ball_color = "R"
    matrix[first_move_ball[0]][first_move_ball[1]] = "."
    while matrix[first_move_ball[0]][first_move_ball[1] - 1] == ".":
        first_move_ball[1] -= 1
    if matrix[first_move_ball[0]][first_move_ball[1] - 1] == "O":
        one_goal = True
        goal_color = first_move_ball_color
    else:
        matrix[first_move_ball[0]][first_move_ball[1]] = first_move_ball_color

    matrix[second_move_ball[0]][second_move_ball[1]] = "."
    while matrix[second_move_ball[0]][second_move_ball[1] - 1] == ".":
        second_move_ball[1] -= 1
    if matrix[second_move_ball[0]][second_move_ball[1] - 1] == "O":
        if one_goal:
            return -1
        one_goal = True
        goal_color = second_move_ball_color
    else:
        matrix[second_move_ball[0]][second_move_ball[1]] = second_move_ball_color

    if one_goal:
        if goal_color == "R":
            return 1
        else:
            return -1
    return 0


def right(red_ball, blue_ball, matrix):
    one_goal = False
    goal_color = "N"
    if red_ball[1] >= blue_ball[1]:
        first_move_ball = red_ball
        second_move_ball = blue_ball
        first_move_ball_color = "R"
        second_move_ball_color = "B"
    else:
        first_move_ball = blue_ball
        second_move_ball = red_ball
        first_move_ball_color = "B"
        second_move_ball_color = "R"

    matrix[first_move_ball[0]][first_move_ball[1]] = "."
    while matrix[first_move_ball[0]][first_move_ball[1] + 1] == ".":
        first_move_ball[1] += 1
    if matrix[first_move_ball[0]][first_move_ball[1] + 1] == "O":
        one_goal = True
        goal_color = first_move_ball_color
    else:
        matrix[first_move_ball[0]][first_move_ball[1]] = first_move_ball_color

    matrix[second_move_ball[0]][second_move_ball[1]] = "."
    while matrix[second_move_ball[0]][second_move_ball[1] + 1] == ".":
        second_move_ball[1] += 1
    if matrix[second_move_ball[0]][second_move_ball[1] + 1] == "O":
        if one_goal:
            return -1
        one_goal = True
        goal_color = second_move_ball_color
    else:
        matrix[second_move_ball[0]][second_move_ball[1]] = second_move_ball_color

    if one_goal:
        if goal_color == "R":
            return 1
        else:
            return -1
    return 0


def up(red_ball, blue_ball, matrix):
    one_goal = False
    goal_color = "N"
    if red_ball[0] <= blue_ball[0]:
        first_move_ball = red_ball
        second_move_ball = blue_ball
        first_move_ball_color = "R"
        second_move_ball_color = "B"
    else:
        first_move_ball = blue_ball
        second_move_ball = red_ball
        first_move_ball_color = "B"
        second_move_ball_color = "R"

    matrix[first_move_ball[0]][first_move_ball[1]] = "."
    while matrix[first_move_ball[0] - 1][first_move_ball[1]] == ".":
        first_move_ball[0] -= 1
    if matrix[first_move_ball[0] - 1][first_move_ball[1]] == "O":
        one_goal = True
        goal_color = first_move_ball_color
    else:
        matrix[first_move_ball[0]][first_move_ball[1]] = first_move_ball_color

    matrix[second_move_ball[0]][second_move_ball[1]] = "."
    while matrix[second_move_ball[0] - 1][second_move_ball[1]] == ".":
        second_move_ball[0] -= 1
    if matrix[second_move_ball[0] - 1][second_move_ball[1]] == "O":
        if one_goal:
            return -1
        one_goal = True
        goal_color = second_move_ball_color
    else:
        matrix[second_move_ball[0]][second_move_ball[1]] = second_move_ball_color

    if one_goal:
        if goal_color == "R":
            return 1
        else:
            return -1
    return 0


def down(red_ball, blue_ball, matrix):
    one_goal = False
    goal_color = "N"
    if red_ball[0] >= blue_ball[0]:
        first_move_ball = red_ball
        second_move_ball = blue_ball
        first_move_ball_color = "R"
        second_move_ball_color = "B"
    else:
        first_move_ball = blue_ball
        second_move_ball = red_ball
        first_move_ball_color = "B"
        second_move_ball_color = "R"

    matrix[first_move_ball[0]][first_move_ball[1]] = "."
    while matrix[first_move_ball[0] + 1][first_move_ball[1]] == ".":
        first_move_ball[0] += 1
    if matrix[first_move_ball[0] + 1][first_move_ball[1]] == "O":
        one_goal = True
        goal_color = first_move_ball_color
    else:
        matrix[first_move_ball[0]][first_move_ball[1]] = first_move_ball_color

    matrix[second_move_ball[0]][second_move_ball[1]] = "."
    while matrix[second_move_ball[0] + 1][second_move_ball[1]] == ".":
        second_move_ball[0] += 1
    if matrix[second_move_ball[0] + 1][second_move_ball[1]] == "O":
        if one_goal:
            return -1
        one_goal = True
        goal_color = second_move_ball_color
    else:
        matrix[second_move_ball[0]][second_move_ball[1]] = second_move_ball_color

    if one_goal:
        if goal_color == "R":
            return 1
        else:
            return -1
    return 0


for i in range(1, n - 1):
    for j in range(1, m - 1):
        if ori_matrix[i][j] == "B":
            blue_ball = [i, j]
        elif ori_matrix[i][j] == "R":
            red_ball = [i, j]

min_count = 11


def find_way(red_ball, blue_ball, matrix, count):
    # global total_cnt
    # total_cnt += 1
    # if total_cnt % 100000 == 0:
    #     print(total_cnt)
    global min_count
    if count >= min_count:
        return

    for i in range(4):
        status = -1
        rb = copy.deepcopy(red_ball)
        bb = copy.deepcopy(blue_ball)
        copy_matrix = copy.deepcopy(matrix)
        if i == 0 and (
            copy_matrix[rb[0]][rb[1] - 1] != "#" or copy_matrix[bb[0]][bb[1] - 1] != "#"
        ):
            status = left(rb, bb, copy_matrix)
        elif i == 1 and (
            copy_matrix[rb[0]][rb[1] + 1] != "#" or copy_matrix[bb[0]][bb[1] + 1] != "#"
        ):
            status = right(rb, bb, copy_matrix)
        elif i == 2 and (
            copy_matrix[rb[0] + 1][rb[1]] != "#" or copy_matrix[bb[0] + 1][bb[1]] != "#"
        ):
            status = down(rb, bb, copy_matrix)
        elif i == 3 and (
            copy_matrix[rb[0] - 1][rb[1]] != "#" or copy_matrix[bb[0] - 1][bb[1]] != "#"
        ):
            status = up(rb, bb, copy_matrix)

        if status == 1:
            min_count = min(min_count, count + 1)
            return
        elif status == 0:
            find_way(rb, bb, copy_matrix, count + 1)


find_way(red_ball, blue_ball, ori_matrix, 0)
# left(red_ball, blue_ball, ori_matrix)
# down(red_ball, blue_ball, ori_matrix)
# right(red_ball, blue_ball, ori_matrix)
# down(red_ball, blue_ball, ori_matrix)
# st = left(red_ball, blue_ball, ori_matrix)


print(min_count if min_count < 11 else -1)
