import sys

n, q = map(int, sys.stdin.readline().split())

d_pok = {}
d_num = {}

for i in range(1,n+1):
    pok_name = str(sys.stdin.readline().rstrip())
    d_pok[pok_name] = i
    d_num[i] = pok_name

for j in range(q):
    question = str(sys.stdin.readline().rstrip())
    if question.isdigit():
        print(d_num[int(question)])
    else:
        print(d_pok[question])