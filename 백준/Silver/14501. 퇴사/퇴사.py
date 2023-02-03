n = int(input())

d = {}
for i in range(1,n+1):
    during_days, payment = map(int, input().split())
    if n >= i + during_days -1:
        d[i] = [during_days, payment]
    else:
        d[i] = [-1,0]
        
sum = 0
ans = 0
arr = [0 for i in range(n+1)]

def backTracking (idx):
    global ans, sum
    if ans < sum:
        ans = sum
    for i in range(idx,n+1): 
        if arr[i] or d[i][0] == -1:
            continue
        during_days = d[i][0]
        
        for j in range(during_days):
            arr[i+j] = 1
        sum += d[i][1]
        backTracking(i+1)

        for j in range(during_days):
            arr[i+j] = 0
        sum -= d[i][1]
        backTracking(i+1)

backTracking(1)
print(ans)