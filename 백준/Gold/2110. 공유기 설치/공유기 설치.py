import sys
input = sys.stdin.readline

n, c = map(int ,input().split())
router = [int(input()) for _ in range(n)]

router.sort()

start = 1
mid = (router[n - 1] - router[0]) // c
end = (router[n - 1] - router[0])

while start <= end:
    count = 1
    pre_router = router[0]
    for idx, rou in enumerate(router):
        if rou < pre_router + mid:
            continue
        else:
            count += 1
            pre_router = rou
    
    if count >= c:
        start = mid + 1
    else:
        end = mid - 1
    
    mid = (start + end) // 2

print(mid)