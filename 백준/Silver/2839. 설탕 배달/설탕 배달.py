num = int(input())
answer = 0
list = [1,2,4,7]
plus_1 = [1,3]
plus_2 = [2,4]
if num in list:
    print(-1)
    exit()

answer = num // 5

if num % 5 in plus_1:
    answer += 1
elif num % 5 in plus_2:
    answer += 2

print(answer)