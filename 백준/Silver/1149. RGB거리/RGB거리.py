n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

d = {1 : arr[0]}
if n != 1:
    for i in range(2, n+1):
        d[i] = [
            min(d[i-1][1],d[i-1][2]) + arr[i-1][0],
            min(d[i-1][0],d[i-1][2]) + arr[i-1][1],
            min(d[i-1][0],d[i-1][1]) + arr[i-1][2]        
        ]

print(min(d[n]))