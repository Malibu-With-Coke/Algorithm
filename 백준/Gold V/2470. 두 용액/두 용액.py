import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_abs = abs(arr[n - 1] + arr[0])
max_idx = n - 1
min_idx = 0

left, right = 0, n - 1

while left < right:
    gap = arr[right] + arr[left]
    if abs(gap) < min_abs:
        min_abs = abs(gap)
        max_idx = right
        min_idx = left

    if gap > 0:
        right -= 1
    elif gap < 0:
        left += 1
    else:
        break

print(arr[min_idx], arr[max_idx])