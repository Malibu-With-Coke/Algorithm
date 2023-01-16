import sys
sys.setrecursionlimit(10000)

num = int(input())
answer_list = []

def solve():
    answer = 0
    row, column, bug = map(int, input().split())
    graph = [[0 for i in range (column)] for i in range (row)]
    for i in range(bug):
        r, w = map(int, input().split())
        graph[r][w] = 1
    for i in range(row):
        for j in range(column):
            if graph[i][j] == 1:
                dfs(graph, i, j)
                # print("start : ", i, j)
                answer += 1
    answer_list.append(answer)

def dfs(graph, r, w):
    graph[r][w] = 0
    # print(len(graph),len(graph[r]),"!!!")
    if r+1 < len(graph) and graph[r+1][w] == 1:
        dfs(graph, r+1, w)
    if r-1 >= 0 and graph[r-1][w] == 1:
        dfs(graph, r-1, w)
    if w+1 < len(graph[r]) and graph[r][w+1] == 1:
        dfs(graph, r, w+1)
    if w-1 >= 0 and graph[r][w-1] == 1:
        dfs(graph, r, w-1)


for _ in range(num):
    solve()
    
for i in answer_list:
    print(i)