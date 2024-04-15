import sys

input = sys.stdin.readline

num_solution = int(input())
solutions = list(map(int, input().split()))

solutions.sort()
find_zero = False

min_sum_solutions = 10e11
min_solutions = []

for idx, a_solution in enumerate(solutions):
    left_idx = 0
    right_idx = len(solutions) - 1

    while left_idx < right_idx:
        if left_idx == idx:
            left_idx += 1
            continue
        if right_idx == idx:
            right_idx -= 1
            continue

        sum_solution = a_solution + solutions[left_idx] + solutions[right_idx]
        if abs(min_sum_solutions) > abs(sum_solution):
            min_sum_solutions = sum_solution
            min_solutions = [a_solution, solutions[left_idx], solutions[right_idx]]

        if sum_solution < 0:
            left_idx += 1
        elif sum_solution > 0:
            right_idx -= 1
        else:
            find_zero = True
            break

    if find_zero:
        break

min_solutions.sort()

print(*min_solutions)
