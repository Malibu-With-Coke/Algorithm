import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
a, s, m, d = list(map(int, input().split()))
max_num = -10e10
min_num = 10e10


def get_max_min(depth, total, add, sub, mul, div):
    if depth == n:
        global max_num, min_num
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return

    if add > 0:
        get_max_min(depth + 1, total + numbers[depth], add - 1, sub, mul, div)
    if sub > 0:
        get_max_min(depth + 1, total - numbers[depth], add, sub - 1, mul, div)
    if mul > 0:
        get_max_min(depth + 1, total * numbers[depth], add, sub, mul - 1, div)
    if div > 0:
        get_max_min(depth + 1, int(total / numbers[depth]), add, sub, mul, div - 1)


get_max_min(1, numbers[0], a, s, m, d)
print(max_num)
print(min_num)
