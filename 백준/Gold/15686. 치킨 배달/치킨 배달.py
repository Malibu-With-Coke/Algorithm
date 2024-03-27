import sys

input = sys.stdin.readline

matrix_n, max_chicken = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_n)]
min_distance_chicken = 10e10


def choice_chicken(cnt, idx, choice_chickens):
    if cnt == max_chicken:
        global min_distance_chicken
        distance_chicken = 0

        for house in houses:
            closest_distance = 10e10

            for chicken in choice_chickens:
                distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

                if closest_distance > distance:
                    closest_distance = distance

            distance_chicken += closest_distance
            if distance_chicken > min_distance_chicken:
                return

        if min_distance_chicken > distance_chicken:
            min_distance_chicken = distance_chicken
        return

    for i in range(idx, len(chickens)):
        choice_chickens.append(chickens[i])
        choice_chicken(cnt + 1, i + 1, choice_chickens)
        choice_chickens.pop()


chickens = []
houses = []
for i in range(matrix_n):
    for j in range(matrix_n):
        if matrix[i][j] == 2:
            chickens.append((i, j))
        elif matrix[i][j] == 1:
            houses.append((i, j))


for house in houses:
    closest_distance = 10e10

    for chicken in chickens:
        distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

choice_chicken(0, 0, [])
print(min_distance_chicken)
