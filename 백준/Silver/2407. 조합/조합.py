n, m = map(int, input().split())

up, down = 1, 1

for i in range(m):
    up *= (n-i)
    down *= (i+1)

print(up//down)