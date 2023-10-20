import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

p = [i for i in range(n+1)]

def find(a):
    if a == p[a]:
        return a
    else:
        p[a] = find(p[a])
        return p[a]
    
def merge(a, b):
    p[find(a)] = find(b)


for _ in range(m):
    check, a, b = map(int, input().split())
    
    if check:
        print("yes" if find(a) == find(b) else "no")
    else:
        merge(a, b)