import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
f_array = {}
stack = []
ans = [-1] * n

for i in seq:
    if i not in f_array:
        f_array[i] = 1
    else:
        f_array[i] += 1

for idx in range(n - 1, -1, -1):
    while stack and f_array[seq[stack[-1]]] <= f_array[seq[idx]]:
        stack.pop()

    if stack:
        ans[idx] = seq[stack[-1]]
    stack.append(idx)

print(*ans)