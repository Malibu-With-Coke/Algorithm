import sys
input = sys.stdin.readline

INF = sys.maxsize

n = int(input())
matrix = [list(map(int, (input().split()))) for _ in range(n)]

dp = [[INF if i != j else 0 for i in range(n)] for j in range(n)]

for gap in range(1, n):
    
    for start_idx in range(n - gap):
        end_idx = start_idx + gap

        dp[start_idx][end_idx] = min(dp[start_idx][mid_idx] + dp[mid_idx + 1][end_idx] + matrix[start_idx][0] * matrix[mid_idx][1] * matrix[end_idx][1] for mid_idx in range(start_idx, end_idx))

print(dp[0][n - 1])