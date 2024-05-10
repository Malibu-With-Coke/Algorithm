import sys

input = sys.stdin.readline


nodes_num = int(input())

parent = [0] * (nodes_num + 1)
graph = [[] for _ in range(nodes_num + 1)]
depth = [0] * (nodes_num + 1)

for _ in range(nodes_num - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

deq = deque()
deq.append((1, 1))
depth[1] = 1

while deq:
    cur_node, cur_depth = deq.popleft()

    for next_node in graph[cur_node]:
        if depth[next_node] == 0:
            parent[next_node] = cur_node
            deq.append((next_node, cur_depth + 1))
            depth[next_node] = cur_depth + 1

search_num = int(input())
for _ in range(search_num):
    node_a, node_b = map(int, input().split())

    while node_a != node_b:
        if depth[node_a] > depth[node_b]:
            node_a = parent[node_a]
        elif depth[node_b] > depth[node_a]:
            node_b = parent[node_b]
        else:
            node_a = parent[node_a]
            node_b = parent[node_b]
    print(node_b)
