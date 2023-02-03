import math

n = int(input())

d = {0:0,1:1}

for i in range(2, n+1):
    min_value = 999
    sqrt_i = int(math.sqrt(i))+1
    for j in range(1, sqrt_i):
        # print(i,j)
        min_value = min(min_value,d[i-j**2])
    d[i] = min_value + 1
print(d[n])