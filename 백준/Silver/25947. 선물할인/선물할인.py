import sys
input = sys.stdin.readline

n, b, a = map(int, input().split())
gifts = list(map(int, input().split()))

gifts.sort()

sum_cost = [gifts[0]]
for i in range(1, n):
    sum_cost.append(gifts[i] + sum_cost[-1])

ans = 0
current_cost = 0
for i in range(n):
    if i < a:
        current_cost = sum_cost[i] / 2
    else:
        current_cost = sum_cost[i - a] + (sum_cost[i] - sum_cost[i - a]) / 2
    
    if current_cost > b:
        break

    if i == n - 1:
        i = n

print(i)