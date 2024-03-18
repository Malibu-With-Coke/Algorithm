import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]


def robotCHHHIIIKINNGG(first_row, first_col, first_dir):
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    cur_row = first_row
    cur_col = first_col
    cur_dir = first_dir
    clean_count = 0

    while True:
        # for i in range(n):
        #     print(*matrix[i])
        # print()
        if matrix[cur_row][cur_col] == 0:
            matrix[cur_row][cur_col] = -1
            clean_count += 1

        nearby_dirty = False
        for dr, dc in direction:
            if (
                0 <= cur_row + dr < n
                and 0 <= cur_col + dc < m
                and matrix[cur_row + dr][cur_col + dc] == 0
            ):
                nearby_dirty = True

        if not nearby_dirty:
            dr, dc = direction[cur_dir - 2]
            cur_row += dr
            cur_col += dc
            if 0 <= cur_row < n and 0 <= cur_col < m and matrix[cur_row][cur_col] == -1:
                continue
            else:
                break

        if nearby_dirty:
            for i in range(1, 5):
                next_dir = (cur_dir - i) % 4
                dr, dc = direction[next_dir]
                if (
                    0 <= cur_row + dr < n
                    and 0 <= cur_col + dc < m
                    and matrix[cur_row + dr][cur_col + dc] == 0
                ):
                    cur_row += dr
                    cur_col += dc
                    cur_dir = next_dir
                    break
    print(clean_count)


robotCHHHIIIKINNGG(r, c, d)
