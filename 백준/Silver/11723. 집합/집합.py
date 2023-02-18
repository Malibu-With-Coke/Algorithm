import sys
input = sys.stdin.readline

n = int(input())

arr = [0 for _ in range(21)]

def add(num):
    arr[num] = 1

def remove(num):
    arr[num] = 0

def check(num):
    print(arr[num])

def toggle(num):
    arr[num] = 1 - arr[num]

def all():
    for i in range(21):
        arr[i] = 1

def empty():
    for i in range(21):
        arr[i] = 0

for _ in range(n):
    input_list = list(input().split())
    if input_list[0] == "add":
        add(int(input_list[1]))
    elif input_list[0] == "remove":
        remove(int(input_list[1]))
    elif input_list[0] == "check":
        check(int(input_list[1]))
    elif input_list[0] == "toggle":
        toggle(int(input_list[1]))
    elif input_list[0] == "all":
        all()
    elif input_list[0] == "empty":
        empty()