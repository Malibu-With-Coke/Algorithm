import sys
input = sys.stdin.readline
from collections import deque
import copy

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def bfs():
    global ans
    deq = deque()
    copy_matrix = copy.deepcopy(matrix)

    for i in range(n):
        for j in range(m):
            if copy_matrix[i][j] == 2:
                deq.append((i, j))

                while deq:
                    a, b = deq.popleft()

                    for move in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        move_a = a + move[0]
                        move_b = b + move[1]

                        if 0 <= move_a < n and 0 <= move_b < m and copy_matrix[move_a][move_b] == 0:
                            deq.append((move_a, move_b))
                            copy_matrix[move_a][move_b] = 2
    
    zero_count = 0

    for i in range(n):
        for j in range(m):
            if copy_matrix[i][j] == 0:
                zero_count += 1
    
    ans = max(ans, zero_count)
    return 
def backTracking(num, idx):
    if num == 3:
        bfs()
    else:
        for i in range(idx, n*m):
            if matrix[i//m][i%m] == 0:
                matrix[i//m][i%m] = 1
                backTracking(num+1, i+1)
                matrix[i//m][i%m] = 0

backTracking(0, 0)

print(ans)