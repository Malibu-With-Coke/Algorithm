import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+2)

dp[2] = 3
dp[0] = 1

for i in range(4, n+1, 2):
    dp[i] = dp[i-2] * 3
    for j in range(i-4, -1, -2):
        dp[i] += dp[j] * 2

print(dp[n]) 