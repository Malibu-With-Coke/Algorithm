n, k = map(int, input().split())

goods = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = goods[i-1][0]
        value = goods[i-1][1]
        if weight <= j:
            if value + dp[i-1][j-weight] > dp[i-1][j]:
                dp[i][j] = value + dp[i-1][j-weight]
            else:
                dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[i][j])