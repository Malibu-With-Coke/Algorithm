from collections import deque

n, m = map(int, input().split())

d_graph = {i : [] for i in range(1,n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    d_graph[a].append(b)
    d_graph[b].append(a)


def bfs(num):
    already_visited = [False for _ in range(n+1)]
    deq = deque()

    count = 0
    return_value = 0
    deq.append([num, count])
    already_visited[num] = True
    
    while deq:
        num, count = deq.popleft()
        return_value += count
        for i in d_graph[num]:
            if not already_visited[i]:
                deq.append([i, count+1])
                already_visited[i] = True
    return return_value

min_num = 9999999
min_index = 0

for i in range(1,n+1):
    temp = bfs(i)
    if min_num > temp:
        min_num = temp
        min_index = i

print(min_index)