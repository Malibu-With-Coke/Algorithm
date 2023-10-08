import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = []
maxLen = 1

from bisect import bisect_left

dp.append(arr[0])

for i in range(1, n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        maxLen += 1
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]
    
print(maxLen)