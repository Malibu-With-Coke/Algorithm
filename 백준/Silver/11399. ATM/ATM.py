num = int(input())
_list = list(map(int, input().split()))
_list.sort()
answer = 0
sum = 0
for i in _list:
    sum += i
    answer += sum
print(answer)
