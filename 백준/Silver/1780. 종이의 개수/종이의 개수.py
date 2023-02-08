n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

d_count = {-1:0, 0:0, 1:0}

def recur(num, x, y):

    if num == 1:
        d_count[matrix[x][y]] += 1
    
    else:
        word = matrix[x][y]
        check = True
        for i in range(num):
            for j in range(num):
                if matrix[x+i][y+j] != word:
                    check = False
                    break
        if check:
            d_count[matrix[x][y]] += 1
        else:
            num = num // 3
            for i in range(3):
                for j in range(3):
                    recur(num, x+i*num, y+j*num)

recur(n, 0, 0)
for i in (-1, 0, 1):
    print(d_count[i])