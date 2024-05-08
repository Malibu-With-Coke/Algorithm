import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(n)]
can_move = [[0 for _ in range(m)] for _ in range(n)]
already_visited = [[False for _ in range(m)] for _ in range(n)]
coloring = [[0 for _ in range(m)] for _ in range(n)]
break_walls = [[0 for _ in range(m)] for _ in range(n)]

from collections import deque

deq = deque()
color_idx = 1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0 and not already_visited[i][j]:
            deq.append((i, j))
            same_area = [(i, j)]
            already_visited[i][j] = True
            while deq:
                a, b = deq.popleft()

                for da, db in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if (
                        0 <= a + da < n
                        and 0 <= b + db < m
                        and not already_visited[a + da][b + db]
                        and matrix[a + da][b + db] == 0
                    ):
                        deq.append((a + da, b + db))
                        already_visited[a + da][b + db] = True
                        same_area.append((a + da, b + db))

            extent = len(same_area)
            for a, b in same_area:
                can_move[a][b] = extent
                coloring[a][b] = color_idx
            color_idx += 1

# for line in can_move:
#     print(*line)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            can_move_cnt = 1
            coloring_idx = []
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (
                    0 <= i + di < n
                    and 0 <= j + dj < m
                    and can_move[i + di][j + dj] > 0
                    and coloring[i + di][j + dj] not in coloring_idx
                ):
                    can_move_cnt += can_move[i + di][j + dj]
                    coloring_idx.append(coloring[i + di][j + dj])

            break_walls[i][j] = can_move_cnt % 10

# for line in can_move:
#     print(*line)
# print()
for line in break_walls:
    for item in line:
        print(item, end="")
    print()
