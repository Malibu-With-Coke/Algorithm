import sys
input = sys.stdin.readline

n = int(input())
city_distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_oil = 10e10
ans = 0

for idx, distance in enumerate(city_distance):
    if min_oil > oil[idx]:
        min_oil = oil[idx]

    ans += min_oil * distance    

print(ans)