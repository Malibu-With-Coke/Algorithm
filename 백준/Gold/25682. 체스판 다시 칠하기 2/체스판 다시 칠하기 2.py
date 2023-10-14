import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(n)]

def count_minimal(color):
    global n, m, k, matrix
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    result = 0
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                result = matrix[i][j] == color
            else:
                result = matrix[i][j] != color
            prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + result
    
    count = 1000000000

    for i in range(1, n - k + 2):
        for j in range(1, m - k + 2):
            count = min(count, prefix[i + k - 1][j + k - 1] - prefix[i - 1][j + k - 1] - prefix[i + k - 1][j - 1] + prefix[i - 1][j - 1])
        
    return count

print(min(count_minimal('W'), count_minimal('B')))