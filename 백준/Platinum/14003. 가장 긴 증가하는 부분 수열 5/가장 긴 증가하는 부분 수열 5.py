import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = []
dp2 = []
maxLen = 1

from bisect import bisect_left

dp.append(arr[0])
dp2.append((arr[0], 1))
for i in range(1, n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        maxLen += 1
        dp2.append((arr[i], maxLen))
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]
        dp2.append((arr[i], idx + 1))
    
print(maxLen)
ans = []
len = maxLen

for i in range(n - 1, -1, -1):
    if dp2[i][1] == len:
        ans.append(dp2[i][0])
        len -= 1

ans.reverse()
print(*ans)