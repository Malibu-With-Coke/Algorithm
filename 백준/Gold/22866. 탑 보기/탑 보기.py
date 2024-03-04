import sys

input = sys.stdin.readline

num_towrer = int(input())
towers = list(map(int, input().split()))

can_see_tower = [-1] * (num_towrer)
nearest_tower = [-1] * (num_towrer)

stack = []

for idx, tower in enumerate(towers):
    while stack and stack[-1][0] <= tower:
        stack.pop()

    can_see_tower[idx] = len(stack)
    if stack:
        nearest_tower[idx] = stack[-1][1]

    stack.append((tower, idx))

stack = []

for idx in range(num_towrer - 1, -1, -1):
    tower = towers[idx]
    while stack and stack[-1][0] <= tower:
        stack.pop()

    can_see_tower[idx] += len(stack)
    if stack and (
        nearest_tower[idx] == -1 or idx - nearest_tower[idx] > abs(idx - stack[-1][1])
    ):
        nearest_tower[idx] = stack[-1][1]

    stack.append((tower, idx))

for i in range(num_towrer):
    if can_see_tower[i] == 0:
        print(0)
    else:
        print(can_see_tower[i], nearest_tower[i] + 1)
