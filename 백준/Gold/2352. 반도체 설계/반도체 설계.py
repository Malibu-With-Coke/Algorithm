import sys
input = sys.stdin.readline

n = int(input())
electric_wire = list(map(int, input().split()))

from bisect import bisect_left

countOfWires = 0
wires = []
wires.append(electric_wire[0])
countOfWires += 1

for i in range(1, n):
    if wires[-1] < electric_wire[i]:
        wires.append(electric_wire[i])
        countOfWires += 1
    else:
        idx = bisect_left(wires, electric_wire[i])
        wires[idx] = electric_wire[i]

print(countOfWires)