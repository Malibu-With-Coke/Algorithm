N, M = map(int, input().split())

arr = list(map(int, input().split()))


start = 0
end = max(arr)
ans = 0
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in arr:
        chopped_tree = i - mid
        if chopped_tree> 0:
            sum += chopped_tree
    # print(start,end,mid,sum)
    
    if sum >= M:
        start = mid + 1
        if ans < mid:
            ans = mid
            # print(ans)
    else:
        end = mid - 1

print(ans)