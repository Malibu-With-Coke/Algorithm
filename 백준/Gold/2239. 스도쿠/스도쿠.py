import sys

input = sys.stdin.readline

board = [list(input().rstrip()) for _ in range(9)]

row = [[False for _ in range(10)] for _ in range(9)]
column = [[False for _ in range(10)] for _ in range(9)]
block = [[False for _ in range(10)] for _ in range(9)]


def getBlockIdx(i, j):
    if i < 3:
        if j < 3:
            return 0
        elif j < 6:
            return 1
        else:
            return 2
    elif i < 6:
        if j < 3:
            return 3
        elif j < 6:
            return 4
        else:
            return 5
    else:
        if j < 3:
            return 6
        elif j < 6:
            return 7
        else:
            return 8


def complete_board(idx):
    if idx == total_zero_count:
        for one_line in board:
            for one in one_line:
                print(one, end="")
            print()
        exit()

    i, j = zero_list[idx]
    for num in range(1, 10):
        if not row[i][num] and not column[j][num] and not block[getBlockIdx(i, j)][num]:
            row[i][num] = True
            column[j][num] = True
            block[getBlockIdx(i, j)][num] = True
            board[i][j] = num

            complete_board(idx + 1)

            row[i][num] = False
            column[j][num] = False
            block[getBlockIdx(i, j)][num] = False
            board[i][j] = 0


zero_list = []
for i in range(9):
    for j in range(9):
        board[i][j] = int(board[i][j])
        if board[i][j] > 0:
            row[i][board[i][j]] = True
            column[j][board[i][j]] = True
            block[getBlockIdx(i, j)][board[i][j]] = True
        else:
            zero_list.append((i, j))
total_zero_count = len(zero_list)
complete_board(0)
