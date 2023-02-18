n = int(input())

matrix = [list(input()) for _ in range(n)]

ans = []

def recur(num, x, y):
    a = matrix[y][x]
    for i in range(y, y+num):
        for j in range(x, x+num):
            if a != matrix[i][j]:
                ans.append("(")
                num = num // 2
                recur(num, x, y)
                recur(num, x+num, y)
                recur(num, x, y+num)
                recur(num, x+num, y+num)
                ans.append(")")
                return
    ans.append(a)
                
recur(n, 0, 0)
print("".join(ans))