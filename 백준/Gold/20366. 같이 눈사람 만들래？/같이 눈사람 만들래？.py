import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
ans = int(10e9)

for a_left in range(n-3):
    for a_right in range(a_left+3, n):
        b_left = a_left + 1
        b_right = a_right - 1
        a_sum = arr[a_left] + arr[a_right]

        while b_left < b_right:
            b_sum = arr[b_left] + arr[b_right]
            if ans > abs(a_sum - b_sum):
                ans = abs(a_sum - b_sum)

            if a_sum > b_sum:
                b_left += 1
            elif a_sum < b_sum:
                b_right -= 1
            else:
                ans = 0
                break

        if ans == 0:
            break

print(ans)