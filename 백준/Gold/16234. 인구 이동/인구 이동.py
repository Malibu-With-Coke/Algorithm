import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
deq = deque()

def bfs(a, b):
    global people_move
    open_country = []
    open_country.append([a, b])
    count_country = 1
    count_people = matrix[a][b]

    visited[a][b] = 1
    deq.append((a, b))

    while deq:
        a, b = deq.popleft()
        
        for movement in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            move_a = a + movement[0]
            move_b = b + movement[1]

            if 0 <= move_a < n and 0 <= move_b < n and not visited[move_a][move_b]\
                and l <= abs(matrix[a][b] - matrix[move_a][move_b]) <= r:
                deq.append((move_a, move_b))
                visited[move_a][move_b] = 1
                open_country.append([move_a, move_b])
                count_country += 1
                count_people += matrix[move_a][move_b]
                people_move = True
    
    avg_people = count_people // count_country

    for a, b in open_country:
        matrix[a][b] = avg_people
    


ans = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    people_move = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)

    if people_move:
        ans += 1
    else:
        break
    
print(ans)