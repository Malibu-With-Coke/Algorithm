n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
check = [False for _ in range(n)]

def solve(num):
    if num == m:
        for i in ans:
            print(i, end=" ")
        print()
    
    else:
        for i in range(n):
            if not check[i]:
                ans.append(arr[i])
                check[i] = True
                solve(num+1)
                ans.pop()
                check[i] = False

ans = []
solve(0)