import sys
input = sys.stdin.readline

cities_num = int(input())
plan_num = int(input())

matrix = [list(map(int, input().split())) for _ in range(cities_num)]
plan = list(map(int, input().split()))


p = [i for i in range(cities_num)]


def find(a):
    if p[a] == a:
        return a
    else:
        p[a] = find(p[a])
        return p[a]


def union(a, b):
    p[find(a)] = find(b)


for i in range(cities_num):
    for j in range(cities_num):
        if i == j:
            continue
        if matrix[i][j]:
            union(i, j)

for i in range(len(plan) - 1):
    if find(plan[i] - 1) != find(plan[i + 1] - 1):
        print("NO")
        break
else:
    print("YES")
