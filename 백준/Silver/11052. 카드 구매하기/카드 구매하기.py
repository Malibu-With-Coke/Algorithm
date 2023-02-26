import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(card[i-j] + dp[j-1] , dp[i])

print(dp[n])