import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

sum = 0
d = {0:0}
for i in range(1, len(arr)+1):
    d[i] = d[i-1] + arr[i-1]

for _ in range(m):
    start, end = map(int, input().split())
    print(d[end]-d[start-1])