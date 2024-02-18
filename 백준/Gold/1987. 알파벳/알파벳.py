import sys

input = sys.stdin.readline

row, column = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(row)]

alpha_visted = [0] * 26
max_move_count = 1


def dfs(a, b, move_count):
    global max_move_count
    if max_move_count < move_count:
        max_move_count = move_count
    for da, db in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if (
            0 <= a + da < row
            and 0 <= b + db < column
            and not alpha_visted[board[a + da][b + db]]
        ):
            alpha_visted[board[a + da][b + db]] = True
            dfs(a + da, b + db, move_count + 1)
            alpha_visted[board[a + da][b + db]] = False


alpha_visted[board[0][0]] = True
dfs(0, 0, 1)
print(max_move_count)