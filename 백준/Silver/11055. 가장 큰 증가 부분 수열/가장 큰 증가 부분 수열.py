n = int(input())

arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(len(arr)):
    for j in range(i):
        if dp[i] < dp[j] and arr[i] > arr[j]:
            dp[i] = dp[j]
    dp[i] += arr[i]

print(max(dp))