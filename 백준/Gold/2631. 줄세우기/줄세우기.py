import sys

input = sys.stdin.readline


n = int(input())
children = list(int(input()) for _ in range(n))

dp = [0] * (n + 1)

for i in range(n):
    for j in range(i):
        if dp[i] < dp[j] and children[i] > children[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))
