import sys

input = sys.stdin.readline

top_floor, digit, change_max_count, cur_flo = map(int, input().split())


def change_list(num):
    arr = list(map(int, str(num)))
    if digit > len(arr):
        add_num = digit - len(arr)
        for _ in range(add_num):
            arr = [0] + arr
    return arr


cur_floor = change_list(cur_flo)

change_cost = [
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
    [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
    [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
    [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
    [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
    [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
    [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0],
]

can_change = 0
for floor in range(1, top_floor + 1):
    if floor == cur_flo:
        continue
    change_floor = change_list(floor)
    cost = 0

    for idx in range(digit):
        if change_floor[idx] == cur_floor[idx]:
            continue

        cost += change_cost[cur_floor[idx]][change_floor[idx]]
    if cost <= change_max_count:
        can_change += 1

print(can_change)