import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

left_idx = 0
right_idx = n - 1
final_sum = arr[left_idx] + arr[right_idx]
final_left_idx = 0
final_right_idx = n - 1

while left_idx < right_idx:
    sum_of_value = arr[left_idx] + arr[right_idx]

    if abs(final_sum) > abs(sum_of_value):
        final_sum = sum_of_value
        final_left_idx = left_idx
        final_right_idx = right_idx

    if sum_of_value > 0:
        right_idx -= 1
    elif sum_of_value < 0:
        left_idx += 1
    else:
        break

print(arr[final_left_idx], arr[final_right_idx])
