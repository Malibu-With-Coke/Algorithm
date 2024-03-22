import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

cctvs = []
minimum_blind_spot = n * m


def view_cctv(line_idx, isrow, mat):
    if isrow:
        for k in range(m):
            if mat[line_idx][k] == 0:
                mat[line_idx][k] = -1
            elif mat[line_idx][k] == 6:
                break
    else:
        for k in range(n):
            if mat[k][line_idx] == 0:
                mat[k][line_idx] = -1
            elif mat[k][line_idx] == 6:
                break


def view_up(mat, cur_row, cur_col):
    for k in range(cur_row - 1, -1, -1):
        if mat[k][cur_col] == 0:
            mat[k][cur_col] = -1
        elif mat[k][cur_col] == 6:
            break


def view_down(mat, cur_row, cur_col):
    for k in range(cur_row + 1, n):
        if mat[k][cur_col] == 0:
            mat[k][cur_col] = -1
        elif mat[k][cur_col] == 6:
            break


def view_left(mat, cur_row, cur_col):
    for k in range(cur_col - 1, -1, -1):
        if mat[cur_row][k] == 0:
            mat[cur_row][k] = -1
        elif mat[cur_row][k] == 6:
            break


def view_right(mat, cur_row, cur_col):
    for k in range(cur_col + 1, m):
        if mat[cur_row][k] == 0:
            mat[cur_row][k] = -1
        elif mat[cur_row][k] == 6:
            break


def find_minimum_blind_spot(depth, mat):
    if depth == len(cctvs):
        global minimum_blind_spot
        count_blind_spot = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    count_blind_spot += 1

        # view_matrix(mat)
        minimum_blind_spot = min(minimum_blind_spot, count_blind_spot)
        return

    cctv_r, cctv_c, cctv_ver = cctvs[depth]
    if cctv_ver == 1:
        for i in range(4):
            temp_mat = copy.deepcopy(mat)
            if i == 0:
                view_up(temp_mat, cctv_r, cctv_c)
            elif i == 1:
                view_down(temp_mat, cctv_r, cctv_c)
            elif i == 2:
                view_left(temp_mat, cctv_r, cctv_c)
            elif i == 3:
                view_right(temp_mat, cctv_r, cctv_c)

            find_minimum_blind_spot(depth + 1, temp_mat)

    elif cctv_ver == 2:
        for i in range(2):
            temp_mat = copy.deepcopy(mat)
            if i == 0:
                view_up(temp_mat, cctv_r, cctv_c)
                view_down(temp_mat, cctv_r, cctv_c)
            elif i == 1:
                view_left(temp_mat, cctv_r, cctv_c)
                view_right(temp_mat, cctv_r, cctv_c)

            find_minimum_blind_spot(depth + 1, temp_mat)

    elif cctv_ver == 3:
        for i in range(4):
            temp_mat = copy.deepcopy(mat)
            if i == 0:
                view_up(temp_mat, cctv_r, cctv_c)
                view_right(temp_mat, cctv_r, cctv_c)

            elif i == 1:
                view_down(temp_mat, cctv_r, cctv_c)
                view_right(temp_mat, cctv_r, cctv_c)

            elif i == 2:
                view_down(temp_mat, cctv_r, cctv_c)
                view_left(temp_mat, cctv_r, cctv_c)

            elif i == 3:
                view_up(temp_mat, cctv_r, cctv_c)
                view_left(temp_mat, cctv_r, cctv_c)

            find_minimum_blind_spot(depth + 1, temp_mat)

    elif cctv_ver == 4:
        for i in range(4):
            temp_mat = copy.deepcopy(mat)
            if i == 0:
                view_down(temp_mat, cctv_r, cctv_c)
                view_left(temp_mat, cctv_r, cctv_c)
                view_right(temp_mat, cctv_r, cctv_c)

            elif i == 1:
                view_up(temp_mat, cctv_r, cctv_c)
                view_left(temp_mat, cctv_r, cctv_c)
                view_right(temp_mat, cctv_r, cctv_c)

            elif i == 2:
                view_up(temp_mat, cctv_r, cctv_c)
                view_down(temp_mat, cctv_r, cctv_c)
                view_right(temp_mat, cctv_r, cctv_c)

            elif i == 3:
                view_up(temp_mat, cctv_r, cctv_c)
                view_down(temp_mat, cctv_r, cctv_c)
                view_left(temp_mat, cctv_r, cctv_c)

            find_minimum_blind_spot(depth + 1, temp_mat)


for i in range(n):
    for j in range(m):
        if 1 <= matrix[i][j] <= 4:
            cctvs.append((i, j, matrix[i][j]))
        elif matrix[i][j] == 5:
            view_up(matrix, i, j)
            view_down(matrix, i, j)
            view_left(matrix, i, j)
            view_right(matrix, i, j)


def view_matrix(print_matrix):
    for i in range(n):
        print(*print_matrix[i])
    print()


# view_matrix()
find_minimum_blind_spot(0, matrix)

print(minimum_blind_spot)
