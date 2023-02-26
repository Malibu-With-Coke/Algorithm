import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]* m for _ in range(n)]

que = []
heapq.heappush(que, (-arr[0][0], 0, 0))
dp[0][0] = 1

while que:
    h, a, b = heapq.heappop(que)
    if a == n-1 and b == m-1:
        continue
    for down, right in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        move_a = a + down
        move_b = b + right

        if 0 <= move_a < n and 0 <= move_b < m and arr[a][b] > arr[move_a][move_b]:
            if dp[move_a][move_b] == 0:
                heapq.heappush(que, (-arr[move_a][move_b], move_a, move_b))
            dp[move_a][move_b] += dp[a][b]

print(dp[n-1][m-1])