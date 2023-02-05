from bisect import *

n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()

two_sum = []

for i in range(n):
    for j in range(i,n):
        two_sum.append(arr[i] + arr[j])

two_sum.sort()

for i in range(n-1, -1, -1):
    for j in range(i):
        num = bisect_right(two_sum, arr[i] - arr[j])
        if two_sum[num-1] == arr[i] - arr[j]:
            print(arr[i])
            exit()