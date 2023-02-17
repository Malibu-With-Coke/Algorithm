n, m = map(int, input().split())

d = {}
for _ in range(n):
    site, password = input().split()
    d[site] = password

for _ in range(m):
    ask_site = input()
    print(d[ask_site])