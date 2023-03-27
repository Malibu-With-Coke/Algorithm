import sys
input = sys.stdin.readline
from collections import deque

start, end = map(int, input().split())

deq = deque()
deq.append((start, 0))
d = {start : start}

while deq:
    a, count = deq.popleft()
    if a == end:
        break    
    for movement in (a-1, a+1, a*2):
        if 0 <= movement <= 100000 and not movement in d:
            deq.append((movement, count+1))
            d[movement] = a
ans = []
a = end
while True:
    ans.append(a)
    if a == start:
        break
    
    a = d[a]

print(count)
for i in range(len(ans)-1, -1, -1):
    print(ans[i], end=" ")
print()