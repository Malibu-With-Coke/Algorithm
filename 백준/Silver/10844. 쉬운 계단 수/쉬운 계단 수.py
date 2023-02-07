import copy

n = int(input())

arr = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(1,n):
    temp = copy.deepcopy(arr)

    arr[0] = temp[1]
    for i in range(1,9):
        arr[i] = temp[i-1] + temp[i+1]
    arr[9] = temp[8]

print(sum(arr) % 1000000000)