import sys

input = sys.stdin.readline

matrix = [list(map(int, input().split())) for _ in range(9)]

rows = [[False for _ in range(9)] for _ in range(9)]
columns = [[False for _ in range(9)] for _ in range(9)]
boxes = [[False for _ in range(9)] for _ in range(9)]

zeros = []


def where_is_box(i, j):
    if i < 3 and j < 3:
        return 0
    elif i < 3 and j < 6:
        return 1
    elif i < 3 and j < 9:
        return 2
    elif i < 6 and j < 3:
        return 3
    elif i < 6 and j < 6:
        return 4
    elif i < 6 and j < 9:
        return 5
    elif i < 9 and j < 3:
        return 6
    elif i < 9 and j < 6:
        return 7
    else:
        return 8


for i in range(9):
    for j in range(9):
        if matrix[i][j] == 0:
            zeros.append((i, j))
        else:
            rows[i][matrix[i][j] - 1] = True
            columns[j][matrix[i][j] - 1] = True
            temp = where_is_box(i, j)
            boxes[temp][matrix[i][j] - 1] = True


def solve(num, max):
    if num == max:
        for i in range(9):
            for j in range(9):
                print(matrix[i][j], end=" ")
            print()

        exit(0)
    i, j = zeros[num]
    temp = where_is_box(i, j)
    for n in range(9):
        if not rows[i][n] and not columns[j][n] and not boxes[temp][n]:
            rows[i][n] = True
            columns[j][n] = True
            boxes[temp][n] = True
            matrix[i][j] = n + 1

            solve(num + 1, max)

            rows[i][n] = False
            columns[j][n] = False
            boxes[temp][n] = False


solve_num = len(zeros)

solve(0, solve_num)