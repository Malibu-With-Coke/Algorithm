n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))
ans = []

def backtracking(num, index):
    if num == m:
        print(*ans)
        return
    
    for i in range(index, n):
        ans.append(arr[i])
        backtracking(num+1, i)
        ans.pop()
    
backtracking(0,0)