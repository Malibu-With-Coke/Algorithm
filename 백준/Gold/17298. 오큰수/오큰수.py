import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
ans = [-1] * n
stack = [(-1,1000001)]

for idx, num in enumerate(seq):
    while stack[-1][1] < num:
        get_idx, get_num = stack.pop()
        ans[get_idx] = num
    stack.append((idx, num))
    
print(*ans)