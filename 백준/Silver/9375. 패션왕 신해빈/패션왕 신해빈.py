n = int(input())

def solve():
    num = int(input())
    wear = {}
    for i in range(num):
        temp = list(input().split())
        if temp[1] in wear:
            wear[temp[1]].append(temp[0])
        else:
            wear[temp[1]] = [temp[0]]
    
    ans = 1

    for i in wear:
        ans *= (len(wear[i])+1)
    print(ans-1)

for i in range(n):
    solve()