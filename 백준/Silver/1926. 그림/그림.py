import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

paint_count = 0
max_drawing = 0

from collections import deque

deq = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            deq.append((i, j))
            arr[i][j] = 0
            paint_count += 1
            drawing_size = 0

            while deq:
                a, b = deq.popleft()
                drawing_size += 1

                for move_a, move_b in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    new_a = a + move_a
                    new_b = b + move_b
                    if 0 <= new_a < n and 0 <= new_b < m and arr[new_a][new_b] == 1:
                        deq.append((new_a, new_b))
                        arr[new_a][new_b] = 0

            if drawing_size > max_drawing:
                max_drawing = drawing_size

print(paint_count)
print(max_drawing)