import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans, cnt, start_idx, end_idx = 0, 0, 0, 0
dic = {i : 0 for i in range(1, 100001)}

for start_idx in range(n):
    while end_idx < n and dic[arr[end_idx]] < k:
        dic[arr[end_idx]] += 1
        end_idx += 1
        cnt += 1

    if ans < cnt:
        ans = cnt

    dic[arr[start_idx]] -= 1
    cnt -= 1

print(ans)