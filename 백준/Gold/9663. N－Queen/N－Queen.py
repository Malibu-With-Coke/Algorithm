num = int(input())

chess = [[0 for _ in range(num)] for __ in range(num)]

vertex = [0 for _ in range(num)]
diagonal1 = [0 for _ in range(num*2-1)]
diagonal2 = [0 for _ in range(num*2-1)]

answer = 0

def n_queen(n):
    if n == num:
        global answer
        answer += 1
        return
    for i in range(num):
        a = n+i
        b = i-n+num-1
        if vertex[i] == 1 or diagonal1[a] == 1 or diagonal2[b] == 1:
            continue
        vertex[i] = 1
        diagonal1[a] = 1
        diagonal2[b] = 1

        n_queen(n+1)

        vertex[i] = 0
        diagonal1[a] = 0
        diagonal2[b] = 0

n_queen(0)
print(answer)