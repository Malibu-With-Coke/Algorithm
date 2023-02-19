import sys

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

def backtracking(count, idx):
    if count == m:
        print(*ans)
        return
    remember = 0

    for i in range(idx, n):
        num = arr[i]
        if remember == num:
            continue
        remember = num
        ans.append(num)
        backtracking(count+1, i)
        ans.pop()
    
backtracking(0, 0)