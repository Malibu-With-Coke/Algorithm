from collections import deque
import copy
n = int(input())

arr = [list(input()) for _ in range(n)]
arr2 = copy.deepcopy(arr)


ans1 = 0
ans2 = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            deq = deque()
            deq.append([i,j,arr[i][j]])
            arr[i][j] = 0
            ans1 += 1
            while deq:
                x, y, c = deq.popleft()
                for a, b in ((-1,0),(1,0),(0,1),(0,-1)):
                    yy = y + a
                    xx = x + b
                    if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] == c:
                        deq.append([xx,yy,arr[xx][yy]])
                        arr[xx][yy] = 0
        if arr2[i][j] != 0:
            deq = deque()
            deq.append([i,j,arr2[i][j]])
            arr2[i][j] = 0
            ans2 += 1
            while deq:
                x, y, c = deq.popleft()
                if c == 'R':
                    cc = 'G'
                elif c == 'G':
                    cc = 'R'
                else:
                    cc = 'B' 
                for a, b in ((-1,0),(1,0),(0,1),(0,-1)):
                    yy = y + a
                    xx = x + b
                    if 0 <= xx < n and 0 <= yy < n and (arr2[xx][yy] == c or arr2[xx][yy] == cc):
                        deq.append([xx,yy,arr2[xx][yy]])
                        arr2[xx][yy] = 0
        
                

print(ans1,ans2)