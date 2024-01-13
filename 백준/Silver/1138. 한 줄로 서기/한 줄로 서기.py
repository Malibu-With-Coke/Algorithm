import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

line = [0] * 10
k = 1
for idx in arr:
    cnt = 0

    for line_idx, line_person in enumerate(line):
        # print(line_idx)
        if cnt == idx and line_person == 0:
            line[line_idx] = k
            k += 1
            break
        if line_person == 0:
            cnt += 1

print(*line[0:n])