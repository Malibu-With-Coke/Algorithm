import sys

input = sys.stdin.readline

test_case_num = int(input())


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if count[b] > count[a]:
            parent[a] = b
            count[b] += count[a]
        else:
            parent[b] = a
            count[a] += count[b]
            count[b] = count[a]
    return count[b]


for _ in range(test_case_num):
    connection_num = int(input())
    parent = {}
    count = {}
    for _ in range(connection_num):
        people_a, people_b = map(str, input().split())
        if people_a not in parent:
            parent[people_a] = people_a
            count[people_a] = 1
        if people_b not in parent:
            parent[people_b] = people_b
            count[people_b] = 1

        print(union(people_a, people_b))
