n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key= lambda x: x[0])

dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if dp[i] < dp[j] and arr[i][1] > arr[j][1]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))