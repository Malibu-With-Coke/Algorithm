import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dic = {i : False for i in range(1, 100001)}

ans = 0
start_idx = 0
end_idx = 0
dic[arr[start_idx]] = True

for start_idx in range(n):
    while end_idx + 1 < n and not dic[arr[end_idx + 1]]:
        end_idx += 1
        dic[arr[end_idx]] = True

    dic[arr[start_idx]] = False
    ans += (end_idx - start_idx) + 1

print(ans)

