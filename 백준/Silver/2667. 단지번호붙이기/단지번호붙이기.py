from collections import deque

num = int(input())

house = [list(map(int,input())) for _ in range(num)]

# print(house)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(x, y):
    deq.append([x, y])
    house[x][y] = 0
    count = 0
    while deq:
        x, y = deq.popleft()
        count += 1
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0<=a<num and 0<=b<num and house[a][b] == 1:
                deq.append([a,b])
                house[a][b] = 0
    return count

deq = deque()
x = y = 0
answer = []

for x in range(num):
    for y in range(num):
        if house[x][y] == 1:
            answer.append(bfs(x, y))

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])