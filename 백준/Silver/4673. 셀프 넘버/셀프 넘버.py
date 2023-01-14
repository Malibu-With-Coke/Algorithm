check = [False for i in range(12000)]

def sum_num(num):
    sum = 0
    while(True):
        sum += num % 10
        num = num // 10
        if (num == 0):
            break
    return sum


for i in range(1,10000):
    # print(sum_num(i))
    check[i+sum_num(i)] = True
    if (not check[i]):
        print(i)