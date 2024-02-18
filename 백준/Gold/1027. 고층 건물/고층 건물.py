import sys

input = sys.stdin.readline

num_buildings = int(input())
buildings = list(map(int, input().split()))

max_cnt = 0

for idx in range(num_buildings):
    cur_building = buildings[idx]

    left_cnt = 0
    max_incline = 10e9
    for left_idx in range(idx - 1, -1, -1):
        try:
            if max_incline > (cur_building - buildings[left_idx]) / (idx - left_idx):
                max_incline = (cur_building - buildings[left_idx]) / (idx - left_idx)
                left_cnt += 1
        except:
            print(idx - left_idx, (cur_building - buildings[left_idx]))

    right_cnt = 0
    min_incline = -10e9
    for right_idx in range(idx + 1, num_buildings):
        if min_incline < (cur_building - buildings[right_idx]) / (idx - right_idx):
            min_incline = (cur_building - buildings[right_idx]) / (idx - right_idx)
            right_cnt += 1

    max_cnt = max(max_cnt, left_cnt + right_cnt)

print(max_cnt)
