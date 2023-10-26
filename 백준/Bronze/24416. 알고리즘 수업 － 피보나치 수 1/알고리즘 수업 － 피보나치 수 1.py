import sys
input = sys.stdin.readline

n = int(input())

fun1_cal = 0
fun2_cal = 0

def fibonacci1(n):
    if n == 1 or n == 2:
        global fun1_cal
        fun1_cal += 1
        return 1
    else:
        return fibonacci1(n - 1) + fibonacci1(n - 2)
    
fibonacci1(n)
print(fun1_cal, end = " ")
print(max(n - 2, 1))