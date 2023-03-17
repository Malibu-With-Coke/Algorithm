import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())

computer = {i : [] for i in range(1, a+1)}

for i in range(b):
    x, y = map(int, input().split())
    computer[y].append(x)

def bfs(n):
    visited = [0 for i in range(a+1)]
    deq = deque()

    deq.append(n)
    visited[n] = 1

    count = 0
    while deq:
        count +=1
        n = deq.popleft()
        for i in computer[n]:
            if not visited[i]:
                deq.append(i)
                visited[i] = 1
        
    return count

ans = []
max_num = 0

for i in range(1, a+1):
    temp = bfs(i)
    if max_num < temp:
        max_num = temp
        ans.clear()
        ans.append(i)

    elif max_num == temp:
        ans.append(i)

print(*ans)