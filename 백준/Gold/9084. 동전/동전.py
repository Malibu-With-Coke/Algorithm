import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0 for _ in range(m+1)]
    dp[0] = 1
    for coin in coins:
        for idx in range(m+1):
            if not dp[idx]:
                continue
            elif idx + coin > m:
                break
            dp[idx + coin] += dp[idx]

    print(dp[m])

T = int(input())
for _ in range(T):
    solve()