import sys

input = sys.stdin.readline

# n 접시 수 d 초밥의 가지 수 k 연속해서 먹는 접시 수 c 쿠폰번호
n, d, k, c = map(int, input().split())
k -= 1

arr = [int(input()) for _ in range(n)]
cnt = 0
ans = 0
start_idx = 0
end_idx = 0
eaten = {i : 0 for i in range(1, d+1)}

while True:
    if start_idx == n:
        break
    if start_idx == 0:
        for next_idx in range(k+1):
            if not eaten[arr[start_idx + next_idx]]:
                cnt += 1
            eaten[arr[start_idx + next_idx]] += 1
    else:
        eaten[arr[start_idx-1]] -= 1
        if not eaten[arr[start_idx-1]]:
            cnt -= 1
        if not eaten[arr[(start_idx + k) % n]]:
            cnt += 1
        eaten[arr[(start_idx + k) % n]] += 1

    if not eaten[c] and ans < cnt + 1:
        ans = cnt + 1
    elif ans < cnt:
        ans = cnt

    start_idx += 1
print(ans)