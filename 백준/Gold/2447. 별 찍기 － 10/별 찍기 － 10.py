num = int(input())

answer = [[' ' for _ in range(num)] for __ in range(num)]

# print(answer)
def star(n,x,y):
    if n == 3:
        for i in range(x,x+3):
            for j in range(y,y+3):
                if i == x+1 and j == y+1:
                    continue
                else:
                    answer[i][j] = '*'
                    # print(answer)
                    
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
# print(answer)
for i in range(num):
    for j in range(num):
        print(answer[i][j],end="")
    print()