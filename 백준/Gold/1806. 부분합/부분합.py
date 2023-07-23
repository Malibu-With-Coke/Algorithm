import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 100001
end_idx = 0
sum_arr = arr[0]
for start_idx in range(n):
    while sum_arr < m and end_idx < n-1:
        end_idx += 1
        sum_arr += arr[end_idx]
    
    if sum_arr >= m and end_idx - start_idx < ans:
        ans = end_idx - start_idx

    sum_arr -= arr[start_idx]

print(ans+1 if ans != 100001 else 0)