import sys
input = sys.stdin.readline

n, m = map(int, input().split())

not_hear = {}

for _ in range(n):
    name = input().rstrip()
    not_hear[name] = 1

ans = []

for _ in range(n):
    name = input().rstrip()
    if name in not_hear:
        ans.append(name)

ans.sort()
print(len(ans))
for i in ans:
    print(i)