from collections import deque
import copy

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]    # input array
check_matrix = [[1 for _ in range(n)] for _ in range(n)]    # bfs if have already visited

# Shark location check
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            matrix[i][j] = 0
            x, y = i, j
            break


# BFS
def bfs (x, y):
    deq = deque()
    deq.append([x, y, 0])
    vistied = copy.deepcopy(check_matrix)
    vistied[x][y] = 0
    while deq:
        x, y, movement = deq.popleft()
    
        if matrix[x][y] and matrix[x][y] < shark_size:
            fish_list.append([x, y, movement])
        for move_x, move_y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            a = x + move_x
            b = y + move_y

            if (0 <= a < n and 0 <= b < n and vistied[a][b] and matrix[a][b] <= shark_size):
                deq.append([a, b, movement+1])
                vistied[a][b] = 0

ans = 0
eatFishCount = 0
shark_size = 2
while True:
    fish_list = []
    bfs (x, y)
    if not fish_list:
        break
    fish_list.sort(key = lambda x :(x[2], x[0], x[1]))
    # print(fish_list)
    x = fish_list[0][0]
    y = fish_list[0][1]
    ans += fish_list[0][2]
    matrix[x][y] = 0
    # print("shark : ",x+1 ,y+1, fish_list[0][2])

    eatFishCount += 1
    if shark_size == eatFishCount:
        shark_size += 1
        eatFishCount = 0
    
print(ans)