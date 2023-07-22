import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    if not arr:
        for temp_item in temp:
            heapq.heappush(arr, temp_item)
    else:
        for temp_item in temp:
            if arr[0] < temp_item:
                heapq.heappop(arr)
                heapq.heappush(arr, temp_item)

print(arr[0])

