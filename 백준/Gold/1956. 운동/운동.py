import sys

input = sys.stdin.readline
INF = sys.maxsize

cities_count, road_count = map(int, input().split())

cities_distance = [[INF for _ in range(cities_count)] for _ in range(cities_count)]

for _ in range(road_count):
    a_city, b_city, distance = map(int, input().split())
    cities_distance[a_city - 1][b_city - 1] = distance

for k in range(cities_count):
    for i in range(cities_count):
        for j in range(cities_count):
            if cities_distance[i][j] > cities_distance[i][k] + cities_distance[k][j]:
                cities_distance[i][j] = cities_distance[i][k] + cities_distance[k][j]

min_distance = INF
for i in range(cities_count):
    if cities_distance[i][i] != INF:
        min_distance = min(min_distance, cities_distance[i][i])

print(min_distance if min_distance != INF else -1)
