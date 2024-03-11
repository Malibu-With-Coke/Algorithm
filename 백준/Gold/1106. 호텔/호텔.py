import sys

input = sys.stdin.readline
INF = sys.maxsize

target, num_of_cities = map(int, input().split())
cities = [[0, 0]] + [list(map(int, input().split())) for _ in range(num_of_cities)]
dp = [[INF for _ in range(target + 1)] for _ in range(num_of_cities + 1)]

for i in range(1, num_of_cities + 1):
    benefit = cities[i][1]
    cost = cities[i][0]

    for j in range(1, target + 1):
        dp[i][j] = dp[i - 1][j]

        count = 0
        while True:
            if j - count * benefit <= 0:
                dp[i][j] = min(dp[i][j], count * cost)
                break
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - count * benefit] + count * cost)
            count += 1

print(dp[num_of_cities][target])
