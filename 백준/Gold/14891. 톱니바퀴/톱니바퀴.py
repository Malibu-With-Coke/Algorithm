import sys
from collections import deque

input = sys.stdin.readline

gears = [list(input().rstrip()) for _ in range(4)]
count_rotate = int(input())
rotates = [list(map(int, input().split())) for _ in range(count_rotate)]

S = "1"
N = "0"


def rotating(lst, rotate_dir):
    temp = deque(lst)
    temp.rotate(rotate_dir)
    return list(temp)


for rotate_gear, rotate_dir in rotates:
    rotate_gear -= 1
    next_rotate = [False] * 4
    next_rotate[rotate_gear] = rotate_dir

    temp_rotate_dir = rotate_dir

    for gear_idx in range(rotate_gear - 1, -1, -1):
        if gears[gear_idx][2] != gears[gear_idx + 1][6]:
            temp_rotate_dir *= -1
            next_rotate[gear_idx] = temp_rotate_dir
        else:
            break

    temp_rotate_dir = rotate_dir

    for gear_idx in range(rotate_gear + 1, 4):
        if gears[gear_idx][6] != gears[gear_idx - 1][2]:
            temp_rotate_dir *= -1
            next_rotate[gear_idx] = temp_rotate_dir
        else:
            break

    for idx in range(4):
        if next_rotate[idx] != False:
            gears[idx] = rotating(gears[idx], next_rotate[idx])

ans = 0
for idx in range(4):
    if gears[idx][0] == S:
        ans += 2**idx
print(ans)
