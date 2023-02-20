n = int(input())

def solve():
    m, n = map(int, input().split())

    up = 1
    down = 1

    for i in range(m):
        up *= (n-i)
        down *= (i+1)
    
    print(up//down)
    
for _ in range(n):
    solve()