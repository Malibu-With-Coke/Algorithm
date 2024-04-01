import sys
import heapq

input = sys.stdin.readline

num_diamond, num_bag = map(int, input().split())

diamond = [list(map(int, input().split())) for _ in range(num_diamond)]  # 무게, 가격
bags = [int(input()) for _ in range(num_bag)]

diamond.sort(reverse=True)
bags.sort()

can_pack = []
sum_weight = 0
for bag in bags:

    while diamond and diamond[-1][0] <= bag:
        heapq.heappush(can_pack, -diamond[-1][1])
        diamond.pop()
    if can_pack:
        sum_weight -= heapq.heappop(can_pack)

print(sum_weight)
