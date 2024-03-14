import sys

input = sys.stdin.readline

import copy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def merge(lst):
    merge_lst = []
    front_already_merge = False
    for block in lst:
        if block == 0:
            continue
        if merge_lst and merge_lst[-1] == block and front_already_merge == False:
            merge_lst.pop()
            merge_lst.append(block * 2)
            front_already_merge = True
        else:
            merge_lst.append(block)
            front_already_merge = False

    if len(merge_lst) < n:
        merge_lst = merge_lst + [0] * (n - len(merge_lst))

    return merge_lst


def left(matrix):
    for i in range(n):
        matrix[i] = merge(matrix[i])


def right(matrix):
    for i in range(n):
        matrix[i].reverse()
        matrix[i] = merge(matrix[i])
        matrix[i].reverse()


def up(matrix):
    for i in range(n):
        temp_lst = []
        for idx in range(n):
            temp_lst.append(matrix[idx][i])

        temp_lst = merge(temp_lst)

        for idx in range(n):
            matrix[idx][i] = temp_lst[idx]


def down(matrix):
    for i in range(n):
        temp_lst = []
        for idx in range(n - 1, -1, -1):
            temp_lst.append(matrix[idx][i])

        temp_lst = merge(temp_lst)
        temp_lst.reverse()

        for idx in range(n - 1, -1, -1):
            matrix[idx][i] = temp_lst[idx]


max_value = 0


def find_max_value(movement_count, cur_matrix):
    if movement_count == 5:
        global max_value
        for i in range(n):
            for j in range(n):
                if cur_matrix[i][j] > max_value:
                    max_value = cur_matrix[i][j]
        return

    for direction in range(4):
        temp_matrix = copy.deepcopy(cur_matrix)
        if direction == 0:
            left(temp_matrix)
        elif direction == 1:
            right(temp_matrix)
        elif direction == 2:
            down(temp_matrix)
        elif direction == 3:
            up(temp_matrix)

        find_max_value(movement_count + 1, temp_matrix)


find_max_value(0, board)
print(max_value)
