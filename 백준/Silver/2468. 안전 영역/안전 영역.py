import sys

input = sys.stdin.readline
from collections import deque

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_num = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] > max_num:
            max_num = matrix[i][j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


result = 0
for i in range(max_num):
    visited = [[False] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if matrix[j][k] > i and not visited[j][k]:
                bfs(j, k, i, visited)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)
