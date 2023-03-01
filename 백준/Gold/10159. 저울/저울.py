import sys
INF = int(1e9)

N = int(sys.stdin.readline())
goods = [[0] * N for _ in range(N)]

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    goods[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if goods[i][k] == 1 and goods[k][j] == 1:
                goods[i][j] = 1

answer = 0
for i in range(N):
    count = 0
    for j in range(N):
        count += goods[i][j] + goods[j][i]
    print((N - 1) - count)