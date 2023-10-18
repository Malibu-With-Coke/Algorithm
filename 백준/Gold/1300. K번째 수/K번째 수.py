import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = n * n
ans = 0

while start <= end:
    mid = (start + end) // 2
    # print(start, mid, end)
    under_mid = sum(min(mid // i, n) for i in range(1, n + 1))
    # print("under_mid", under_mid)
    
    if k <= under_mid:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1


print(ans)