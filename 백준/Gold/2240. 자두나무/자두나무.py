import sys
input = sys.stdin.readline

T, W = map(int, input().split())

plums = [int(input()) for _ in range(T)]
dp = [[0, 0] for _ in range(W+1)]

for plum in plums:
    plum -= 1
    not_plum = 1 - plum
    for i in range(W, 0, -1):
        dp[i][plum] = max(dp[i][plum], dp[i-1][not_plum]) + 1
    if plum == 0:
        dp[0][plum] += 1
print(max(dp[W][0], dp[W][1]))