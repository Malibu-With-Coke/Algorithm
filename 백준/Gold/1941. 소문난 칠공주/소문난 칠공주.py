import sys

input = sys.stdin.readline

class_student = [list(input()) for _ in range(5)]
ans = 0

import itertools
from collections import deque

s = []
y = []
for i in range(5):
    for j in range(5):
        if class_student[i][j] == "S":
            s.append((i, j))
        else:
            y.append((i, j))

ans = 0
k = [(1, 1), (1, 3), (2, 4)]
for i in range(4, 8, 1):
    s_comb = list(itertools.combinations(s, i))
    y_comb = list(itertools.combinations(y, 7 - i))
    for s_list in s_comb:
        for y_list in y_comb:
            temp = list(s_list + y_list)
            deq = deque()
            deq.append(temp.pop())
            while deq:
                dir_x, dir_y = deq.popleft()
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                    if (dir_x + dx, dir_y + dy) in temp:
                        deq.append((dir_x + dx, dir_y + dy))
                        temp.remove((dir_x + dx, dir_y + dy))

            if not temp:
                ans += 1

print(ans)