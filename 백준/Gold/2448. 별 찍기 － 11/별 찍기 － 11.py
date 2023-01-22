num = int(input())

answer = [[' ' for _ in range(num*2)] for __ in range(num)]

def star(n, x, y):
    if (n == 3):
        answer[x][y] = '*'
        answer[x+1][y-1] = '*'
        answer[x+1][y+1] = '*'
        for i in range(5):
            answer[x+2][y-2+i] = '*'
    else:
        n = n // 2
        star(n,x,y)
        star(n,x+n,y-n)
        star(n,x+n,y+n)

star(num,0,num-1)


for i in range(num):
    for j in range(num*2):
        print(answer[i][j],end="")
    print()
