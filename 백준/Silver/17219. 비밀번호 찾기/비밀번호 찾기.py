import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = {}
for _ in range(n):
    site, password = input().rstrip().split()
    d[site] = password

for _ in range(m):
    ask_site = input().rstrip()
    print(d[ask_site])