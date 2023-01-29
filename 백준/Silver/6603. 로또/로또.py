def backTracking (idx, depth):
    if depth == 6:
        for i in ans:
            print(i, end=" ")
        print()
        return
    else:
        for i in range(idx, len(arr)-1):
            ans[depth] = arr[i+1]
            backTracking(i+1, depth+1)

ans = [0 for _ in range(6)]

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    backTracking(0, 0)
    print()