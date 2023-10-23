import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
ans = [[-1 for _ in range(m)] for _ in range(n)]

from collections import deque

deq = deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            deq.append((i, j, 1))
            ans[i][j] = 0
        elif matrix[i][j] == 0:
            ans[i][j] = 0
            

while deq:
    x, y, distance = deq.popleft()

    for d_x, d_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        next_x = d_x + x
        next_y = d_y + y
    
        if 0 <= next_x < n and 0 <= next_y < m and ans[next_x][next_y] == -1:
            ans[next_x][next_y] = distance
            deq.append((next_x, next_y, distance + 1))

for i in range(n):
    for j in range(m):
        print(ans[i][j], end=" ")
    print()