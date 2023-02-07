n, m = map(int, input().split())

def backTracking(num,idx):
    if num == m:
        for i in arr:
            print(i, end=" ")
        print()
    else:
        for i in range(idx, n+1):
            arr.append(i)
            backTracking(num+1, i)
            arr.pop()

arr = []
backTracking(0,1)