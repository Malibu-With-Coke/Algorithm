import sys

input = sys.stdin.readline

row, column, num_of_sharks = map(int, input().split())
matrix = [[0 for _ in range(column)] for _ in range(row)]
shark_info = [0]
dead_shark = [True] + [False for _ in range(num_of_sharks)]
RIGHT_END = column - 1
LEFT_END = 0
UP_END = 0
DOWN_END = row - 1
UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4

for idx in range(1, num_of_sharks + 1):
    r, c, speed, direction, size = map(int, input().split())
    if direction == 1 or direction == 2:
        speed = speed % (2 * row - 2)
    elif direction == 3 or direction == 4:
        speed = speed % (2 * column - 2)

    shark_info.append([speed, direction, size])
    matrix[r - 1][c - 1] = idx


def move_and_catch(cur_pos):
    catch_shark = -1
    for idx in range(row):
        if matrix[idx][cur_pos] > 0:
            catch_shark = matrix[idx][cur_pos]
            dead_shark[matrix[idx][cur_pos]] = True
            matrix[idx][cur_pos] = 0
            break

    if catch_shark == -1:
        return 0
    else:
        return shark_info[catch_shark][2]


def move_right(num_movement, cur_pos):
    # print("right", cur_pos, num_movement)
    if num_movement + cur_pos >= RIGHT_END:
        return move_left(num_movement - (RIGHT_END - cur_pos), RIGHT_END)

    return cur_pos + num_movement, 3


def move_left(num_movement, cur_pos):
    # print("left", cur_pos, num_movement)
    if cur_pos - num_movement <= LEFT_END:
        return move_right(num_movement - cur_pos, LEFT_END)

    return cur_pos - num_movement, 4


def move_down(num_movement, cur_pos):
    # print("down", cur_pos, num_movement)
    if num_movement + cur_pos >= DOWN_END:
        return move_up(num_movement - (DOWN_END - cur_pos), DOWN_END)

    return cur_pos + num_movement, 2


def move_up(num_movement, cur_pos):
    # print("up", cur_pos, num_movement)
    if cur_pos - num_movement <= UP_END:
        return move_down(num_movement - cur_pos, UP_END)

    return cur_pos - num_movement, 1


def move(move_dir, num_movement, cur_pos_i, cur_pos_j):
    if move_dir == 1:
        cur_pos_i, move_dir = move_up(num_movement, cur_pos_i)
    elif move_dir == 2:
        cur_pos_i, move_dir = move_down(num_movement, cur_pos_i)
    elif move_dir == 3:
        cur_pos_j, move_dir = move_right(num_movement, cur_pos_j)
    elif move_dir == 4:
        cur_pos_j, move_dir = move_left(num_movement, cur_pos_j)

    return move_dir, cur_pos_i, cur_pos_j


def shark_moving(matrix):
    new_matrix = [[0 for _ in range(column)] for _ in range(row)]
    for i in range(row):
        for j in range(column):
            if matrix[i][j] > 0 and not dead_shark[matrix[i][j]]:
                cur_shark = matrix[i][j]
                shark_speed, shark_dir, shark_size = shark_info[cur_shark]
                next_dir, next_i, next_j = move(shark_dir, shark_speed, i, j)
                # print(next_i, next_j, cur_shark, "<- cur")
                if new_matrix[next_i][next_j] > 0:  # 다른 상어가 있음
                    other_shark = new_matrix[next_i][next_j]

                    if shark_size < shark_info[other_shark][2]:
                        dead_shark[cur_shark] = True
                        continue

                    dead_shark[other_shark] = True
                new_matrix[next_i][next_j] = cur_shark
                shark_info[cur_shark][1] = next_dir

    return new_matrix


ans = 0
for i in range(column):
    ans += move_and_catch(i)
    matrix = shark_moving(matrix)
    # for j in matrix:
    #     print(*j)
    # print()
print(ans)
