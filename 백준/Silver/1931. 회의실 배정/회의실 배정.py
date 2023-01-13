num = int(input())

data = []
answer = 0
end_time = 0
for i in range(num):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[1], x[0]))

for i in range(num):
    if end_time <= data[i][0]:
        end_time = data[i][1]
        answer += 1


print(answer)