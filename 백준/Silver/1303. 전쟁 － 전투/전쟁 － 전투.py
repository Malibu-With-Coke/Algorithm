row, column = map(int, input().split())

matrix = [list(input()) for _ in range(column)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, word):
    matrix[x][y] = 'E'
    count = 1
    for i in range(4):
        a = dx[i] + x
        b = dy[i] + y
        if (0<= a < column and 0<= b < row and matrix[a][b] == word):
            count += dfs(a, b, word)
    return count

w_count = 0
b_count = 0
for i in range(column):
    for j in range(row):
        if matrix[i][j] == 'W':
            w_count += pow(dfs(i,j,'W'),2)
        elif matrix[i][j] == 'B':
            b_count += pow(dfs(i,j,'B'),2)

print(w_count, b_count)