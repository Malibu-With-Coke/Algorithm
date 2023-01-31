d = {0:0, 1:1}
def fibonacci (num):
    if num in d:
        return d[num]
    else:
        d[num] = fibonacci(num-1) + fibonacci(num-2)
        return d[num]

num = int(input())
print(fibonacci(num))