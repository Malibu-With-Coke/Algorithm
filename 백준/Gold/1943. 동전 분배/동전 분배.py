import sys

input = sys.stdin.readline

for _ in range(3):
    num_coins = int(input())
    coins = [list(map(int, input().split())) for _ in range(num_coins)]
    sum_coins = 0
    for coin, num in coins:
        sum_coins += coin * num

    if sum_coins % 2 == 1:
        print(0)
        continue

    half_sum = sum_coins // 2

    dp = [True] + [False] * (half_sum)

    for coin, num in coins:
        for money in range(half_sum, coin - 1, -1):
            if dp[money - coin]:
                for i in range(num):
                    if money + i * coin <= half_sum:
                        dp[money + i * coin] = True

        if dp[-1]:
            print(1)
            break

    if not dp[-1]:
        print(0)
