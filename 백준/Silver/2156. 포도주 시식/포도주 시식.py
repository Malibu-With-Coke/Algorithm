n = int(input())

arr = [int(input()) for _ in range(n)]

d = {0 : [0, 0, 0], 1 : [arr[0], arr[0], 0]}    # 2, 1, 0

for i in range(2, n+1):
    d[i] = [d[i-1][1] + arr[i-1], d[i-1][2] + arr[i-1], max(d[i-1])]

print(max(d[n]))