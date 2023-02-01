n = int(input())

arr = [i for i in range(n+1)]

for i in range(3,n+1):
    arr[i] = arr[i-2] + arr[i-1]

print(arr[n] % 10007)