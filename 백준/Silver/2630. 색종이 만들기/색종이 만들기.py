n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

confetti = {0 : 0, 1 : 0} # 0 white 1 blue

def recur(num, x, y):
    color = matrix[y][x]
    for i in range(y, y+num):
        for j in range(x, x+num):
            if color != matrix[i][j]:
                num = num // 2
                recur(num, x, y)
                recur(num, x+num, y)
                recur(num, x, y+num)
                recur(num, x+num, y+num)
                return
    confetti[color] += 1

recur(n, 0, 0)
for i in confetti.values():
    print(i)