from collections import deque

N, M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    S, E = map(int,input().split())
    graph[S].append(E)
    graph[E].append(S)
    

for i in range(N+1):
    graph[i].sort()
# print(graph)

check_dfs = [False for i in range(N+1)]
check_bfs = [False for i in range(N+1)]

# V += 1
def dfs(v):
    check_dfs[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if(not check_dfs[i]):
            check_dfs[i] = True
            dfs(i)

queue = deque()
# Add element to the end
# deq.append(0)

# Pop element from the start
# deq.popleft()

def bfs(v):
    check_bfs[v] = True
    queue.append(v)
    while(queue):
        node = queue.popleft()
        
        print(node, end=" ")
        for i in graph[node]:
            # print(i, end="!")
            if (not check_bfs[i]):
                queue.append(i)
                check_bfs[i] = True
                


dfs(V)
print()  
bfs(V)
