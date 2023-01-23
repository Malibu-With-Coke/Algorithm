num = int(input())

num_pow = pow(2, num) -1    # 1,3, 7, 15, 31

arr = [[' ' for _ in range(num_pow*2-1)]for __ in range(num_pow)]


def star(num, x, y):
    if num == 1:
        arr[x][y] = '*'
        return
    elif num % 2 == 1:
        n = int(pow(2,num)-1)
        n_2 = int(n//2)
        arr[x-n_2][y] = '*'
        for i in range(1,n-1):
            arr[x-n_2+i][y-i] = '*'
            arr[x-n_2+i][y+i] = '*'
        for i in range(1,2*n):
            arr[x+n_2][y-n+i] = '*'
        star(num-1, x + int(n_2//2), y)
    else:
        n = int(pow(2,num)-1)
        n_2 = int(n//2)
        # print(n, n_2)
        arr[x+n_2][y] = '*'
        for i in range(1,n-1):
            arr[x+n_2-i][y-i] = '*'
            arr[x+n_2-i][y+i] = '*'
        for i in range(1,2*n):
            arr[x-n_2][y-n+i] = '*'
        star(num-1, x - int(n_2//2), y)

star(num, num_pow//2, num_pow-1)
# print(num_pow//2, num_pow)

for k in arr:
    print(''.join(k).rstrip())