import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx = dx + x
        ny = dy + y
        if 0 <= nx < n and 0 <= ny < n and bamboo[nx][ny] > bamboo[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
        
    return dp[x][y]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j) + 1)

print(ans)