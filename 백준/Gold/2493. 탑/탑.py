import sys

input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))

stack = []
communicate = [0 for _ in range(len(tops))]

for idx in range(len(tops) - 1, -1, -1):
    while stack and tops[stack[-1]] < tops[idx]:
        communicate[stack[-1]] = idx + 1
        stack.pop()
    stack.append(idx)


print(*communicate)