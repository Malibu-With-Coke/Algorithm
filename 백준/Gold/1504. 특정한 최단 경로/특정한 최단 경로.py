import sys
input = sys.stdin.readline
from queue import PriorityQueue

INF = int(1e9)

N, E = map(int, input().split())

d_graph = {i : [] for i in range(1, N+1)}

for _ in range(E):
    a, b, c = map(int, input().split())
    d_graph[a].append((b, c))
    d_graph[b].append((a, c))

edge1, edge2 = map(int, input().split())

def dijkstra(start, end):
    q = PriorityQueue()
    distance = [INF] * (N+1)
    q.put((0, start))
    find_way = False

    while not q.empty():
        dist, now = q.get()

        if now == end:
            find_way = True
            break

        if distance[now] < dist:
            continue
            
        for i in d_graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.put((cost, i[0]))
    if find_way:
        return dist
    else:
        return -1

ans1 = 0
for start, end in ((1, edge1), (edge1, edge2), (edge2, N)):
    temp = dijkstra(start, end)
    if temp == -1:
        ans1 = -1
        break
    else:
        ans1 += temp

ans2 = 0
for start, end in ((1, edge2), (edge2, edge1), (edge1, N)):
    temp = dijkstra(start, end)
    if temp == -1:
        ans2 = -1
        break
    else:
        ans2 += temp

print(min(ans1, ans2))