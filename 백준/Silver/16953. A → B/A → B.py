from collections import deque

a, b = map(int, input().split())

deq = deque()

deq.append([a, 0])
ans = -1

while deq:
    num, count = deq.popleft()
    n1 = num * 2
    n2 = 10*num + 1

    if (n1 == b or n2 == b):
        ans = count + 2
        break
    if (n1 < b):
        deq.append([n1, count+1])
    if (n2 < b):
        deq.append([n2, count+1])

print(ans)