import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
for idx in range(n):
    tar = arr[idx]
    start, end = 0, n - 1

    while start < end:

        sum_ = arr[start] + arr[end]

        if tar == sum_:
            if start == idx:
                start += 1
            elif end == idx:
                end -= 1
            else:
                ans += 1
                break

        elif tar > sum_:
            start += 1
        else:
            end -= 1
print(ans)
