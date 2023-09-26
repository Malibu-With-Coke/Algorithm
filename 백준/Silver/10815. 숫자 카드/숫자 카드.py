import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))

cards.sort()
for num in nums:
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == num:
            print(1, end=' ')
            break
        elif cards[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print(0, end=' ')