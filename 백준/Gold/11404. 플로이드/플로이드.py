import sys

n = int(input())
m = int(input())

INF = 99999999

cities = [[INF for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if cities[a-1][b-1] > c:
        cities[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if cities[i][j] > cities[i][k] + cities[k][j]:
                cities[i][j] = cities[i][k] + cities[k][j]

for i in range(n):
    for j in range(n):
        if cities[i][j] == INF:
            print(0, end=" ")
        else:
            print(cities[i][j], end=" ")
    print()