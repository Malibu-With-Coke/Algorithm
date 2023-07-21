import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start_idx = 0
end_idx = 0
interval_sum = 0
ans = 0

for start_idx in range(n):
    while end_idx <= n and interval_sum < m:
        end_idx += 1
        interval_sum = sum(arr[start_idx:end_idx])

    if interval_sum == m:
        ans += 1
    start_idx += 1
    interval_sum = sum(arr[start_idx:end_idx])

print(ans)