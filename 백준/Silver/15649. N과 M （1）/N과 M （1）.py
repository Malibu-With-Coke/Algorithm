n, m = map(int, input().split())

choice_num = [0 for _ in range(n)]
arr = []

def combination(num):
    if num == m:
        for i in arr:
            print(i,end=" ")
        print()
    else:
        for i in range(n):
            if choice_num[i]:
                continue
            choice_num[i] = 1
            arr.append(i+1)
            combination(num+1)
            arr.pop()
            choice_num[i] = 0

combination(0)