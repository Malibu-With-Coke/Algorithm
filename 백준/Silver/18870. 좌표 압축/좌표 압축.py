import copy

n = int(input())
arr = list(map(int, input().split()))

arr_copy = list(set(arr))
arr_copy.sort()
dic = {arr_copy[i] : i for i in range(len(arr_copy))}

for i in arr:
    print(dic[i], end=" ")