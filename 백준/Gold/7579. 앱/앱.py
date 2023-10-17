import sys
input = sys.stdin.readline

INF = sys.maxsize
CAPACITY = 10000

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

possible_memory = [[0 for _ in range(CAPACITY + 1)] for _ in range(n + 1)]
ans = 10 ** 9

for i in range(1, n + 1):
    for j in range(1, CAPACITY + 1):
        if cost[i] > j:
            possible_memory[i][j] = possible_memory[i - 1][j]
        else:
            possible_memory[i][j] = max(possible_memory[i - 1][j], possible_memory[i - 1][j - cost[i]] + memory[i])

for i in range(1, CAPACITY + 1):
    if possible_memory[n][i] >= m:
        ans = i
        break
print(ans)