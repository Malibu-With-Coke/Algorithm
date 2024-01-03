import sys
input = sys.stdin.readline

n = int(input())


def find_steps():
    arr = list(map(int, input().split()))
    total = 0
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                total += 1
    print(arr[0], total)


for _ in range(n):
    find_steps()