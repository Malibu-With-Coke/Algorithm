import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

ans = 9999999999999
end_idx = 0

for start_idx in range(n-1):
    while arr[end_idx] - arr[start_idx] < m and end_idx < n-1:
        end_idx += 1
    if m <= arr[end_idx] - arr[start_idx] < ans:
        ans = arr[end_idx] - arr[start_idx]

print(ans if n != 1 else arr[0])