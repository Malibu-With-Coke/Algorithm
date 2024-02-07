import sys
import copy

input = sys.stdin.readline

num_of_bulb = int(input())
cur_bulb = list(map(int, list(input().rstrip())))
final_bulb = list(map(int, list(input().rstrip())))


def change(cur_obj, final_obj):

    copy_obj = copy.deepcopy(cur_obj)
    press = 0

    for i in range(1, num_of_bulb):

        if copy_obj[i - 1] == final_obj[i - 1]:
            continue

        press += 1

        for j in range(i - 1, i + 2):
            if j < num_of_bulb:
                copy_obj[j] = 1 - copy_obj[j]

    if copy_obj == final_obj:
        return press

    else:
        return 10e9


other_case_bulb = copy.deepcopy(cur_bulb)
other_case_bulb[0] = 1 - other_case_bulb[0]
other_case_bulb[1] = 1 - other_case_bulb[1]

case1 = change(cur_bulb, final_bulb)
case2 = change(other_case_bulb, final_bulb)

if case1 == 10e9 and case2 == 10e9:
    print(-1)
else:
    print(min(case1, case2+1))
