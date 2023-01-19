import sys
sys.setrecursionlimit(10**6)

column, row, trash = map(int,input().split())

matrix = [[0 for _ in range(row)] for __ in range(column)]

for _ in range(trash):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
    
def dfs(x, y):
    matrix[x][y] = 0
    count = 1
    for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
        a = dx + x
        b = dy + y
        if 0 <= a < column and 0 <= b < row and matrix[a][b] == 1:
            count += dfs(a,b)
    return count

ans = 0

for i in range(column):
    for j in range(row):
        if matrix[i][j] == 1:
            ans = max(ans,dfs(i,j))
print(ans)