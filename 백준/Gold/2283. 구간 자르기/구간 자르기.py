import sys

input = sys.stdin.readline

n, target = map(int, input().split())
arr = [0 for _ in range(1000001)]
start = int(10e9)
end = 0

for _ in range(n):
    s, e = map(int, input().split())
    if start > s: start = s
    if end < e: end = e
    arr[s] += 1
    arr[e] -= 1

for i in range(start+1, end+1):
    arr[i] += arr[i-1]


sum_arr = 0
start_idx = 0
end_idx = 0
flag = False

for start_idx in range(0, end+1):
    while sum_arr < target and end_idx <= end:
        sum_arr += arr[end_idx]
        end_idx += 1

    if sum_arr == target:
        flag = True
        break

    sum_arr -= arr[start_idx]

if flag:
    print(start_idx, end_idx)
else:
    print(0, 0)