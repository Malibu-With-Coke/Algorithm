from collections import deque

column, row = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(row)]

# print(matrix)

deq = deque()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    global count
    while deq:
        x, y, count = deq.popleft()
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if (0 <= a < row and 0 <= b < column and matrix[a][b] == 0):
                deq.append([a, b, count+1])
                matrix[a][b] = 1

for i in range(row):
    for j in range(column):
        if matrix[i][j] == 1:
            deq.append([i, j, 0])

bfs()

for i in range(row):
    for j in range(column):
        if matrix[i][j] == 0:
            print(-1)
            exit()

print(count)