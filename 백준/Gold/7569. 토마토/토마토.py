from collections import deque

column, row, height = map(int, input().split())

matrix = [[list(map(int,input().split())) for _ in range(row)] for _ in range(height)]

# print(matrix[1][1][2])

deq = deque()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    global count
    while deq:
        x, y, z, count = deq.popleft()
        for i in range(6):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dz[i]
            if (0 <= a < row and 0 <= b < column and 0<= c < height and matrix[c][a][b] == 0):
                deq.append([a, b, c, count+1])
                matrix[c][a][b] = 1

for k in range(height):
    for i in range(row):
        for j in range(column):
            if matrix[k][i][j] == 1:
                deq.append([i, j, k, 0])

bfs()

for k in range(height):
    for i in range(row):
        for j in range(column):
            if matrix[k][i][j] == 0:
                print(-1)
                exit()

print(count)