n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))
ans = []
already_used = [False for _ in range(n)]

def backtracking(count):
    if count == m:
        print(*ans)
        return
    remember = 0

    for i in range(n):
        num = arr[i]
        if already_used[i] or remember == num:
            continue
        remember = num
        already_used[i] = True
        ans.append(num)
        backtracking(count+1)
        already_used[i] = False
        ans.pop()
    
backtracking(0)