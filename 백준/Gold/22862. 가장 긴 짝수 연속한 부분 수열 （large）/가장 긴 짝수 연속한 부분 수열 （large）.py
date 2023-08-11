import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

start_idx = 0
end_idx = 0
erase_count = 0
ans = 0
count = 0

while start_idx < n:
    while erase_count <= k and end_idx < n:
        if arr[end_idx] % 2 == 1:
            erase_count += 1
        else:
            count += 1
        end_idx += 1

        if start_idx == 0 and end_idx == n:
            ans = count
            break

    if erase_count == k + 1 and ans < count:
        ans = count

    if arr[start_idx] % 2 == 1:
        erase_count -= 1
    else:
        count -= 1

    start_idx += 1

print(ans)