import sys

input = sys.stdin.readline

NO_THERE = 1

n, k = map(int, input().split())
rail = list(map(int, input().split()))
robot = [1] * n
count = 0


def next_pos(cur_pos):
    if cur_pos == 0:
        return -(2 * n - 1)
    return cur_pos + 1


while True:
    count += 1

    cur_rail = (-1) * (count % (2 * n))  # step 1


    for i in range(n - 1, 0, -1):
        robot[i] = robot[i - 1]
    robot[-1] = NO_THERE
    robot[0] = NO_THERE

    for i in range(n - 2, -1, -1):
        if (
            robot[i] != NO_THERE
            and robot[i + 1] == NO_THERE
            and rail[next_pos(robot[i])]
        ):
            rail[next_pos(robot[i])] -= 1
            robot[i + 1] = next_pos(robot[i])
            robot[i] = NO_THERE
    robot[-1] = NO_THERE

    if rail[cur_rail]:
        robot[0] = cur_rail
        rail[cur_rail] -= 1

    if rail.count(0) >= k:
        break

print(count)
