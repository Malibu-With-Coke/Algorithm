num = int(input())

answer = [[' ' for _ in range(num)] for __ in range(num)]

# print(answer)
def star(n,x,y):
    if n == 1:
        answer[x][y] = '*'
                    
    else:
        n = n//3
        star(n, x, y)
        star(n, x+n, y)
        star(n, x+2*n, y)
        star(n, x, y+n)
        star(n, x+2*n, y+n)
        star(n, x, y+2*n)
        star(n, x+n, y+2*n)
        star(n, x+2*n, y+2*n)

star(num, 0, 0)
for i in range(num):
    for j in range(num):
        print(answer[i][j],end="")
    print()