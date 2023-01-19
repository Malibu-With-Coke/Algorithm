from collections import deque
import sys
input = sys.stdin.readline
num = int(input())

q_list = []
a_list = []



def slice_num(num):
    return num//1000, (num%1000)//100, (num%100)//10, (num%10)

def bfs(num, ans):
    deq = deque()
    deq.append([num, ""])
    arr = [0 for i in range(10000)]
    while deq:
        num, st = deq.popleft()
        
        d_num = 2*num%10000
        if d_num == ans:
            print(st+'D')
            return
        elif arr[d_num] == 0:
            arr[d_num] = 1
            deq.append([d_num, st + 'D'])
        
        s_num = num - 1 if num != 0 else 9999
        if s_num == ans:
            print(st+'S')
            return
        elif arr[s_num] == 0:
            arr[s_num] = 1
            deq.append([s_num, st+'S'])
            
        l_num = int(num % 1000 * 10 + num / 1000)
        if l_num == ans:
            print(st + 'L')
            return
        elif arr[l_num] == 0:
            arr[l_num] = 1
            deq.append([l_num, st + 'L'])
            
        r_num = int(num % 10 * 1000 + num // 10)
        if r_num == ans:
            print(st + 'R')
            return 
        elif arr[r_num] == 0:
            arr[r_num] = 1
            deq.append([r_num, st + "R"])

for i in range(num):
    q, a = map(int, input().split())
    bfs(q, a)