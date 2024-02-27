import sys

input = sys.stdin.readline

import heapq

INF = int(10e9)

n, d = map(int, input().split())
graph = [[] for _ in range(d + 1)]
distance = [INF] * (d + 1)

for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    s, e, l = map(int, input().split())
    if e > d:
        continue

    graph[s].append((e, l))

pq = []
heapq.heappush(pq, (0, 0))
distance[0] = 0

while pq:
    dist, now = heapq.heappop(pq)

    if dist > distance[now]:
        continue

    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(pq, (cost, i[0]))

print(distance[d])
