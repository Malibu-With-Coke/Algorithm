from collections import deque

l, s = map(int, input().split())

ladderOrSnake = [0 for i in range(101)]

for _ in range(l):
    start,end = map(int, input().split())
    ladderOrSnake[start] = end

for _ in range(s):
    start,end = map(int, input().split())
    ladderOrSnake[start] = end



ans = 0
already_visited = [0 for _ in range(101)]
deq = deque()
deq.append([1,0])   # start, count(ans)
already_visited[1] = 0

while deq:
    num, count = deq.popleft()
    if num == 100:
            ans = count
            break
    for dice in (1,2,3,4,5,6):
        move = num + dice
        if move > 100 or already_visited[move]:
            continue
        if ladderOrSnake[move]:
            move = ladderOrSnake[move]
        deq.append([move, count+1])
        already_visited[move] = 1

print(ans)