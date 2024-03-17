import sys

input = sys.stdin.readline

class_count = int(input())
class_students = list(map(int, input().split()))
main_teacher, sub_teacher = map(int, input().split())

count_teacher = 0
for students in class_students:
    count_teacher += 1
    students -= main_teacher

    if students > 0:
        count_teacher += students // sub_teacher
        if students % sub_teacher != 0:
            count_teacher += 1

print(count_teacher)
