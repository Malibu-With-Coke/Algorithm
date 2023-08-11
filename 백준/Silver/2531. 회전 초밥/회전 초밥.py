import sys

input = sys.stdin.readline

# n 접시 수 d 초밥의 가지 수 k 연속해서 먹는 접시 수 c 쿠폰번호
n, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
ans = 0

for s in range(n):
    cnt = 0
    dic = {arr[s] : True, c : True}
    if arr[s] == c:
        cnt += 1
    else:
        cnt += 2

    for next_idx in range(1, k):
        next = (s + next_idx) % n
        if arr[next] not in dic:
            dic[arr[next]] = True
            cnt += 1

    if ans < cnt:
        ans = cnt

print(ans)