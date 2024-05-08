import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dots_num, line_num = map(int, input().split())

parent = [i for i in range(dots_num)]


def find(num):
    if parent[num] == num:
        return num
    else:
        parent[num] = find(parent[num])
    return parent[num]


def union(num1, num2):
    num1 = find(num1)
    num2 = find(num2)

    if num1 == num2:
        return 0
    parent[num1] = num2
    return 1


for i in range(1, line_num + 1):
    a, b = map(int, input().split())
    if union(a, b) == 0:
        print(i)
        break
else:
    print(0)
