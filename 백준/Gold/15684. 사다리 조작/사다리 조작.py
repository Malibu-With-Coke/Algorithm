import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())

ladders = [[0 for _ in range(n + 1)] for _ in range(h + 1)]

for _ in range(m):
    height, dot1 = map(int, input().split())
    dot2 = dot1 + 1
    ladders[height][dot1] = dot2
    ladders[height][dot2] = dot1

# for i in range(h + 1):
#     print(*ladders[i])
# print()


def ifsucess():
    for start_point in range(1, n + 1):
        height = 0
        point = start_point

        while True:
            height += 1

            if height == h + 1:
                break

            if ladders[height][point] == 0:
                continue

            point = ladders[height][point]

        if point != start_point:
            return False

    return True


min_cnt = 4


def backtracking(cnt, idx):
    if ifsucess():
        global min_cnt
        min_cnt = min(cnt, min_cnt)
        return

    if cnt == 3:
        # for i in range(h + 1):
        #     print(*ladders[i])
        # print()
        return
    cur_idx = 0
    for height in range(1, h + 1):
        for dot in range(1, n):
            cur_idx += 1
            if cur_idx <= idx:
                continue

            # print(
            #     height,
            #     dot,
            #     ladders[height][dot],
            #     ladders[height][dot + 1],
            #     already_checked[height][dot],
            # )
            if (
                ladders[height][dot] == 0
                and ladders[height][dot + 1] == 0
                # and not already_checked[height][dot]
            ):
                ladders[height][dot] = dot + 1
                ladders[height][dot + 1] = dot
                # if cnt == 1:
                #     already_checked[height][dot] == True
                backtracking(cnt + 1, cur_idx)
                ladders[height][dot] = 0
                ladders[height][dot + 1] = 0


backtracking(0, 0)
print(min_cnt if min_cnt < 4 else -1)
