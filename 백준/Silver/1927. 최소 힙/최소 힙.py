import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())

que = PriorityQueue()

for _ in range(n):
    num = int(input())
    if num == 0:
        if que.empty():
            print(0)
        else:
            print(que.get())
    else:
        que.put(num)