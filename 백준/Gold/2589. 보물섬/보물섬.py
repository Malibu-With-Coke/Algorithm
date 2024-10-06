import sys

input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]


def bfs(a, b):
    far = 0
    deq = deque()
    already_visited = [[False for _ in range(m)] for _ in range(n)]
    already_visited[a][b] = True
    deq.append((a, b, far))

    while deq:
        cur_a, cur_b, cur_far = deq.popleft()
        far = max(far, cur_far)

        for da, db in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (
                0 <= cur_a + da < n
                and 0 <= cur_b + db < m
                and board[cur_a + da][cur_b + db] == "L"
                and not already_visited[cur_a + da][cur_b + db]
            ):
                deq.append((cur_a + da, cur_b + db, cur_far + 1))
                already_visited[cur_a + da][cur_b + db] = True

    return far


max_far = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "L":
            max_far = max(max_far, bfs(i, j))

print(max_far)
