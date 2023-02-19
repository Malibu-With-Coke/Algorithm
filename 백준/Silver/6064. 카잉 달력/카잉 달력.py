import sys
input = sys.stdin.readline
 
def solve(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1
 
num = int(input())
for i in range(num):
    m, n, x, y = map(int, input().split())
    print(solve(m, n, x, y))