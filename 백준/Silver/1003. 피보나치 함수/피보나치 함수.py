n = int(input())

d0 = {0:1, 1:0}
d1 = {0:0, 1:1}
def fibonacci (num):
    if num in d1:
        return
    else:
        fibonacci(num-1)
        fibonacci(num-2)
        d1[num] = d1[num-1] + d1[num-2]
        d0[num] = d0[num-1] + d0[num-2]

for _ in range(n):
    num = int(input())
    fibonacci(num)
    print(d0[num], d1[num])