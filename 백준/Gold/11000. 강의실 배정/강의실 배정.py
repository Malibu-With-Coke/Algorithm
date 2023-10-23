import sys
input = sys.stdin.readline

from heapq import heappop, heappush

n = int(input())

classes = [list(map(int, input().split())) for _ in range(n)]
classes.sort()

room = [classes[0][1]]
count_room = 0
for i in range(1, n):
    if room[0] <= classes[i][0]:
        heappop(room)
    heappush(room, classes[i][1])

print(len(room))