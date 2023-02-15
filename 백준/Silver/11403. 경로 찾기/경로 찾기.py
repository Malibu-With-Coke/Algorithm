import sys
import math

n = int(input())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not matrix[i][j]:
            matrix[i][j] = math.inf

for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for i in range(n):
    for j in range(n):
        if matrix[i][j] == math.inf:
            print(0, end=" ")
        else:
            print(1, end= " ")
    print()