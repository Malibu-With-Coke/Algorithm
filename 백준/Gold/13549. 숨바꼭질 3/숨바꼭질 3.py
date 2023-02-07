from collections import deque

s, d = map(int, input().split())
if s == d:
    print(0)
    exit()
count = 0

check = [0 for _ in range(100001)]

deq = deque()
deq.append([s, count])

ans = 9999999
ans_find = False

def check_num(num, count):
    if not (0<= num <= 100000):
        return
    if check[num] == 1:
        return
    if num == d:
        global ans
        global ans_find
        if ans > count:
            ans = count
        ans_find = True
        return
    if ans_find and ans <= count:
        return
    check[num] = 1
    deq.append([num, count])

while deq:
    num, count = deq.popleft()
    check_num(num*2, count)
    check_num(num-1, count+1)
    check_num(num+1, count+1)

print(ans)