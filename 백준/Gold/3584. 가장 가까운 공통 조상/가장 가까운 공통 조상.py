import sys

input = sys.stdin.readline

from collections import deque

for _ in range(int(input())):
    nodes_num = int(input())
    parent = [0] * (nodes_num + 1)
    child = [[] for _ in range(nodes_num + 1)]
    depth = [0] * (nodes_num + 1)

    for _ in range(nodes_num - 1):
        a, b = map(int, input().split())
        parent[b] = a
        child[a].append(b)
    find_a, find_b = map(int, input().split())

    root_node = 0
    for i in range(1, nodes_num + 1):
        if parent[i] == 0:
            root_node = i
            break

    deq = deque()
    deq.append((root_node, 0))

    while deq:
        cur_node, cur_depth = deq.popleft()

        for child_node in child[cur_node]:
            depth[child_node] = cur_depth + 1
            deq.append((child_node, cur_depth + 1))


    while find_a != find_b:
        if depth[find_a] > depth[find_b]:
            find_a = parent[find_a]
        elif depth[find_a] < depth[find_b]:
            find_b = parent[find_b]
        else:
            find_a = parent[find_a]
            find_b = parent[find_b]

    print(find_a)