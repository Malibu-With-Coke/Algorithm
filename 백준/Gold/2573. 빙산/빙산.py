import sys

input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    que = deque([(x, y)])
    visited[x][y] = 1
    seaList = []

    while que:
        x, y  = que.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not matrix[nx][ny]:
                    sea += 1
                elif not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x, y, sea))

    for x, y, sea in seaList:
        matrix[x][y] = max(0, matrix[x][y] - sea)

    return 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            ice.append((i, j))

while ice:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if matrix[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if matrix[i][j] == 0:
            delList.append((i, j))

    if group > 1:
        print(year)
        break

    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)