import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "I":
            deq = deque()
            deq.append((i, j))

            while deq:
                x, y = deq.popleft()

                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nx = dx + x
                    ny = dy + y
                    
                    if 0 <= nx < n and 0 <= ny < m and (matrix[nx][ny] == "O" or matrix[nx][ny] == "P"):
                        if matrix[nx][ny] == "P":
                            ans += 1
                        deq.append((nx, ny))
                        matrix[nx][ny] = "X"
            break

print(ans if ans != 0 else "TT")