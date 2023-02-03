n = int(input())

arr = list(map(int, input().split()))

dp_inc = [0 for i in range(n)]
dp_dec = [0 for i in range(n)]

for i in range(0,n,1):
    for j in range(0,i,1):
        if arr[i] > arr[j] and dp_inc[i] < dp_inc[j]:
            dp_inc[i] = dp_inc[j]
    dp_inc[i] += 1

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[i] > arr[j] and dp_dec[i] < dp_dec[j]:
            dp_dec[i] = dp_dec[j]
    dp_dec[i] += 1

ans = 0
for i in range(n):
    if ans < dp_dec[i] + dp_inc[i]:
        ans = dp_dec[i] + dp_inc[i]
print(ans-1)