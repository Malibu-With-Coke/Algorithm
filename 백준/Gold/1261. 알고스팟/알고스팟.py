import sys

input = sys.stdin.readline
INF = 1e9

m, n = map(int, input().split())

miro = [list(input().rstrip()) for _ in range(n)]

from collections import deque

deq = deque()
already_visited = [[False for _ in range(m)] for _ in range(n)]
already_visited[0][0] = True
deq.append((0, 0, 0))

while deq:
    x, y, block_count = deq.popleft()
    if x == n - 1 and y == m - 1:
        break

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if 0 <= dx + x < n and 0 <= dy + y < m and not already_visited[dx + x][dy + y]:
            already_visited[dx + x][dy + y] = True
            if miro[dx + x][dy + y] == "1":
                deq.append((dx + x, dy + y, block_count + 1))
            else:
                deq.appendleft((dx + x, dy + y, block_count))

print(block_count)
