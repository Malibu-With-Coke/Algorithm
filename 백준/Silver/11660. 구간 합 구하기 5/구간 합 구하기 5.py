import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = matrix[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + matrix[i][0]
    dp[0][i] = dp[0][i-1] + matrix[0][i]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + matrix[i][j] - dp[i-1][j-1]

def minus_one(n):
    return int(n) - 1

def solve():
    x1, y1, x2, y2 = map(minus_one, input().split())
    if x1 == 0 and y1 == 0:
        ans = dp[x2][y2]
    elif y1 == 0:
        ans = dp[x2][y2] - dp[x1-1][y2]
    elif x1 == 0:
        ans = dp[x2][y2] - dp[x2][y1-1]
    else:
        ans = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(ans)

for _ in range(m):
    solve()