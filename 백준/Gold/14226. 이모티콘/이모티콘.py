import sys

input = sys.stdin.readline

from queue import PriorityQueue


n = int(input())

que = PriorityQueue()
que.put((0, 1, 0))
already_visited = {i: [] for i in range(1, 1001)}
while not que.empty():
    time, s, copy = que.get()
    if s == n:
        break
    for next_s, next_copy in ((s - 1, copy), (s, s), (s + copy, copy)):
        if 0 < next_s <= 1000 and next_copy not in already_visited[next_s]:
            already_visited[next_s].append(next_copy)
            que.put((time + 1, next_s, next_copy))

print(time)
