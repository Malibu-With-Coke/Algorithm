import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

start_idx = 0
end_idx = n - 1
ans = 0

while start_idx < end_idx:
    if arr[start_idx] + arr[end_idx] == x:
        ans += 1
        start_idx += 1
    elif arr[start_idx] + arr[end_idx] > x:
        end_idx -= 1
    elif arr[start_idx] + arr[end_idx] < x:
        start_idx += 1

print(ans)