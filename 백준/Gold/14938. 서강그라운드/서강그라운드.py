import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

count_of_itmes = [0] + list(map(int, input().split()))
cost_of_dest = [[10e9 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    cost_of_dest[a][b] = c
    cost_of_dest[b][a] = c


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            if cost_of_dest[i][j] > cost_of_dest[i][k] + cost_of_dest[k][j]:
                cost_of_dest[i][j] = cost_of_dest[i][k] + cost_of_dest[k][j]

ans = 0
for i in range(1, n + 1):
    sum_i = count_of_itmes[i]

    for j in range(1, n + 1):
        if cost_of_dest[i][j] <= m:
            sum_i += count_of_itmes[j]
    ans = max(ans, sum_i)

print(ans)
