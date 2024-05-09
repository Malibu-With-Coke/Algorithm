import sys

input = sys.stdin.readline


def find(num):
    if parent[num] == num:
        return num

    parent[num] = find(parent[num])
    return parent[num]


def union(num1, num2):
    num1 = find(num1)
    num2 = find(num2)

    if num1 != num2:
        parent[num1] = num2
        return 1

    return 0


planet_num = int(input())
planet_lst = []
planet_dis = []
parent = [i for i in range(planet_num + 1)]

for i in range(1, planet_num + 1):
    x, y, z = map(int, input().split())
    planet_lst.append((i, x, y, z))

for xyz in range(1, 4):
    planet_lst.sort(key=lambda x: x[xyz])

    for idx in range(planet_num - 1):
        planet_dis.append(
            (
                planet_lst[idx + 1][xyz] - planet_lst[idx][xyz],
                planet_lst[idx + 1][0],
                planet_lst[idx][0],
            )
        )

planet_dis.sort(key=lambda x: x[0])

total_dis = 0
for dis, idx1, idx2 in planet_dis:
    if union(idx1, idx2) == 1:
        total_dis += dis

print(total_dis)
