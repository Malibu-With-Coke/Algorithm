import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

def solve():
    size = int(input())
    visited = [[0 for _ in range(size)] for _ in range(size)]

    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    deq = deque()
    deq.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = 1

    while deq:
        a, b, c = deq.popleft()
        if a == end[0] and b == end[1]:
            break
        for movement in ((-2, -1), (-1, -2), (1, -2), (2, -1),\
                          (-2, 1), (-1, 2), (1, 2), (2, 1)):
            movement_a = a + movement[0]
            movement_b = b + movement[1]

            if 0 <= movement_a < size and 0 <= movement_b < size and not visited[movement_a][movement_b]:
                deq.append((movement_a, movement_b, c+1))
                visited[movement_a][movement_b] = 1
    
    print(c)


for i in range(n):
    solve()