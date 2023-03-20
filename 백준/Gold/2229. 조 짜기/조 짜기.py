import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1, n):
    dp[i] = dp[i-1]
    for j in range(i, -1, -1):
        temp = arr[j:i+1]
        if dp[i] < dp[j-1] + (max(temp) - min(temp)):
            dp[i] = dp[j-1] + (max(temp) - min(temp))

print(dp[n-1])