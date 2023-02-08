from collections import deque

n = int(input())

def solve():
    arr = input()
    word_len = int(input())
    word = input().rstrip(']').lstrip('[')  # 데이터 파싱
    if word_len == 0:
        word_list = deque()
    else:
        word_list = deque(map(int, word.split(',')))

    not_reverse = True
    
    for i in arr:
        if i == "R":
            if not_reverse:
                not_reverse = False
            else:
                not_reverse = True

        else:
            if word_len == 0:
                print("error")
                return
            
            if not_reverse:
                word_list.popleft()
            else:
                word_list.pop()
            word_len -= 1

    if not not_reverse:
        word_list.reverse()
        word_list = list(word_list)
    else:
        word_list = list(word_list)
    
    print('[',end="")
    for i in range(len(word_list)):
        if i == len(word_list)-1:
            print(word_list[i],end='')
        else:
            print(word_list[i],end=',')
    print(']')
for _ in range(n):
    solve()