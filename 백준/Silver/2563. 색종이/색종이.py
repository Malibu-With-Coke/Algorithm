import sys
input = sys.stdin.readline

matrix = [[0 for _ in range(101)] for _ in range((101))]

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(10):
        for j in range(10):
            matrix[a+i][b+j] = 1

    
ans = 0
for i in range(1, 101):
    for j in range(1, 101):
        if matrix[i][j] == 1:
            ans += 1

print(ans)