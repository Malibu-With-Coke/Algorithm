n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
find_num = list(map(int, input().split()))

for i in find_num:
    start = 0
    end = n-1
    
    find_check = False

    while start <= end:
        mid = (start + end) // 2
        target = arr[mid]
        if target == i:
            find_check = True
            break
    
        elif target < i:
            start = mid + 1
        
        else:
            end = mid - 1
    
    if find_check:
        print(1)
    else:
        print(0)