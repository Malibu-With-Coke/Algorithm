import sys

input = sys.stdin.readline

count_of_buildings, gahui, danbi = map(int, input().split())

buildings = []

for i in range(1, gahui):
    buildings.append(i)
buildings.append(max(gahui, danbi))
for i in range(danbi - 1, 0, -1):
    buildings.append(i)

if len(buildings) > count_of_buildings:
    print(-1)

else:
    print(buildings[0], end=" ")
    for i in range(count_of_buildings - len(buildings)):
        print(1, end=" ")

    for i in range(1, len(buildings)):
        print(buildings[i], end=" ")
