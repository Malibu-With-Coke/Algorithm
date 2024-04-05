import sys

input = sys.stdin.readline

r_idx, c_idx, target_num = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]


def r_calcul(matrix, RC):
    next_r_size = 0
    for row in range(len(matrix)):
        count_num = [0] * 101
        number_of_occur = [[] for _ in range(101)]
        next_arr = []
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                count_num[matrix[row][col]] += 1

        for idx, num in enumerate(count_num):
            if num == 0:
                continue

            number_of_occur[num].append(idx)

        for idx, num_occur in enumerate(number_of_occur):
            if not num_occur:
                continue

            num_occur.sort()
            for num in num_occur:
                next_arr.append(num)
                next_arr.append(idx)

        matrix[row] = next_arr
        if next_r_size < len(next_arr):
            next_r_size = len(next_arr)

    if next_r_size > 100:
        next_r_size = 100

    for row in matrix:
        if len(row) < next_r_size:
            for _ in range(next_r_size - len(row)):
                row.append(0)
        elif len(row) > 100:
            row = row[:100]

    if RC == "R":
        return matrix
    elif RC == "C":
        return list(zip(*matrix))


time = 0
while True:
    if time >= 101:
        time = -1
        break

    if (
        r_idx - 1 < len(matrix)
        and c_idx - 1 < len(matrix[0])
        and matrix[r_idx - 1][c_idx - 1] == target_num
    ):
        break

    if len(matrix) >= len(matrix[0]):
        matrix = r_calcul(matrix, "R")
    else:
        matrix = r_calcul(list(zip(*matrix)), "C")
    time += 1
print(time)
