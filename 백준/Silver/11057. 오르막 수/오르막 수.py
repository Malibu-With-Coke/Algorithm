n = int(input())

dp = [1 for _ in range(10)]

for _ in range(1, n):
    tmep_sum = 0
    for i in range(10):
        tmep_sum += dp[i]
        dp[i] = tmep_sum

print(sum(dp) % 10007)