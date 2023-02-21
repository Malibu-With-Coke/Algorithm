import sys
input = sys.stdin.readline

n1 = int(input())

def solve():
    n2 = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n2)] for _ in range(2)]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n2 >= 2:
        dp[0][1] = dp[1][0] + arr[0][1]
        dp[1][1] = dp[0][0] + arr[1][1]

        for i in range(2, n2):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]

    print(max(dp[0][n2-1], dp[1][n2-1]))

for _ in range(n1):
    solve()