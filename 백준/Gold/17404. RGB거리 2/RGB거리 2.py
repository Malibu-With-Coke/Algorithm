import sys

input = sys.stdin.readline
INF = 10e10

n = int(input())
house_info = [list(map(int, input().split())) for _ in range(n)]

house_coloring = [[0 for _ in range(3)] for _ in range(n + 1)]
ans = 10e10
for start_idx in range(3):
    house_coloring[0] = [INF] * 3
    house_coloring[0][start_idx] = house_info[0][start_idx]
    for i in range(1, n):
        house_coloring[i][0] = (
            min(house_coloring[i - 1][1], house_coloring[i - 1][2]) + house_info[i][0]
        )
        house_coloring[i][1] = (
            min(house_coloring[i - 1][0], house_coloring[i - 1][2]) + house_info[i][1]
        )
        house_coloring[i][2] = (
            min(house_coloring[i - 1][0], house_coloring[i - 1][1]) + house_info[i][2]
        )
    house_coloring[n - 1][start_idx] = INF
    house_coloring[n][start_idx] = min(house_coloring[n - 1])
print(min(house_coloring[n]))
