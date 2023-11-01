import sys

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
distance = [INF] * (n + 1)


def bellmanford():
    distance[1] = 0
    for i in range(n):
        for j in range(m):
            s, e, c = edges[j]

            if distance[s] != INF and distance[e] > distance[s] + c:
                distance[e] = distance[s] + c

                if i == n - 1:
                    print(-1)
                    return

    for i in range(2, n + 1):
        print(distance[i] if distance[i] != INF else -1)

    return

bellmanford()