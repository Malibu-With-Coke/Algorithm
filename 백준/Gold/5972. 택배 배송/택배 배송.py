import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ways = {i: [] for i in range(n + 1)}
for _ in range(m):
    a, b, cost = map(int, input().split())
    ways[a].append((b, cost))
    ways[b].append((a, cost))

from collections import deque
import heapq

distance = [10e9] * (n + 1)

que = []
heapq.heappush(que, (1, 0))
distance[1] = 0

while que:
    from_here, cur_cost = heapq.heappop(que)
    if distance[from_here] < cur_cost:
        continue

    for to_there, add_cost in ways[from_here]:
        next_cost = cur_cost + add_cost

        if next_cost < distance[to_there]:
            distance[to_there] = next_cost
            heapq.heappush(que, (to_there, next_cost))

print(distance[n])
