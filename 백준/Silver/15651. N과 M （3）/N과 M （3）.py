n, m = map(int, input().split())

def backTracking(num):
    if num == m:
        for i in arr:
            print(i, end=" ")
        print()
    else:
        for i in range(1,n+1):
            arr.append(i)
            backTracking(num+1)
            arr.pop()

arr = []
backTracking(0)