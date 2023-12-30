import sys

input = sys.stdin.readline

def ifTriangle(a, b, c):
    if max(a, b, c) - (a + b + c - max(a, b, c)) >= 0:
        print("Invalid")

    elif a == b == c:
        print("Equilateral")

    elif a == b or b == c or a == c:
        print("Isosceles")

    else:
        print("Scalene")


while True:
    a, b, c = map(int, input().split())

    if a == 0:
        break
    ifTriangle(a, b, c)