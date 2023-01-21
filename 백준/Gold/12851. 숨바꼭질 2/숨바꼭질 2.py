from collections import deque

s, d = map(int, input().split())
if s == d:
    print(0)
    print(1)
    exit()
count = 0

check = [0 for _ in range(100001)]

deq = deque()
deq.append([s, count])

answer_first = 0    # 수빈이가 동생을 찾은 가장 빠른 시간
answer_second = 0   # 가장 빠른 시간의 횟수
while deq:
    num, count = deq.popleft()
    if (answer_second != 0 and answer_first < count +1):
        break
    for i in (num-1, num+1, num*2):
        if not (0 <= i <= 100000):
            continue
        if i == d:
            if not answer_second:
                answer_first = count + 1
            answer_second += 1
            continue
        if check[i] == 0 or check[i] == count + 1:
            check[i] = count + 1
            deq.append([i, count + 1])
        # print(i, count+1)

print(answer_first)
print(answer_second)