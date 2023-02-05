K, N = map(int, input().split())

arr = [int(input()) for i in range(K)]

start = 1
end = max(arr)

def count_cable (num):
    sum = 0
    for i in arr:
        sum += (i//num)
    
    return sum

ans = 0

while start <= end:
    mid = (start + end) // 2

    target = count_cable(mid)
    if target < N:
        end = mid -1

    else:
        start = mid + 1
        if ans < mid:
            ans = mid
        
print(ans)