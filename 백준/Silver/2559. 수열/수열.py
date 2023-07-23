import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start_idx = 0
end_idx = m
sum_arr = sum(arr[start_idx:end_idx])
ans = sum_arr

while end_idx < n:
    sum_arr += arr[end_idx]
    sum_arr -= arr[start_idx]
    if ans < sum_arr:
        ans = sum_arr
    end_idx += 1
    start_idx += 1

print(ans)
