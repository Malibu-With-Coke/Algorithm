import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [sorted(list(map(int, input().split()))) for _ in range(n)]

gap = 10 ** 9 + 1
min_idx = 0

# from collections import deque
from heapq import heappush, heappop

hq = []

min_value = 10 ** 9 + 1
max_value = 0
for i in range(n):
    temp = arr[i][0]
    if min_value > temp: min_value = temp
    if max_value < temp: max_value = temp
    heappush(hq, (temp, i, 0))
    # deq.append((temp, i, 0))

ans = max_value - min_value

while True:
    # temp = deq.popleft()
    temp = heappop(hq)
    gap = max_value - temp[0]
    if gap < ans:
        ans = gap

    if temp[2] == m-1:
        break

    if arr[temp[1]][temp[2]+1] > max_value:
        max_value = arr[temp[1]][temp[2]+1]

    # deq.append((arr[temp[1]][temp[2]+1], temp[1], temp[2]+1))
    heappush(hq, (arr[temp[1]][temp[2]+1], temp[1], temp[2]+1))
print(ans)