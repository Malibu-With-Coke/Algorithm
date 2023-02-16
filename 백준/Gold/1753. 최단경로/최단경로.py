import sys
input = sys.stdin.readline
from queue import PriorityQueue

INF = int(1e9)

v, e = map(int, input().split())

start = int(input())

d_vertex = {i : [] for i in range(1, v+1)}
distance = [INF] * (v+1)

for _ in range(e):
    u, vertex, weight = map(int, input().split())
    d_vertex[u].append((vertex, weight))

def dijkstra(start):
    que = PriorityQueue()
    
    que.put((0, start))
    distance[start] = 0

    while not que.empty():

        dist, now = que.get()
        if distance[now] < dist:
            continue
            
        for i in d_vertex[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                que.put((cost, i[0]))
        
dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])