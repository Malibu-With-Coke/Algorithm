n = int(input())
stairs = [int(input()) for _ in range(n)]

if n == 1:
    print(stairs[0])
    exit(0)
elif n == 2:
    print(stairs[0]+stairs[1])
    exit(0)


d = {1 : [stairs[0],stairs[0]], 2 : [stairs[1],stairs[1]+stairs[0]]}

for i in range(3, n+1):
    first_step = stairs[i-1] + max(d[i-2])
    second_step = stairs[i-1] + d[i-1][0]
    d[i] = [first_step, second_step]

print(max(d[n]))