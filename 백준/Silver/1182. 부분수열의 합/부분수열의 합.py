n, s = map(int, input().split())
input_arr = list(map(int, input().split()))
already_choice = [1 for _ in range(n)]
arr = []

answer = 0

def backtracking(num):
    if num == n:
        if arr and sum(arr) == s:
            # print(arr)
            global answer
            answer += 1
        return
    
    i = input_arr[num]
    arr.append(i)
    backtracking(num+1)
    arr.pop()
    backtracking(num+1)
    
backtracking(0)
print(answer)