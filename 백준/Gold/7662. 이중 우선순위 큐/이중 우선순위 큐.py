import sys
input = sys.stdin.readline
import heapq

n = int(input())

def solve():
    num = int(input())

    visited = [False] * 1_000_001
    minheap, maxheap = [], []
    for i in range(num):
        s = input().split()
        if s[0] == 'I':
            heapq.heappush(minheap, (int(s[1]), i))
            heapq.heappush(maxheap, (-int(s[1]), i))
            visited[i] = True
        elif s[1] == '1':
            while maxheap and not visited[maxheap[0][1]]:
                heapq.heappop(maxheap)
            if maxheap:
                visited[maxheap[0][1]] = False
                heapq.heappop(maxheap)
        else:
            while minheap and not visited[minheap[0][1]]:
                heapq.heappop(minheap)
            if minheap:
                visited[minheap[0][1]] = False
                heapq.heappop(minheap)
        
    while minheap and not visited[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and not visited[maxheap[0][1]]:
        heapq.heappop(maxheap)
    print(f'{-maxheap[0][0]} {minheap[0][0]}'if maxheap and minheap else'EMPTY')


for _ in range(n):
    solve()