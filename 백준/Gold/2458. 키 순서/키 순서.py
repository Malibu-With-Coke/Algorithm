import sys
input = sys.stdin.readline

INF = 9999999

node_count, vertex_count = map(int, input().split())

students = [[INF for _ in range(node_count)] for _ in range(node_count)]

for i in range(vertex_count):
    a, b = map(int, input().split())
    students[a-1][b-1] = 0

for k in range(node_count):
    for i in range(node_count):
        for j in range(node_count):
            if i == j:
                continue
            students[i][j] = min(students[i][j], students[i][k] + students[k][j])

ans = 0
for i in range(node_count):
    for j in range(node_count):
        if i == j:
            continue
        if students[i][j] == INF and students[j][i] == INF:
            ans -= 1
            break
    ans += 1

print(ans)