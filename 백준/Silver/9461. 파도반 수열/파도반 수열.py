n = int(input())

d = {1:1, 2:1, 3:1, 4:2, 5:2}
def padoban (num):
    if num in d:
        return d[num]
    else:
        d[num] = padoban(num-1) + padoban(num-5)
        return d[num]

for _ in range(n):
    num = int(input())
    print(padoban(num))