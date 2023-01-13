a, b = map(int, input().split())
coins = []
answer = 0
for i in range(a):
    coins.append(int(input()))

for i in range(a-1, -1, -1):
    if  b/coins[i]>=1:
       answer += b // coins[i]
       b = b % coins[i]

print(answer)