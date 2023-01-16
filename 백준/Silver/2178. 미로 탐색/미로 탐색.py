from collections import deque
row, column = map(int, input().split())

miro = [list(map(int,input())) for _ in range(row)]

deq = deque()
answer = 0
deq.append([0, 0, 1])
miro[0][0] = 0
# print(deq)
while deq:
    a, b, c = deq.popleft()
    # print(a, b, c)
    if(a == row-1 and b == column-1):
        # print("break")
        answer = c
        break
    else:
        if(a+1<row and miro[a+1][b] == 1):
            deq.append([a+1, b, c+1])
            miro[a+1][b] = 0
        if(a-1>=0 and miro[a-1][b] == 1):
            deq.append([a-1, b, c+1])
            miro[a-1][b] = 0
        if(b+1<column and miro[a][b+1] == 1):
            deq.append([a, b+1, c+1])
            miro[a][b+1] = 0
        if(b-1>= 0 and miro[a][b-1] == 1):
            deq.append([a, b-1, c+1])
            miro[a][b-1] = 0
print(answer)