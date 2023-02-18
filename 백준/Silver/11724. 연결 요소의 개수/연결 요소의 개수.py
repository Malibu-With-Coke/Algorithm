import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

edge, vertex = map(int, input().split())

d = {i : [] for i in range(1, edge+1)}

for _ in range(vertex):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

ans = 0
visited = [False] * (edge + 1)

def dfs (num):
    if visited[num]:
        return
    visited[num] = True
    for connected_edge in d[num]:
        dfs(connected_edge)

for i in range(1, edge+1):
    if not visited[i]:
        ans += 1
        dfs(i)
print(ans)