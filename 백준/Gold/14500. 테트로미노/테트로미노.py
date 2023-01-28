r, c = map(int, input().split())    # r = 세로 c = 가로

matrix = [list(map(int, input().split())) for _ in range(r)]

ans = 0

# 일자 도형
for i in range(0, r-3):
    for j in range(0, c):
        num = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]
        # print(i,j)
        if ans < num:
            # print(i, j)
            ans = num

for i in range(0, r):
    for j in range(0, c-3):
        num = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3]
        if ans < num:
            ans = num

# 정사각형
for i in range(0, r-1):
    for j in range(0, c-1):
        num = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
        if ans < num:
            ans = num

# ㅜ
for i in range(0, r-1):
    for j in range(0, c-2):
        num = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1]
        if ans < num:
            ans = num
# ㅏ
for i in range(0, r-2):
    for j in range(0, c-1):
        num = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+1][j+1]
        if ans < num:
            ans = num
# ㅓ
for i in range(0, r-2):
    for j in range(1, c):
        num = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+1][j-1]
        if ans < num:
            ans = num
# ㅗ
for i in range(1, r):
    for j in range(0, c-2):
        num = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i-1][j+1]
        if ans < num:
            ans = num

# ㄹ
for i in range(0, r-1):
    for j in range(0, c-2):
        num = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j+2]
        if ans < num:
            ans = num

# ㄹ(대칭)
for i in range(0, r-1):
    for j in range(0, c-2):
        num = matrix[i+1][j] + matrix[i+1][j+1] + matrix[i][j+1] + matrix[i][j+2]
        if ans < num:
            ans = num

# ㄹ (세로)
for i in range(0, r-2):
    for j in range(0, c-1):
        num = matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j] + matrix[i+2][j]
        if ans < num:
            ans = num

# ㄹ(대칭) (세로)
for i in range(0, r-2):
    for j in range(0, c-1):
        num = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1]
        if ans < num:
            ans = num

# (1236)
for i in range(0, r-1):
    for j in range(0, c-2):
        num = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+2]
        if ans < num:
            ans = num

# (4563)
for i in range(0, r-1):
    for j in range(0, c-2):
        num = matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i][j+2]
        if ans < num:
            ans = num

# (1472)
for i in range(0, r-2):
    for j in range(0, c-1):
        num = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i][j+1]
        if ans < num:
            ans = num

# (1478)
for i in range(0, r-2):
    for j in range(0, c-1):
        num = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j+1]
        if ans < num:
            ans = num

# (1456)
for i in range(0, r-1):
    for j in range(0, c-2):
        num = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2]
        if ans < num:
            ans = num

# (1423)
for i in range(0, r-1):
    for j in range(0, c-2):
        num = matrix[i][j] + matrix[i+1][j] + matrix[i][j+1] + matrix[i][j+2]
        if ans < num:
            ans = num

# (2587)
for i in range(0, r-2):
    for j in range(0, c-1):
        num = matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1] + matrix[i+2][j]
        if ans < num:
            ans = num

# (2581)
for i in range(0, r-2):
    for j in range(0, c-1):
        num = matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1] + matrix[i][j]
        if ans < num:
            ans = num

print(ans)