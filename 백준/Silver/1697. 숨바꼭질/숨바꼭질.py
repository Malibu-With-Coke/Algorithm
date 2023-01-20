# import sys
# sys.stdin = open('input.txt', 'r')

from collections import deque

s, d = map(int, input().split())
if s == d:
    print(0)
    exit()
count = 0

check = [0 for _ in range(100001)]

deq = deque()
deq.append([s, count])

def check_num(num, count):
    if not (0<= num <= 100000):
        return
    if check[num] == 1:
        return
    if num == d:
        print(count)
        exit()
    check[num] = 1
    deq.append([num, count])

while deq:
    num, count = deq.popleft()
    # print(num, count)
    check_num(num-1, count+1)
    check_num(num+1, count+1)
    check_num(num*2, count+1)
    # if num == d:
    #     break
    # if not check[num-1]:
    #     check[num-1] = 1
    #     deq.append([num-1, count+1])
    # if not check[num+1]:
    #     check[num+1] = 1    
    #     deq.append([num+1, count+1])
    # if num*2 <= 100000 and not check[num*2]:
    #     check[num*2] = 1    
    #     deq.append([num*2, count+1])



# print(count)