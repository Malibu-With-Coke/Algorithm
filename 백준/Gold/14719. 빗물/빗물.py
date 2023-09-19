import sys
input = sys.stdin.readline

H, W = map(int, input().split())

dim = list(list(map(int, input().split())))

left, right = 0, W-1
left_max, right_max = dim[0], dim[W-1]
rain_total = 0

while left <= right:
    left_max = max(left_max, dim[left])
    right_max = max(right_max, dim[right])

    if left_max < right_max:
        rain_total += left_max - dim[left]
        left += 1

    else:
        rain_total += right_max - dim[right]
        right -= 1

print(rain_total)