import sys

input = sys.stdin.readline


def find(num):
    if num == parent[num]:
        return num

    parent[num] = find(parent[num])
    return parent[num]


def merge(num1, num2):
    num1 = find(num1)
    num2 = find(num2)

    if num1 != num2:
        parent[num1] = num2
        return 1

    return 0


n = int(input())
m = int(input())

parent = [i for i in range(n + 1)]
networks = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    networks.append((cost, a, b))

networks.sort()

total_cost = 0
add_conn = 0
for cost, a, b in networks:
    if merge(a, b) == 1:
        total_cost += cost
        add_conn += 1

        if add_conn == n - 1:
            break
print(total_cost)
