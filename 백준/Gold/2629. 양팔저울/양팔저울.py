import sys
input = sys.stdin.readline

weight_num = int(input())
weight = list(map(int, input().split()))
marble_num = int(input())
marble = list(map(int, input().split()))

max_marble = max(marble)
possible_weight = set()

for i in weight:
    temp = set()
    for wei in possible_weight:
        temp.add(abs(i - wei))
        temp.add(i + wei)

    possible_weight.update(temp)
    possible_weight.add(i)

for i in range(marble_num):
    print("Y" if marble[i] in possible_weight else "N", end = " ")