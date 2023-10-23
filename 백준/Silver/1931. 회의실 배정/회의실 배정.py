import sys
input = sys.stdin.readline

n = int(input())

classes = [list(map(int, input().split())) for _ in range(n)]
classes.sort(key=lambda x : (x[1], x[0]))

prev_end = 0
count_class = 0
for i in range(n):
    if prev_end <= classes[i][0]:
        prev_end = classes[i][1]
        count_class += 1

print(count_class)
