import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

def solve():
    num = int(input())
    a, b = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(num)]
    visited = [False for _ in range(num)]

    y, z = map(int, input().split())
    
    deq = deque()
    deq.append([a, b])

    while deq:
        a, b = deq.popleft()

        if abs(y - a) + abs(z - b) <= 1000:
            print("happy")
            return

        for i in range(num):
            if visited[i]:
                continue
            temp = arr[i]
            if abs(temp[0] - a) + abs(temp[1] - b) <= 1000:
                deq.append([temp[0], temp[1]])
                visited[i] = True
    
    print("sad")
    return

for _ in range(n):
    solve()