import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    dif_idx = n
    arr.sort()
    for i in range(1, n):
        if arr[i][0] != arr[i-1][0]:
            dif_idx = i
            break

    for i in range(dif_idx, n):
        if arr[i][1] != arr[i%dif_idx][1]:
            print("NOT BALANCED")
            return
        
    print("BALANCED")

n = int(input())
for _ in range(n):
    solve()