import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [0 for _ in range(k+1)]

for _ in range(n):
    num = int(input())
    if num > 10000:
        continue
    coins.append(num)

coins_len = len(coins)

dp[0] = 1
for j in range(coins_len):
    for i in range(k+1):
        if i - coins[j] < 0:
            continue
        dp[i] += dp[i - coins[j]]

print(dp[k])