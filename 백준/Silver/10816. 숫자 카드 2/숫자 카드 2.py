import sys

input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))
n_dic = {}

for i in n_arr:
    if i in n_dic:
        n_dic[i] += 1
    else:
        n_dic[i] = 1

m = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
    if i not in n_dic:
        print("0", end=" ")
    else:
        print(n_dic[i], end=" ")
