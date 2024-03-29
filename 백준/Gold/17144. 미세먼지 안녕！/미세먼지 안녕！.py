import sys

input = sys.stdin.readline

row, column, end_time = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]
air_cleaner = []
for r in range(row):
    if matrix[r][0] == -1:
        air_cleaner.append(r)


def spread_dust(matrix):
    next_matrix = [[0 for _ in range(column)] for _ in range(row)]

    for i in range(row):
        for j in range(column):
            if matrix[i][j] > 0:
                amount_spread = matrix[i][j]
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if (
                        0 <= i + di < row
                        and 0 <= j + dj < column
                        and matrix[i + di][j + dj] != -1
                    ):
                        next_matrix[i + di][j + dj] += matrix[i][j] // 5
                        amount_spread -= matrix[i][j] // 5
                next_matrix[i][j] += amount_spread

    next_matrix[air_cleaner[0]][0] = -1
    next_matrix[air_cleaner[1]][0] = -1

    return next_matrix


def cleaning(matrix):
    # 1
    for i in range(air_cleaner[0], 0, -1):
        matrix[i][0] = matrix[i - 1][0]

    for i in range(column - 1):
        matrix[0][i] = matrix[0][i + 1]

    for i in range(air_cleaner[0]):
        matrix[i][column - 1] = matrix[i + 1][column - 1]

    for i in range(column - 1, 1, -1):
        matrix[air_cleaner[0]][i] = matrix[air_cleaner[0]][i - 1]

    # 2
    for i in range(air_cleaner[1], row - 1):
        matrix[i][0] = matrix[i + 1][0]

    for i in range(column - 1):
        matrix[row - 1][i] = matrix[row - 1][i + 1]

    for i in range(row - 1, air_cleaner[1], -1):
        matrix[i][column - 1] = matrix[i - 1][column - 1]

    for i in range(column - 1, 1, -1):
        matrix[air_cleaner[1]][i] = matrix[air_cleaner[1]][i - 1]

    matrix[air_cleaner[0]][0] = -1
    matrix[air_cleaner[1]][0] = -1
    matrix[air_cleaner[0]][1] = 0
    matrix[air_cleaner[1]][1] = 0


for _ in range(end_time):
    matrix = spread_dust(matrix)

    cleaning(matrix)

rest_dust = 0
for i in range(row):
    rest_dust += sum(matrix[i])

rest_dust += 2
print(rest_dust)
