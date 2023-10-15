import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

remain_list = [0]

for i in arr:
    remain_list.append((remain_list[-1] + i) % m)

remain_dic = {i : 0 for i in range(m)}
for i in remain_list:
    remain_dic[i] += 1

ans = 0
for i in range(m):
    if remain_dic[i] == 0:
        continue
    
    ans += (remain_dic[i] * (remain_dic[i] - 1)) // 2

print(ans)