from collections import deque

com_num = int(input())
n = int(input())

graph = [[0 for _ in range(com_num+1)] for _ in range(com_num+1)]

# print(graph)

for _ in range(n):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# print(graph)
answer = 0
# com = 1
deq = deque()
check = [True for _ in range(com_num+1)]
# check[1] = False
deq.append(1)
check[1] = False
while deq:
    com = deq.popleft()
    # print(com)
    for i in range(com_num+1):
        # print(i)
        if(graph[com][i] == 1 and check[i]):
            deq.append(i)
            check[i] = False
            answer += 1

print(answer)