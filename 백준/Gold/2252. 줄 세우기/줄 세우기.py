import sys

input = sys.stdin.readline

n, m = map(int, input().split())

front = [0 for _ in range(n + 1)]
back = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    front[b] += 1
    back[a].append(b)

from collections import deque

deq = deque()

for i in range(1, n + 1):
    if front[i] == 0:
        deq.append(i)

order_lst = []

while deq:
    cur_node = deq.popleft()
    order_lst.append(cur_node)

    for next_node in back[cur_node]:
        front[next_node] -= 1

        if front[next_node] == 0:
            deq.append(next_node)

print(*order_lst)
