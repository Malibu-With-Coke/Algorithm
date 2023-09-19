import sys
input = sys.stdin.readline

dp = [0 for _ in range(1000001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
for idx in range(3,1000001):
    dp[idx] = (dp[idx-1] + dp[idx-2] + dp[idx-3]) % 1000000009

n = int(input())
for _ in range(n):
    num = int(input())
    print(dp[num])